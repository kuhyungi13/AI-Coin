"""TRAINER: TF팀 보고서(ACE 결정)대로 모의투자를 하는 8번째 팀원. 실제 주문은 절대 내지 않는다.

paper/tf/verdicts.csv 의 ACE 결정을 시간 순서대로 읽어 가상 계좌로 사고판다. 규칙이 정해져 있어 누가 돌려도 같은 결과가 나온다.

보고서 확실성 (0~100, ACE 확신도와 별도로 매긴다)
- ACE 확신도 × 4 (최대 40)
- 애널리스트 4명이 결정과 같은 방향이면 +10, 반대 방향이면 -10 (중립 0)
- 토론 승자가 결정과 같은 편(매수면 BULL)이면 +10, 반대 편이면 -10
- 지난 성적: 그 결정(매수)이 10번 넘게 채점됐고 승률 60% 이상이면 +10, 45% 미만이면 -10
- 0~100 사이로 자른다

레버리지 (확실성으로 정함, 최대 10배)
- 60 미만 1배 · 60~69 2배 · 70~79 3배 · 80~89 5배 · 90 이상 10배
- 증거금 = 총자산 × 확신도 × 2% (최대 20%), 포지션 크기 = 증거금 × 레버리지
- 손절 거리 = min(5%, 30% ÷ 레버리지) → 10배면 가격 -3% (증거금 -30%)에서 손절해 청산(-10%) 전에 끊는다
- 익절 거리 = 손절 거리 × 2

매매 규칙
- 시작 자금 10,000 USDT, 롱만, 수수료는 포지션 크기의 0.1% (펀딩비는 계산하지 않음)
- 매수: ACE가 "매수"이고 확신도 5 이상이면 정상 진입. 확신도 4는 "소액 탐색"으로 증거금 절반·1배만. 동시에 최대 5종목
- 매도: ACE가 "매도"면 들고 있던 코인을 전부 판다. "관망"이면 그대로 둔다.
- 체결 가격: 회의(정각)가 끝난 뒤 첫 정시 1시간봉 시가 = (자료 수집 시각 + 1시간)을 올림한 정시
- 최대 72시간 보유. 1시간봉 고가·저가로 확인하고, 한 봉에서 손절·익절 둘 다 닿으면 손절로 본다.

파일 (paper/tf/trainer/)
- state.json: 현금, 보유 코인, 처리한 결정
- trades.csv: 체결 기록 (확실성, 레버리지 포함)
- equity.csv: 실행 때마다 총자산
- summary.json, TRAINER.md: 요약
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from ..data import fetch_klines

START_CASH = 10_000.0
FEE = 0.001
MIN_CONF = 5
PROBE_CONF = 4  # 소액 탐색: 증거금 절반, 레버리지 1배
PROBE_SIZE = 0.5
SIZE_PER_CONF = 0.02
MAX_SIZE = 0.20
MAX_POSITIONS = 5
BASE_STOP = 0.05
MARGIN_STOP = 0.30
MAX_LEVERAGE = 10
LEVERAGE_STEPS = [(90, 10), (80, 5), (70, 3), (60, 2), (0, 1)]
MAX_HOLD = pd.Timedelta(hours=72)
ANALYSTS = ["TARO", "DIANA", "NOVA", "VIBE"]
TRADE_COLUMNS = ["time", "coin", "side", "price", "qty", "value", "fee", "reason", "pnl", "pnl_pct", "run_at",
                 "certainty", "leverage", "margin"]
RULES = (f"시작 {START_CASH:,.0f} USDT · ACE 매수+확신도 {MIN_CONF} 이상이면 진입(확신도 {PROBE_CONF}는 증거금 절반·1배 탐색) · 증거금 총자산×확신도×2%(최대 20%) · "
         "레버리지는 확실성 60↓1배 60 2배 70 3배 80 5배 90 10배 · 손절 min(5%, 30%÷레버리지), 익절 손절×2 · "
         f"최대 {MAX_POSITIONS}종목 · 최대 72시간 · 수수료 0.1%")


def utc(t) -> pd.Timestamp:
    t = pd.Timestamp(t)
    return t.tz_localize("UTC") if t.tzinfo is None else t.tz_convert("UTC")


def klines_1h(coin: str, start: pd.Timestamp, end: pd.Timestamp) -> pd.DataFrame:
    """[start, end) 사이에 시작한 1시간봉 (UTC 인덱스, open/high/low/close)."""
    df = fetch_klines(f"{coin}USDT", "1h", start=str(start), end=str(end))
    if df.empty:
        return df
    df.index = [utc(i) for i in df.index]
    return df[(df.index >= start) & (df.index < end)]


# ---- 보고서 확실성과 레버리지 ----
def direction(view) -> int:
    """긍정/매수 +1, 부정/매도 -1, 중립/관망·모름 0."""
    v = str(view or "").strip()
    if not v:
        return 0
    if "긍정" in v or v == "매수":
        return 1
    if "부정" in v or v == "매도":
        return -1
    return 0


def certainty(row, board: dict | None = None) -> tuple[int, list[str]]:
    """한 회의 결정의 확실성 점수(0~100)와 점수 내역."""
    decision = str(row.get("decision", "")).strip()
    d = direction(decision)
    try:
        conf = int(float(row.get("confidence", 0)))
    except (TypeError, ValueError):
        conf = 0
    score = conf * 4
    why = [f"ACE 확신도 {conf}/10 → {conf * 4}"]
    if d:
        same = [a for a in ANALYSTS if direction(row.get(a)) == d]
        against = [a for a in ANALYSTS if direction(row.get(a)) == -d]
        score += 10 * len(same) - 10 * len(against)
        why.append(f"같은 방향 애널리스트 {len(same)}명, 반대 {len(against)}명 → {10 * (len(same) - len(against)):+d}")
        winner = str(row.get("winner", "")).strip().upper()
        side = "BULL" if d > 0 else "BEAR"
        other = "BEAR" if d > 0 else "BULL"
        if winner == side:
            score += 10
            why.append(f"토론 {side} 승 → +10")
        elif winner == other:
            score -= 10
            why.append(f"토론 {other} 승 → -10")
        rec = ((board or {}).get("결정별") or {}).get(decision) or {}
        if (rec.get("전체") or 0) >= 10 and rec.get("승률(%)") is not None:
            if rec["승률(%)"] >= 60:
                score += 10
                why.append(f"지난 {decision} 승률 {rec['승률(%)']}% → +10")
            elif rec["승률(%)"] < 45:
                score -= 10
                why.append(f"지난 {decision} 승률 {rec['승률(%)']}% → -10")
    return max(0, min(100, score)), why


def leverage_for(score: int) -> int:
    return next(lev for floor, lev in LEVERAGE_STEPS if score >= floor)


def stop_distance(lev: int) -> float:
    return min(BASE_STOP, MARGIN_STOP / lev)


def new_state() -> dict:
    return {"cash": START_CASH, "start_cash": START_CASH, "positions": {}, "processed": [], "updated_at": ""}


class Trainer:
    def __init__(self, state: dict, klines=klines_1h, board: dict | None = None):
        self.s = state
        self.klines = klines
        self.board = board or {}
        self.trades: list[dict] = []

    @staticmethod
    def value(p: dict, price: float) -> float:
        """포지션 평가액 = 증거금 + 미실현 손익 (0 아래로는 안 내려감)."""
        return max(0.0, p["margin"] + p["qty"] * (price - p["entry"]))

    # ---- 체결 ----
    def _record(self, t, coin, side, price, p, reason, pnl=None, pnl_pct=None):
        notional = price * p["qty"]
        self.trades.append({"time": utc(t).isoformat(), "coin": coin, "side": side, "price": f"{price:g}",
                            "qty": f"{p['qty']:.8g}", "value": f"{notional:.2f}", "fee": f"{notional * FEE:.2f}",
                            "reason": reason, "pnl": "" if pnl is None else f"{pnl:.2f}",
                            "pnl_pct": "" if pnl_pct is None else f"{pnl_pct:.2f}", "run_at": p["run_at"],
                            "certainty": p["certainty"], "leverage": p["leverage"], "margin": f"{p['margin']:.2f}"})

    def buy(self, t, coin, price, confidence, score, run_at):
        probe = confidence < MIN_CONF
        lev = 1 if probe else leverage_for(score)
        margin = self.equity() * min(MAX_SIZE, confidence * SIZE_PER_CONF) * (PROBE_SIZE if probe else 1)
        margin = min(margin, self.s["cash"] / (1 + lev * FEE))
        if margin < 10:
            return
        notional = margin * lev
        stop = stop_distance(lev)
        p = {"qty": notional / price, "entry": price, "margin": margin, "leverage": lev, "certainty": score,
             "fee_in": notional * FEE, "entry_at": utc(t).isoformat(), "checked_to": utc(t).isoformat(),
             "stop": price * (1 - stop), "target": price * (1 + 2 * stop), "stop_pct": stop,
             "confidence": confidence, "run_at": run_at, "last": price}
        self.s["cash"] -= margin + p["fee_in"]
        self.s["positions"][coin] = p
        self._record(t, coin, "매수", price, p, f"ACE 매수 {confidence}/10{' (소액 탐색)' if probe else ''} · 확실성 {score} · {lev}배")

    def sell(self, t, coin, price, reason):
        p = self.s["positions"].pop(coin)
        fee_out = p["qty"] * price * FEE
        back = self.value(p, price) - fee_out
        self.s["cash"] += max(0.0, back)
        cost = p["margin"] + p["fee_in"]
        pnl = max(0.0, back) - cost
        self._record(t, coin, "매도", price, p, reason, pnl, pnl / cost * 100)

    # ---- 손절·익절·기간 만료 ----
    def check_exits(self, until: pd.Timestamp):
        """보유 코인마다 checked_to ~ until 사이 1시간봉을 보며 청산 조건을 확인한다."""
        for coin in list(self.s["positions"]):
            p = self.s["positions"][coin]
            start = utc(p["checked_to"])
            if start >= until:
                continue
            try:
                df = self.klines(coin, start, until)
            except Exception:
                continue  # 다음 실행 때 다시
            expire = utc(p["entry_at"]) + MAX_HOLD
            sp = p["stop_pct"] * 100
            for t, row in df.iterrows():
                if t >= expire:
                    self.sell(t, coin, float(row["open"]), "보유 72시간 만료")
                    break
                if float(row["low"]) <= p["stop"]:
                    self.sell(t, coin, p["stop"], f"손절 -{sp:g}%")
                    break
                if float(row["high"]) >= p["target"]:
                    self.sell(t, coin, p["target"], f"익절 +{2 * sp:g}%")
                    break
                p["last"] = float(row["close"])
                p["checked_to"] = (t + pd.Timedelta(hours=1)).isoformat()

    # ---- ACE 결정 처리 ----
    def apply(self, verdicts: pd.DataFrame, now: pd.Timestamp):
        done = set(self.s["processed"])
        rows = []
        for _, v in verdicts.iterrows():
            key = f"{v['run_at']}|{v['coin']}"
            if key in done or not v["run_at"]:
                continue
            act_at = (utc(v["run_at"]) + pd.Timedelta(hours=1)).ceil("h")
            if act_at > now.floor("h"):
                continue  # 체결할 봉이 아직 안 열림
            rows.append((act_at, key, v))
        for act_at, key, v in sorted(rows, key=lambda r: r[0]):
            self.check_exits(act_at)
            coin, decision = v["coin"], str(v["decision"]).strip()
            try:
                conf = int(float(v["confidence"]))
            except (TypeError, ValueError):
                conf = 0
            held = coin in self.s["positions"]
            want_buy = decision == "매수" and conf >= PROBE_CONF and not held \
                and len(self.s["positions"]) < MAX_POSITIONS
            if want_buy or (decision == "매도" and held):
                try:
                    bar = self.klines(coin, act_at, act_at + pd.Timedelta(hours=1))
                except Exception:
                    continue  # 가격을 못 받으면 처리하지 않고 다음에 다시
                if bar.empty:
                    continue
                price = float(bar["open"].iloc[0])
                if want_buy:
                    score, _ = certainty(v, self.board)
                    self.buy(act_at, coin, price, conf, score, v["run_at"])
                else:
                    self.sell(act_at, coin, price, f"ACE 매도 {conf}/10")
            self.s["processed"].append(key)
            done.add(key)
        self.check_exits(now.floor("h"))

    def equity(self) -> float:
        return self.s["cash"] + sum(self.value(p, p.get("last", p["entry"])) for p in self.s["positions"].values())


def summary(state: dict, trades: pd.DataFrame) -> dict:
    pos = []
    total = 0.0
    for c, p in state["positions"].items():
        px = p.get("last", p["entry"])
        v = Trainer.value(p, px)
        total += v
        pos.append({"코인": c, "레버리지": p["leverage"], "확실성": p["certainty"], "진입가": round(p["entry"], 6),
                    "현재가": round(px, 6), "증거금": round(p["margin"], 2), "평가액": round(v, 2),
                    "수익률(%)": round((v / p["margin"] - 1) * 100, 2), "손절": round(p["stop"], 6),
                    "익절": round(p["target"], 6), "진입": p["entry_at"]})
    equity = state["cash"] + total
    closed = trades[trades["pnl"] != ""] if len(trades) else trades
    wins = int((closed["pnl"].astype(float) > 0).sum()) if len(closed) else 0
    return {"총자산": round(equity, 2), "현금": round(state["cash"], 2), "수익률(%)":
            round((equity / state["start_cash"] - 1) * 100, 2), "보유": pos, "청산 거래": len(closed),
            "이긴 거래": wins, "승률(%)": round(wins / len(closed) * 100, 1) if len(closed) else None,
            "규칙": RULES, "updated_at": state["updated_at"]}


def markdown(sm: dict, trades: pd.DataFrame) -> str:
    out = ["# TRAINER 모의투자 계좌", "",
           "> TF팀 ACE 결정대로 가상으로 사고판 기록입니다. **실제 주문은 없으며 투자 조언이 아닙니다.** "
           "레버리지는 손실도 그만큼 키웁니다.", "",
           f"갱신 {sm['updated_at']} · 규칙: {sm['규칙']}", "",
           f"**총자산 {sm['총자산']:,.2f} USDT ({sm['수익률(%)']:+.2f}%)** · 현금 {sm['현금']:,.2f} · "
           f"청산 {sm['청산 거래']}건, 승률 {sm['승률(%)'] if sm['승률(%)'] is not None else '자료 없음'}%", "",
           "## 보유 코인", ""]
    if sm["보유"]:
        out += ["| 코인 | 레버리지 | 확실성 | 진입가 | 현재가 | 증거금 수익률 | 손절 | 익절 | 진입(UTC) |",
                "|---|---|---|---|---|---|---|---|---|"]
        out += [f"| {p['코인']} | {p['레버리지']}배 | {p['확실성']} | {p['진입가']:g} | {p['현재가']:g} | "
                f"{p['수익률(%)']:+.2f}% | {p['손절']:g} | {p['익절']:g} | {p['진입'][:16]} |" for p in sm["보유"]]
    else:
        out.append("없음 (현금 100%)")
    out += ["", "## 최근 거래 20건", ""]
    if len(trades):
        out += ["| 시각(UTC) | 코인 | 매매 | 가격 | 레버리지 | 이유 | 손익 |", "|---|---|---|---|---|---|---|"]
        for _, t in trades.tail(20).iloc[::-1].iterrows():
            pnl = f"{float(t['pnl']):+.2f} ({float(t['pnl_pct']):+.2f}%)" if t["pnl"] else ""
            out.append(f"| {t['time'][:16]} | {t['coin']} | {t['side']} | {t['price']} | {t['leverage']}배 | "
                       f"{t['reason']} | {pnl} |")
    else:
        out.append("아직 거래 없음. ACE가 확신도 5 이상(4는 소액 탐색)으로 매수를 내면 다음 정시에 삽니다.")
    return "\n".join(out) + "\n"


def run(folder: Path, now: pd.Timestamp | None = None, klines=klines_1h) -> dict:
    """verdicts.csv를 읽어 모의 매매를 진행하고 파일을 쓴다. 요약을 돌려준다."""
    now = utc(now or pd.Timestamp.now(tz="UTC"))
    d = folder / "trainer"
    d.mkdir(parents=True, exist_ok=True)
    sp = d / "state.json"
    state = json.loads(sp.read_text()) if sp.exists() else new_state()
    vpath = folder / "verdicts.csv"
    verdicts = pd.read_csv(vpath, dtype=str).fillna("") if vpath.exists() else pd.DataFrame(
        columns=["run_at", "coin", "decision", "confidence"])
    bpath = folder / "scoreboard.json"
    board = json.loads(bpath.read_text()) if bpath.exists() else {}

    tr = Trainer(state, klines, board)
    tr.apply(verdicts, now)
    state["updated_at"] = now.isoformat()

    tp = d / "trades.csv"
    old = pd.read_csv(tp, dtype=str).fillna("") if tp.exists() else pd.DataFrame(columns=TRADE_COLUMNS)
    trades = pd.concat([old, pd.DataFrame(tr.trades, columns=TRADE_COLUMNS)], ignore_index=True).fillna("")
    trades.to_csv(tp, index=False)
    sp.write_text(json.dumps(state, ensure_ascii=False, indent=1))

    sm = summary(state, trades.astype(str))
    ep = d / "equity.csv"
    line = pd.DataFrame([{"time": now.isoformat(), "equity": sm["총자산"], "cash": sm["현금"],
                          "positions": len(sm["보유"])}])
    (pd.concat([pd.read_csv(ep), line]) if ep.exists() else line).to_csv(ep, index=False)
    (d / "summary.json").write_text(json.dumps(sm, ensure_ascii=False, indent=1))
    (d / "TRAINER.md").write_text(markdown(sm, trades.astype(str)), encoding="utf-8")
    return sm
