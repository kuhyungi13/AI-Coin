"""변동성 돌파 전략 백테스트 실행 파일.

사용법:
    pip install -r requirements.txt
    python run_backtest.py                      # BTC/USDT, 2018년부터, k=0.5
    python run_backtest.py --k 0.4 --ma 5       # k 바꾸고 5일 이동평균 필터 켜기
    python run_backtest.py --sweep              # k 값을 여러 개 비교
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from aicoin.data import load_klines
from aicoin.strategy import Params, run, summarize

PERCENT_KEYS = {"총수익률", "연평균수익률(CAGR)", "최대낙폭(MDD)", "승률", "거래당평균수익",
                "단순보유_총수익률", "단순보유_MDD"}


def fmt(key: str, val) -> str:
    if key in PERCENT_KEYS:
        return f"{val * 100:,.2f}%"
    if isinstance(val, float):
        return f"{val:.2f}"
    return str(val)


def main() -> None:
    ap = argparse.ArgumentParser(description="변동성 돌파 전략 백테스트")
    ap.add_argument("--symbol", default="BTCUSDT")
    ap.add_argument("--start", default="2018-01-01")
    ap.add_argument("--end", default=None)
    ap.add_argument("--k", type=float, default=0.5)
    ap.add_argument("--ma", type=int, default=None, help="이동평균 필터 일수 (예: 5)")
    ap.add_argument("--fee", type=float, default=0.001)
    ap.add_argument("--slippage", type=float, default=0.0005)
    ap.add_argument("--sweep", action="store_true", help="k와 이동평균 필터 조합을 비교")
    ap.add_argument("--csv", default=None, help="바이낸스 대신 이 CSV 파일(date,open,high,low,close)을 사용")
    ap.add_argument("--refresh", action="store_true", help="저장된 데이터를 무시하고 새로 받기")
    args = ap.parse_args()

    if args.csv:
        df = pd.read_csv(args.csv, index_col="date", parse_dates=["date"])
    else:
        df = load_klines(args.symbol, "1d", args.start, args.end, refresh=args.refresh)
    print(f"{args.symbol} 일봉 {len(df)}개 불러옴\n")

    Path("results").mkdir(exist_ok=True)
    if args.sweep:
        rows = []
        for ma in (None, 5, 10, 20):
            for k in (0.3, 0.4, 0.5, 0.6, 0.7):
                p = Params(k=k, fee=args.fee, slippage=args.slippage, ma_filter=ma)
                s = summarize(run(df, p))
                rows.append({"k": k, "이동평균필터": ma or "없음", **s})
        table = pd.DataFrame(rows).drop(columns=["기간"])
        table.to_csv("results/sweep.csv", index=False, encoding="utf-8-sig")
        shown = table.copy()
        for col in shown.columns:
            if col in PERCENT_KEYS:
                shown[col] = shown[col].map(lambda v: f"{v * 100:,.1f}%")
        shown["샤프지수"] = shown["샤프지수"].round(2)
        print(shown[["k", "이동평균필터", "총수익률", "연평균수익률(CAGR)", "최대낙폭(MDD)",
                     "거래횟수", "승률", "샤프지수"]].to_string(index=False))
        print(f"\n같은 기간 그냥 사서 보유: 총수익률 {table['단순보유_총수익률'][0] * 100:,.1f}%, "
              f"MDD {table['단순보유_MDD'][0] * 100:,.1f}%")
        print("\n전체 표: results/sweep.csv")
        return

    p = Params(k=args.k, fee=args.fee, slippage=args.slippage, ma_filter=args.ma)
    res = run(df, p)
    res.to_csv("results/trades.csv", encoding="utf-8-sig")
    for key, val in summarize(res).items():
        print(f"{key:>14}: {fmt(key, val)}")
    print("\n날짜별 결과: results/trades.csv")


if __name__ == "__main__":
    main()
