"""여러 코인 중 오르는 코인을 골라 들고 있다가 주기적으로 바꾸는 전략(코인 고르기).

고르는 방법 (전부 '어제 종가까지' 알던 정보만 쓴다):
1. 후보: 상장된 지 min_age일 넘었고, 최근 30일 거래대금이 상위 top_n인 코인.
   거래가 적은 코인은 사고팔 때 손해가 크고 조작되기 쉬워서 뺀다.
2. 추세: 종가가 자기 ma일 이동평균 위인 코인만 남긴다.
3. 점수: 최근 lookback일 동안 오른 비율. 높은 순서로 picks개를 고른다.
4. 시장 날씨: 비트코인이 자기 ma일 이동평균 아래면 아무것도 사지 않는다(전부 현금).

사고팔기:
- rebalance일마다 시가에 바꾼다. 빠진 코인은 팔고, 새로 뽑힌 코인은 전체 돈의 1/picks씩 산다.
  계속 뽑힌 코인은 그대로 둔다(수수료 아끼기). 자리가 비면 그만큼 현금으로 둔다.
- 매일: 비트코인 추세가 꺾였으면 다음 날 시가에 전부 판다.
  exit_ma=True면 들고 있는 코인 하나가 자기 이동평균 아래로 내려가도 그 코인만 판다.
- 들고 있던 코인이 상장 폐지되면 마지막 종가에 팔았다고 본다.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass
class RotationParams:
    top_n: int = 10          # 거래대금 상위 몇 개 중에서 고를지
    picks: int = 5           # 몇 개를 들고 있을지
    lookback: int = 14       # 몇 일 동안 오른 비율로 순위를 매길지
    ma: int = 50             # 추세 판단 이동평균 일수 (코인, 비트코인 같이)
    rebalance: int = 7       # 며칠마다 바꿀지
    min_age: int = 90        # 상장 후 며칠 지나야 후보가 되는지
    exit_ma: bool = True     # 코인별 추세가 꺾이면 바로 팔지
    btc_filter: bool = True  # 비트코인 추세로 시장 날씨를 볼지
    vs_btc: bool = False     # 비트코인보다 더 오른 코인만 고르고, 빈 자리는 비트코인으로 채울지
    fee: float = 0.001
    slippage: float = 0.0005


@dataclass
class Panels:
    """날짜×코인 표들. load_many 결과에서 만든다."""
    open: pd.DataFrame
    close: pd.DataFrame
    qvol: pd.DataFrame

    @classmethod
    def from_frames(cls, frames: dict[str, pd.DataFrame]) -> "Panels":
        def p(col):
            return pd.DataFrame({s: df[col] for s, df in frames.items()}).sort_index()
        return cls(p("open"), p("close"), p("quote_volume"))


def scores(px: Panels, p: RotationParams) -> dict[str, pd.DataFrame]:
    """날짜별 '어제 종가까지'로 계산한 후보 여부·추세·점수. 오늘 시가에 쓸 수 있도록 하루 밀어 둔다."""
    close = px.close
    age = close.notna().cumsum()
    vol30 = px.qvol.rolling(30, min_periods=1).sum()
    alive = close.notna() & (age >= p.min_age)
    rank = vol30.where(alive).rank(axis=1, ascending=False)
    eligible = rank <= p.top_n
    ma = close.rolling(p.ma, min_periods=p.ma).mean()
    up = close > ma
    mom = close / close.shift(p.lookback) - 1
    btc = close["BTCUSDT"]
    btc_up = btc > btc.rolling(p.ma).mean()
    if not p.btc_filter:
        btc_up = pd.Series(True, index=close.index)
    sh = lambda x: x.shift(1)
    return {"eligible": sh(eligible).fillna(False).astype(bool), "up": sh(up).fillna(False).astype(bool),
            "mom": sh(mom), "btc_up": sh(btc_up).fillna(False).astype(bool), "rank": sh(rank)}


def pick(sc: dict[str, pd.DataFrame], day, p: RotationParams) -> list[str]:
    """그날 시가에 들고 있어야 할 코인들(점수 높은 순)."""
    if not sc["btc_up"].loc[day]:
        return []
    ok = sc["eligible"].loc[day] & sc["up"].loc[day]
    m = sc["mom"].loc[day][ok].dropna()
    m = m[m > 0]
    if p.vs_btc:
        btc_mom = sc["mom"].loc[day, "BTCUSDT"]
        m = m[(m > btc_mom) | (m.index == "BTCUSDT")]
    return list(m.sort_values(ascending=False).index[: p.picks])


def run_rotation(px: Panels, p: RotationParams = RotationParams(), start=None,
                 log: list | None = None) -> tuple[pd.DataFrame, pd.Series]:
    """날짜별 결과(strategy.summarize와 같은 열)와, 끝난 거래별 수익률을 돌려준다."""
    sc = scores(px, p)
    dates = px.close.index
    if start is not None:
        start = pd.Timestamp(start)
        if start.tzinfo is None and dates.tz is not None:
            start = start.tz_localize(dates.tz)
        dates = dates[dates >= start]
    opens, closes = px.open, px.close
    last_close = closes.ffill()

    cash = 1.0
    qty: dict[str, float] = {}
    spent: dict[str, float] = {}     # 거래별 수익률 계산용
    trades: dict[tuple, float] = {}
    equity, n_held = [], []
    buy_cost = (1 + p.slippage) / (1 - p.fee)
    sell_keep = (1 - p.slippage) * (1 - p.fee)

    def sell(sym: str, price: float, day, why: str) -> None:
        nonlocal cash
        got = qty.pop(sym) * price * sell_keep
        cash += got
        trades[(day, sym)] = got / spent.pop(sym) - 1
        if log is not None:
            log.append({"date": day, "symbol": sym, "action": why, "price": price, "amount": got})

    for i, day in enumerate(dates):
        o = opens.loc[day]
        # 상장 폐지(또는 거래 중단)돼서 오늘 가격이 없는 코인은 마지막 종가에 판 것으로 친다.
        for sym in [s for s in qty if np.isnan(o.get(s, np.nan))]:
            sell(sym, last_close.loc[day, sym], day, "상장폐지")

        if not sc["btc_up"].loc[day]:
            for sym in list(qty):
                sell(sym, o[sym], day, "시장 하락 매도")
        elif p.exit_ma:
            for sym in [s for s in qty if not sc["up"].loc[day, s]]:
                sell(sym, o[sym], day, "추세이탈 매도")

        if i % p.rebalance == 0:
            target = [s for s in pick(sc, day, p) if not np.isnan(o[s])]
            for sym in [s for s in qty if s not in target]:
                sell(sym, o[sym], day, "순위 밀려 매도")
            total = cash + sum(q * o[s] for s, q in qty.items())
            for sym in target:
                if sym in qty or cash <= 1e-9:
                    continue
                spend = min(total / p.picks, cash)
                qty[sym] = spend / (o[sym] * buy_cost)
                spent[sym] = spend
                cash -= spend
                if log is not None:
                    log.append({"date": day, "symbol": sym, "action": "매수", "price": o[sym], "amount": spend})

        c = last_close.loc[day]
        equity.append(cash + sum(q * c[s] for s, q in qty.items()))
        n_held.append(len(qty))

    # open/close는 비교용 비트코인 가격 (strategy.period가 그냥 보유 수익률을 다시 계산할 때 쓴다).
    out = pd.DataFrame({"open": opens["BTCUSDT"].loc[dates], "close": closes["BTCUSDT"].loc[dates]})
    out["equity"] = equity
    out["ret"] = out["equity"].pct_change().fillna(out["equity"].iloc[0] - 1)
    out["trade"] = np.array(n_held) > 0
    out["held"] = n_held
    out["hold_equity"] = out["close"] / out["open"].iloc[0]
    return out, pd.Series(trades, dtype=float)
