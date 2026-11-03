"""TRAINER: TF팀 보고서(ACE 결정)대로 모의투자를 하는 8번째 팀원. 실제 주문은 절대 내지 않는다.

paper/tf/verdicts.csv 의 ACE 결정을 시간 순서대로 읽어 가상 계좌로 사고판다. 규칙이 정해져 있어 누가 돌려도 같은 결과가 나온다.

매매 규칙
- 시작 자금 10,000 USDT, 현물만 (공매도 없음), 수수료 0.1%
- 매수: ACE가 "매수"이고 확신도 6 이상일 때. 금액 = 총자산 × 확신도 × 2% (최대 20%), 동시에 최대 5종목
- 매도: ACE가 "매도"면 들고 있던 코인을 전부 판다. "관망"이면 그대로 둔다.
- 체결 가격: 회의가 끝난 다음 정시 1시간봉 시가 (자료 수집 시각 + 1시간)
- 손절 -5%, 익절 +10%, 최대 72시간 보유. 1시간봉 고가·저가로 확인하고, 한 봉에서 둘 다 닿으면 손절로 본다.

파일 (paper/tf/trainer/)
- state.json: 현금, 보유 코인, 처리한 결정
- trades.csv: 체결 기록
- equity.csv: 실행 때마다 총자산
- TRAINER.md: 사람이 읽는 요약
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from ..data import fetch_klines

START_CASH = 10_000.0
FEE = 0.001
MIN_CONF = 6
SIZE_PER_CONF = 0.02
MAX_SIZE = 0.20
MAX_POSITIONS = 5
STOP = -0.05
TAKE = 0.10
MAX_HOLD = pd.Timedelta(hours=72)
TRADE_COLUMNS = ["time", "coin", "side", "price", "qty", "value", "fee", "reason", "pnl", "pnl_pct", "run_at"]
RULES = (f"시작 {START_CASH:,.0f} USDT · 매수는 ACE 매수+확신도 {MIN_CONF} 이상, 금액 총자산×확신도×2%(최대 20%) · "
         f"최대 {MAX_POSITIONS}종목 · 손절 {STOP:.0%} · 익절 +{TAKE:.0%} · 최대 {MAX_HOLD.days * 24}시간 · 수수료 0.1%")


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


def new_state() -> dict:
    return {"cash": START_CASH, "start_cash": START_CASH, "positions": {}, "processed": [], "updated_at": ""}


class Trainer:
    def __init__(self, state: dict, klines=klines_1h):
        self.s = state
        self.klines = klines
        self.trades: list[dict] = []
        self.last_price: dict[str, float] = {}

    # ---- 체결 ----
    def _record(self, t, coin, side, price, qty, reason, run_at, pnl=None, pnl_pct=None):
        value = price * qty
        self.trades.append({"time": utc(t).isoformat(), "coin": coin, "side": side, "price": f"{price:g}",
                            "qty": f"{qty:.8g}", "value": f"{value:.2f}", "fee": f"{value * FEE:.2f}",
                            "reason": reason, "pnl": "" if pnl is None else f"{pnl:.2f}",
                            "pnl_pct": "" if pnl_pct is None else f"{pnl_pct:.2f}", "run_at": run_at})

    def buy(self, t, coin, price, confidence, run_at):
        equity = self.equity_estimate()
        budget = min(equity * min(MAX_SIZE, confidence * SIZE_PER_CONF), self.s["cash"] / (1 + FEE))
        if budget < 10:
            return
        qty = budget / price
        self.s["cash"] -= budget * (1 + FEE)
        self.s["positions"][coin] = {"qty": qty, "entry": price, "cost": budget * (1 + FEE),
                                     "entry_at": utc(t).isoformat(), "checked_to": utc(t).isoformat(),
                                     "stop": price * (1 + STOP), "target": price * (1 + TAKE),
                                     "confidence": confidence, "run_at": run_at}
        self.last_price[coin] = price
        self._record(t, coin, "매수", price, qty, f"ACE 매수 {confidence}/10", run_at)

    def sell(self, t, coin, price, reason):
        p = self.s["positions"].pop(coin)
        proceeds = p["qty"] * price * (1 - FEE)
        self.s["cash"] += proceeds
        pnl = proceeds - p["cost"]
        self.last_price[coin] = price
        self._record(t, coin, "매도", price, p["qty"], reason, p["run_at"], pnl, pnl / p["cost"] * 100)

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
            for t, row in df.iterrows():
                if t >= expire:
                    self.sell(t, coin, float(row["open"]), "보유 72시간 만료")
                    break
                if float(row["low"]) <= p["stop"]:
                    self.sell(t, coin, p["stop"], "손절 -5%")
                    break
                if float(row["high"]) >= p["target"]:
                    self.sell(t, coin, p["target"], "익절 +10%")
                    break
                self.last_price[coin] = p["last"] = float(row["close"])
                p["checked_to"] = (t + pd.Timedelta(hours=1)).isoformat()

    # ---- ACE 결정 처리 ----
    def apply(self, verdicts: pd.DataFrame, now: pd.Timestamp):
        done = set(self.s["processed"])
        rows = []
        for _, v in verdicts.iterrows():
            key = f"{v['run_at']}|{v['coin']}"
            if key in done or not v["run_at"]:
                continue
            act_at = utc(v["run_at"]).floor("h") + pd.Timedelta(hours=1)
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
            want_buy = decision == "매수" and conf >= MIN_CONF and not held \
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
                    self.buy(act_at, coin, price, conf, v["run_at"])
                else:
                    self.sell(act_at, coin, price, f"ACE 매도 {conf}/10")
            self.s["processed"].append(key)
            done.add(key)
        self.check_exits(now.floor("h"))

    def equity_estimate(self) -> float:
        return self.s["cash"] + sum(p["qty"] * self.last_price.get(c, p.get("last", p["entry"]))
                                    for c, p in self.s["positions"].items())


def summary(state: dict, trades: pd.DataFrame, last_price: dict[str, float]) -> dict:
    pos = []
    value = 0.0
    for c, p in state["positions"].items():
        px = last_price.get(c, p.get("last", p["entry"]))
        v = p["qty"] * px
        value += v
        pos.append({"코인": c, "진입가": round(p["entry"], 6), "현재가": round(px, 6), "평가액": round(v, 2),
                    "수익률(%)": round((px / p["entry"] - 1) * 100, 2), "손절": round(p["stop"], 6),
                    "익절": round(p["target"], 6), "진입": p["entry_at"]})
    equity = state["cash"] + value
    closed = trades[trades["pnl"] != ""] if len(trades) else trades
    wins = int((closed["pnl"].astype(float) > 0).sum()) if len(closed) else 0
    return {"총자산": round(equity, 2), "현금": round(state["cash"], 2), "수익률(%)":
            round((equity / state["start_cash"] - 1) * 100, 2), "보유": pos, "청산 거래": len(closed),
            "이긴 거래": wins, "승률(%)": round(wins / len(closed) * 100, 1) if len(closed) else None,
            "규칙": RULES, "updated_at": state["updated_at"]}


def markdown(sm: dict, trades: pd.DataFrame) -> str:
    out = ["# TRAINER 모의투자 계좌", "",
           "> TF팀 ACE 결정대로 가상으로 사고판 기록입니다. **실제 주문은 없으며 투자 조언이 아닙니다.**", "",
           f"갱신 {sm['updated_at']} · 규칙: {sm['규칙']}", "",
           f"**총자산 {sm['총자산']:,.2f} USDT ({sm['수익률(%)']:+.2f}%)** · 현금 {sm['현금']:,.2f} · "
           f"청산 {sm['청산 거래']}건, 승률 {sm['승률(%)'] if sm['승률(%)'] is not None else '자료 없음'}%", "",
           "## 보유 코인", ""]
    if sm["보유"]:
        out += ["| 코인 | 진입가 | 현재가 | 수익률 | 손절 | 익절 | 진입(UTC) |", "|---|---|---|---|---|---|---|"]
        out += [f"| {p['코인']} | {p['진입가']:g} | {p['현재가']:g} | {p['수익률(%)']:+.2f}% | {p['손절']:g} | "
                f"{p['익절']:g} | {p['진입'][:16]} |" for p in sm["보유"]]
    else:
        out.append("없음 (현금 100%)")
    out += ["", "## 최근 거래 20건", ""]
    if len(trades):
        out += ["| 시각(UTC) | 코인 | 매매 | 가격 | 금액 | 이유 | 손익 |", "|---|---|---|---|---|---|---|"]
        for _, t in trades.tail(20).iloc[::-1].iterrows():
            pnl = f"{float(t['pnl']):+.2f} ({float(t['pnl_pct']):+.2f}%)" if t["pnl"] else ""
            out.append(f"| {t['time'][:16]} | {t['coin']} | {t['side']} | {t['price']} | {t['value']} | "
                       f"{t['reason']} | {pnl} |")
    else:
        out.append("아직 거래 없음. ACE가 확신도 6 이상으로 매수를 내면 다음 정시에 삽니다.")
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

    tr = Trainer(state, klines)
    tr.apply(verdicts, now)
    state["updated_at"] = now.isoformat()

    tp = d / "trades.csv"
    old = pd.read_csv(tp, dtype=str).fillna("") if tp.exists() else pd.DataFrame(columns=TRADE_COLUMNS)
    trades = pd.concat([old, pd.DataFrame(tr.trades, columns=TRADE_COLUMNS)], ignore_index=True)
    trades.to_csv(tp, index=False)
    sp.write_text(json.dumps(state, ensure_ascii=False, indent=1))

    sm = summary(state, trades, tr.last_price)
    ep = d / "equity.csv"
    line = pd.DataFrame([{"time": now.isoformat(), "equity": sm["총자산"], "cash": sm["현금"],
                          "positions": len(sm["보유"])}])
    (pd.concat([pd.read_csv(ep), line]) if ep.exists() else line).to_csv(ep, index=False)
    (d / "summary.json").write_text(json.dumps(sm, ensure_ascii=False, indent=1))
    (d / "TRAINER.md").write_text(markdown(sm, trades), encoding="utf-8")
    return sm
