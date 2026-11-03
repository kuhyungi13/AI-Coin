"""7명 코인 분석 TF팀.

1) 애널리스트 4명(TARO 차트, DIANA 펀더멘털, NOVA 뉴스, VIBE 센티먼트)이 각자 자료로 보고서를 쓴다 (동시에).
2) BULL(매수 논거)과 BEAR(매도·리스크 논거)가 보고서를 읽고 정해진 라운드만큼 서로 반박한다.
3) ACE(수석 트레이더)가 전부 듣고 매수/관망/매도 의견을 낸다.

분석용이며 투자 조언이 아니다. Claude API 키(ANTHROPIC_API_KEY)가 필요하다.
"""

from __future__ import annotations

import json
import os
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from typing import Callable

MODEL = os.environ.get("TF_MODEL", "claude-opus-5-5")

COMMON = (
    "당신은 코인 분석 TF팀의 팀원입니다. 한국어로 씁니다. 주어진 자료에 있는 숫자와 사실만 근거로 쓰고, "
    "자료에 없는 것은 지어내지 말고 '자료 없음'이라고 적습니다. 자료 수집이 실패한 항목은 실패했다고 밝힙니다. "
    "이 분석은 참고용이며 투자 조언이 아닙니다."
)

ANALYSTS = {
    "TARO": ("기술적 분석", "차트 담당 애널리스트입니다. 일봉·4시간봉의 MA20/MA60/MA120 배열, 최근 골든·데드크로스, "
             "RSI, 거래량, 변동성(ATR), 30일 고점·저점을 보고 추세와 지지·저항 구간을 정리합니다."),
    "DIANA": ("기본적 분석", "펀더멘털 담당 애널리스트입니다. 코인은 재무제표가 없으므로 시가총액·순위, FDV 대비 시총(추가 발행 부담), "
              "유통 비율, 거래대금, 역대 최고가 대비 위치, 체인 TVL, 프로젝트 성격으로 가치와 구조적 위험을 평가합니다."),
    "NOVA": ("뉴스 분석", "뉴스 담당 애널리스트입니다. 최근 3일 기사에서 가격에 영향을 줄 만한 사건(규제, ETF·기관 자금, 해킹, 상장·업그레이드, "
             "거시 경제)을 골라 호재/악재/중립으로 나누고 중요도를 매깁니다."),
    "VIBE": ("센티먼트", "센티먼트 담당 애널리스트입니다. 공포·탐욕 지수, 선물 펀딩비·롱숏 비율·미결제약정, 커뮤니티 인기글로 "
             "개미 투자자 분위기를 읽습니다. 과열(모두가 롱)과 공포(투매) 신호를 특히 짚습니다."),
}
ANALYST_FORMAT = (
    "\n\n다음 형식으로 20줄 이내로 씁니다.\n"
    "### 한 줄 요약\n### 핵심 근거 (숫자 포함, 3~5개)\n### 이 관점의 판단: 긍정 / 중립 / 부정 중 하나와 이유"
)

BULL = ("BULL", "매수 논거 담당 리서처입니다. 애널리스트 보고서에서 사야 할 이유를 가장 설득력 있게 정리합니다. "
        "약점도 알지만 상대(BEAR)의 주장에 근거로 반박합니다. 숫자를 인용하고 12줄 이내로 씁니다.")
BEAR = ("BEAR", "리스크 담당 리서처입니다. 애널리스트 보고서에서 팔거나 피해야 할 이유와 리스크 목록을 가장 설득력 있게 정리합니다. "
        "상대(BULL)의 주장에 근거로 반박합니다. 숫자를 인용하고 12줄 이내로 씁니다.")
ACE = ("ACE", "수석 트레이더입니다. 애널리스트 4명의 보고와 BULL·BEAR 토론을 모두 듣고 최종 의견을 냅니다. "
       "어느 한쪽 말만 따르지 말고, 근거가 더 탄탄한 쪽과 무시할 수 없는 리스크를 함께 저울질합니다. "
       "확신이 낮으면 관망을 택합니다.")

ACE_SCHEMA = {
    "type": "object",
    "properties": {
        "decision": {"type": "string", "enum": ["매수", "관망", "매도"]},
        "confidence": {"type": "integer", "description": "확신도 1~10"},
        "one_line": {"type": "string", "description": "결론 한 문장"},
        "reasons": {"type": "array", "items": {"type": "string"}, "description": "결정 이유 3~5개"},
        "risks": {"type": "array", "items": {"type": "string"}, "description": "반대로 갈 수 있는 리스크 2~4개"},
        "watch": {"type": "array", "items": {"type": "string"},
                  "description": "의견을 바꿀 조건이나 지켜볼 가격대·지표 2~4개"},
        "winner": {"type": "string", "enum": ["BULL", "BEAR", "무승부"], "description": "토론에서 더 설득력 있던 쪽"},
    },
    "required": ["decision", "confidence", "one_line", "reasons", "risks", "watch", "winner"],
    "additionalProperties": False,
}

# (system, user, effort, json_schema 또는 None) -> 응답 텍스트
LLM = Callable[[str, str, str, dict | None], str]


def claude_llm(model: str = MODEL) -> LLM:
    import anthropic

    client = anthropic.Anthropic()

    def call(system: str, user: str, effort: str, schema: dict | None) -> str:
        output_config: dict = {"effort": effort}
        if schema is not None:
            output_config["format"] = {"type": "json_schema", "schema": schema}
        resp = client.beta.messages.create(
            model=model,
            max_tokens=16000,
            system=system,
            messages=[{"role": "user", "content": user}],
            output_config=output_config,
            # 안전 분류기가 거절하면 서버가 알맞은 다른 모델로 자동 재시도한다
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
        )
        if resp.stop_reason == "refusal":
            raise RuntimeError(f"Claude가 응답을 거절했습니다: {getattr(resp.stop_details, 'explanation', '')}")
        text = "".join(b.text for b in resp.content if b.type == "text").strip()
        if not text:
            raise RuntimeError(f"빈 응답 (stop_reason={resp.stop_reason})")
        return text

    return call


@dataclass
class Meeting:
    coin: str
    reports: dict[str, str] = field(default_factory=dict)
    debate: list[tuple[str, str]] = field(default_factory=list)  # (BULL|BEAR, 발언)
    verdict: dict = field(default_factory=dict)


def _dump(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=1, default=str)


def _reports_text(m: Meeting) -> str:
    return "\n\n".join(f"## {name} ({ANALYSTS[name][0]}) 보고서\n{text}" for name, text in m.reports.items())


def _debate_text(m: Meeting) -> str:
    return "\n\n".join(f"**{who}**: {say}" for who, say in m.debate) or "(아직 발언 없음)"


def run_meeting(coin: str, data: dict, llm: LLM, rounds: int = 2,
                log: Callable[[str], None] = print) -> Meeting:
    m = Meeting(coin.upper())

    # 1) 애널리스트 4명 동시에
    log(f"[{m.coin}] 애널리스트 팀 분석 중... (TARO, DIANA, NOVA, VIBE)")

    def analyst(name: str) -> tuple[str, str]:
        role, desc = ANALYSTS[name]
        system = f"{COMMON}\n당신의 이름은 {name}, {desc}{ANALYST_FORMAT}"
        user = f"{m.coin} 분석 자료입니다.\n```json\n{_dump(data.get(name))}\n```\n{role} 보고서를 써 주세요."
        return name, llm(system, user, "medium", None)

    with ThreadPoolExecutor(4) as ex:
        m.reports = dict(ex.map(analyst, ANALYSTS))

    # 2) BULL vs BEAR 토론. 라운드마다 둘이 동시에 말하고, 다음 라운드엔 상대 발언을 보고 반박한다.
    for r in range(1, rounds + 1):
        log(f"[{m.coin}] 리서치 팀 토론 {r}/{rounds}라운드...")

        def speak(persona: tuple[str, str]) -> tuple[str, str]:
            name, desc = persona
            system = f"{COMMON}\n당신의 이름은 {name}, {desc}"
            task = ("첫 발언입니다. 핵심 논거를 제시하세요." if r == 1 else
                    "상대의 직전 발언을 구체적으로 반박하고 논거를 보강하세요. 이미 한 말은 반복하지 마세요.")
            user = (f"{m.coin} 애널리스트 보고서:\n\n{_reports_text(m)}\n\n"
                    f"지금까지의 토론:\n{_debate_text(m)}\n\n{r}라운드. {task}")
            return name, llm(system, user, "medium", None)

        with ThreadPoolExecutor(2) as ex:
            m.debate.extend(ex.map(speak, [BULL, BEAR]))

    # 3) ACE 최종 결정
    log(f"[{m.coin}] ACE가 팀 보고 청취 후 결정 중...")
    system = f"{COMMON}\n당신의 이름은 {ACE[0]}, {ACE[1]}"
    user = (f"{m.coin} 애널리스트 보고서:\n\n{_reports_text(m)}\n\nBULL vs BEAR 토론:\n{_debate_text(m)}\n\n"
            "최종 의견을 정해진 JSON 형식으로 내 주세요.")
    m.verdict = json.loads(llm(system, user, "high", ACE_SCHEMA))
    return m
