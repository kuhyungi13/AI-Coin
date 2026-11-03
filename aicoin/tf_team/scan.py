"""바이낸스 전체 코인 훑기. 정식 회의에 올릴 후보를 고른다 (무료 공개 데이터).

바이낸스에서 지금 거래 중인 USDT 코인 전부의 일봉을 받아, 마감된 캔들만으로 지표를 계산한다.
거래가 적은 코인(30일 하루 평균 거래대금 MIN_VOLUME 미만)과 상장 60일 미만 코인은 뺀다.

후보 두 종류 (정해진 규칙이라 매번 같은 기준으로 고른다)
- 상승 추세: 종가 > MA20 > MA60 이고 RSI 70 미만(과열 제외). 14일 상승률 높은 순.
- 과매도 반등: RSI 30 미만. RSI 낮은 순.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import pandas as pd

from ..data import fetch_klines
from ..universe import usdt_symbols
from .indicators import rsi

MIN_VOLUME = 5_000_000   # USDT, 30일 하루 평균 거래대금
MIN_DAYS = 60
ALWAYS = ["BTC", "ETH"]  # 매번 회의하는 코인


def metrics(df: pd.DataFrame) -> dict | None:
    """마감된 일봉 DataFrame(close, quote_volume 포함) 하나의 요약. 자료가 짧으면 None."""
    if len(df) < MIN_DAYS:
        return None
    c = df["close"]
    ma20, ma60 = c.rolling(20).mean().iloc[-1], c.rolling(60).mean().iloc[-1]
    last = c.iloc[-1]
    vol20 = df["quote_volume"].iloc[-21:-1].mean()
    return {
        "종가": float(last),
        "1일(%)": round((last / c.iloc[-2] - 1) * 100, 2),
        "14일(%)": round((last / c.iloc[-15] - 1) * 100, 2),
        "30일(%)": round((last / c.iloc[-31] - 1) * 100, 2),
        "MA20 거리(%)": round((last / ma20 - 1) * 100, 2),
        "MA60 거리(%)": round((last / ma60 - 1) * 100, 2),
        "추세": "상승" if last > ma20 > ma60 else ("하락" if last < ma20 < ma60 else "혼조"),
        "RSI14": round(float(rsi(c).iloc[-1]), 1),
        "거래대금 30일 평균(USD)": round(float(df["quote_volume"].iloc[-30:].mean())),
        "거래량 배수": round(float(df["quote_volume"].iloc[-1] / vol20), 2) if vol20 else None,
    }


def pick(table: pd.DataFrame, n_trend: int = 2, n_oversold: int = 1) -> dict[str, list[str]]:
    """표(index=코인)에서 정식 회의 후보를 고른다. BTC·ETH는 항상 따로 회의하므로 뺀다."""
    t = table[(table["거래대금 30일 평균(USD)"] >= MIN_VOLUME) & ~table.index.isin(ALWAYS)]
    trend = t[(t["추세"] == "상승") & (t["RSI14"] < 70)].sort_values("14일(%)", ascending=False)
    over = t[t["RSI14"] < 30].sort_values("RSI14")
    return {"상승 추세": list(trend.index[:n_trend]), "과매도 반등": list(over.index[:n_oversold])}


def scan(workers: int = 8, log=print) -> pd.DataFrame:
    symbols = usdt_symbols(include_delisted=False)
    start = f"{pd.Timestamp.now(tz='UTC') - pd.Timedelta(days=MIN_DAYS + 40):%Y-%m-%d}"
    now = pd.Timestamp.now(tz="UTC")
    log(f"바이낸스 USDT 코인 {len(symbols)}개 훑는 중...")

    def one(sym: str):
        try:
            df = fetch_klines(sym, "1d", start=start, quote_volume=True)
            df = df[df.index + pd.Timedelta(days=1) <= now]  # 마감된 캔들만
            m = metrics(df)
            return (sym[:-4], m) if m else None
        except Exception:  # 한 코인 실패는 건너뛴다
            return None

    with ThreadPoolExecutor(workers) as ex:
        rows = [r for r in ex.map(one, symbols) if r]
    table = pd.DataFrame({k: v for k, v in rows}).T
    for col in table.columns:
        if col != "추세":
            table[col] = pd.to_numeric(table[col])
    log(f"지표 계산 완료: {len(table)}개 (상장 {MIN_DAYS}일 미만 등 {len(symbols) - len(table)}개 제외)")
    return table.sort_values("거래대금 30일 평균(USD)", ascending=False)


def scan_markdown(table: pd.DataFrame, picks: dict[str, list[str]], when: str) -> str:
    liquid = table[table["거래대금 30일 평균(USD)"] >= MIN_VOLUME]
    up = (liquid["추세"] == "상승").sum()
    down = (liquid["추세"] == "하락").sum()
    lines = [
        f"# 바이낸스 전체 코인 스캔 ({when})",
        "",
        f"거래 중인 USDT 코인 {len(table)}개 중 거래대금 충분한 {len(liquid)}개 기준 · "
        f"상승 추세 {up}개 · 하락 추세 {down}개 · 혼조 {len(liquid) - up - down}개",
        "",
        "**이번 회의 후보** " + " · ".join(f"{k}: {', '.join(v) or '없음'}" for k, v in picks.items()),
        "",
    ]
    cols = ["종가", "1일(%)", "14일(%)", "30일(%)", "MA20 거리(%)", "MA60 거리(%)", "추세", "RSI14", "거래량 배수", "거래대금 30일 평균(USD)"]
    lines += ["| 코인 | " + " | ".join(cols) + " |", "|" + "---|" * (len(cols) + 1)]
    for coin, r in liquid.iterrows():
        vals = []
        for c in cols:
            v = r[c]
            vals.append(f"{v:,.0f}" if c.startswith("거래대금") else (f"{v:g}" if isinstance(v, float) else str(v)))
        lines.append(f"| {coin} | " + " | ".join(vals) + " |")
    return "\n".join(lines) + "\n"
