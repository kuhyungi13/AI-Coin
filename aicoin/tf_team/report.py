"""회의 결과를 마크다운 보고서로 만든다."""

from __future__ import annotations

from .team import ANALYSTS, Meeting

DECISION_ICON = {"매수": "🟢", "관망": "🟡", "매도": "🔴"}


def coin_section(m: Meeting) -> str:
    v = m.verdict
    lines = [
        f"## {m.coin}: {DECISION_ICON.get(v.get('decision'), '')} {v.get('decision')} (확신도 {v.get('confidence')}/10)",
        "",
        f"> **ACE**: {v.get('one_line')}",
        "",
        "**결정 이유**",
        *[f"- {x}" for x in v.get("reasons", [])],
        "",
        "**리스크**",
        *[f"- {x}" for x in v.get("risks", [])],
        "",
        "**지켜볼 것**",
        *[f"- {x}" for x in v.get("watch", [])],
        "",
        f"토론 판정: **{v.get('winner')}** 쪽이 더 설득력 있었음",
        "",
        "<details><summary>애널리스트 팀 보고서</summary>",
        "",
    ]
    for name, text in m.reports.items():
        lines += [f"### {name} · {ANALYSTS[name][0]}", "", text, ""]
    lines += ["</details>", "", "<details><summary>리서치 팀 토론 (BULL vs BEAR)</summary>", ""]
    for i, (who, say) in enumerate(m.debate):
        lines += [f"### {who} ({i // 2 + 1}라운드)", "", say, ""]
    lines += ["</details>", ""]
    return "\n".join(lines)


def build_report(meetings: list[Meeting], when: str, model: str, failures: dict[str, str] | None = None) -> str:
    rows = [f"| {m.coin} | {DECISION_ICON.get(m.verdict.get('decision'), '')} {m.verdict.get('decision')} "
            f"| {m.verdict.get('confidence')}/10 | {m.verdict.get('one_line')} |" for m in meetings]
    head = [
        f"# 코인 분석 TF팀 보고서 ({when})",
        "",
        "> 7명의 AI 팀(TARO 차트 · DIANA 펀더멘털 · NOVA 뉴스 · VIBE 센티먼트 · BULL · BEAR · ACE)이 공개 자료로 낸 의견입니다. "
        "**참고용이며 투자 조언이 아닙니다.**",
        "",
        "| 코인 | ACE 의견 | 확신도 | 한 줄 요약 |",
        "|---|---|---|---|",
        *rows,
        "",
    ]
    if failures:
        head += ["**분석 실패**", *[f"- {c}: {e}" for c, e in failures.items()], ""]
    body = [coin_section(m) for m in meetings]
    return "\n".join(head + body + [f"<sub>모델: {model}</sub>", ""])
