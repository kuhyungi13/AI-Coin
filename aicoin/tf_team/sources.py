"""팀원들이 보는 자료를 모은다. 전부 무료 공개 API이고 키가 필요 없다.

- TARO(차트): 바이낸스 일봉 → indicators.technical_snapshot
- DIANA(펀더멘털): CoinGecko 시총·유통량·발행량, DefiLlama 체인 TVL
- NOVA(뉴스): CoinDesk·Cointelegraph·Decrypt RSS
- VIBE(센티먼트): 공포·탐욕 지수(alternative.me), 바이낸스 선물 펀딩비·롱숏 비율, 레딧 인기글

한 곳이 막혀도 전체가 멈추지 않도록 실패는 {"오류": "..."}로 돌려주고, 팀원은 "자료 없음"으로 보고한다.
(바이낸스 선물 API는 미국 서버 등 일부 지역에서 막혀 있다.)
"""

from __future__ import annotations

import os
import re
import time
from functools import lru_cache
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from html import unescape

import pandas as pd
import requests

from ..data import fetch_klines
from .indicators import technical_snapshot

UA = {"User-Agent": "coin-tf-team/0.1 (+https://github.com)"}
TIMEOUT = 20

# 심볼 → CoinGecko id. 목록에 없으면 CoinGecko 검색으로 찾는다.
COINGECKO_IDS = {
    "BTC": "bitcoin", "ETH": "ethereum", "SOL": "solana", "XRP": "ripple", "BNB": "binancecoin",
    "DOGE": "dogecoin", "ADA": "cardano", "TRX": "tron", "AVAX": "avalanche-2", "LINK": "chainlink",
    "DOT": "polkadot", "SUI": "sui", "TON": "the-open-network", "LTC": "litecoin", "NEAR": "near",
    "APT": "aptos", "ARB": "arbitrum", "OP": "optimism", "PEPE": "pepe", "SHIB": "shiba-inu",
}
# 뉴스 제목에서 코인을 알아보기 위한 이름
COIN_NAMES = {
    "BTC": ["bitcoin", "btc"], "ETH": ["ethereum", "ether", "eth"], "SOL": ["solana", "sol"],
    "XRP": ["xrp", "ripple"], "BNB": ["bnb", "binance coin"], "DOGE": ["dogecoin", "doge"],
    "ADA": ["cardano", "ada"], "AVAX": ["avalanche", "avax"], "LINK": ["chainlink", "link"],
}
RSS_FEEDS = {
    "CoinDesk": "https://www.coindesk.com/arc/outboundfeeds/rss/",
    "Cointelegraph": "https://cointelegraph.com/rss",
    "Decrypt": "https://decrypt.co/feed",
}


def _safe(fn, *args, **kwargs):
    try:
        return fn(*args, **kwargs)
    except Exception as e:  # 자료 하나 실패가 전체 분석을 멈추면 안 된다
        return {"오류": f"{type(e).__name__}: {e}"[:300]}


def _get_json(url: str, params: dict | None = None, headers: dict | None = None):
    for attempt in range(2):
        resp = requests.get(url, params=params, headers={**UA, **(headers or {})}, timeout=TIMEOUT)
        if resp.status_code == 429 and attempt == 0:  # 무료 CoinGecko는 1분에 몇 번만 허용한다. 한 번 쉬었다 다시.
            time.sleep(min(int(resp.headers.get("Retry-After") or 30), 60))
            continue
        resp.raise_for_status()
        return resp.json()


# ---------- TARO: 차트 ----------

def technical(coin: str) -> dict:
    start = f"{pd.Timestamp.now(tz='UTC') - pd.Timedelta(days=200):%Y-%m-%d}"
    df = fetch_klines(f"{coin}USDT", "1d", start=start)
    if len(df) < 30:
        return {"오류": f"{coin}USDT 일봉이 {len(df)}개뿐이라 지표를 계산할 수 없습니다"}
    daily = technical_snapshot(df)
    start4h = f"{pd.Timestamp.now(tz='UTC') - pd.Timedelta(days=25):%Y-%m-%d}"
    df4h = fetch_klines(f"{coin}USDT", "4h", start=start4h)
    four = technical_snapshot(df4h) if len(df4h) >= 30 else None
    if four:
        four = {k: four[k] for k in ("등락률(%)", "종가와 이평선 거리(%)", "MA20>MA60", "최근 교차", "RSI14")}
    return {"일봉": daily, "4시간봉(요약)": four}


# ---------- DIANA: 펀더멘털 ----------

def _coingecko_headers() -> dict:
    key = os.environ.get("COINGECKO_API_KEY")
    return {"x-cg-demo-api-key": key} if key else {}


def coingecko_id(coin: str) -> str:
    if coin in COINGECKO_IDS:
        return COINGECKO_IDS[coin]
    found = _get_json("https://api.coingecko.com/api/v3/search", {"query": coin}, _coingecko_headers())
    for c in found.get("coins", []):
        if c.get("symbol", "").upper() == coin:
            return c["id"]
    raise ValueError(f"CoinGecko에서 {coin}을 찾지 못했습니다")


@lru_cache(maxsize=32)
def _coin_detail(coin: str) -> dict:
    """CoinGecko 코인 상세. DIANA와 VIBE가 같이 쓰므로 한 번만 받는다 (무료 요청 한도 절약)."""
    return _get_json(f"https://api.coingecko.com/api/v3/coins/{coingecko_id(coin)}",
                     {"localization": "false", "tickers": "false", "community_data": "false",
                      "developer_data": "false", "sparkline": "false"}, _coingecko_headers())


@lru_cache(maxsize=4)
def _coingecko_global(path: str, query: str = ""):
    """여러 코인이 같이 쓰는 CoinGecko 자료(선물 목록, 인기 검색)는 실행당 한 번만 받는다."""
    params = dict(p.split("=") for p in query.split("&")) if query else None
    return _get_json(f"https://api.coingecko.com/api/v3/{path}", params, _coingecko_headers())


def fundamentals(coin: str) -> dict:
    d = _coin_detail(coin)
    m = d.get("market_data", {})
    usd = lambda k: (m.get(k) or {}).get("usd")  # noqa: E731
    circ, total, mx = m.get("circulating_supply"), m.get("total_supply"), m.get("max_supply")
    out = {
        "이름": d.get("name"),
        "분류": (d.get("categories") or [])[:5],
        "시가총액 순위": d.get("market_cap_rank"),
        "시가총액(USD)": usd("market_cap"),
        "완전희석가치 FDV(USD)": usd("fully_diluted_valuation"),
        "24시간 거래대금(USD)": usd("total_volume"),
        "유통량": circ, "총발행량": total, "최대발행량": mx,
        "유통 비율(%)": round(circ / (mx or total) * 100, 1) if circ and (mx or total) else None,
        "역대 최고가(USD)": usd("ath"),
        "역대 최고가 대비(%)": (m.get("ath_change_percentage") or {}).get("usd"),
        "가격 변화(%)": {k: m.get(f"price_change_percentage_{k}") for k in ("7d", "30d", "1y")},
        "소개": re.sub(r"<[^>]+>", "", (d.get("description") or {}).get("en", ""))[:400],
    }
    tvl = _safe(chain_tvl, coin)
    if tvl:
        out["체인 TVL (DefiLlama)"] = tvl
    return out


def chain_tvl(coin: str) -> dict | None:
    """그 코인이 자기 블록체인의 기본 코인이면(ETH, SOL 등) 체인에 묶인 예치금(TVL)."""
    for ch in _get_json("https://api.llama.fi/v2/chains"):
        if (ch.get("tokenSymbol") or "").upper() == coin:
            return {"체인": ch.get("name"), "TVL(USD)": round(ch.get("tvl") or 0)}
    return None


# ---------- NOVA: 뉴스 ----------

def _rss_items(url: str) -> list[dict]:
    resp = requests.get(url, headers=UA, timeout=TIMEOUT)
    resp.raise_for_status()
    root = ET.fromstring(resp.content)
    items = []
    for it in root.iter("item"):
        title = unescape((it.findtext("title") or "").strip())
        desc = re.sub(r"<[^>]+>", "", unescape(it.findtext("description") or "")).strip()
        try:
            when = parsedate_to_datetime(it.findtext("pubDate") or "")
        except (TypeError, ValueError):
            when = None
        items.append({"title": title, "summary": desc[:240], "published": when})
    return items


def news(coin: str, max_items: int = 15) -> dict:
    names = COIN_NAMES.get(coin, [coin.lower()])
    pat = re.compile(r"\b(" + "|".join(re.escape(n) for n in names) + r")\b", re.I)
    about, general, errors = [], [], {}
    cutoff = pd.Timestamp.now(tz="UTC") - pd.Timedelta(days=3)
    for src, url in RSS_FEEDS.items():
        got = _safe(_rss_items, url)
        if isinstance(got, dict):
            errors[src] = got["오류"]
            continue
        for it in got:
            if it["published"] is not None and pd.Timestamp(it["published"]) < cutoff:
                continue
            row = {"출처": src, "제목": it["title"], "요약": it["summary"],
                   "시각(UTC)": None if it["published"] is None else f"{pd.Timestamp(it['published']).tz_convert('UTC'):%m-%d %H:%M}"}
            (about if pat.search(it["title"] + " " + it["summary"]) else general).append(row)
    out = {f"{coin} 관련 기사": about[:max_items], "시장 전반 기사": general[:8]}
    if errors:
        out["수집 실패"] = errors
    return out


# ---------- VIBE: 센티먼트 ----------

def fear_greed() -> dict:
    data = _get_json("https://api.alternative.me/fng/", {"limit": 7})["data"]
    return {"오늘": f"{data[0]['value']} ({data[0]['value_classification']})",
            "최근 7일": [int(x["value"]) for x in data]}


def futures_positioning(coin: str) -> dict:
    sym = f"{coin}USDT"
    base = "https://fapi.binance.com"
    prem = _get_json(base + "/fapi/v1/premiumIndex", {"symbol": sym})
    ls = _get_json(base + "/futures/data/globalLongShortAccountRatio", {"symbol": sym, "period": "1d", "limit": 7})
    oi = _get_json(base + "/futures/data/openInterestHist", {"symbol": sym, "period": "1d", "limit": 7})
    return {
        "펀딩비(%/8시간)": round(float(prem["lastFundingRate"]) * 100, 4),
        "롱숏 계정 비율(최근 7일)": [round(float(x["longShortRatio"]), 2) for x in ls],
        "미결제약정 USD(최근 7일)": [round(float(x["sumOpenInterestValue"])) for x in oi],
    }


def derivatives_coingecko(coin: str) -> dict:
    """바이낸스 선물 API가 막힌 지역(미국 서버 등)용 대안: CoinGecko에 모인 거래소별 무기한 선물 펀딩비·미결제약정."""
    rows = _coingecko_global("derivatives", "include_tickers=unexpired")
    perps = [r for r in rows if (r.get("index_id") or "").upper() == coin
             and r.get("contract_type") == "perpetual" and r.get("funding_rate") is not None]
    perps.sort(key=lambda r: r.get("open_interest") or 0, reverse=True)
    if not perps:
        raise ValueError(f"{coin} 무기한 선물 자료 없음")
    top = perps[:6]
    return {
        "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
        "거래소별 펀딩비(%)": {r["market"]: round(float(r["funding_rate"]), 4) for r in top},
        "미결제약정 합계 USD(상위)": round(sum(r.get("open_interest") or 0 for r in top)),
    }


def crowd_coingecko(coin: str) -> dict:
    """레딧이 막혔을 때의 대안: CoinGecko 이용자 투표(오늘 오를까/내릴까)와 지금 많이 검색되는 코인."""
    d = _coin_detail(coin)
    trend = _coingecko_global("search/trending")
    names = [c["item"]["symbol"].upper() for c in trend.get("coins", [])][:15]
    return {
        "CoinGecko 이용자 투표 상승(%)": d.get("sentiment_votes_up_percentage"),
        "CoinGecko 인기 검색 코인": names,
        f"{coin}가 인기 검색에 있음": coin in names,
    }


def reddit_hot(coin: str) -> dict:
    subs = {"BTC": "Bitcoin", "ETH": "ethereum", "SOL": "solana", "XRP": "XRP"}
    out = {}
    for sub in ["CryptoCurrency"] + ([subs[coin]] if coin in subs else []):
        posts = _get_json(f"https://www.reddit.com/r/{sub}/hot.json", {"limit": 15})["data"]["children"]
        out[f"r/{sub}"] = [{"제목": p["data"]["title"], "추천": p["data"]["score"], "댓글": p["data"]["num_comments"]}
                           for p in posts if not p["data"].get("stickied")][:10]
    return out


def sentiment(coin: str, fng: dict | None = None) -> dict:
    out = {"공포·탐욕 지수": fng if fng is not None else _safe(fear_greed)}
    futures = _safe(futures_positioning, coin)
    if "오류" in futures:  # 미국 서버(GitHub Actions)에서는 바이낸스 선물 API가 451로 막힌다
        futures = _safe(derivatives_coingecko, coin)
    out["선물 포지션"] = futures
    out["커뮤니티 인기글(레딧)"] = _safe(reddit_hot, coin)
    out["군중 심리(CoinGecko)"] = _safe(crowd_coingecko, coin)
    return out


def collect(coin: str, fng: dict | None = None) -> dict:
    """한 코인에 대한 4명분 자료를 모두 모은다."""
    coin = coin.upper()
    return {
        "TARO": _safe(technical, coin),
        "DIANA": _safe(fundamentals, coin),
        "NOVA": _safe(news, coin),
        "VIBE": sentiment(coin, fng),
    }
