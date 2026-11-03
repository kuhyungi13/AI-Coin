"""회의 자료(브리프) 만들기. 모은 자료를 사람과 Claude가 읽기 좋은 마크다운 한 파일로 묶는다.

회의 자체(애널리스트 4명 → BULL/BEAR 토론 → ACE 결정)는 Claude 프로젝트 안의 Claude가
aicoin/tf_team/PLAYBOOK.md 순서대로 이 파일을 읽고 진행한다. 그래서 API 비용이 들지 않는다.
"""

from __future__ import annotations

import json

TEAM = {
    "TARO": "기술적 분석 (차트)",
    "DIANA": "기본적 분석 (펀더멘털)",
    "NOVA": "뉴스 분석",
    "VIBE": "센티먼트 (개미 분위기)",
}


def find_errors(obj, path: str = "") -> list[tuple[str, str]]:
    """수집 결과 안의 실패 항목({"오류": ...} 또는 {"수집 실패": {...}})을 모두 찾는다."""
    if not isinstance(obj, dict):
        return []
    if "오류" in obj:
        return [(path, obj["오류"])]
    out = []
    if "수집 실패" in obj:  # 뉴스처럼 출처 여러 곳 중 일부만 실패한 경우
        out += [(f"{path}/{src}", err) for src, err in obj["수집 실패"].items()]
    return out + [e for k, v in obj.items() if k != "수집 실패"
                  for e in find_errors(v, f"{path}/{k}" if path else k)]


def build_brief(data: dict[str, dict], when: str) -> str:
    """data: {코인: sources.collect(코인) 결과}"""
    lines = [
        f"# TF팀 회의 자료 ({when})",
        "",
        "GitHub Actions가 무료 공개 API로 모은 자료입니다. 회의 진행 방법은 `aicoin/tf_team/PLAYBOOK.md`.",
        "자료에 없는 숫자는 쓰지 않습니다. 실패한 자료는 아래 '수집 실패'에 있습니다.",
        "",
        f"분석 대상: {', '.join(data)}",
        "",
    ]
    for coin, parts in data.items():
        lines += [f"## {coin}", ""]
        errs = find_errors(parts)
        if errs:
            lines += ["**수집 실패**", *[f"- {p}: {e}" for p, e in errs], ""]
        for who, label in TEAM.items():
            lines += [f"### {who} 자료 · {label}", "", "```json",
                      json.dumps(parts.get(who), ensure_ascii=False, indent=1, default=str), "```", ""]
    return "\n".join(lines)
