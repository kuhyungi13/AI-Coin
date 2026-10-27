"""바이낸스 USDT 코인 목록과 여러 코인의 일봉을 한꺼번에 받는다.

과거를 시험할 때 지금 살아남은 코인만 쓰면 결과가 부풀려진다(망한 코인이 빠지므로).
그래서 상장 폐지된 코인(status=BREAK)도 받을 수 있는 만큼 같이 받는다.
"""

from __future__ import annotations

import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import pandas as pd
import requests

from .data import BASE_URLS, fetch_klines

# 달러에 묶인 코인, 법정화폐, 금 코인은 오르내림이 거의 없어 고를 이유가 없다.
STABLE = {
    "USDC", "BUSD", "TUSD", "USDP", "PAX", "DAI", "FDUSD", "USDS", "USDSB", "UST", "USTC",
    "SUSD", "USDD", "AEUR", "EUR", "EURI", "GBP", "AUD", "XUSD", "USD1", "BFUSD", "PAXG",
    "RLUSD", "USDE", "USDT", "U", "BKRW", "IDRT", "BIDR", "NGN", "TRY", "BRL", "ZAR",
}
# BTCUP, ETHDOWN, BNBBULL 같은 레버리지 토큰은 장기 보유용이 아니다.
LEVERAGED = re.compile(r".+(UP|DOWN|BULL|BEAR)$")


def usdt_symbols(include_delisted: bool = True) -> list[str]:
    """USDT로 사고파는 코인 목록. 스테이블코인과 레버리지 토큰은 뺀다."""
    for base in BASE_URLS:
        try:
            info = requests.get(base + "/api/v3/exchangeInfo", timeout=30).json()
            break
        except requests.RequestException:
            continue
    else:
        raise RuntimeError("바이낸스 코인 목록을 받지 못했습니다")
    out = []
    for s in info["symbols"]:
        if s["quoteAsset"] != "USDT":
            continue
        if s["status"] != "TRADING" and not include_delisted:
            continue
        coin = s["baseAsset"]
        if coin in STABLE or (LEVERAGED.match(coin) and coin not in ("JUP", "SUP")):
            continue
        out.append(s["symbol"])
    return sorted(out)


def load_many(symbols: list[str], start: str = "2018-01-01", cache_dir: str | Path = "data/daily",
              refresh: bool = False, workers: int = 6) -> dict[str, pd.DataFrame]:
    """코인별 일봉(시가·고가·저가·종가·거래대금). 한 번 받은 것은 cache_dir에 저장해 다시 쓴다."""
    cache_dir = Path(cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)

    def one(sym: str) -> tuple[str, pd.DataFrame | None]:
        path = cache_dir / f"{sym}.csv"
        if path.exists() and not refresh:
            return sym, pd.read_csv(path, index_col="date", parse_dates=["date"])
        try:
            df = fetch_klines(sym, "1d", start, quote_volume=True)
        except RuntimeError:
            return sym, None
        df.to_csv(path)
        return sym, df

    with ThreadPoolExecutor(workers) as ex:
        return {s: df for s, df in ex.map(one, symbols) if df is not None and len(df)}


def panel(frames: dict[str, pd.DataFrame], col: str) -> pd.DataFrame:
    """코인별 표를 날짜×코인 한 장으로 합친다. 그날 거래가 없던 코인은 빈칸."""
    return pd.DataFrame({s: df[col] for s, df in frames.items()}).sort_index()
