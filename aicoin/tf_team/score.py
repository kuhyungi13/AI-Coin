"""ACE와 애널리스트 의견 채점. 승률을 재야 무엇을 고칠지 알 수 있다.

paper/tf/verdicts.csv 한 줄 = 한 회의에서 한 코인에 낸 의견. 회의를 연 Claude가 보고서와 함께 적는다.
의견을 낸 지 24시간이 지나면 이 모듈이 바이낸스 1시간봉으로 그 사이 가격 변화를 재서 맞았는지 적는다.

채점 기준 (24시간 수익률 r)
- 매수 / 긍정: r > 0 이면 맞음
- 매도 / 부정: r < 0 이면 맞음
- 관망 / 중립: |r| < FLAT(3%) 이면 맞음 (크게 움직이지 않을 거라는 의견)
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from ..data import fetch_klines

HORIZON = pd.Timedelta(hours=24)
FLAT = 3.0
AGENTS = ["TARO", "DIANA", "NOVA", "VIBE"]
COLUMNS = ["run_at", "coin", "decision", "confidence", "TARO", "DIANA", "NOVA", "VIBE", "winner",
           "entry", "exit", "ret_24h", "ace_hit", "TARO_hit", "DIANA_hit", "NOVA_hit", "VIBE_hit"]


def hit(view: str, r: float) -> bool | None:
    if not isinstance(view, str) or not view:
        return None
    if view in ("매수", "긍정") or view.startswith("약한 긍정"):
        return r > 0
    if view in ("매도", "부정") or view.startswith("약한 부정"):
        return r < 0
    if view in ("관망", "중립") or view.startswith("관망"):
        return abs(r) < FLAT
    return None


def price_at(coin: str, t: pd.Timestamp) -> float:
    """t가 들어 있는 1시간봉의 시가."""
    start = t.floor("h")
    df = fetch_klines(f"{coin}USDT", "1h", start=str(start), end=str(start + pd.Timedelta(hours=1)))
    if df.empty:
        raise ValueError(f"{coin} {start} 가격 없음")
    return float(df["open"].iloc[0])


def load(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame(columns=COLUMNS)
    df = pd.read_csv(path, dtype=str).fillna("")
    for c in COLUMNS:
        if c not in df:
            df[c] = ""
    return df[COLUMNS]


def score_pending(df: pd.DataFrame, now: pd.Timestamp | None = None, price=price_at) -> int:
    """24시간 지난 미채점 줄을 채점한다. 채점한 줄 수를 돌려준다."""
    now = now or pd.Timestamp.now(tz="UTC")
    done = 0
    for i, row in df.iterrows():
        if row["ret_24h"] != "":
            continue
        t = pd.Timestamp(row["run_at"])
        t = t.tz_localize("UTC") if t.tzinfo is None else t.tz_convert("UTC")
        if t + HORIZON > now:
            continue
        try:
            entry, exit_ = price(row["coin"], t), price(row["coin"], t + HORIZON)
        except Exception:
            continue  # 다음 실행 때 다시 시도
        r = (exit_ / entry - 1) * 100
        df.loc[i, ["entry", "exit", "ret_24h"]] = [f"{entry:g}", f"{exit_:g}", f"{r:.2f}"]
        df.loc[i, "ace_hit"] = str(hit(row["decision"], r))
        for a in AGENTS:
            h = hit(row[a], r)
            df.loc[i, f"{a}_hit"] = "" if h is None else str(h)
        done += 1
    return done


def summary(df: pd.DataFrame) -> dict:
    scored = df[df["ace_hit"].isin(["True", "False"])]

    def rate(s: pd.Series) -> dict:
        s = s[s.isin(["True", "False"])]
        return {"맞음": int((s == "True").sum()), "전체": int(len(s)),
                "승률(%)": round((s == "True").mean() * 100, 1) if len(s) else None}

    return {
        "채점된 의견": int(len(scored)),
        "채점 대기": int((df["ret_24h"] == "").sum()),
        "ACE": rate(scored["ace_hit"]),
        "결정별": {d: rate(scored[scored["decision"] == d]["ace_hit"]) for d in ("매수", "관망", "매도")},
        "애널리스트별": {a: rate(scored[f"{a}_hit"]) for a in AGENTS},
        "코인별": {c: rate(g["ace_hit"]) for c, g in scored.groupby("coin")},
        "기준": f"24시간 뒤 가격. 매수는 오르면, 매도는 내리면, 관망은 ±{FLAT:g}% 안이면 맞음",
    }


def scoreboard_markdown(s: dict, df: pd.DataFrame, when: str) -> str:
    def cell(r):
        return "자료 없음" if r["승률(%)"] is None else f"{r['승률(%)']}% ({r['맞음']}/{r['전체']})"

    lines = [f"# TF팀 승률 ({when})", "", f"기준: {s['기준']}", "",
             f"- **ACE 전체**: {cell(s['ACE'])} · 채점 대기 {s['채점 대기']}개", ""]
    lines += ["| 구분 | 승률 |", "|---|---|"]
    lines += [f"| ACE {d} | {cell(r)} |" for d, r in s["결정별"].items()]
    lines += [f"| {a} | {cell(r)} |" for a, r in s["애널리스트별"].items()]
    lines += ["", "| 코인 | ACE 승률 |", "|---|---|"] + [f"| {c} | {cell(r)} |" for c, r in s["코인별"].items()]
    recent = df[df["ret_24h"] != ""].tail(15)
    if len(recent):
        lines += ["", "**최근 채점**", "", "| 회의 시각 | 코인 | ACE | 24시간 | 결과 |", "|---|---|---|---|---|"]
        lines += [f"| {r.run_at} | {r.coin} | {r.decision} | {r.ret_24h}% | {'✅' if r.ace_hit == 'True' else '❌'} |"
                  for r in recent.itertuples()]
    return "\n".join(lines) + "\n"


def run(folder: Path = Path("paper/tf")) -> dict:
    path = folder / "verdicts.csv"
    df = load(path)
    n = score_pending(df)
    if len(df):
        df.to_csv(path, index=False)
    s = summary(df)
    now = pd.Timestamp.now(tz="Asia/Seoul")
    (folder / "SCOREBOARD.md").write_text(scoreboard_markdown(s, df, f"{now:%Y-%m-%d %H:%M} KST"), encoding="utf-8")
    (folder / "scoreboard.json").write_text(json.dumps(s, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"채점 {n}개, 누적 {s['채점된 의견']}개, ACE 승률 {s['ACE']['승률(%)']}")
    return s
