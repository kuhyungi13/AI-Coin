"""50일선 말고 다른 "상승 추세" 신호로 분할 추세 전략을 돌려 비교한다.

신호 종류마다 연습 기간(샤프 기준) 1등 설정을 고르고, 처음 보는 시험 기간 성적을 본다.
손절/익절은 지금 모의 투자와 같다(손절 5%, 익절 20%/40%).

사용법:
    python run_entry_variants.py
    python run_entry_variants.py --symbol ETHUSDT --interval 4h
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from aicoin import signals
from aicoin.data import load_klines
from aicoin.split_trend import SplitParams, run_split
from run_split_trend import pct, stats

FAMILIES = {
    "이동평균(SMA)": (signals.ma_gate, [{"n": n} for n in (10, 20, 30, 50, 100)]),
    "지수이동평균(EMA)": (signals.ema_gate, [{"n": n} for n in (10, 20, 30, 50)]),
    "느슨한 50일선(-k×ATR)": (signals.loose_ma, [{"n": n, "k": k} for n in (30, 50) for k in (0.5, 1, 2)]),
    "켈트너 돌파": (signals.keltner, [{"n": n, "k": k} for n in (10, 20, 50) for k in (0.5, 1, 2)]),
    "볼린저 돌파": (signals.bollinger, [{"n": n, "k": k} for n in (10, 20, 50) for k in (0.5, 1, 2)]),
    "슈퍼트렌드": (signals.supertrend, [{"n": n, "k": k} for n in (7, 10, 20) for k in (2, 3, 4)]),
    "돈키언 돌파": (signals.donchian, [{"n": n, "m": m} for n in (10, 20, 55) for m in (5, 10, 20)]),
}


def main() -> None:
    ap = argparse.ArgumentParser(description="추세 신호 종류별 분할 추세 전략 비교")
    ap.add_argument("--symbol", default="BTCUSDT")
    ap.add_argument("--interval", default="1d")
    ap.add_argument("--start", default="2018-01-01")
    ap.add_argument("--split", default="2023-01-01")
    ap.add_argument("--stop", type=float, default=0.05)
    ap.add_argument("--tp", type=float, default=0.20)
    args = ap.parse_args()

    df = load_klines(args.symbol, args.interval, args.start, None)
    split = pd.Timestamp(args.split, tz=df.index.tz)
    train_end = split - pd.Timedelta(seconds=1)
    p = SplitParams(stop=args.stop, tp=args.tp)

    rows = []
    for family, (fn, grid) in FAMILIES.items():
        for kw in grid:
            res, trades = run_split(df, p, signal=fn(df, **kw))
            tr, te = stats(res, trades, end=train_end), stats(res, trades, start=split)
            rows.append({"신호": family, "설정": ", ".join(f"{k}={v}" for k, v in kw.items()),
                         "투자중_비율": float(period_in_pos(res, split)),
                         **{f"연습_{k}": v for k, v in tr.items()},
                         **{f"시험_{k}": v for k, v in te.items()}})
    table = pd.DataFrame(rows)
    Path("results").mkdir(exist_ok=True)
    out = f"results/entry_variants_{args.symbol}_{args.interval}.csv"
    table.to_csv(out, index=False, encoding="utf-8-sig")

    hold = table.iloc[0]
    print(f"{args.symbol} {args.interval}, 연습 ~{train_end:%Y-%m-%d} / 시험 {split:%Y-%m-%d}~")
    print(f"시험 기간 그냥 보유: {pct(hold['시험_보유_총수익률'])} (MDD {pct(hold['시험_보유_MDD'])})\n")
    best = table.loc[table.groupby("신호")["연습_샤프"].idxmax()]
    cols = ["신호", "설정", "연습_총수익률", "시험_총수익률", "시험_MDD", "시험_샤프",
            "시험_거래", "시험_승률", "투자중_비율"]
    shown = best[cols].sort_values("시험_샤프", ascending=False).copy()
    for c in ("연습_총수익률", "시험_총수익률", "시험_MDD", "시험_승률", "투자중_비율"):
        shown[c] = shown[c].map(pct)
    shown["시험_샤프"] = shown["시험_샤프"].round(2)
    print("신호별 연습 기간 1등 설정 → 시험 기간 성적")
    print(shown.to_string(index=False))
    med = table.groupby("신호")["시험_총수익률"].median().map(pct)
    print("\n신호별 모든 설정의 시험 기간 수익률 중앙값")
    print(med.to_string())
    print(f"\n전체 표: {out}")


def period_in_pos(res: pd.DataFrame, start) -> float:
    return res.loc[start:, "trade"].mean()


if __name__ == "__main__":
    main()
