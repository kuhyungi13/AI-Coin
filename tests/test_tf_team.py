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


def test_closed_only_drops_unfinished_candle():
    from aicoin.tf_team.sources import closed_only

    df = make_df([1, 2, 3])  # 2024-01-01, 02, 03 일봉
    now = pd.Timestamp("2024-01-03 15:00", tz="UTC")  # 1월 3일 봉은 아직 진행 중
    assert list(closed_only(df, pd.Timedelta(days=1), now)["close"]) == [1, 2]
    now = pd.Timestamp("2024-01-04 00:00", tz="UTC")  # 막 마감됨
    assert list(closed_only(df, pd.Timedelta(days=1), now)["close"]) == [1, 2, 3]


def test_scan_pick_rules():
    from aicoin.tf_team.scan import pick

    t = pd.DataFrame({
        "거래대금 30일 평균(USD)": [9e9, 2e7, 2e7, 2e7, 1e6, 2e7],
        "추세": ["상승", "상승", "상승", "하락", "상승", "상승"],
        "RSI14": [60, 65, 75, 25, 60, 55],
        "14일(%)": [5, 30, 50, -20, 90, 10],
    }, index=["BTC", "AAA", "HOT", "DIP", "TINY", "BBB"])
    p = pick(t, n_trend=2, n_oversold=1)
    assert p["상승 추세"] == ["AAA", "BBB"]   # BTC는 항상 따로, HOT은 과열, TINY는 거래 부족
    assert p["과매도 반등"] == ["DIP"]


def test_scan_metrics():
    from aicoin.tf_team.scan import metrics

    df = make_df(np.linspace(100, 160, 70))
    df["quote_volume"] = 1e7
    m = metrics(df)
    assert m["추세"] == "상승" and m["14일(%)"] > 0 and m["거래량 배수"] == 1.0
    assert metrics(df.iloc[:50]) is None


def test_score_hits_and_summary():
    from aicoin.tf_team import score

    assert score.hit("매수", 1.0) and not score.hit("매수", -1.0)
    assert score.hit("매도", -0.5) and score.hit("관망", 2.9) and not score.hit("관망", -3.5)
    assert score.hit("약한 부정", -1) and score.hit("", 1) is None

    df = pd.DataFrame([
        {"run_at": "2026-11-01T00:00:00Z", "coin": "BTC", "decision": "매수", "TARO": "긍정", "VIBE": "부정"},
        {"run_at": "2026-11-01T00:00:00Z", "coin": "ETH", "decision": "관망", "TARO": "중립"},
        {"run_at": "2026-11-02T23:00:00Z", "coin": "BTC", "decision": "매도"},  # 아직 24시간 안 됨
    ]).reindex(columns=score.COLUMNS).fillna("")
    prices = {("BTC", "2026-11-01 00:00"): 100, ("BTC", "2026-11-02 00:00"): 105,
              ("ETH", "2026-11-01 00:00"): 100, ("ETH", "2026-11-02 00:00"): 90}
    n = score.score_pending(df, now=pd.Timestamp("2026-11-03 00:00", tz="UTC"),
                            price=lambda c, t: prices[(c, f"{t:%Y-%m-%d %H:%M}")])
    assert n == 2
    assert list(df["ret_24h"][:2]) == ["5.00", "-10.00"] and df["ret_24h"][2] == ""
    assert list(df["ace_hit"][:2]) == ["True", "False"]
    assert df["TARO_hit"][0] == "True" and df["VIBE_hit"][0] == "False"
    s = score.summary(df)
    assert s["ACE"] == {"맞음": 1, "전체": 2, "승률(%)": 50.0}
    assert s["채점 대기"] == 1
    assert "50.0% (1/2)" in score.scoreboard_markdown(s, df, "x")


# ---- TRAINER 모의투자 ----
from aicoin.tf_team import trainer as trainer_mod


def _bars(prices):
    """{(coin, 'YYYY-mm-dd HH'): (open, high, low, close)} 로 가짜 1시간봉."""
    def klines(coin, start, end):
        rows = {pd.Timestamp(k[1], tz="UTC"): v for k, v in prices.items() if k[0] == coin}
        rows = {t: v for t, v in rows.items() if start <= t < end}
        df = pd.DataFrame(rows.values(), index=list(rows.keys()), columns=["open", "high", "low", "close"])
        return df.sort_index()
    return klines


def _verdicts(tmp_path, rows):
    pd.DataFrame(rows, columns=["run_at", "coin", "decision", "confidence"]).to_csv(tmp_path / "verdicts.csv", index=False)


def test_trainer_buys_on_confident_buy_and_takes_profit(tmp_path):
    _verdicts(tmp_path, [["2026-11-03T05:40:00Z", "SOL", "매수", "8"],
                         ["2026-11-03T05:40:00Z", "BTC", "관망", "6"]])
    k = _bars({("SOL", "2026-11-03 07:00"): (100, 101, 99, 100),
               ("SOL", "2026-11-03 08:00"): (100, 111, 99, 110)})
    sm = trainer_mod.run(tmp_path, pd.Timestamp("2026-11-03 09:05", tz="UTC"), k)
    trades = pd.read_csv(tmp_path / "trainer/trades.csv")
    assert list(trades["side"]) == ["매수", "매도"]
    assert trades["reason"].iloc[1] == "익절 +10%"
    assert float(trades["price"].iloc[0]) == 100
    # 16% 투자해 10% 수익, 수수료 왕복 0.2% 정도
    assert 10_140 < sm["총자산"] < 10_160
    assert sm["보유"] == [] and sm["청산 거래"] == 1


def test_trainer_skips_low_confidence_and_stops_out(tmp_path):
    _verdicts(tmp_path, [["2026-11-03T05:40:00Z", "ETH", "매수", "3"],
                         ["2026-11-03T05:40:00Z", "SOL", "매수", "6"]])
    k = _bars({("SOL", "2026-11-03 07:00"): (100, 100, 100, 100),
               ("SOL", "2026-11-03 08:00"): (100, 112, 94, 95)})  # 한 봉에서 둘 다 닿으면 손절
    trainer_mod.run(tmp_path, pd.Timestamp("2026-11-03 09:05", tz="UTC"), k)
    trades = pd.read_csv(tmp_path / "trainer/trades.csv")
    assert list(trades["coin"]) == ["SOL", "SOL"]
    assert trades["reason"].iloc[1] == "손절 -5%"


def test_trainer_probe_entry_is_half_size_and_1x(tmp_path):
    _verdicts(tmp_path, [["2026-11-03T05:40:00Z", "SOL", "매수", "4"],
                         ["2026-11-03T05:40:00Z", "BTC", "매수", "5"]])
    k = _bars({("SOL", "2026-11-03 07:00"): (100, 100, 100, 100), ("BTC", "2026-11-03 07:00"): (100, 100, 100, 100)})
    trainer_mod.run(tmp_path, pd.Timestamp("2026-11-03 07:30", tz="UTC"), k)
    t = pd.read_csv(tmp_path / "trainer/trades.csv").set_index("coin")
    assert t.loc["SOL", "leverage"] == 1 and "소액 탐색" in t.loc["SOL", "reason"]
    assert abs(t.loc["SOL", "margin"] / t.loc["BTC", "margin"] - 0.4) < 0.01  # 4×2%×½ vs 5×2%


def test_trainer_waits_for_next_hour_and_is_idempotent(tmp_path):
    _verdicts(tmp_path, [["2026-11-03T05:40:00Z", "SOL", "매수", "7"]])
    k = _bars({("SOL", "2026-11-03 07:00"): (50, 51, 49, 50)})
    trainer_mod.run(tmp_path, pd.Timestamp("2026-11-03 06:55", tz="UTC"), k)  # 06시 정각 회의 중, 체결은 07시
    assert not (pd.read_csv(tmp_path / "trainer/trades.csv")).shape[0]
    trainer_mod.run(tmp_path, pd.Timestamp("2026-11-03 07:20", tz="UTC"), k)
    trainer_mod.run(tmp_path, pd.Timestamp("2026-11-03 07:40", tz="UTC"), k)
    trades = pd.read_csv(tmp_path / "trainer/trades.csv")
    assert list(trades["side"]) == ["매수"]
    _verdicts(tmp_path, [["2026-11-03T05:40:00Z", "SOL", "매수", "7"],
                         ["2026-11-03T06:40:00Z", "SOL", "매도", "7"]])
    k2 = _bars({("SOL", "2026-11-03 07:00"): (50, 51, 49, 50), ("SOL", "2026-11-03 08:00"): (52, 52, 51, 51)})
    sm = trainer_mod.run(tmp_path, pd.Timestamp("2026-11-03 08:30", tz="UTC"), k2)
    trades = pd.read_csv(tmp_path / "trainer/trades.csv")
    assert list(trades["side"]) == ["매수", "매도"] and trades["reason"].iloc[1] == "ACE 매도 7/10"
    assert sm["수익률(%)"] > 0


def test_certainty_and_leverage_steps():
    full = {"decision": "매수", "confidence": "9", "TARO": "긍정", "DIANA": "약한 긍정", "NOVA": "긍정",
            "VIBE": "긍정", "winner": "BULL"}
    s, why = trainer_mod.certainty(full)
    assert s == 86 and trainer_mod.leverage_for(s) == 5  # 지난 성적 없으면 10배 못 감
    board = {"결정별": {"매수": {"맞음": 7, "전체": 10, "승률(%)": 70.0}}}
    s, _ = trainer_mod.certainty(full, board)
    assert s == 96 and trainer_mod.leverage_for(s) == 10
    mixed = dict(full, confidence="7", DIANA="부정", VIBE="중립", winner="BEAR")
    s, _ = trainer_mod.certainty(mixed)
    assert s == 28 + 10 - 10 - 10 + 10 and trainer_mod.leverage_for(s) == 1
    assert trainer_mod.stop_distance(10) == 0.03 and trainer_mod.stop_distance(3) == 0.05


def test_trainer_leverage_magnifies_and_stops_before_liquidation(tmp_path):
    rows = [["2026-11-03T05:40:00Z", "SOL", "매수", "9", "긍정", "긍정", "긍정", "긍정", "BULL"]]
    pd.DataFrame(rows, columns=["run_at", "coin", "decision", "confidence", "TARO", "DIANA", "NOVA", "VIBE",
                                "winner"]).to_csv(tmp_path / "verdicts.csv", index=False)
    (tmp_path / "scoreboard.json").write_text('{"결정별": {"매수": {"맞음": 8, "전체": 10, "승률(%)": 80.0}}}')
    k = _bars({("SOL", "2026-11-03 07:00"): (100, 100, 100, 100),
               ("SOL", "2026-11-03 08:00"): (100, 101, 96, 96)})  # -4%: 10배면 -3%에서 손절
    sm = trainer_mod.run(tmp_path, pd.Timestamp("2026-11-03 09:05", tz="UTC"), k)
    t = pd.read_csv(tmp_path / "trainer/trades.csv")
    assert list(t["leverage"]) == [10, 10] and t["reason"].iloc[1] == "손절 -3%"
    # 증거금 1,800(18%) × 10배, 가격 -3% → 증거금 -30% + 수수료
    assert -620 < sm["총자산"] - 10_000 < -560
