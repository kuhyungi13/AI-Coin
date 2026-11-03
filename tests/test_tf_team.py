import numpy as np
import pandas as pd
import pytest

from aicoin.tf_team.indicators import last_cross, rsi, technical_snapshot


@pytest.fixture(autouse=True)
def clear_caches():
    from aicoin.tf_team import sources
    sources._coin_detail.cache_clear()
    sources._coingecko_global.cache_clear()
    yield


def make_df(closes):
    idx = pd.date_range("2024-01-01", periods=len(closes), freq="D", tz="UTC", name="date")
    c = pd.Series(closes, index=idx, dtype=float)
    return pd.DataFrame({"open": c, "high": c * 1.01, "low": c * 0.99, "close": c, "volume": 100.0})


def test_rsi_extremes():
    up = pd.Series(np.arange(1, 40, dtype=float))
    assert rsi(up).iloc[-1] == pytest.approx(100)
    down = pd.Series(np.arange(40, 1, -1, dtype=float))
    assert rsi(down).iloc[-1] == pytest.approx(0)


def test_golden_cross_detected():
    fast = pd.Series([1, 1, 1, 3, 3], dtype=float)
    slow = pd.Series([2, 2, 2, 2, 2], dtype=float)
    assert last_cross(fast, slow) == ("골든크로스", 1)
    assert last_cross(slow, fast) == ("데드크로스", 1)
    assert last_cross(fast * 0 + 5, slow) is None


def test_snapshot_uptrend():
    snap = technical_snapshot(make_df(np.linspace(100, 200, 130)))
    assert snap["MA20>MA60"] is True
    assert snap["종가와 이평선 거리(%)"]["MA20"] > 0
    assert snap["RSI14"] > 70
    assert snap["등락률(%)"]["1일"] > 0
    assert len(snap["최근 10일 종가"]) == 10


def test_snapshot_short_history_has_no_ma60():
    snap = technical_snapshot(make_df(np.linspace(100, 110, 40)))
    assert snap["이동평균"]["MA60"] is None
    assert snap["MA20>MA60"] is None


def test_brief_lists_data_and_failures():
    from aicoin.tf_team.brief import build_brief

    data = {"BTC": {"TARO": {"일봉": {"종가": 100}}, "DIANA": {"오류": "429"},
                    "NOVA": {"BTC 관련 기사": [], "수집 실패": {"Decrypt": "403"}},
                    "VIBE": {"공포·탐욕 지수": {"오늘": "40 (Fear)"}}}}
    md = build_brief(data, "2026-11-03 09:20 KST")
    assert md.startswith("# TF팀 회의 자료 (2026-11-03 09:20 KST)")
    assert "- DIANA: 429" in md and "- NOVA/Decrypt: 403" in md
    assert '"종가": 100' in md and "### VIBE 자료" in md
    assert "PLAYBOOK.md" in md


RSS = b"""<?xml version="1.0"?><rss><channel>
<item><title>Bitcoin ETF inflows hit record</title><description>&lt;p&gt;BTC funds&lt;/p&gt;</description>
<pubDate>%s</pubDate></item>
<item><title>Fed holds rates</title><description>macro</description><pubDate>%s</pubDate></item>
<item><title>Old bitcoin story</title><description>old</description><pubDate>Mon, 01 Jan 2024 00:00:00 +0000</pubDate></item>
</channel></rss>"""


def test_news_filters_by_coin_and_age(monkeypatch):
    from aicoin.tf_team import sources

    now = pd.Timestamp.now(tz="UTC").strftime("%a, %d %b %Y %H:%M:%S +0000")

    class Resp:
        content = RSS % (now.encode(), now.encode())

        def raise_for_status(self):
            pass

    monkeypatch.setattr(sources, "RSS_FEEDS", {"Test": "http://x"})
    monkeypatch.setattr(sources.requests, "get", lambda *a, **k: Resp())
    out = sources.news("BTC")
    assert [r["제목"] for r in out["BTC 관련 기사"]] == ["Bitcoin ETF inflows hit record"]
    assert out["BTC 관련 기사"][0]["요약"] == "BTC funds"
    assert [r["제목"] for r in out["시장 전반 기사"]] == ["Fed holds rates"]


def test_collect_survives_network_failure(monkeypatch):
    from aicoin.tf_team import sources

    def boom(*a, **k):
        raise sources.requests.ConnectionError("blocked")

    monkeypatch.setattr(sources.requests, "get", boom)
    monkeypatch.setattr(sources, "fetch_klines", boom)
    data = sources.collect("btc")
    assert "오류" in data["TARO"] and "오류" in data["DIANA"]
    assert "수집 실패" in data["NOVA"]
    assert "오류" in data["VIBE"]["공포·탐욕 지수"]


def test_futures_falls_back_to_coingecko(monkeypatch):
    from aicoin.tf_team import sources

    rows = [
        {"market": "Binance (Futures)", "index_id": "BTC", "contract_type": "perpetual",
         "funding_rate": 0.01, "open_interest": 300},
        {"market": "Bybit", "index_id": "BTC", "contract_type": "perpetual",
         "funding_rate": -0.005, "open_interest": 500},
        {"market": "X", "index_id": "ETH", "contract_type": "perpetual", "funding_rate": 0.02, "open_interest": 900},
        {"market": "Y", "index_id": "BTC", "contract_type": "futures", "funding_rate": 0.0, "open_interest": 900},
    ]

    def fake_get_json(url, params=None, headers=None):
        if "fapi.binance.com" in url:
            raise sources.requests.HTTPError("451")
        if url.endswith("/derivatives"):
            return rows
        raise sources.requests.ConnectionError("blocked")

    monkeypatch.setattr(sources, "_get_json", fake_get_json)
    out = sources.sentiment("BTC", fng={"오늘": "50"})
    fut = out["선물 포지션"]
    assert list(fut["거래소별 펀딩비(%)"]) == ["Bybit", "Binance (Futures)"]
    assert fut["미결제약정 합계 USD(상위)"] == 800
    assert "오류" in out["커뮤니티 인기글(레딧)"]


def test_get_json_retries_once_on_429(monkeypatch):
    from aicoin.tf_team import sources

    class R:
        def __init__(self, code):
            self.status_code, self.headers = code, {"Retry-After": "1"}

        def raise_for_status(self):
            if self.status_code >= 400:
                raise sources.requests.HTTPError(str(self.status_code))

        def json(self):
            return {"ok": True}

    seq = [R(429), R(200)]
    monkeypatch.setattr(sources.requests, "get", lambda *a, **k: seq.pop(0))
    monkeypatch.setattr(sources.time, "sleep", lambda s: None)
    assert sources._get_json("http://x") == {"ok": True}
