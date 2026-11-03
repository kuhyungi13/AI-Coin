# TF팀 회의 자료 (2026-11-04 04:32 KST)

GitHub Actions가 무료 공개 API로 모은 자료입니다. 회의 진행 방법은 `aicoin/tf_team/PLAYBOOK.md`.
자료에 없는 숫자는 쓰지 않습니다. 실패한 자료는 아래 '수집 실패'에 있습니다.

분석 대상: BTC, ETH, BEAMX, PEPE, GOOGLB

**지금까지 승률** ACE 자료 없음% (0/0), 채점 대기 7개 · 자세히는 `paper/tf/SCOREBOARD.md`, 교훈은 `aicoin/tf_team/LESSONS.md`

**TRAINER 모의 계좌** 총자산 10,000.00 USDT (+0.00%), 보유 없음 · 자세히는 `paper/tf/trainer/TRAINER.md`

**전체 스캔 후보** (`paper/tf/SCAN.md`) 상승 추세: BEAMX, PEPE · 과매도 반등: GOOGLB

## BTC

**수집 실패**
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-02",
  "종가": 76816.0,
  "등락률(%)": {
   "1일": -1.96,
   "7일": -4.16,
   "30일": -9.37,
   "90일": 19.83
  },
  "이동평균": {
   "MA20": 80618.7435,
   "MA60": 81378.111,
   "MA120": 74536.7915
  },
  "종가와 이평선 거리(%)": {
   "MA20": -4.72,
   "MA60": -5.61,
   "MA120": 3.06
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 3
  },
  "RSI14": 34.8,
  "ATR14(%)": 2.57,
  "거래량(20일 평균 대비 배수)": 0.89,
  "30일 최고가": 86999.11,
  "30일 최저가": 76325.98,
  "최근 10일 종가": [
   80888.16,
   80154.09,
   80150.56,
   80909.77,
   81343.5,
   77991.89,
   77368.77,
   77582.02,
   78354.0,
   76816.0
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-03",
  "등락률(%)": {
   "1일": 0.75,
   "7일": -0.26,
   "30일": -5.0,
   "90일": -5.19
  },
  "종가와 이평선 거리(%)": {
   "MA20": 0.05,
   "MA60": -1.83,
   "MA120": -3.55
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 59
  },
  "RSI14": 47.3
 }
}
```

### DIANA 자료 · 기본적 분석 (펀더멘털)

```json
{
 "이름": "Bitcoin",
 "분류": [
  "Smart Contract Platform",
  "Layer 1 (L1)",
  "FTX Holdings",
  "Proof of Work (PoW)",
  "Bitcoin Ecosystem"
 ],
 "시가총액 순위": 1,
 "시가총액(USD)": 1558326674654,
 "완전희석가치 FDV(USD)": 1558326674654,
 "24시간 거래대금(USD)": 26261166264,
 "유통량": 20105365.0,
 "총발행량": 20105365.0,
 "최대발행량": 21000000.0,
 "유통 비율(%)": 95.7,
 "역대 최고가(USD)": 126080,
 "역대 최고가 대비(%)": -38.52141,
 "가격 변화(%)": {
  "7d": -3.75198,
  "30d": -9.15543,
  "1y": -27.55208
 },
 "소개": "Bitcoin is the world's first decentralized cryptocurrency, created in 2009 by the pseudonymous Satoshi Nakamoto. It enables peer-to-peer electronic cash transactions without intermediaries like banks or governments, operating on a blockchain secured by Proof of Work mining and the SHA-256 cryptographic algorithm. \n\nWith a fixed supply cap of 21 million coins and programmatic halvings every four ye",
 "체인 TVL (DefiLlama)": {
  "체인": "Bitcoin",
  "TVL(USD)": 4126531015
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "BTC 관련 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin is breaking a midterm election pattern going back to 2014",
   "요약": "Your day-ahead look for Nov. 3, 2026",
   "시각(UTC)": "11-03 12:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin steadies after dip to $76,300 as ETF outflows and midterm elections weigh on crypto",
   "요약": "Bitcoin edged up 0.2% to around $76,900 since midnight UTC as spot ETFs lost $399 million for a second day and Binance customers pulled a net $4.72 billion.",
   "시각(UTC)": "11-03 11:28"
  },
  {
   "출처": "CoinDesk",
   "제목": "Liquid’s bitcoin IOUs are fully backed again after a $320 million exploit",
   "요약": "A final 250 BTC transfer closed the hole left by September’s bug, but the federation behind the network still hasn’t said who paid to fill it.",
   "시각(UTC)": "11-03 11:12"
  },
  {
   "출처": "CoinDesk",
   "제목": "Tether holds 150,000 bitcoin worth $11.5 billion, CEO Paolo Ardoino says",
   "요약": "Ardoino didn’t say where the extra coins sit. Holdings outside USDT reserves, such as Tether’s investments, wouldn’t appear in the report.",
   "시각(UTC)": "11-03 10:15"
  },
  {
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin faces fifth weekly loss as midterm elections weigh on markets",
   "요약": "A fifth straight weekly decline would mark bitcoin’s joint third-longest losing streak, as oil rebounds and Apple’s margin warning adds to investor caution ahead of the U.S. midterms.",
   "시각(UTC)": "11-03 09:50"
  },
  {
   "출처": "CoinDesk",
   "제목": "Mercado Bitcoin pledges to cover all user losses after near $40 million hack",
   "요약": "Partners like Tether, Circle, and Chainalysis helped freeze $11M of the stolen assets.",
   "시각(UTC)": "11-03 08:56"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin’s latest chart signal looks a lot like the ones before its big crashes",
   "요약": "The Guppy Multiple Moving Average bands signal a bearish momentum, even as seasonality and post-midterm history lean bullish.",
   "시각(UTC)": "11-03 08:50"
  },
  {
   "출처": "CoinDesk",
   "제목": "Binance has spent half its SAFU bitcoin, about $580 million worth, data shows",
   "요약": "The user protection fund now sits below the $800 million level that Binance’s own rules say triggers a top-up, and the exchange hasn’t said when it will refill it.",
   "시각(UTC)": "11-03 05:36"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin miner Cipher posts $31 million profit as AI pivot begins",
   "요약": "The company's revenue dropped 63% in the third quarter, while a $127 million accounting gain helped turn an operating loss into a reported profit.",
   "시각(UTC)": "11-03 05:29"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin drops below $77,000 as chip rout deepens ahead of U.S. midterm vote",
   "요약": "ZEC tumbled nearly 10% and BNB fell under $700 as the Nasdaq 100 slid into a correction, dragging Asian stocks lower.",
   "시각(UTC)": "11-03 04:48"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin traders eye post-election rally as exchange outflows point to supply squeeze",
   "요약": "Bulls are watching short positions, exchange withdrawals and key price levels for signs of a rebound after the midterms.",
   "시각(UTC)": "11-02 18:13"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Wall Street killed Bitcoin’s wild rallies: 10x’s Markus Thielen",
   "요약": "Markus Thielen sees Bitcoin reaching $90,000 by year-end, questions institutional ETF demand and says Ethereum must do more for holders.",
   "시각(UTC)": "11-03 16:47"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin price defends $76K lows as analysts see stocks pricing in ‘political gridlock’",
   "요약": "Bitcoin made modest gains at the start of Wall Street trading on Tuesday as markets awaited cues from the US midterm elections.",
   "시각(UTC)": "11-03 15:44"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Here’s what happened in crypto today",
   "요약": "Need to know what happened in crypto today? Here is the latest news on daily trends and events impacting Bitcoin price, blockchain, DeFi, Web3 and crypto regulation.",
   "시각(UTC)": "11-03 13:50"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Moscow Exchange to launch Bitcoin, Ether and USDT trading in December",
   "요약": "Moscow Exchange plans to launch crypto trading on Dec. 1 under Russia’s new law, with annual purchase limits for non-qualified investors.",
   "시각(UTC)": "11-03 13:15"
  }
 ],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Justin Sun seeks sanctions against Trump-linked World Liberty Financial over UAE ties",
   "요약": "The Tron founder says World Liberty failed to disclose its UAE ties until months into his lawsuit over $45 million in WLFI tokens.",
   "시각(UTC)": "11-03 16:55"
  },
  {
   "출처": "CoinDesk",
   "제목": "South Korea's president says country needs a ‘cybersecurity czar’ following $6.3 billion Binance hack",
   "요약": "Lee Jae Myung said he wants a government-wide agency to tackle cyberattacks as AI raises security concerns across financial institutions and critical infrastructure.",
   "시각(UTC)": "11-03 16:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Amazon, Tesla and SpaceX join OKX–ICE tokenized stock objections as deadline looms",
   "요약": "Objections have reached 56 companies, with nearly 80% of the venture’s initial stock selection opting out.",
   "시각(UTC)": "11-03 16:17"
  },
  {
   "출처": "CoinDesk",
   "제목": "Stablecoin governance group behind OUSD sets out management fee, offers equity earning pool",
   "요약": "Governance group Open Standard will charge a 0.1 basis point management fee on payment volume, capped at at $0.01 per payment.",
   "시각(UTC)": "11-03 16:12"
  },
  {
   "출처": "CoinDesk",
   "제목": "CFTC clears perpetual futures on stocks, bringing crypto trading model to Wall Street",
   "요약": "CFTC Chair Michael Selig said the move gives U.S. traders a regulated alternative to “offshore, and often unregulated, venues.”",
   "시각(UTC)": "11-03 15:02"
  },
  {
   "출처": "CoinDesk",
   "제목": "Binance's $6.3 billion hack began with a fake job interview, and a campaign 'built over many months'",
   "요약": "North Korea-linked attackers spent months compromising Binance employees and internal systems before exploiting its hot-wallet signing infrastructure through Ethereum's EIP-7702 mechanism.",
   "시각(UTC)": "11-03 14:53"
  },
  {
   "출처": "CoinDesk",
   "제목": "South Korea asks its biggest banks how a major crypto hack would hit them",
   "요약": "In its first such survey, the BOK also asked about a crypto price crash, losses at another firm, and each firm’s crypto teams, budgets and investments.",
   "시각(UTC)": "11-03 14:42"
  },
  {
   "출처": "CoinDesk",
   "제목": "CZ warns of more AI-driven hacks following Binance’s historic $6.3 billion heist",
   "요약": "While investigators found no evidence that AI agents laundered the stolen Binance funds, Zhao stressed that automated tools are lowering the barrier for complex breaches.",
   "시각(UTC)": "11-03 14:22"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "26 (Fear)",
  "최근 7일": [
   26,
   37,
   34,
   30,
   30,
   51,
   51
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.01,
   "Bybit (Futures)": 0.01,
   "Gate (Futures)": 0.01,
   "MEXC (Futures)": 0.01,
   "WEEX (Futures)": 0.0001,
   "Tapbit (Futures)": 0.01
  },
  "미결제약정 합계 USD(상위)": 29638515925
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 63.16,
  "CoinGecko 인기 검색 코인": [
   "SNOWMOON",
   "DACITYCOIN",
   "SP",
   "PEARL",
   "KNTQ",
   "XMR",
   "HYPE",
   "CC",
   "NEAR",
   "PENGU",
   "PONS",
   "BTC",
   "LIT",
   "SOL",
   "ETH"
  ],
  "BTC가 인기 검색에 있음": true
 }
}
```

## ETH

**수집 실패**
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-02",
  "종가": 2253.29,
  "등락률(%)": {
   "1일": -0.97,
   "7일": -3.07,
   "30일": -16.15,
   "90일": 20.51
  },
  "이동평균": {
   "MA20": 2360.7135,
   "MA60": 2508.155833,
   "MA120": 2265.417083
  },
  "종가와 이평선 거리(%)": {
   "MA20": -4.55,
   "MA60": -10.16,
   "MA120": -0.54
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 13
  },
  "RSI14": 33.0,
  "ATR14(%)": 3.55,
  "거래량(20일 평균 대비 배수)": 1.05,
  "30일 최고가": 2739.5,
  "30일 최저가": 2174.08,
  "최근 10일 종가": [
   2358.82,
   2329.87,
   2324.55,
   2350.36,
   2359.68,
   2253.13,
   2245.54,
   2255.66,
   2275.31,
   2253.29
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-03",
  "등락률(%)": {
   "1일": 1.42,
   "7일": 0.56,
   "30일": -2.94,
   "90일": -3.96
  },
  "종가와 이평선 거리(%)": {
   "MA20": 1.38,
   "MA60": -0.04,
   "MA120": -2.49
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 60
  },
  "RSI14": 57.7
 }
}
```

### DIANA 자료 · 기본적 분석 (펀더멘털)

```json
{
 "이름": "Ethereum",
 "분류": [
  "Smart Contract Platform",
  "Layer 1 (L1)",
  "Ethereum Ecosystem",
  "FTX Holdings",
  "Multicoin Capital Portfolio"
 ],
 "시가총액 순위": 2,
 "시가총액(USD)": 279438463768,
 "완전희석가치 FDV(USD)": 279438463768,
 "24시간 거래대금(USD)": 8334738477,
 "유통량": 122186161.86556138,
 "총발행량": 122186161.86556138,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 4946.05,
 "역대 최고가 대비(%)": -53.75672,
 "가격 변화(%)": {
  "7d": -2.30999,
  "30d": -15.3059,
  "1y": -37.04581
 },
 "소개": "Ethereum is a global, open-source platform for decentralized applications. In other words, it is a decentralized blockchain platform that enables developers to build and deploy smart contracts and applications without central authority control. Unlike Bitcoin, which primarily functions as digital currency, Ethereum operates as a programmable global computer where developers can create any type of ",
 "체인 TVL (DefiLlama)": {
  "체인": "Ethereum",
  "TVL(USD)": 44115156590
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "ETH 관련 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Binance's $6.3 billion hack began with a fake job interview, and a campaign 'built over many months'",
   "요약": "North Korea-linked attackers spent months compromising Binance employees and internal systems before exploiting its hot-wallet signing infrastructure through Ethereum's EIP-7702 mechanism.",
   "시각(UTC)": "11-03 14:53"
  },
  {
   "출처": "CoinDesk",
   "제목": "ETHGas wants to bring Wall Street to public Ethereum by selling advance block reservations",
   "요약": "But there’s a catch: validators that fail to deliver on their commitments currently face no financial compensation requirement under the service.",
   "시각(UTC)": "11-03 12:01"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Wall Street killed Bitcoin’s wild rallies: 10x’s Markus Thielen",
   "요약": "Markus Thielen sees Bitcoin reaching $90,000 by year-end, questions institutional ETF demand and says Ethereum must do more for holders.",
   "시각(UTC)": "11-03 16:47"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Moscow Exchange to launch Bitcoin, Ether and USDT trading in December",
   "요약": "Moscow Exchange plans to launch crypto trading on Dec. 1 under Russia’s new law, with annual purchase limits for non-qualified investors.",
   "시각(UTC)": "11-03 13:15"
  },
  {
   "출처": "Decrypt",
   "제목": "Ethereum Privacy Network Aztec Rolls Out Major Security and Speed Upgrade",
   "요약": "The “Tierra” upgrade resolves a critical bug from the prior version, adds formal verification, and an AI-powered testing harness.",
   "시각(UTC)": "11-03 14:01"
  },
  {
   "출처": "Decrypt",
   "제목": "Morning Minute: Tom Lee Calls the Binance Hack Bullish for Ethereum",
   "요약": "Meanwhile, both the BTC ETFs and ETH ETFs bleed outflows in the Binance hack aftermath, dragging down prices.",
   "시각(UTC)": "11-03 13:11"
  },
  {
   "출처": "Decrypt",
   "제목": "Bitmine Buys More Ethereum as Tom Lee Calls the Binance Hack Bullish",
   "요약": "The chairman laid out six reasons the market’s “muted” 4% ETH drop after the record Binance theft shows crypto is “increasingly resilient,” as the firm’s stash neared its 5% supply goal.",
   "시각(UTC)": "11-02 16:23"
  }
 ],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Justin Sun seeks sanctions against Trump-linked World Liberty Financial over UAE ties",
   "요약": "The Tron founder says World Liberty failed to disclose its UAE ties until months into his lawsuit over $45 million in WLFI tokens.",
   "시각(UTC)": "11-03 16:55"
  },
  {
   "출처": "CoinDesk",
   "제목": "South Korea's president says country needs a ‘cybersecurity czar’ following $6.3 billion Binance hack",
   "요약": "Lee Jae Myung said he wants a government-wide agency to tackle cyberattacks as AI raises security concerns across financial institutions and critical infrastructure.",
   "시각(UTC)": "11-03 16:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Amazon, Tesla and SpaceX join OKX–ICE tokenized stock objections as deadline looms",
   "요약": "Objections have reached 56 companies, with nearly 80% of the venture’s initial stock selection opting out.",
   "시각(UTC)": "11-03 16:17"
  },
  {
   "출처": "CoinDesk",
   "제목": "Stablecoin governance group behind OUSD sets out management fee, offers equity earning pool",
   "요약": "Governance group Open Standard will charge a 0.1 basis point management fee on payment volume, capped at at $0.01 per payment.",
   "시각(UTC)": "11-03 16:12"
  },
  {
   "출처": "CoinDesk",
   "제목": "CFTC clears perpetual futures on stocks, bringing crypto trading model to Wall Street",
   "요약": "CFTC Chair Michael Selig said the move gives U.S. traders a regulated alternative to “offshore, and often unregulated, venues.”",
   "시각(UTC)": "11-03 15:02"
  },
  {
   "출처": "CoinDesk",
   "제목": "South Korea asks its biggest banks how a major crypto hack would hit them",
   "요약": "In its first such survey, the BOK also asked about a crypto price crash, losses at another firm, and each firm’s crypto teams, budgets and investments.",
   "시각(UTC)": "11-03 14:42"
  },
  {
   "출처": "CoinDesk",
   "제목": "CZ warns of more AI-driven hacks following Binance’s historic $6.3 billion heist",
   "요약": "While investigators found no evidence that AI agents laundered the stolen Binance funds, Zhao stressed that automated tools are lowering the barrier for complex breaches.",
   "시각(UTC)": "11-03 14:22"
  },
  {
   "출처": "CoinDesk",
   "제목": "LO:TECH raises $12 million to expand crypto trading into U.S. and Asia",
   "요약": "LO:TECH is betting on round-the-clock tokenized stock trading but didn’t say if it trades them now; a WFE study found stock exchanges still set prices.",
   "시각(UTC)": "11-03 14:00"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "26 (Fear)",
  "최근 7일": [
   26,
   37,
   34,
   30,
   30,
   51,
   51
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.01,
   "WEEX (Futures)": 0.0001,
   "MEXC (Futures)": 0.01,
   "CoinW (Futures)": 0.01,
   "Hyperliquid (Futures)": 0.0013
  },
  "미결제약정 합계 USD(상위)": 18513395794
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 95.65,
  "CoinGecko 인기 검색 코인": [
   "SNOWMOON",
   "DACITYCOIN",
   "SP",
   "PEARL",
   "KNTQ",
   "XMR",
   "HYPE",
   "CC",
   "NEAR",
   "PENGU",
   "PONS",
   "BTC",
   "LIT",
   "SOL",
   "ETH"
  ],
  "ETH가 인기 검색에 있음": true
 }
}
```

## BEAMX

**수집 실패**
- DIANA: ValueError: CoinGecko에서 BEAMX을 찾지 못했습니다
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15
- VIBE/군중 심리(CoinGecko): ValueError: CoinGecko에서 BEAMX을 찾지 못했습니다

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-02",
  "종가": 0.00449,
  "등락률(%)": {
   "1일": -18.94,
   "7일": 33.35,
   "30일": 110.11,
   "90일": 215.53
  },
  "이동평균": {
   "MA20": 0.003499,
   "MA60": 0.002517,
   "MA120": 0.002003
  },
  "종가와 이평선 거리(%)": {
   "MA20": 28.34,
   "MA60": 78.36,
   "MA120": 124.18
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 59
  },
  "RSI14": 63.2,
  "ATR14(%)": 14.32,
  "거래량(20일 평균 대비 배수)": 1.25,
  "30일 최고가": 0.006377,
  "30일 최저가": 0.002127,
  "최근 10일 종가": [
   0.003226,
   0.002987,
   0.003367,
   0.003332,
   0.003422,
   0.003338,
   0.004652,
   0.0052,
   0.005539,
   0.00449
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-03",
  "등락률(%)": {
   "1일": 1.87,
   "7일": -15.86,
   "30일": 20.75,
   "90일": 39.93
  },
  "종가와 이평선 거리(%)": {
   "MA20": -15.2,
   "MA60": 3.84,
   "MA120": 17.91
  },
  "MA20>MA60": true,
  "최근 교차": null,
  "RSI14": 42.7
 }
}
```

### DIANA 자료 · 기본적 분석 (펀더멘털)

```json
{
 "오류": "ValueError: CoinGecko에서 BEAMX을 찾지 못했습니다"
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "BEAMX 관련 기사": [],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Justin Sun seeks sanctions against Trump-linked World Liberty Financial over UAE ties",
   "요약": "The Tron founder says World Liberty failed to disclose its UAE ties until months into his lawsuit over $45 million in WLFI tokens.",
   "시각(UTC)": "11-03 16:55"
  },
  {
   "출처": "CoinDesk",
   "제목": "South Korea's president says country needs a ‘cybersecurity czar’ following $6.3 billion Binance hack",
   "요약": "Lee Jae Myung said he wants a government-wide agency to tackle cyberattacks as AI raises security concerns across financial institutions and critical infrastructure.",
   "시각(UTC)": "11-03 16:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Amazon, Tesla and SpaceX join OKX–ICE tokenized stock objections as deadline looms",
   "요약": "Objections have reached 56 companies, with nearly 80% of the venture’s initial stock selection opting out.",
   "시각(UTC)": "11-03 16:17"
  },
  {
   "출처": "CoinDesk",
   "제목": "Stablecoin governance group behind OUSD sets out management fee, offers equity earning pool",
   "요약": "Governance group Open Standard will charge a 0.1 basis point management fee on payment volume, capped at at $0.01 per payment.",
   "시각(UTC)": "11-03 16:12"
  },
  {
   "출처": "CoinDesk",
   "제목": "CFTC clears perpetual futures on stocks, bringing crypto trading model to Wall Street",
   "요약": "CFTC Chair Michael Selig said the move gives U.S. traders a regulated alternative to “offshore, and often unregulated, venues.”",
   "시각(UTC)": "11-03 15:02"
  },
  {
   "출처": "CoinDesk",
   "제목": "Binance's $6.3 billion hack began with a fake job interview, and a campaign 'built over many months'",
   "요약": "North Korea-linked attackers spent months compromising Binance employees and internal systems before exploiting its hot-wallet signing infrastructure through Ethereum's EIP-7702 mechanism.",
   "시각(UTC)": "11-03 14:53"
  },
  {
   "출처": "CoinDesk",
   "제목": "South Korea asks its biggest banks how a major crypto hack would hit them",
   "요약": "In its first such survey, the BOK also asked about a crypto price crash, losses at another firm, and each firm’s crypto teams, budgets and investments.",
   "시각(UTC)": "11-03 14:42"
  },
  {
   "출처": "CoinDesk",
   "제목": "CZ warns of more AI-driven hacks following Binance’s historic $6.3 billion heist",
   "요약": "While investigators found no evidence that AI agents laundered the stolen Binance funds, Zhao stressed that automated tools are lowering the barrier for complex breaches.",
   "시각(UTC)": "11-03 14:22"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "26 (Fear)",
  "최근 7일": [
   26,
   37,
   34,
   30,
   30,
   51,
   51
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.005,
   "WEEX (Futures)": 0.0001,
   "XT.COM (Derivatives)": 0.005,
   "Toobit Futures": 0.005,
   "Bitunix Futures": 0.005,
   "MEXC (Futures)": 0.005
  },
  "미결제약정 합계 USD(상위)": 43271297
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "오류": "ValueError: CoinGecko에서 BEAMX을 찾지 못했습니다"
 }
}
```

## PEPE

**수집 실패**
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-02",
  "종가": 5e-06,
  "등락률(%)": {
   "1일": -2.05,
   "7일": 10.65,
   "30일": 10.9,
   "90일": 65.97
  },
  "이동평균": {
   "MA20": 4e-06,
   "MA60": 4e-06,
   "MA120": 4e-06
  },
  "종가와 이평선 거리(%)": {
   "MA20": 7.04,
   "MA60": 15.25,
   "MA120": 33.53
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 97
  },
  "RSI14": 56.2,
  "ATR14(%)": 11.12,
  "거래량(20일 평균 대비 배수)": 0.79,
  "30일 최고가": 6e-06,
  "30일 최저가": 4e-06,
  "최근 10일 종가": [
   5e-06,
   4e-06,
   4e-06,
   5e-06,
   5e-06,
   5e-06,
   5e-06,
   5e-06,
   5e-06,
   5e-06
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-03",
  "등락률(%)": {
   "1일": 2.09,
   "7일": 0.82,
   "30일": -11.09,
   "90일": 18.69
  },
  "종가와 이평선 거리(%)": {
   "MA20": 0.31,
   "MA60": 2.83,
   "MA120": 8.58
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 82
  },
  "RSI14": 52.0
 }
}
```

### DIANA 자료 · 기본적 분석 (펀더멘털)

```json
{
 "이름": "Pepe",
 "분류": [
  "BNB Chain Ecosystem",
  "Avalanche Ecosystem",
  "Meme",
  "Arbitrum Ecosystem",
  "Ethereum Ecosystem"
 ],
 "시가총액 순위": 45,
 "시가총액(USD)": 2050843466,
 "완전희석가치 FDV(USD)": 2050843466,
 "24시간 거래대금(USD)": 390933543,
 "유통량": 420690000000000.0,
 "총발행량": 420690000000000.0,
 "최대발행량": 420690000000000.0,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 2.803e-05,
 "역대 최고가 대비(%)": -82.60783,
 "가격 변화(%)": {
  "7d": 9.28259,
  "30d": 13.21811,
  "1y": -16.35951
 },
 "소개": "What is the project about?\nPepe is a community based meme token surround the iconic meme Pepe the frog. Pepe aims to leverage the power of such an iconic meme to become the most memeable memecoin in existence. \n\nWhat makes your project unique?\nPepe is here to make memecoins great again. Ushering in a new paradigm for memecoins, Pepe represents the memecoin in it's purest simplicity. With zero taxe"
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "PEPE 관련 기사": [],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Justin Sun seeks sanctions against Trump-linked World Liberty Financial over UAE ties",
   "요약": "The Tron founder says World Liberty failed to disclose its UAE ties until months into his lawsuit over $45 million in WLFI tokens.",
   "시각(UTC)": "11-03 16:55"
  },
  {
   "출처": "CoinDesk",
   "제목": "South Korea's president says country needs a ‘cybersecurity czar’ following $6.3 billion Binance hack",
   "요약": "Lee Jae Myung said he wants a government-wide agency to tackle cyberattacks as AI raises security concerns across financial institutions and critical infrastructure.",
   "시각(UTC)": "11-03 16:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Amazon, Tesla and SpaceX join OKX–ICE tokenized stock objections as deadline looms",
   "요약": "Objections have reached 56 companies, with nearly 80% of the venture’s initial stock selection opting out.",
   "시각(UTC)": "11-03 16:17"
  },
  {
   "출처": "CoinDesk",
   "제목": "Stablecoin governance group behind OUSD sets out management fee, offers equity earning pool",
   "요약": "Governance group Open Standard will charge a 0.1 basis point management fee on payment volume, capped at at $0.01 per payment.",
   "시각(UTC)": "11-03 16:12"
  },
  {
   "출처": "CoinDesk",
   "제목": "CFTC clears perpetual futures on stocks, bringing crypto trading model to Wall Street",
   "요약": "CFTC Chair Michael Selig said the move gives U.S. traders a regulated alternative to “offshore, and often unregulated, venues.”",
   "시각(UTC)": "11-03 15:02"
  },
  {
   "출처": "CoinDesk",
   "제목": "Binance's $6.3 billion hack began with a fake job interview, and a campaign 'built over many months'",
   "요약": "North Korea-linked attackers spent months compromising Binance employees and internal systems before exploiting its hot-wallet signing infrastructure through Ethereum's EIP-7702 mechanism.",
   "시각(UTC)": "11-03 14:53"
  },
  {
   "출처": "CoinDesk",
   "제목": "South Korea asks its biggest banks how a major crypto hack would hit them",
   "요약": "In its first such survey, the BOK also asked about a crypto price crash, losses at another firm, and each firm’s crypto teams, budgets and investments.",
   "시각(UTC)": "11-03 14:42"
  },
  {
   "출처": "CoinDesk",
   "제목": "CZ warns of more AI-driven hacks following Binance’s historic $6.3 billion heist",
   "요약": "While investigators found no evidence that AI agents laundered the stolen Binance funds, Zhao stressed that automated tools are lowering the barrier for complex breaches.",
   "시각(UTC)": "11-03 14:22"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "26 (Fear)",
  "최근 7일": [
   26,
   37,
   34,
   30,
   30,
   51,
   51
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "MEXC (Futures)": 0.01,
   "Gate (Futures)": 0.01,
   "OKX (Futures)": 0.01,
   "Bitget Futures": 0.01,
   "WhiteBIT Futures": 0.01,
   "KCEX (Futures)": 0.01
  },
  "미결제약정 합계 USD(상위)": 260957808
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 85.71,
  "CoinGecko 인기 검색 코인": [
   "SNOWMOON",
   "DACITYCOIN",
   "SP",
   "PEARL",
   "KNTQ",
   "XMR",
   "HYPE",
   "CC",
   "NEAR",
   "PENGU",
   "PONS",
   "BTC",
   "LIT",
   "SOL",
   "ETH"
  ],
  "PEPE가 인기 검색에 있음": false
 }
}
```

## GOOGLB

**수집 실패**
- VIBE/선물 포지션: ValueError: GOOGLB 무기한 선물 자료 없음
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-02",
  "종가": 280.54,
  "등락률(%)": {
   "1일": -1.1,
   "7일": -11.96,
   "30일": -18.4,
   "90일": -26.08
  },
  "이동평균": {
   "MA20": 318.4755,
   "MA60": 336.018167,
   "MA120": null
  },
  "종가와 이평선 거리(%)": {
   "MA20": -11.91,
   "MA60": -16.51,
   "MA120": null
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 8
  },
  "RSI14": 20.0,
  "ATR14(%)": 3.4,
  "거래량(20일 평균 대비 배수)": 2.22,
  "30일 최고가": 359.6,
  "30일 최저가": 277.39,
  "최근 10일 종가": [
   321.33,
   321.37,
   318.64,
   323.81,
   293.03,
   281.17,
   281.88,
   283.1,
   283.65,
   280.54
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-03",
  "등락률(%)": {
   "1일": -0.03,
   "7일": -1.19,
   "30일": -2.6,
   "90일": -19.25
  },
  "종가와 이평선 거리(%)": {
   "MA20": -1.01,
   "MA60": -6.58,
   "MA120": -12.19
  },
  "MA20>MA60": false,
  "최근 교차": null,
  "RSI14": 28.9
 }
}
```

### DIANA 자료 · 기본적 분석 (펀더멘털)

```json
{
 "이름": "Alphabet (bStocks Tokenized Stock)",
 "분류": [
  "Tokenized Assets",
  "BNB Chain Ecosystem",
  "Tokenized Stocks",
  "Real World Assets (RWA)",
  "bStocks Ecosystem"
 ],
 "시가총액 순위": 230,
 "시가총액(USD)": 123678543,
 "완전희석가치 FDV(USD)": 123787809,
 "24시간 거래대금(USD)": 16271175,
 "유통량": 442788.1698068,
 "총발행량": 443179.36058215,
 "최대발행량": null,
 "유통 비율(%)": 99.9,
 "역대 최고가(USD)": 383.58,
 "역대 최고가 대비(%)": -27.19037,
 "가격 변화(%)": {
  "7d": -13.18976,
  "30d": -18.89706,
  "1y": null
 },
 "소개": ""
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "GOOGLB 관련 기사": [],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Justin Sun seeks sanctions against Trump-linked World Liberty Financial over UAE ties",
   "요약": "The Tron founder says World Liberty failed to disclose its UAE ties until months into his lawsuit over $45 million in WLFI tokens.",
   "시각(UTC)": "11-03 16:55"
  },
  {
   "출처": "CoinDesk",
   "제목": "South Korea's president says country needs a ‘cybersecurity czar’ following $6.3 billion Binance hack",
   "요약": "Lee Jae Myung said he wants a government-wide agency to tackle cyberattacks as AI raises security concerns across financial institutions and critical infrastructure.",
   "시각(UTC)": "11-03 16:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Amazon, Tesla and SpaceX join OKX–ICE tokenized stock objections as deadline looms",
   "요약": "Objections have reached 56 companies, with nearly 80% of the venture’s initial stock selection opting out.",
   "시각(UTC)": "11-03 16:17"
  },
  {
   "출처": "CoinDesk",
   "제목": "Stablecoin governance group behind OUSD sets out management fee, offers equity earning pool",
   "요약": "Governance group Open Standard will charge a 0.1 basis point management fee on payment volume, capped at at $0.01 per payment.",
   "시각(UTC)": "11-03 16:12"
  },
  {
   "출처": "CoinDesk",
   "제목": "CFTC clears perpetual futures on stocks, bringing crypto trading model to Wall Street",
   "요약": "CFTC Chair Michael Selig said the move gives U.S. traders a regulated alternative to “offshore, and often unregulated, venues.”",
   "시각(UTC)": "11-03 15:02"
  },
  {
   "출처": "CoinDesk",
   "제목": "Binance's $6.3 billion hack began with a fake job interview, and a campaign 'built over many months'",
   "요약": "North Korea-linked attackers spent months compromising Binance employees and internal systems before exploiting its hot-wallet signing infrastructure through Ethereum's EIP-7702 mechanism.",
   "시각(UTC)": "11-03 14:53"
  },
  {
   "출처": "CoinDesk",
   "제목": "South Korea asks its biggest banks how a major crypto hack would hit them",
   "요약": "In its first such survey, the BOK also asked about a crypto price crash, losses at another firm, and each firm’s crypto teams, budgets and investments.",
   "시각(UTC)": "11-03 14:42"
  },
  {
   "출처": "CoinDesk",
   "제목": "CZ warns of more AI-driven hacks following Binance’s historic $6.3 billion heist",
   "요약": "While investigators found no evidence that AI agents laundered the stolen Binance funds, Zhao stressed that automated tools are lowering the barrier for complex breaches.",
   "시각(UTC)": "11-03 14:22"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "26 (Fear)",
  "최근 7일": [
   26,
   37,
   34,
   30,
   30,
   51,
   51
  ]
 },
 "선물 포지션": {
  "오류": "ValueError: GOOGLB 무기한 선물 자료 없음"
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": null,
  "CoinGecko 인기 검색 코인": [
   "SNOWMOON",
   "DACITYCOIN",
   "SP",
   "PEARL",
   "KNTQ",
   "XMR",
   "HYPE",
   "CC",
   "NEAR",
   "PENGU",
   "PONS",
   "BTC",
   "LIT",
   "SOL",
   "ETH"
  ],
  "GOOGLB가 인기 검색에 있음": false
 }
}
```
