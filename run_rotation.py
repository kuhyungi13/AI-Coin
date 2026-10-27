"""코인 고르기(순환매) 전략 검증 실행 파일.

바이낸스 USDT 코인 전체 일봉을 받아, 설정 여러 개를 연습 기간(2019~2022)에 돌려 보고
처음 보는 시험 기간(2023~)에서 비트코인 그냥 보유와 비교한다.

기본은 지금 거래 중인 코인만 쓴다. 상장 폐지된 코인은 빠지므로 과거 성적이 실제보다 좋게 나온다.
    python run_rotation.py
    python run_rotation.py --include-delisted   # 상장 폐지 코인까지 넣어 시험
처음 실행할 때 코인 500여 개를 받느라 몇 분 걸린다(data/daily/에 저장해 두고 다음부터 재사용).
"""

from __future__ import annotations

import argparse
import itertools
from pathlib import Path

import pandas as pd

from aicoin.rotation import Panels, RotationParams, run_rotation
from aicoin.strategy import period, summarize
from aicoin.universe import load_many, usdt_symbols


def pct(v: float) -> str:
    return f"{v * 100:,.1f}%"


def main() -> None:
    ap = argparse.ArgumentParser(description="코인 고르기 전략 연습/시험 검증")
    ap.add_argument("--start", default="2019-01-01")
    ap.add_argument("--split", default="2023-01-01")
    ap.add_argument("--include-delisted", action="store_true", help="상장 폐지된 코인도 넣는다")
    ap.add_argument("--refresh", action="store_true", help="저장해 둔 데이터를 새로 받는다")
    args = ap.parse_args()

    symbols = usdt_symbols(include_delisted=args.include_delisted)
    print(f"코인 {len(symbols)}개 데이터 준비 중...")
    px = Panels.from_frames(load_many(symbols, refresh=args.refresh))
    split = pd.Timestamp(args.split, tz="UTC")
    train_end = split - pd.Timedelta(days=1)

    rows = []
    for top, picks, lookback in itertools.product((5, 10, 20, 50), (1, 3, 5), (14, 30, 60, 90)):
        if picks >= top:
            continue
        p = RotationParams(top_n=top, picks=picks, lookback=lookback)
        res, _ = run_rotation(px, p, start=args.start)
        tr, te = summarize(period(res, None, train_end)), summarize(period(res, split, None))
        rows.append({"후보수": top, "보유수": picks, "기간": lookback,
                     "연습_총수익률": tr["총수익률"], "연습_MDD": tr["최대낙폭(MDD)"], "연습_샤프": tr["샤프지수"],
                     "시험_총수익률": te["총수익률"], "시험_MDD": te["최대낙폭(MDD)"], "시험_샤프": te["샤프지수"],
                     "시험_보유": te["단순보유_총수익률"], "시험_보유_MDD": te["단순보유_MDD"]})
    table = pd.DataFrame(rows)
    Path("results").mkdir(exist_ok=True)
    table.to_csv("results/rotation.csv", index=False, encoding="utf-8-sig")

    shown = table.drop(columns=["시험_보유", "시험_보유_MDD"]).copy()
    for col in shown.columns:
        if col.endswith(("총수익률", "MDD")):
            shown[col] = shown[col].map(pct)
        elif col.endswith("샤프"):
            shown[col] = shown[col].round(2)
    print(shown.to_string(index=False))

    best = table.loc[table["연습_샤프"].idxmax()]
    hold = best["시험_보유"]
    print(f"\n연습 기간 {args.start}~{train_end:%Y-%m-%d} / 시험 기간 {split:%Y-%m-%d}~")
    print(f"연습 기간 1등(샤프 기준): 거래대금 상위 {int(best['후보수'])}개 중 {int(best['기간'])}일 동안 많이 오른 "
          f"{int(best['보유수'])}개")
    print(f"  연습 기간: 총수익률 {pct(best['연습_총수익률'])}, MDD {pct(best['연습_MDD'])}")
    print(f"  시험 기간: 총수익률 {pct(best['시험_총수익률'])}, MDD {pct(best['시험_MDD'])}")
    print(f"  시험 기간 비트코인 그냥 보유: 총수익률 {pct(hold)}, MDD {pct(best['시험_보유_MDD'])}")
    print(f"시험 기간에 돈을 번 설정: {(table['시험_총수익률'] > 0).sum()}/{len(table)}개, "
          f"비트코인 보유보다 나은 설정: {(table['시험_총수익률'] > hold).sum()}개")
    print("\n전체 표: results/rotation.csv")


if __name__ == "__main__":
    main()
