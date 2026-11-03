"""코인 분석 TF팀 회의를 연다.

애널리스트 4명(TARO 차트, DIANA 펀더멘털, NOVA 뉴스, VIBE 센티먼트)이 보고서를 쓰고,
BULL과 BEAR가 토론한 뒤, 수석 트레이더 ACE가 매수/관망/매도 의견을 낸다.
참고용 분석이며 투자 조언이 아니다.

사용법:
    pip install -r requirements-tf.txt
    set ANTHROPIC_API_KEY=sk-ant-...      (맥/리눅스: export ANTHROPIC_API_KEY=sk-ant-...)
    python run_tf_team.py                 # 기본: BTC ETH, 토론 2라운드
    python run_tf_team.py BTC SOL XRP --rounds 3
    python run_tf_team.py --dry-run       # Claude 없이 자료 수집만 확인 (API 키 불필요, 비용 없음)

결과: paper/TF_REPORT.md (최신) 와 paper/tf/날짜.md (기록)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import pandas as pd

from aicoin.tf_team import sources
from aicoin.tf_team.report import build_report
from aicoin.tf_team.team import MODEL, claude_llm, run_meeting

OUT_LATEST = Path("paper/TF_REPORT.md")
OUT_DIR = Path("paper/tf")


def find_errors(obj, path: str = "") -> list[tuple[str, str]]:
    """수집 결과 안의 {"오류": ...} 항목을 모두 찾는다."""
    if not isinstance(obj, dict):
        return []
    if "오류" in obj:
        return [(path, obj["오류"])]
    if "수집 실패" in obj:  # 뉴스처럼 출처 여러 곳 중 일부만 실패한 경우
        return [(f"{path}/{src}", err) for src, err in obj["수집 실패"].items()]
    return [e for k, v in obj.items() for e in find_errors(v, f"{path}/{k}" if path else k)]


def main() -> int:
    ap = argparse.ArgumentParser(description="코인 분석 TF팀 (참고용, 투자 조언 아님)")
    ap.add_argument("coins", nargs="*", default=["BTC", "ETH"], help="분석할 코인 심볼 (기본: BTC ETH)")
    ap.add_argument("--rounds", type=int, default=2, help="BULL vs BEAR 토론 라운드 수 (기본 2)")
    ap.add_argument("--dry-run", action="store_true", help="자료 수집만 하고 결과를 출력 (Claude 호출 없음)")
    ap.add_argument("--model", default=MODEL, help=f"Claude 모델 (기본 {MODEL})")
    args = ap.parse_args()

    coins = [c.upper() for c in args.coins]
    fng = sources._safe(sources.fear_greed)  # 시장 전체 지표라 한 번만 받는다

    if args.dry_run:
        broken, chart_ok = 0, True
        for coin in coins:
            data = sources.collect(coin, fng)
            print(f"\n===== {coin} =====")
            print(json.dumps(data, ensure_ascii=False, indent=1, default=str)[:4000])
            for path, err in find_errors(data):
                print(f"  ! {path} 수집 실패: {err}")
                broken += 1
            chart_ok &= "오류" not in data["TARO"]
        print(f"\n자료 수집 완료. 실패한 자료 수: {broken}")
        return 0 if chart_ok else 1  # 차트 자료는 꼭 있어야 한다

    llm = claude_llm(args.model)
    meetings, failures = [], {}
    for coin in coins:
        try:
            print(f"[{coin}] 자료 수집 중...")
            data = sources.collect(coin, fng)
            meetings.append(run_meeting(coin, data, llm, rounds=args.rounds))
            v = meetings[-1].verdict
            print(f"[{coin}] ACE: {v['decision']} (확신도 {v['confidence']}/10) - {v['one_line']}")
        except Exception as e:  # 한 코인이 실패해도 나머지는 계속한다
            failures[coin] = f"{type(e).__name__}: {e}"
            print(f"[{coin}] 실패: {failures[coin]}", file=sys.stderr)

    if not meetings:
        print("모든 코인 분석이 실패했습니다.", file=sys.stderr)
        return 1

    now = pd.Timestamp.now(tz="Asia/Seoul")
    report = build_report(meetings, f"{now:%Y-%m-%d %H:%M} KST", args.model, failures)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_LATEST.write_text(report, encoding="utf-8")
    (OUT_DIR / f"{now:%Y-%m-%d}.md").write_text(report, encoding="utf-8")
    print(f"\n보고서 저장: {OUT_LATEST}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
