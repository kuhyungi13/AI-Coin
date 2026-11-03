"""코인 분석 TF팀 회의 자료 모으기 (무료, API 키 불필요).

애널리스트 4명(TARO 차트, DIANA 펀더멘털, NOVA 뉴스, VIBE 센티먼트)이 볼 자료를 모아
paper/tf/BRIEF.md 한 파일로 만든다. 회의(BULL/BEAR 토론, ACE 결정)는 Claude 프로젝트 안의 Claude가
aicoin/tf_team/PLAYBOOK.md 순서대로 진행한다. 참고용이며 투자 조언이 아니다.

사용법:
    pip install -r requirements-tf.txt
    python run_tf_team.py                 # 기본: BTC ETH
    python run_tf_team.py BTC SOL XRP
    python run_tf_team.py --print         # 파일로 저장하지 않고 화면에만 출력
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

from aicoin.tf_team import sources
from aicoin.tf_team.brief import build_brief, find_errors

OUT = Path("paper/tf/BRIEF.md")


def main() -> int:
    ap = argparse.ArgumentParser(description="코인 분석 TF팀 회의 자료 모으기")
    ap.add_argument("coins", nargs="*", default=["BTC", "ETH"], help="분석할 코인 심볼 (기본: BTC ETH)")
    ap.add_argument("--print", action="store_true", help="저장하지 않고 화면에 출력")
    args = ap.parse_args()

    coins = [c.upper() for c in args.coins]
    fng = sources._safe(sources.fear_greed)  # 시장 전체 지표라 한 번만 받는다
    data = {}
    for coin in coins:
        print(f"[{coin}] 자료 수집 중...")
        data[coin] = sources.collect(coin, fng)
        for path, err in find_errors(data[coin]):
            print(f"  ! {path} 수집 실패: {err}")

    now = pd.Timestamp.now(tz="Asia/Seoul")
    brief = build_brief(data, f"{now:%Y-%m-%d %H:%M} KST")
    if args.print:
        print(brief)
    else:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(brief, encoding="utf-8")
        print(f"회의 자료 저장: {OUT}")

    # 차트 자료가 하나도 없으면 회의를 열 수 없으므로 실패로 알린다
    return 0 if any("오류" not in d["TARO"] for d in data.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
