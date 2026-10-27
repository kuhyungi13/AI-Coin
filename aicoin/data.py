"""바이낸스 공개 과거 시세(캔들) 데이터를 내려받는다. API 키는 필요 없다."""

from __future__ import annotations

import time
from pathlib import Path

import pandas as pd
import requests

# api.binance.com 이 막혀 있는 지역/네트워크를 위해 공개 데이터 전용 주소도 순서대로 시도한다.
BASE_URLS = [
    "https://data-api.binance.vision",
    "https://api.binance.com",
]
KLINES_PATH = "/api/v3/klines"
LIMIT = 1000  # 바이낸스가 한 번에 주는 최대 캔들 수

COLUMNS = [
    "open_time", "open", "high", "low", "close", "volume",
    "close_time", "quote_volume", "trades", "taker_base", "taker_quote", "ignore",
]


def _get(params: dict) -> list:
    last_error: Exception | None = None
    for base in BASE_URLS:
        try:
            resp = requests.get(base + KLINES_PATH, params=params, timeout=20)
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            last_error = e
    raise RuntimeError(f"바이낸스 데이터를 받지 못했습니다: {last_error}")


def fetch_klines(symbol: str = "BTCUSDT", interval: str = "1d",
                 start: str = "2018-01-01", end: str | None = None,
                 quote_volume: bool = False) -> pd.DataFrame:
    """start~end 기간의 캔들을 모두 받아 DataFrame(index=UTC 날짜)으로 돌려준다.

    quote_volume=True면 거래대금(USDT 기준) 열 quote_volume도 넣는다.
    """
    start_ms = int(pd.Timestamp(start, tz="UTC").timestamp() * 1000)
    end_ms = int(pd.Timestamp(end, tz="UTC").timestamp() * 1000) if end else None

    rows: list = []
    while True:
        params = {"symbol": symbol, "interval": interval, "startTime": start_ms, "limit": LIMIT}
        if end_ms is not None:
            params["endTime"] = end_ms
        batch = _get(params)
        if not batch:
            break
        rows.extend(batch)
        if len(batch) < LIMIT:
            break
        start_ms = batch[-1][0] + 1
        time.sleep(0.2)  # 서버에 부담을 주지 않도록 잠깐 쉰다

    df = pd.DataFrame(rows, columns=COLUMNS)
    df["date"] = pd.to_datetime(df["open_time"], unit="ms", utc=True)
    cols = ["open", "high", "low", "close", "volume"] + (["quote_volume"] if quote_volume else [])
    df = df.set_index("date")[cols].astype(float)
    return df[~df.index.duplicated()].sort_index()


def load_klines(symbol: str = "BTCUSDT", interval: str = "1d", start: str = "2018-01-01",
                end: str | None = None, cache_dir: str | Path = "data",
                refresh: bool = False) -> pd.DataFrame:
    """한 번 받은 데이터는 data/ 폴더에 저장해 두고 다음부터는 저장본을 쓴다."""
    cache = Path(cache_dir) / f"{symbol}_{interval}_{start}_{end or 'now'}.csv"
    if cache.exists() and not refresh:
        return pd.read_csv(cache, index_col="date", parse_dates=["date"])
    df = fetch_klines(symbol, interval, start, end)
    cache.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(cache)
    return df
