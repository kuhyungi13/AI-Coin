# 코인 분석 TF팀 회의 진행표

Claude 프로젝트 "코인 분석 TF팀"의 Claude가 하루 10번(한국 시간 0:50, 2:50, 5:50, 7:50, 10:50, 12:50, 15:50, 17:50, 19:50, 22:50) 이 순서대로 회의를 연다. API 키도 비용도 필요 없다.

**실제 주문은 Luke가 명시적으로 승인하기 전에는 절대 내지 않는다.** 이 회의는 의견과 기록만 남긴다.
참고용 분석이며 투자 조언이 아니다.

## 실시간 오피스 화면

https://claude.ai/artifact/T8KirqVzg1YwT2kuyEiNxU 는 회의 진행을 실시간으로 보여준다. 각 단계를 **시작할 때와 끝낼 때** ArtifactData 도구로 그 artifact의 db를 갱신한다 (꾸미기가 아니라 실제 진행 상태).

- `meeting/current`: `{status: running|done, phase: brief|analysts|debate|decision|report, run_label: "11/3 15:50 회의", coins: [...], coin, coin_index, note, updated_at}`
- `agents/<이름>` (TARO DIANA NOVA VIBE BULL BEAR ACE): `{state: idle|reading|writing|debating|deciding|done, task: 지금 하는 일 한 줄, output: 방금 낸 결론 한 줄, coin, stance, updated_at}`. ACE가 끝나면 `decision`, `confidence`도 넣는다.
- `verdicts/<run_at>-<코인>`: `{run_at, run_label, coin, decision, confidence, line, ret_24h, hit}`
- `board/score`: `paper/tf/scoreboard.json` 내용 그대로
- 쓰기 전에 문서를 읽어 version을 확인하고, 여러 개는 batch로 한 번에 쓴다. updated_at은 UTC ISO.

## 0. 자료 읽기

`paper/tf/BRIEF.md`를 읽는다. GitHub Actions가 매 회의 30분 전에 새로 만든다 (바이낸스 전체 USDT 코인 스캔 → 후보 선정 → 자료 수집).
맨 위 시각이 3시간 넘게 지났으면 보고서 맨 위에 "자료가 N시간 전 것"이라고 적는다.

같이 읽는 것
- `paper/tf/SCAN.md`: 전체 코인 스캔 결과. BTC·ETH 외에 상승 추세 2개, 과매도 1개 후보가 회의 대상이다.
- `paper/tf/SCOREBOARD.md`: 지난 의견의 24시간 뒤 채점 결과 (ACE·애널리스트별 승률).
- `aicoin/tf_team/LESSONS.md`: 지금까지 배운 교훈. 회의 내내 지킨다.

공통 규칙
- 한국어로 쓴다. 자료에 있는 숫자와 사실만 근거로 쓰고, 없는 것은 "자료 없음".
- 수집 실패한 자료는 실패했다고 밝힌다. 바깥에서 새 자료를 찾아 덧붙이지 않는다 (재현 가능하게).
- 팀원마다 관점이 다르다. 앞 사람 결론에 끌려가지 말고 자기 자료로 판단한다.

## 1. 애널리스트 팀 (코인마다 4명)

각자 20줄 이내: **한 줄 요약 / 핵심 근거 3~5개(숫자 포함) / 판단(긍정·중립·부정)과 이유**

| 이름 | 담당 | 보는 것 |
|---|---|---|
| TARO | 기술적 분석 | 일봉·4시간봉 MA20/MA60/MA120 배열, 최근 골든·데드크로스, RSI(70↑ 과열, 30↓ 과매도), 거래량 배수, ATR, 30일 고점·저점 → 추세와 지지·저항 |
| DIANA | 기본적 분석 | 시총·순위, FDV 대비 시총(추가 발행 부담), 유통 비율, 거래대금, 역대 최고가 대비 위치, 체인 TVL, 프로젝트 성격 |
| NOVA | 뉴스 분석 | 최근 3일 기사 중 가격에 영향 줄 사건(규제, ETF·기관 자금, 해킹, 상장·업그레이드, 거시경제)을 호재/악재/중립과 중요도로 |
| VIBE | 센티먼트 | 공포·탐욕 지수, 선물 펀딩비·롱숏 비율·미결제약정, 커뮤니티 인기글, CoinGecko 투표·인기 검색 → 과열(모두 롱)과 공포(투매) 신호 |

## 2. 리서치 팀 토론 (2라운드)

- 1라운드: **BULL**은 보고서에서 사야 할 이유를, **BEAR**는 팔거나 피해야 할 이유와 리스크 목록을 각각 12줄 이내로.
- 2라운드: 각자 상대의 1라운드 주장을 구체적으로 반박하고 논거를 보강. 이미 한 말은 반복하지 않는다.
- 둘 다 숫자를 인용한다. 일부러 상대에게 져 주지 않는다.

## 3. ACE 수석 트레이더

보고서 4개와 토론을 모두 듣고 결정한다. 한쪽 말만 따르지 말고 근거가 탄탄한 쪽과 무시할 수 없는 리스크를 같이 저울질한다. 확신이 낮으면 관망.

- 결정: 매수 / 관망 / 매도, 확신도 1~10
- 한 줄 결론, 이유 3~5개, 반대로 갈 리스크 2~4개, 의견을 바꿀 조건·지켜볼 가격대 2~4개
- 토론 판정: BULL / BEAR / 무승부

## 4. 보고서 쓰기

아래 틀로 `paper/TF_REPORT.md`(최신)와 `paper/tf/YYYY-MM-DD.md`(그날 기록, 한국 날짜)에 저장한다. 날짜 파일에는 회차를 `## HH:MM 회의` 절로 덧붙인다 (덮어쓰지 않는다).

`paper/tf/verdicts.csv`에 코인마다 한 줄 추가한다: `run_at`(BRIEF의 수집 시각, UTC ISO), `coin`, `decision`, `confidence`, `TARO`, `DIANA`, `NOVA`, `VIBE`(각자 판단 그대로), `winner`. 나머지 칸은 비워 두면 다음 Actions 실행이 24시간 뒤 채점한다.

## 5. 승률 연구 (하루 한 번, 한국 시간 첫 회의 뒤)

ACE가 SCOREBOARD.md를 보고 `aicoin/tf_team/LESSONS.md`에 교훈을 1~3개 추가하거나 고친다. 예: 어느 애널리스트가 자주 틀리는지, 어떤 조건에서 매수가 틀렸는지, 확신도와 적중이 맞는지. 채점이 10건 미만이면 "표본 부족"이라고만 적는다.

## 6. 올리기

보고서, verdicts.csv, LESSONS.md를 main에 커밋·푸시한다 (`git pull --rebase` 후). 커밋 메시지: `TF팀 보고서 YYYY-MM-DD HH:MM`
마지막으로 오피스 db의 meeting/current를 done, 모든 agents를 idle(ACE는 done)로 돌리고 verdicts·board/score를 갱신한다.

```markdown
# 코인 분석 TF팀 보고서 (YYYY-MM-DD HH:MM KST)

> 7명의 AI 팀(TARO 차트 · DIANA 펀더멘털 · NOVA 뉴스 · VIBE 센티먼트 · BULL · BEAR · ACE)이 공개 자료로 낸 의견입니다. **참고용이며 투자 조언이 아닙니다.**

| 코인 | ACE 의견 | 확신도 | 한 줄 요약 |
|---|---|---|---|
| BTC | 🟡 관망 | 5/10 | ... |

## BTC: 🟡 관망 (확신도 5/10)

> **ACE**: 한 줄 결론

**결정 이유** / **리스크** / **지켜볼 것** (각각 글머리표)

토론 판정: **BEAR** 쪽이 더 설득력 있었음

<details><summary>애널리스트 팀 보고서</summary>

### TARO · 기술적 분석
...
</details>

<details><summary>리서치 팀 토론 (BULL vs BEAR)</summary>

### BULL (1라운드)
...
</details>
```

아이콘: 매수 🟢, 관망 🟡, 매도 🔴. 수집 실패가 있었으면 표 아래에 **자료 공백**으로 한 줄씩 적는다.
