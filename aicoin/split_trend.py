"""분할 추세 전략 (워뇨띠가 Q&A에서 밝힌 원칙을 규칙으로 바꾼 것. 본인의 실제 전략은 아니다).

원칙 → 규칙:
- 추세를 따른다: 어제 종가가 n일 이동평균 위일 때만 산다.
- 나눠서 산다: 추세가 이어지면 하루에 1/3씩, 최대 3번 시가에 산다.
- 틀리면 바로 줄인다: 평균 매수가보다 stop만큼 떨어지면 전부 판다.
  손절한 뒤에는 추세가 한 번 꺾였다가 다시 살아날 때까지 사지 않는다.
- 나눠서 판다: 평균 매수가보다 tp 오르면 1/3, 2×tp 오르면 1/3을 판다.
  나머지는 어제 종가가 이동평균 아래로 내려가면 다음 날 시가에 판다.
- 레버리지 없이 현물만 쓴다.

하루 안에서 손절가와 익절가를 둘 다 건드리면 손절이 먼저 일어났다고 본다(보수적으로).
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


@dataclass
class SplitParams:
    ma: int = 50                 # 추세 판단 이동평균 일수
    stop: float = 0.08           # 평균 매수가 대비 손절 폭
    tp: float = 0.15             # 첫 익절 폭 (두 번째는 2배)
    tranches: int = 3            # 몇 번에 나눠 살지
    fee: float = 0.001
    slippage: float = 0.0005


def run_split(df: pd.DataFrame, p: SplitParams = SplitParams(), start=None,
              log: list | None = None) -> tuple[pd.DataFrame, pd.Series]:
    """날짜별 결과(strategy.summarize와 같은 열)와, 끝난 날짜별 거래 수익률을 돌려준다.

    start: 이 날짜 전에는 거래하지 않는다(이동평균 계산용 앞 데이터만 쓴다).
    log: 리스트를 주면 사고판 기록(날짜, 종류, 가격, 수량, 금액)을 하나씩 넣어 준다.
    """
    ma = df["close"].rolling(p.ma).mean()
    trend = (df["close"] > ma).shift(1, fill_value=False)
    if start is not None:
        start = pd.Timestamp(start)
        if start.tzinfo is None:
            start = start.tz_localize(df.index.tz)
        trend &= df.index >= start

    cash, qty = 1.0, 0.0
    cost = 0.0          # 지금 들고 있는 코인에 쓴 돈(수수료 포함)
    bought = 0          # 이번 포지션에서 산 횟수
    tp_done = 0         # 이번 포지션에서 익절한 횟수
    base_qty = 0.0      # 익절 1회분 = 다 산 시점 수량의 1/3
    unit = 0.0          # 한 번 살 때 쓸 돈
    locked = False      # 손절 후 추세가 꺾일 때까지 재진입 금지
    entry_value = 0.0   # 거래별 수익률 계산용: 이번 포지션에 넣은 돈
    exit_value = 0.0    # 이번 포지션에서 돌려받은 돈
    trades: dict[pd.Timestamp, float] = {}
    today = None
    equity, in_pos = [], []

    def record(action: str, price: float, q: float, amount: float) -> None:
        if log is not None:
            log.append({"date": today, "action": action, "price": price,
                        "qty": q, "amount": amount})

    def sell(q: float, price: float, action: str) -> None:
        nonlocal cash, qty, cost, exit_value
        got = q * price * (1 - p.slippage) * (1 - p.fee)
        record(action, price, q, got)
        cost -= cost * (q / qty)
        cash += got
        qty -= q
        exit_value += got

    def close_trade() -> None:
        nonlocal qty, cost, bought, tp_done, entry_value, exit_value
        trades[today] = exit_value / entry_value - 1
        qty, cost, bought, tp_done, entry_value, exit_value = 0.0, 0.0, 0, 0, 0.0, 0.0

    for today, o, h, l, c, up in zip(df.index, df["open"], df["high"], df["low"], df["close"], trend):
        if not up:
            locked = False
        # 시가: 추세가 꺾였으면 정리, 이어지면 한 칸 더 산다.
        if qty > 0 and not up:
            sell(qty, o, "추세이탈 매도")
            close_trade()
        elif up and not locked and bought < p.tranches and tp_done == 0:
            if bought == 0:
                unit = cash / p.tranches
            spend = min(unit, cash)
            q = spend * (1 - p.fee) / (o * (1 + p.slippage))
            qty += q
            cost += spend
            cash -= spend
            entry_value += spend
            bought += 1
            record(f"매수 {bought}/{p.tranches}", o, q, spend)
            base_qty = qty / p.tranches

        # 장중: 손절 먼저, 그다음 분할 익절.
        if qty > 0:
            avg = cost / qty
            stop_px = avg * (1 - p.stop)
            if l <= stop_px:
                sell(qty, min(o, stop_px), "손절")
                close_trade()
                locked = True
            else:
                for level in (1, 2):
                    px = avg * (1 + p.tp * level)
                    if tp_done < level and h >= px and qty > 0:
                        sell(min(base_qty, qty), max(o, px), f"익절 {level}")
                        tp_done = level
                if qty <= 1e-12:
                    close_trade()

        equity.append(cash + qty * c)
        in_pos.append(qty > 0)

    out = df[["open", "high", "low", "close"]].copy()
    out["equity"] = equity
    out["ret"] = out["equity"].pct_change().fillna(out["equity"].iloc[0] - 1)
    out["trade"] = in_pos
    out["hold_equity"] = df["close"] / df["open"].iloc[0]
    return out, pd.Series(trades, dtype=float)
