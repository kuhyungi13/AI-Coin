import pandas as pd
import pytest

from aicoin.strategy import Params, max_drawdown, run, summarize


def make_df(rows):
    idx = pd.date_range("2024-01-01", periods=len(rows), freq="D", tz="UTC", name="date")
    return pd.DataFrame(rows, columns=["open", "high", "low", "close"], index=idx)


def test_breakout_buys_at_target_and_sells_at_close():
    df = make_df([
        (100, 110, 90, 100),   # 첫날: 전날 정보가 없어 거래 안 함
        (100, 125, 99, 120),   # 목표가 100 + 0.5*20 = 110 돌파 → 110에 사서 120에 팖
        (120, 121, 115, 118),  # 목표가 120 + 0.5*26 = 133 미돌파
    ])
    res = run(df, Params(k=0.5, fee=0, slippage=0))
    assert list(res["trade"]) == [False, True, False]
    assert res["ret"].iloc[1] == pytest.approx(120 / 110 - 1)
    assert res["equity"].iloc[-1] == pytest.approx(120 / 110)


def test_fees_reduce_return():
    df = make_df([(100, 110, 90, 100), (100, 125, 99, 120)])
    no_fee = run(df, Params(fee=0, slippage=0))["ret"].iloc[1]
    with_fee = run(df, Params(fee=0.001, slippage=0.0005))["ret"].iloc[1]
    assert with_fee < no_fee


def test_gap_up_open_enters_at_open():
    df = make_df([(100, 110, 90, 100), (115, 120, 114, 118)])  # 시가 115 > 목표가 125? 아님
    res = run(df, Params(k=0.1, fee=0, slippage=0))            # 목표가 115+2=117
    assert res["entry"].iloc[1] == pytest.approx(117)
    df2 = make_df([(100, 110, 90, 100), (130, 135, 129, 131)])
    res2 = run(df2, Params(k=0.0, fee=0, slippage=0))           # 목표가 = 시가
    assert res2["entry"].iloc[1] == pytest.approx(130)


def test_ma_filter_blocks_trades_in_downtrend():
    rows = [(100 - i, 101 - i, 98 - i, 99 - i) for i in range(10)]
    rows.append((90, 200, 89, 150))  # 큰 돌파지만 하락 추세
    df = make_df(rows)
    assert run(df, Params(ma_filter=None))["trade"].iloc[-1]
    assert not run(df, Params(ma_filter=5))["trade"].iloc[-1]


def test_max_drawdown_and_summary():
    assert max_drawdown(pd.Series([1, 2, 1, 3])) == pytest.approx(-0.5)
    df = make_df([(100, 110, 90, 100), (100, 125, 99, 120), (120, 121, 115, 118)])
    s = summarize(run(df, Params(fee=0, slippage=0)))
    assert s["거래횟수"] == 1 and s["승률"] == 1.0
