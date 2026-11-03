"""코인 분석 TF팀 회의 자료 모으기 (무료, API 키 불필요). GitHub Actions가 매시간(하루 24번) 돌린다.

1. 채점: 24시간 지난 지난 의견을 실제 가격으로 채점 → paper/tf/SCOREBOARD.md, scoreboard.json
2. 스캔: 바이낸스 USDT 코인 전체를 훑어 후보를 고름 → paper/tf/SCAN.md
3. 자료: BTC·ETH와 후보 코인에 대해 4명분 자료를 모음 → paper/tf/BRIEF.md

회의(BULL/BEAR 토론, ACE 결정)는 Claude 프로젝트 안의 Claude가 aicoin/tf_team/PLAYBOOK.md 순서대로 진행한다.
참고용이며 투자 조언이 아니다.

사용법:
    pip install -r requirements-tf.txt
    python run_tf_team.py                 # 채점 + 전체 스캔 + BTC·ETH·후보 3개 자료
    python run_tf_team.py BTC SOL --no-scan
    python run_tf_team.py --print         # 회의 자료를 저장하지 않고 화면에 출력
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import pandas as pd

from aicoin.tf_team import score, sources
from aicoin.tf_team.brief import build_brief, find_errors
from aicoin.tf_team.scan import ALWAYS, pick, scan, scan_markdown

FOLDER = Path("paper/tf")


def main() -> int:
    ap = argparse.ArgumentParser(description="코인 분석 TF팀 회의 자료 모으기")
    ap.add_argument("coins", nargs="*", help="회의할 코인 (기본: BTC ETH + 스캔 후보)")
    ap.add_argument("--no-scan", action="store_true", help="전체 코인 스캔을 건너뜀")
    ap.add_argument("--trend", type=int, default=2, help="상승 추세 후보 수 (기본 2)")
    ap.add_argument("--oversold", type=int, default=1, help="과매도 반등 후보 수 (기본 1)")
    ap.add_argument("--print", action="store_true", help="회의 자료를 저장하지 않고 화면에 출력")
    args = ap.parse_args()

    FOLDER.mkdir(parents=True, exist_ok=True)
    now = pd.Timestamp.now(tz="Asia/Seoul")
    when = f"{now:%Y-%m-%d %H:%M} KST"
    extra = []

    # 1) 채점
    board = sources._safe(score.run, FOLDER)
    if "오류" in board:
        print(f"채점 실패: {board['오류']}")
    else:
        a = board["ACE"]
        extra.append(f"**지금까지 승률** ACE {a['승률(%)'] if a['승률(%)'] is not None else '자료 없음'}% "
                     f"({a['맞음']}/{a['전체']}), 채점 대기 {board['채점 대기']}개 · 자세히는 `paper/tf/SCOREBOARD.md`, "
                     "교훈은 `aicoin/tf_team/LESSONS.md`")

    # 2) 전체 스캔과 후보
    coins = [c.upper() for c in args.coins] or list(ALWAYS)
    if not args.no_scan:
        table = sources._safe(scan)
        if isinstance(table, dict):
            print(f"스캔 실패: {table['오류']}")
            extra.append(f"**전체 스캔 실패**: {table['오류']}")
        else:
            picks = pick(table, args.trend, args.oversold)
            (FOLDER / "SCAN.md").write_text(scan_markdown(table, picks, when), encoding="utf-8")
            extra.append("**전체 스캔 후보** (`paper/tf/SCAN.md`) " +
                         " · ".join(f"{k}: {', '.join(v) or '없음'}" for k, v in picks.items()))
            if not args.coins:
                coins += [c for group in picks.values() for c in group if c not in coins]

    # 3) 회의 자료
    fng = sources._safe(sources.fear_greed)  # 시장 전체 지표라 한 번만 받는다
    data = {}
    for coin in coins:
        print(f"[{coin}] 자료 수집 중...")
        data[coin] = sources.collect(coin, fng)
        for path, err in find_errors(data[coin]):
            print(f"  ! {path} 수집 실패: {err}")

    brief = build_brief(data, when, "\n\n".join(extra))
    if args.print:
        print(brief)
    else:
        (FOLDER / "BRIEF.md").write_text(brief, encoding="utf-8")
        (FOLDER / "brief_meta.json").write_text(json.dumps({"collected_at": when, "coins": coins}, ensure_ascii=False),
                                                encoding="utf-8")
        print(f"회의 자료 저장: {FOLDER / 'BRIEF.md'} ({', '.join(coins)})")

    # 차트 자료가 하나도 없으면 회의를 열 수 없으므로 실패로 알린다
    return 0 if any("오류" not in d["TARO"] for d in data.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
