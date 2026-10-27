"""분할 추세 전략 검증 실행 파일.

연습 기간에서 샤프지수가 가장 높은 설정을 고르고, 처음 보는 시험 기간에서 성적을 본다.

사용법:
    python run_split_trend.py                     # 2023-01-01 기준으로 나눠 검증
    python run_split_trend.py --split 2022-01-01
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from aicoin.data import load_klines
from aicoin.split_trend import SplitParams, run_split
from aicoin.strategy import period, summarize


def stats(res: pd.DataFrame, trades: pd.Series, start=None, end=None) -> dict:
    s = summarize(period(res, start, end))
    t = trades.loc[start:end]
    return {"총수익률": s["총수익률"], "MDD": s["최대낙폭(MDD)"], "샤프": s["샤프지수"],
            "거래": len(t), "승률": float((t > 0).mean()) if len(t) else 0.0,
            "보유_총수익률": s["단순보유_총수익률"], "보유_MDD": s["단순보유_MDD"]}


def pct(v: float) -> str:
    return f"{v * 100:,.1f}%"


def main() -> None:
    ap = argparse.ArgumentParser(description="분할 추세 전략 연습/시험 검증")
    ap.add_argument("--symbol", default="BTCUSDT")
    ap.add_argument("--start", default="2018-01-01")
    ap.add_argument("--split", default="2023-01-01")
    ap.add_argument("--fee", type=float, default=0.001)
    ap.add_argument("--slippage", type=float, default=0.0005)
    args = ap.parse_args()

    df = load_klines(args.symbol, "1d", args.start, None)
    print(f"{args.symbol} 일봉 {len(df)}개 불러옴\n")
    split = pd.Timestamp(args.split, tz=df.index.tz)
    train_end = split - pd.Timedelta(days=1)

    rows = []
    for ma in (20, 50, 100):
        for stop in (0.05, 0.08, 0.12):
            for tp in (0.10, 0.20):
                p = SplitParams(ma=ma, stop=stop, tp=tp, fee=args.fee, slippage=args.slippage)
                res, trades = run_split(df, p)
                tr, te = stats(res, trades, end=train_end), stats(res, trades, start=split)
                rows.append({"이동평균": ma, "손절": stop, "익절": tp,
                             **{f"연습_{k}": v for k, v in tr.items()},
                             **{f"시험_{k}": v for k, v in te.items()}})
    table = pd.DataFrame(rows)
    Path("results").mkdir(exist_ok=True)
    table.to_csv("results/split_trend.csv", index=False, encoding="utf-8-sig")

    cols = ["이동평균", "손절", "익절", "연습_총수익률", "연습_MDD", "연습_샤프",
            "시험_총수익률", "시험_MDD", "시험_샤프", "시험_거래", "시험_승률"]
    shown = table[cols].copy()
    for col in cols:
        if col.endswith(("총수익률", "MDD", "승률")) or col in ("손절", "익절"):
            shown[col] = shown[col].map(pct)
        elif col.endswith("샤프"):
            shown[col] = shown[col].round(2)
    print(shown.to_string(index=False))

    best = table.loc[table["연습_샤프"].idxmax()]
    print(f"\n연습 기간 ~{train_end:%Y-%m-%d} / 시험 기간 {split:%Y-%m-%d}~")
    print(f"연습 기간 1등(샤프 기준): 이동평균 {best['이동평균']}일, 손절 {pct(best['손절'])}, "
          f"익절 {pct(best['익절'])}")
    print(f"  연습 기간: 총수익률 {pct(best['연습_총수익률'])}, MDD {pct(best['연습_MDD'])} "
          f"(그냥 보유 {pct(best['연습_보유_총수익률'])}, MDD {pct(best['연습_보유_MDD'])})")
    print(f"  시험 기간: 총수익률 {pct(best['시험_총수익률'])}, MDD {pct(best['시험_MDD'])}, "
          f"샤프 {best['시험_샤프']:.2f}, 거래 {best['시험_거래']}번, 승률 {pct(best['시험_승률'])}")
    print(f"  시험 기간 그냥 보유: 총수익률 {pct(best['시험_보유_총수익률'])}, "
          f"MDD {pct(best['시험_보유_MDD'])}")
    print("\n전체 표: results/split_trend.csv")


if __name__ == "__main__":
    main()
