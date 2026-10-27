import pandas as pd
import pytest

from aicoin.split_trend import SplitParams, run_split


def make_df(rows):
    idx = pd.date_range("2024-01-01", periods=len(rows), freq="D", tz="UTC", name="date")
    return pd.DataFrame(rows, columns=["open", "high", "low", "close"], index=idx)


P = dict(ma=2, tranches=3, fee=0, slippage=0)


def test_buys_in_three_tranches_while_trending():
    df = make_df([(100, 100, 100, 100), (100, 101, 100, 101), (101, 102, 101, 102),
                  (102, 103, 102, 103), (103, 104, 103, 104), (104, 105, 104, 105)])
    res, trades = run_split(df, SplitParams(stop=0.5, tp=0.5, **P))
    # 이틀째 종가가 2일 평균 위 → 사흘째부터 하루 1/3씩, 3번 산 뒤엔 현금 0
    assert list(res["trade"]) == [False, False, True, True, True, True]
    assert res["equity"].iloc[-1] == pytest.approx(
        (105 / 101 + 105 / 102 + 105 / 103) / 3)
    assert trades.empty


def test_stop_loss_sells_everything_and_waits_for_new_trend():
    df = make_df([(100, 100, 100, 100), (100, 101, 100, 101),
                  (101, 101, 90, 95),     # 101에 1/3 산 뒤 손절가 101*0.95 터치
                  (95, 99, 95, 99), (99, 100, 99, 100)])
    res, trades = run_split(df, SplitParams(stop=0.05, tp=0.5, **P))
    assert trades.iloc[0] == pytest.approx(-0.05)
    # 손절한 날은 포지션 없음. 95로 추세가 꺾였다가 99로 살아나서 마지막 날 다시 산다
    assert list(res["trade"]) == [False, False, False, False, True]


def test_take_profit_sells_a_third():
    df = make_df([(100, 100, 100, 100), (100, 101, 100, 101), (101, 102, 101, 102),
                  (102, 103, 102, 103), (103, 130, 103, 125)])
    res, _ = run_split(df, SplitParams(stop=0.5, tp=0.2, **P))
    qty = (1 / 101 + 1 / 102 + 1 / 103) / 3
    tp_px = (1 / qty) * 1.2               # 평균 매수가의 120%에서 1/3 익절
    assert res["equity"].iloc[-1] == pytest.approx(qty / 3 * tp_px + qty * 2 / 3 * 125)
