"""분할 추세 전략에 넣을 "상승 추세" 신호들.

모두 캔들 종가 기준 True/False 시리즈를 돌려준다(다음 캔들 시가에 사고판다).
True가 되면 분할 매수를 시작하고, False가 되면 남은 물량을 판다.
"""

from __future__ import annotations

import pandas as pd


def atr(df: pd.DataFrame, n: int = 14) -> pd.Series:
    prev = df["close"].shift(1)
    tr = pd.concat([df["high"] - df["low"], (df["high"] - prev).abs(), (df["low"] - prev).abs()],
                   axis=1).max(axis=1)
    return tr.ewm(alpha=1 / n, adjust=False).mean()


def latch(enter: pd.Series, leave: pd.Series) -> pd.Series:
    """enter가 뜨면 켜지고 leave가 뜰 때까지 켜져 있는 신호."""
    on, out = False, []
    for e, x in zip(enter.fillna(False), leave.fillna(False)):
        if on and x:
            on = False
        elif not on and e:
            on = True
        out.append(on)
    return pd.Series(out, index=enter.index)


def ma_gate(df: pd.DataFrame, n: int = 50) -> pd.Series:
    """지금 쓰는 방식: 종가 > n일 단순 이동평균."""
    return df["close"] > df["close"].rolling(n).mean()


def ema_gate(df: pd.DataFrame, n: int = 20) -> pd.Series:
    """종가 > n일 지수 이동평균(최근 가격에 더 빨리 반응)."""
    return df["close"] > df["close"].ewm(span=n, adjust=False).mean()


def loose_ma(df: pd.DataFrame, n: int = 50, k: float = 1.0) -> pd.Series:
    """변동성만큼 느슨한 이동평균: 종가 > n일선 - k×ATR."""
    return df["close"] > df["close"].rolling(n).mean() - k * atr(df)


def keltner(df: pd.DataFrame, n: int = 20, k: float = 1.0) -> pd.Series:
    """켈트너 돌파: 종가가 n일 EMA + k×ATR을 넘으면 사고, EMA 아래로 내려가면 판다."""
    mid = df["close"].ewm(span=n, adjust=False).mean()
    return latch(df["close"] > mid + k * atr(df), df["close"] < mid)


def bollinger(df: pd.DataFrame, n: int = 20, k: float = 1.0) -> pd.Series:
    """볼린저 돌파: 종가가 n일선 + k×표준편차를 넘으면 사고, n일선 아래로 내려가면 판다."""
    mid = df["close"].rolling(n).mean()
    return latch(df["close"] > mid + k * df["close"].rolling(n).std(), df["close"] < mid)


def supertrend(df: pd.DataFrame, n: int = 10, k: float = 3.0) -> pd.Series:
    """슈퍼트렌드: ATR 폭만큼 떨어진 추적선 위면 상승, 아래로 깨지면 하락."""
    a = atr(df, n)
    hl2 = (df["high"] + df["low"]) / 2
    upper, lower = (hl2 + k * a).tolist(), (hl2 - k * a).tolist()
    close = df["close"].tolist()
    up, out = False, []
    for i in range(len(close)):
        if i > 0:
            if close[i - 1] > lower[i - 1]:
                lower[i] = max(lower[i], lower[i - 1])
            if close[i - 1] < upper[i - 1]:
                upper[i] = min(upper[i], upper[i - 1])
            if up and close[i] < lower[i]:
                up = False
            elif not up and close[i] > upper[i]:
                up = True
        out.append(up)
    return pd.Series(out, index=df.index) & a.notna()


def donchian(df: pd.DataFrame, n: int = 20, m: int = 10) -> pd.Series:
    """돈키언 돌파: 종가가 지난 n일 최고가를 넘으면 사고, 지난 m일 최저가 아래로 내려가면 판다."""
    hi = df["high"].rolling(n).max().shift(1)
    lo = df["low"].rolling(m).min().shift(1)
    return latch(df["close"] > hi, df["close"] < lo)
