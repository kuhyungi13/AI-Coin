"""TARO(차트 담당)가 보는 기술적 지표. 일봉 DataFrame(open/high/low/close/volume)만 있으면 계산된다."""

from __future__ import annotations

import pandas as pd


def rsi(close: pd.Series, n: int = 14) -> pd.Series:
    """RSI: 70 이상이면 과열, 30 이하면 과매도로 흔히 본다 (와일더 평균)."""
    diff = close.diff()
    up = diff.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    down = (-diff.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    rs = up / down
    out = 100 - 100 / (1 + rs)
    return out.where(down != 0, 100.0)


def atr_pct(df: pd.DataFrame, n: int = 14) -> pd.Series:
    """하루 평균 흔들림 폭(ATR)을 종가 대비 %로."""
    prev = df["close"].shift(1)
    tr = pd.concat([df["high"] - df["low"], (df["high"] - prev).abs(), (df["low"] - prev).abs()], axis=1).max(axis=1)
    return tr.rolling(n).mean() / df["close"] * 100


def last_cross(ma_fast: pd.Series, ma_slow: pd.Series) -> tuple[str, int] | None:
    """가장 최근 골든크로스/데드크로스와 그게 며칠 전이었는지."""
    above = (ma_fast > ma_slow).dropna()
    above = above[ma_fast.notna() & ma_slow.notna()]
    flips = above.ne(above.shift(1)) & above.shift(1).notna()
    if not flips.any():
        return None
    when = flips[flips].index[-1]
    kind = "골든크로스" if above.loc[when] else "데드크로스"
    return kind, int(len(above) - 1 - above.index.get_loc(when))


def technical_snapshot(df: pd.DataFrame) -> dict:
    """마지막 캔들 기준 지표 묶음. 숫자는 사람이 읽기 좋게 반올림한다."""
    c = df["close"]
    ma20, ma60, ma120 = c.rolling(20).mean(), c.rolling(60).mean(), c.rolling(120).mean()
    last = c.iloc[-1]

    def chg(days: int) -> float | None:
        return round((last / c.iloc[-1 - days] - 1) * 100, 2) if len(c) > days else None

    def gap(ma: pd.Series) -> float | None:
        v = ma.iloc[-1]
        return None if pd.isna(v) else round((last / v - 1) * 100, 2)

    vol_ratio = None
    if "volume" in df and len(df) >= 21:
        avg = df["volume"].iloc[-21:-1].mean()
        vol_ratio = round(df["volume"].iloc[-1] / avg, 2) if avg else None

    cross = last_cross(ma20, ma60)
    hi30, lo30 = df["high"].iloc[-30:].max(), df["low"].iloc[-30:].min()
    return {
        "기준일": str(df.index[-1].date()) if hasattr(df.index[-1], "date") else str(df.index[-1]),
        "종가": round(float(last), 6),
        "등락률(%)": {"1일": chg(1), "7일": chg(7), "30일": chg(30), "90일": chg(90)},
        "이동평균": {
            "MA20": None if pd.isna(ma20.iloc[-1]) else round(float(ma20.iloc[-1]), 6),
            "MA60": None if pd.isna(ma60.iloc[-1]) else round(float(ma60.iloc[-1]), 6),
            "MA120": None if pd.isna(ma120.iloc[-1]) else round(float(ma120.iloc[-1]), 6),
        },
        "종가와 이평선 거리(%)": {"MA20": gap(ma20), "MA60": gap(ma60), "MA120": gap(ma120)},
        "MA20>MA60": None if pd.isna(ma60.iloc[-1]) else bool(ma20.iloc[-1] > ma60.iloc[-1]),
        "최근 교차": None if cross is None else {"종류": cross[0], "며칠 전": cross[1]},
        "RSI14": round(float(rsi(c).iloc[-1]), 1),
        "ATR14(%)": None if len(df) < 15 else round(float(atr_pct(df).iloc[-1]), 2),
        "거래량(20일 평균 대비 배수)": vol_ratio,
        "30일 최고가": round(float(hi30), 6),
        "30일 최저가": round(float(lo30), 6),
        "최근 10일 종가": [round(float(x), 6) for x in c.iloc[-10:]],
    }
