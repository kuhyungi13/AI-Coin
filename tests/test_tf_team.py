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


def test_trainer_buys_on_confident_buy_and_holds_without_take_profit(tmp_path):
    _verdicts(tmp_path, [["2026-11-03T05:40:00Z", "SOL", "매수", "8"],
                         ["2026-11-03T05:40:00Z", "BTC", "관망", "6"]])
    k = _bars({("SOL", "2026-11-03 07:00"): (100, 101, 99, 100),
               ("SOL", "2026-11-03 08:00"): (100, 111, 99, 110)})
    sm = trainer_mod.run(tmp_path, pd.Timestamp("2026-11-03 09:05", tz="UTC"), k)
    trades = pd.read_csv(tmp_path / "trainer/trades.csv")
    # 익절은 없다: 10% 올라도 팔지 않고 계속 들고 있는다
    assert list(trades["side"]) == ["매수"]
    assert float(trades["price"].iloc[0]) == 100
    assert len(sm["보유"]) == 1 and sm["청산 거래"] == 0
    # 16% 투자해 10% 평가이익 (수수료 0.1%)
    assert 10_140 < sm["총자산"] < 10_160


def test_trainer_skips_low_confidence_and_stops_out(tmp_path):
    _verdicts(tmp_path, [["2026-11-03T05:40:00Z", "ETH", "매수", "3"],
                         ["2026-11-03T05:40:00Z", "SOL", "매수", "6"]])
    k = _bars({("SOL", "2026-11-03 07:00"): (100, 100, 100, 100),
               ("SOL", "2026-11-03 08:00"): (100, 112, 89, 95)})  # 저가가 -10%를 건드리면 로스컷
    trainer_mod.run(tmp_path, pd.Timestamp("2026-11-03 09:05", tz="UTC"), k)
    trades = pd.read_csv(tmp_path / "trainer/trades.csv")
    assert list(trades["coin"]) == ["SOL", "SOL"]
    assert trades["reason"].iloc[1] == "로스컷 가격 -10% (증거금 -10%)"


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
    assert trainer_mod.stop_distance(10) == 0.01 and trainer_mod.stop_distance(1) == 0.10


def test_trainer_leverage_magnifies_and_losscut_is_same_pct_of_margin(tmp_path):
    rows = [["2026-11-03T05:40:00Z", "SOL", "매수", "9", "긍정", "긍정", "긍정", "긍정", "BULL"]]
    pd.DataFrame(rows, columns=["run_at", "coin", "decision", "confidence", "TARO", "DIANA", "NOVA", "VIBE",
                                "winner"]).to_csv(tmp_path / "verdicts.csv", index=False)
    (tmp_path / "scoreboard.json").write_text('{"결정별": {"매수": {"맞음": 8, "전체": 10, "승률(%)": 80.0}}}')
    k = _bars({("SOL", "2026-11-03 07:00"): (100, 100, 100, 100),
               ("SOL", "2026-11-03 08:00"): (100, 101, 98, 98)})  # -2%: 10배면 -1%에서 로스컷
    sm = trainer_mod.run(tmp_path, pd.Timestamp("2026-11-03 09:05", tz="UTC"), k)
    t = pd.read_csv(tmp_path / "trainer/trades.csv")
    assert list(t["leverage"]) == [10, 10] and t["reason"].iloc[1] == "로스컷 가격 -1% (증거금 -10%)"
    # 증거금 1,800(18%) × 10배, 가격 -1% → 증거금 -10%(-180) + 수수료 약 -36
    assert -230 < sm["총자산"] - 10_000 < -200


# ---- 백테스트 연구실 ----
from aicoin.tf_team import research as research_mod


def _daily(n=300, drift=0.001, seed=1):
    import numpy as np
    rng = np.random.default_rng(seed)
    close = 100 * np.exp(np.cumsum(rng.normal(drift, 0.02, n)))
    idx = pd.date_range("2024-01-01", periods=n, freq="D", tz="UTC")
    df = pd.DataFrame({"open": close * 0.999, "high": close * 1.01, "low": close * 0.99, "close": close,
                       "volume": 1.0, "quote_volume": 5e6}, index=idx)
    return df


def test_simulate_losscut_scales_with_leverage():
    idx = pd.date_range("2025-01-01", periods=12, freq="D", tz="UTC")
    df = pd.DataFrame({"open": 100.0, "high": 101.0, "low": 99.5, "close": 100.0}, index=idx)
    df.loc[idx[3], "low"] = 96.0  # 진입(1일차 시가 100) 뒤 -4%
    sig = pd.Series(False, index=idx)
    sig.iloc[0] = True
    r1 = research_mod.simulate(df, sig, lev=1)["ret"].iloc[0]
    r3 = research_mod.simulate(df, sig, lev=3)["ret"].iloc[0]
    assert -0.5 < r1 < 0.1  # 1배는 -4%라 로스컷(-10%)에 안 걸리고 만료 종가 수익률(≈0)이 나온다
    assert abs(r3 - (-10 - 0.6)) < 0.01  # 3배: 가격 -3.33%에서 로스컷 → 증거금 -10% − 수수료 0.6%


def test_research_run_and_markdown():
    frames = {"AAAUSDT": _daily(seed=1), "BBBUSDT": _daily(seed=2, drift=-0.001)}
    res = research_mod.run(frames, lev=1, split="2024-09-01")
    base = "기준선(아무 날이나)"
    assert base in res and res[base]["train"]["n"] > 0 and res[base]["test"]["n"] > 0
    md = research_mod.markdown({1: res}, "2026-11-04", 2)
    assert "레버리지 1배" in md and "검증" in md


def test_market_json(tmp_path):
    from aicoin.tf_team import market
    (tmp_path / "trainer").mkdir()
    (tmp_path / "trainer" / "equity.csv").write_text("time,equity,cash,positions\n2026-11-04T00:00:00+00:00,10000.0,10000.0,0\n")
    now = pd.Timestamp("2026-11-04T05:00:00Z")

    def fake(coin, start, end):
        if coin == "BAD":
            raise ValueError("없음")
        idx = pd.date_range(start, periods=30, freq="h", tz="UTC")
        return pd.DataFrame({"close": [1e-06 * (1 + i / 100) for i in range(30)]}, index=idx)

    data = market.build(["pepe", "PEPE", "BAD"], tmp_path, now=now, klines=fake)
    pepe = data["coins"]["PEPE"]
    assert len(pepe["closes"]) == 30 and pepe["price"] == pytest.approx(1.29e-06)
    assert pepe["chg_24h"] == pytest.approx((1.29 / 1.05 - 1) * 100, abs=0.01)
    assert "오류" in data["coins"]["BAD"]
    assert data["equity"] == [["2026-11-04T00:00:00+00:00", 10000.0]]


# ---- 로스컷 1분 감시 ----
def _bars_1m(rows):
    """rows: {coin: [(분 'YYYY-mm-dd HH:MM', open, high, low, close), ...]}"""
    def klines(coin, start, end):
        data = {pd.Timestamp(t, tz="UTC"): (o, h, l, c) for t, o, h, l, c in rows.get(coin, [])}
        data = {t: v for t, v in data.items() if start <= t < end}
        return pd.DataFrame(list(data.values()), index=list(data.keys()), columns=["open", "high", "low", "close"]).sort_index()
    return klines


def _state_with_position(tmp_path, stop_pct=0.10):
    pos = {"qty": 10.0, "entry": 100.0, "margin": 1000.0, "leverage": 1, "certainty": 40, "fee_in": 1.0,
           "entry_at": "2026-11-04T03:00:00+00:00", "checked_to": "2026-11-04T04:00:00+00:00",
           "stop": 100 * (1 - stop_pct), "stop_pct": stop_pct, "confidence": 6, "run_at": "x", "last": 100.0}
    st = trainer_mod.new_state()
    st["cash"] = 9000.0
    st["positions"]["SOL"] = pos
    d = tmp_path / "trainer"
    d.mkdir()
    (d / "state.json").write_text(__import__("json").dumps(st))
    return d


def test_watch_sells_at_losscut_price_between_meetings(tmp_path):
    d = _state_with_position(tmp_path)
    k = _bars_1m({"SOL": [("2026-11-04 04:10", 99, 99, 98, 98), ("2026-11-04 04:11", 98, 98, 89, 90)]})
    sm = trainer_mod.watch(tmp_path, pd.Timestamp("2026-11-04 04:20", tz="UTC"), k)
    t = pd.read_csv(d / "trades.csv")
    assert sm is not None and list(t["side"]) == ["매도"]
    assert float(t["price"].iloc[0]) == 90.0 and "1분봉 감시" in t["reason"].iloc[0]
    assert t["time"].iloc[0].startswith("2026-11-04T04:11")  # 회의·정시를 기다리지 않고 그 분에 청산


def test_watch_gap_down_fills_at_open_and_quiet_does_nothing(tmp_path):
    d = _state_with_position(tmp_path)
    quiet = _bars_1m({"SOL": [("2026-11-04 04:10", 99, 100, 98, 99)]})
    assert trainer_mod.watch(tmp_path, pd.Timestamp("2026-11-04 04:20", tz="UTC"), quiet) is None
    assert not (d / "trades.csv").exists()
    assert "watched_to" not in __import__("json").loads((d / "state.json").read_text())["positions"]["SOL"]  # 조용하면 상태 파일 그대로
    gap = _bars_1m({"SOL": [("2026-11-04 04:12", 85, 86, 84, 85)]})
    trainer_mod.watch(tmp_path, pd.Timestamp("2026-11-04 04:20", tz="UTC"), gap)
    t = pd.read_csv(d / "trades.csv")
    assert float(t["price"].iloc[0]) == 85.0  # 갭 하락이면 로스컷 가격이 아니라 시가
