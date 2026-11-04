"""TF팀 전략 백테스트 연구 (무료, API 키 불필요). GitHub Actions가 매주 돌려 paper/tf/research/BACKTEST.md 를 만든다.

사용법:
    python run_tf_research.py                # 바이낸스 USDT 코인 전체 (오래 걸림)
    python run_tf_research.py --top 60       # 거래대금 상위 60개만 (시험용)
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from aicoin.tf_team import research
from aicoin.universe import load_many, usdt_symbols

OUT = Path("paper/tf/research")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=0, help="거래대금 상위 N개만 (0이면 전체)")
    ap.add_argument("--start", default="2021-01-01")
    args = ap.parse_args()

    symbols = usdt_symbols(include_delisted=True)
    frames = load_many(symbols, start=args.start, cache_dir="data/daily")
    if args.top:
        vol = {s: df["quote_volume"].tail(90).mean() for s, df in frames.items()}
        keep = sorted(vol, key=vol.get, reverse=True)[: args.top]
        frames = {s: frames[s] for s in keep}
    results = {lev: research.run(frames, lev=lev) for lev in (1, 3)}
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "BACKTEST.md").write_text(research.markdown(results, updated, len(frames)), encoding="utf-8")
    (OUT / "backtest.json").write_text(json.dumps({"updated": updated, "coins": len(frames), "results": results},
                                                   ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"완료: 코인 {len(frames)}개 → {OUT / 'BACKTEST.md'}")


if __name__ == "__main__":
    main()
