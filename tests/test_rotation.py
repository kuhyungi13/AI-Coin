import numpy as np
import pandas as pd
import pytest

from aicoin.rotation import Panels, RotationParams, run_rotation

P = dict(top_n=2, picks=1, lookback=1, ma=2, rebalance=1, min_age=1, fee=0, slippage=0)


def make_px(closes: dict[str, list[float]]) -> Panels:
    idx = pd.date_range("2024-01-01", periods=len(next(iter(closes.values()))), freq="D", tz="UTC")
    close = pd.DataFrame(closes, index=idx, dtype=float)
    # 시가 = 전날 종가 (첫날은 종가와 같게)
    open_ = close.shift(1).fillna(close)
    open_[close.isna()] = np.nan
    return Panels(open_, close, close.notna().astype(float))


def test_picks_the_coin_that_rose_most():
    px = make_px({"BTCUSDT": [100, 101, 102, 103, 104], "AUSDT": [10, 11, 13, 15, 16]})
    res, _ = run_rotation(px, RotationParams(**P))
    # 2일 평균은 2일째 종가부터 있으므로 3일째 시가(11)에 A를 산다.
    assert res["held"].tolist() == [0, 0, 1, 1, 1]
    assert res["equity"].iloc[-1] == pytest.approx(16 / 11)


def test_sells_everything_when_btc_trend_breaks():
    px = make_px({"BTCUSDT": [100, 101, 102, 90, 89], "AUSDT": [10, 11, 13, 15, 16]})
    res, _ = run_rotation(px, RotationParams(**P))
    # 4일째 비트코인 종가가 평균 아래 → 5일째 시가(15)에 판다.
    assert res["held"].tolist() == [0, 0, 1, 1, 0]
    assert res["equity"].iloc[-1] == pytest.approx(15 / 11)


def test_delisted_coin_sold_at_last_close():
    px = make_px({"BTCUSDT": [100, 101, 102, 103, 104], "AUSDT": [10, 11, 13, 12, np.nan]})
    log = []
    res, trades = run_rotation(px, RotationParams(**P), log=log)
    sold = [r for r in log if r["symbol"] == "AUSDT" and r["action"] != "매수"]
    assert [r["action"] for r in sold] == ["상장폐지"]
    assert trades[(px.close.index[4], "AUSDT")] == pytest.approx(12 / 11 - 1)
