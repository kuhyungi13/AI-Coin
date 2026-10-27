"""변동성 돌파 전략 (래리 윌리엄스).

하루 규칙 (바이낸스 일봉은 UTC 00:00, 한국 시간 오전 9시에 시작한다):
1. 목표가 = 오늘 시가 + k × (어제 고가 - 어제 저가)
2. 오늘 가격이 목표가를 넘으면 그 가격에 산다.
3. 산 날의 종가(= 다음 날 시가)에 판다. 하루 넘게 들고 있지 않는다.
4. 선택: 어제 종가가 n일 이동평균보다 높을 때(상승 추세)만 거래한다.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass
class Params:
    k: float = 0.5               # 돌파 계수. 작을수록 자주 산다
    fee: float = 0.001           # 거래 수수료(한 번에). 바이낸스 현물 기본 0.1%
    slippage: float = 0.0005     # 원하는 가격보다 불리하게 체결되는 정도(한 번에)
    ma_filter: int | None = None  # 예: 5 → 5일 이동평균 위일 때만 거래


def run(df: pd.DataFrame, p: Params = Params()) -> pd.DataFrame:
    """일봉 DataFrame(open/high/low/close)을 받아 날짜별 거래 결과를 돌려준다."""
    out = df[["open", "high", "low", "close"]].copy()
    prev_range = (df["high"] - df["low"]).shift(1)
    out["target"] = df["open"] + p.k * prev_range

    signal = df["high"] >= out["target"]
    if p.ma_filter:
        ma = df["close"].rolling(p.ma_filter).mean()
        signal &= (df["close"].shift(1) > ma.shift(1))
    out["trade"] = signal & prev_range.notna()

    # 시가가 이미 목표가 위에서 시작하면 시가에 산 것으로 본다.
    entry = np.maximum(df["open"], out["target"]) * (1 + p.slippage)
    exit_ = df["close"] * (1 - p.slippage)
    gross = exit_ / entry
    out["entry"] = entry.where(out["trade"])
    out["exit"] = exit_.where(out["trade"])
    out["ret"] = np.where(out["trade"], gross * (1 - p.fee) ** 2 - 1, 0.0)
    out["equity"] = (1 + out["ret"]).cumprod()
    out["hold_equity"] = df["close"] / df["open"].iloc[0]
    return out


def max_drawdown(equity: pd.Series) -> float:
    return float((equity / equity.cummax() - 1).min())


def summarize(res: pd.DataFrame) -> dict:
    """결과를 사람이 보기 쉬운 숫자 몇 개로 요약한다."""
    days = (res.index[-1] - res.index[0]).days or 1
    years = days / 365.25
    eq, hold = res["equity"], res["hold_equity"]
    trades = res.loc[res["trade"], "ret"]
    daily = res["ret"]
    sharpe = float(daily.mean() / daily.std() * np.sqrt(365)) if daily.std() > 0 else 0.0
    return {
        "기간": f"{res.index[0]:%Y-%m-%d} ~ {res.index[-1]:%Y-%m-%d}",
        "총수익률": eq.iloc[-1] - 1,
        "연평균수익률(CAGR)": eq.iloc[-1] ** (1 / years) - 1,
        "최대낙폭(MDD)": max_drawdown(eq),
        "거래횟수": int(len(trades)),
        "승률": float((trades > 0).mean()) if len(trades) else 0.0,
        "거래당평균수익": float(trades.mean()) if len(trades) else 0.0,
        "샤프지수": sharpe,
        "단순보유_총수익률": hold.iloc[-1] - 1,
        "단순보유_MDD": max_drawdown(hold),
    }
