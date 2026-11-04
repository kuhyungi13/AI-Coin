"""전략 백테스트 연구실: 어떤 진입 신호가 과거에 실제로 돈이 됐는지 숫자로 비교한다 (모의 연구, 실제 주문 없음).

- 신호는 일봉 종가에서 나오고, 다음 날 시가에 사서 최대 HOLD일 들고 있는다.
- 로스컷은 TRAINER와 같다: 증거금 -10% (가격 하락폭 = 10% ÷ 레버리지). 일봉 저가가 닿으면 그 가격에 판다.
  익절은 없다. 수수료는 한 번 사고팔 때 0.1%씩(포지션 크기 기준).
- 과최적화를 막으려고 앞 기간(학습)과 뒷 기간(검증)을 따로 보여준다. 검증 기간에서도 버티는 신호만 쓸 만하다.
- 상장 폐지된 코인도 데이터가 받아지는 만큼 넣는다 (살아남은 코인만 보면 결과가 부풀려진다).
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .indicators import rsi

FEE = 0.001
LOSSCUT = 0.10
HOLD = 7
SPLIT = "2025-01-01"          # 이 날짜 전은 학습, 이후는 검증
MIN_QUOTE_VOL = 1_000_000     # 신호가 나온 날 직전 30일 평균 거래대금(USDT) 이 정도는 돼야 함


def signals(df: pd.DataFrame) -> dict[str, pd.Series]:
    """코인 하나의 일봉으로 전략별 진입 신호(종가 기준 True/False)를 만든다."""
    c, h = df["close"], df["high"]
    ma20, ma60, ma120 = c.rolling(20).mean(), c.rolling(60).mean(), c.rolling(120).mean()
    r = rsi(c)
    ret30 = c.pct_change(30)
    return {
        "기준선(아무 날이나)": pd.Series(True, index=df.index),
        "추세 추종 (종가>MA20>MA60)": (c > ma20) & (ma20 > ma60),
        "20일 신고가 돌파": c > h.rolling(20).max().shift(1),
        "과매도 반등 (RSI<30)": r < 30,
        "상승 추세 속 눌림 (MA20>MA60, RSI<40)": (ma20 > ma60) & (r < 40),
        "강한 모멘텀 (30일 +20%, 종가>MA20)": (ret30 > 0.20) & (c > ma20),
        "장기 추세 속 과매도 (종가>MA120, RSI<35)": (c > ma120) & (r < 35),
    }


def simulate(df: pd.DataFrame, signal: pd.Series, lev: int = 1, hold: int = HOLD) -> pd.DataFrame:
    """신호가 True인 날마다 다음 날 시가 진입 → 로스컷/기간 만료 청산. 증거금 대비 수익률(%)을 돌려준다."""
    stop = LOSSCUT / lev
    entry = df["open"].shift(-1)
    done = pd.Series(False, index=df.index)
    exit_px = pd.Series(np.nan, index=df.index)
    for k in range(hold):
        low = df["low"].shift(-1 - k)
        hit = (~done) & (low <= entry * (1 - stop)) & low.notna()
        exit_px[hit] = entry[hit] * (1 - stop)
        done |= hit
    last = df["close"].shift(-hold)  # 만료일 종가
    exit_px = exit_px.fillna(last)
    gross = exit_px / entry - 1
    margin_ret = (gross * lev - 2 * FEE * lev) * 100
    ok = signal.fillna(False) & margin_ret.notna()
    return pd.DataFrame({"ret": margin_ret[ok]})


def _stats(rets: pd.Series) -> dict:
    n = len(rets)
    if n == 0:
        return {"n": 0, "win": None, "avg": None, "median": None, "pf": None}
    win = rets[rets > 0]
    loss = rets[rets <= 0]
    pf = float(win.sum() / -loss.sum()) if loss.sum() < 0 else None
    return {"n": n, "win": round(float((rets > 0).mean() * 100), 1), "avg": round(float(rets.mean()), 2),
            "median": round(float(rets.median()), 2), "pf": None if pf is None else round(pf, 2)}


def run(frames: dict[str, pd.DataFrame], lev: int = 1, hold: int = HOLD, split: str = SPLIT) -> dict:
    """전 코인 × 전략을 돌려 학습/검증 통계를 낸다."""
    pools: dict[str, dict[str, list]] = {}
    for sym, df in frames.items():
        if len(df) < 200 or "quote_volume" not in df:
            continue
        liquid = df["quote_volume"].rolling(30).mean() >= MIN_QUOTE_VOL
        for name, sig in signals(df).items():
            res = simulate(df, sig & liquid, lev, hold)
            if res.empty:
                continue
            bucket = pools.setdefault(name, {"train": [], "test": []})
            idx = res.index
            bucket["train"].append(res["ret"][idx < pd.Timestamp(split, tz="UTC")])
            bucket["test"].append(res["ret"][idx >= pd.Timestamp(split, tz="UTC")])
    out = {}
    for name, b in pools.items():
        out[name] = {part: _stats(pd.concat(b[part]) if b[part] else pd.Series(dtype=float)) for part in ("train", "test")}
    return out


def _cell(s: dict) -> str:
    if not s["n"]:
        return "표본 없음"
    pf = "-" if s["pf"] is None else f"{s['pf']}"
    return f"{s['n']:,}건 · 승률 {s['win']}% · 평균 {s['avg']:+.2f}% · 손익비 {pf}"


def markdown(results: dict[int, dict], updated: str, n_coins: int) -> str:
    base = "기준선(아무 날이나)"
    out = ["# 전략 백테스트 결과", "",
           "> 과거 가격으로 시험한 **연구 결과**입니다. 미래 수익을 보장하지 않으며 실제 주문은 없습니다.", "",
           f"갱신 {updated} · 코인 {n_coins}개(상장 폐지 포함) · 일봉 신호 → 다음 날 시가 진입 → 최대 {HOLD}일 보유 · "
           f"로스컷 증거금 -{LOSSCUT * 100:g}% · 수수료 왕복 {2 * FEE * 100:g}% · "
           f"학습 {SPLIT} 이전 / 검증 {SPLIT} 이후", ""]
    for lev, res in sorted(results.items()):
        out += [f"## 레버리지 {lev}배", "", "| 전략 | 학습 | 검증 | 검증 평균 − 기준선 |", "|---|---|---|---|"]
        b = res.get(base, {}).get("test", {}).get("avg")
        ranked = sorted((k for k in res if k != base), key=lambda k: -(res[k]["test"]["avg"] if res[k]["test"]["avg"] is not None else -999))
        for name in [base] + ranked:
            t = res[name]
            edge = "" if name == base or b is None or t["test"]["avg"] is None else f"{t['test']['avg'] - b:+.2f}%p"
            out.append(f"| {name} | {_cell(t['train'])} | {_cell(t['test'])} | {edge} |")
        out.append("")
    out += ["읽는 법: 검증 기간 평균이 기준선보다 높고, 학습과 검증이 같은 방향이며, 표본(건수)이 충분한 신호만 믿을 만합니다. "
            "건수가 적거나 학습에서만 좋은 신호는 우연일 수 있습니다."]
    return "\n".join(out) + "\n"
