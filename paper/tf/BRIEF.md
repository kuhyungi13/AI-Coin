# TF팀 회의 자료 (2026-11-06 12:29 KST)

GitHub Actions가 무료 공개 API로 모은 자료입니다. 회의 진행 방법은 `aicoin/tf_team/PLAYBOOK.md`.
자료에 없는 숫자는 쓰지 않습니다. 실패한 자료는 아래 '수집 실패'에 있습니다.

분석 대상: BTC, ETH, PEPE, INJ, INTCB

**지금까지 승률** ACE 40.9% (9/22), 채점 대기 0개 · 자세히는 `paper/tf/SCOREBOARD.md`, 교훈은 `aicoin/tf_team/LESSONS.md`

**TRAINER 모의 계좌** 총자산 10,007.95 USDT (+0.08%), 보유 PEPE · 자세히는 `paper/tf/trainer/TRAINER.md`

**전체 스캔 후보** (`paper/tf/SCAN.md`) 상승 추세: PEPE, INJ · 과매도 반등: INTCB

## BTC

**수집 실패**
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-05",
  "종가": 76088.01,
  "등락률(%)": {
   "1일": -5.49,
   "7일": -2.44,
   "30일": -11.06,
   "90일": 17.2
  },
  "이동평균": {
   "MA20": 80043.8585,
   "MA60": 81281.6365,
   "MA120": 74906.37375
  },
  "종가와 이평선 거리(%)": {
   "MA20": -4.94,
   "MA60": -6.39,
   "MA120": 1.58
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 6
  },
  "RSI14": 38.5,
  "ATR14(%)": 3.06,
  "거래량(20일 평균 대비 배수)": 1.89,
  "30일 최고가": 85598.22,
  "30일 최저가": 75208.42,
  "최근 10일 종가": [
   80909.77,
   81343.5,
   77991.89,
   77368.77,
   77582.02,
   78354.0,
   76816.0,
   77453.86,
   80504.01,
   76088.01
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-05",
  "등락률(%)": {
   "1일": -0.37,
   "7일": -4.89,
   "30일": -1.93,
   "90일": -9.52
  },
  "종가와 이평선 거리(%)": {
   "MA20": -2.53,
   "MA60": -3.31,
   "MA120": -5.07
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 73
  },
  "RSI14": 37.4
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
 "시가총액(USD)": 1526028634895,
 "완전희석가치 FDV(USD)": 1526028634895,
 "24시간 거래대금(USD)": 44015269455,
 "유통량": 20105365.0,
 "총발행량": 20105365.0,
 "최대발행량": 21000000.0,
 "유통 비율(%)": 95.7,
 "역대 최고가(USD)": 126080,
 "역대 최고가 대비(%)": -39.80741,
 "가격 변화(%)": {
  "7d": -1.73381,
  "30d": -9.48958,
  "1y": -26.57401
 },
 "소개": "Bitcoin is the world's first decentralized cryptocurrency, created in 2009 by the pseudonymous Satoshi Nakamoto. It enables peer-to-peer electronic cash transactions without intermediaries like banks or governments, operating on a blockchain secured by Proof of Work mining and the SHA-256 cryptographic algorithm. \n\nWith a fixed supply cap of 21 million coins and programmatic halvings every four ye",
 "체인 TVL (DefiLlama)": {
  "체인": "Bitcoin",
  "TVL(USD)": 4047799558
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "BTC 관련 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin developer proposes ‘landmines’ to make quantum thieves lose their own BTC",
   "요약": "Anyone trying to move vulnerable bitcoin would have to put up matching collateral, giving prepared owners a chance to take both.",
   "시각(UTC)": "11-06 01:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin tumbles to $76,000 as collapsing AI trade drags stocks sharply lower",
   "요약": "The post-election rally quickly reversed as AI stocks plunged, but cryptocurrencies held up relatively better despite a $1 billion liquidation wave.",
   "시각(UTC)": "11-05 18:48"
  },
  {
   "출처": "CoinDesk",
   "제목": "Standard Chartered and SBI back crypto insurer Soter as funding reaches $23.5 million",
   "요약": "Soter also received backing of 500 BTC and 2000 ETH, worth another $43 million at current prices.",
   "시각(UTC)": "11-05 16:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Google could take stake in bitcoin miner TeraWulf’s $19 billion AI project if Anthropic defaults",
   "요약": "A $19 billion data-center agreement includes an unusual provision allowing Google to acquire part of the project if Anthropic fails to pay its rent.",
   "시각(UTC)": "11-05 13:29"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin is resilient, but leverage is missing and demand still tepid",
   "요약": "Your day-ahead look for Nov. 5, 2026",
   "시각(UTC)": "11-05 12:27"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin miners are oversold following 35% October rout, VanEck says",
   "요약": "Investors dumped AI infrastructure providers across the board in October, treating companies in very different sectors as one monolithic trade.",
   "시각(UTC)": "11-05 11:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Trump-linked American Bitcoin swings to $126 million profit but misses revenue estimates",
   "요약": "Revenue fell to $63.4 million in the third quarter and missed analysts’ forecasts as bitcoin production declined and higher summer electricity prices pushed mining costs up.",
   "시각(UTC)": "11-05 11:45"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin holds above $80,000 after Wednesday’s jump as injective rallies on staked ETF listing",
   "요약": "Bitcoin slipped 0.2% to around $80,250 since midnight UTC, holding above $80,000 after Wednesday’s jump, as spot ETFs ended a three-day outflow streak.",
   "시각(UTC)": "11-05 11:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin drops more than 5% as stocks close out worst day since April 2025",
   "요약": "The continued blowup of the AI trade led markets lower, with Nvidia losing 9.3% and many other chip names down double-digit percentages.",
   "시각(UTC)": "11-05 10:57"
  },
  {
   "출처": "CoinDesk",
   "제목": "Mercado Bitcoin hack continued hours after exchange said attack was contained, report finds",
   "요약": "The same attacker took about $391,000, mostly from wallets Bitquery ties to BitMart, whose founder confirmed a Nov. 2 hack and suspects a link.",
   "시각(UTC)": "11-05 10:44"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin miner Riot could pay Anthropic 12% interest under $28 billion AI deal",
   "요약": "Riot has sold most of its bitcoin to fund its move into data centers. Its latest agreement gives Anthropic a way to finance part of the build and collect interest through rent deductions.",
   "시각(UTC)": "11-05 09:36"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin holds above $80,000 as Zcash jumps 12% in post-election crypto rebound",
   "요약": "Ether rose 8% as falling oil prices and a weaker dollar helped markets recover, even as traders weighed a tougher path for U.S. crypto legislation.",
   "시각(UTC)": "11-05 05:13"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Core Scientific to quit Bitcoin mining by year-end as AI business surges",
   "요약": "The former Bitcoin mining heavyweight plans to become a pure-play data center provider in 2027, with mining now accounting for just 7.5% of quarterly revenue.",
   "시각(UTC)": "11-06 00:19"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Here’s what happened in crypto today",
   "요약": "Need to know what happened in crypto today? Here is the latest news on daily trends and events impacting Bitcoin price, blockchain, DeFi, Web3 and crypto regulation.",
   "시각(UTC)": "11-05 23:03"
  },
  {
   "출처": "Cointelegraph",
   "제목": "American Bitcoin’s $126M profit masks mining pressure as rivals turn to AI",
   "요약": "The Eric Trump-backed miner reported $126 million in quarterly net income, largely driven by gains on its Bitcoin holdings, despite rising mining costs and shrinking margins.",
   "시각(UTC)": "11-05 22:43"
  }
 ],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Hyperliquid treasury firm seeking U.S. regulatory nod as a domestic futures platform",
   "요약": "The company said it's trying to establish a U.S. \"futures commission merchant\" with full compliance for activity with U.S. clients, though the timing is uncertain.",
   "시각(UTC)": "11-06 02:24"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. Justice Department assembles force to shield against foreign AI threats",
   "요약": "The new DOJ task force will aid the recently designated U.S. \"SI Force\" by warding off bad actors backed by other nations, criminal groups or corporate fraud.",
   "시각(UTC)": "11-05 18:59"
  },
  {
   "출처": "CoinDesk",
   "제목": "What is TraderTraitor, the hacking squad behind the $6.3 billion Binance heist?",
   "요약": "The hacking group has been behind some of the crypto industry's most recent high-profile thefts.",
   "시각(UTC)": "11-05 16:58"
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto for Advisors: Where investors stake crypto shapes how much of the reward they keep",
   "요약": "",
   "시각(UTC)": "11-05 16:13"
  },
  {
   "출처": "CoinDesk",
   "제목": "Gate CEO says crypto exchanges must prove they can survive a hack like Binance’s",
   "요약": "Lin Han says Gate holds enough assets in cold storage to cover customer balances even if its hot wallets are emptied. An independent audit is underway.",
   "시각(UTC)": "11-05 14:21"
  },
  {
   "출처": "CoinDesk",
   "제목": "Kraken parent Payward and its clients buy AAVE tokens in DeFi investment push",
   "요약": "The investment follows talks first reported by CoinDesk in June that included a proposed equity stake in Aave Group.",
   "시각(UTC)": "11-05 14:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "Binance cuts SignalPlus access after security warning, urges users to check accounts",
   "요약": "The exchange says its systems are unaffected but has removed trading connections to the third-party platform as a precaution.",
   "시각(UTC)": "11-05 12:55"
  },
  {
   "출처": "CoinDesk",
   "제목": "Ukraine’s central bank opposes crypto bill, citing monetary sovereignty concerns",
   "요약": "Ukraine’s central bank won’t back a crypto legalization bill in its current form and wants lawmakers to revise it before a final vote.",
   "시각(UTC)": "11-05 12:50"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "28 (Fear)",
  "최근 7일": [
   28,
   50,
   34,
   26,
   37,
   34,
   30
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.0062,
   "Bybit (Futures)": 0.0016,
   "MEXC (Futures)": 0.0062,
   "Gate (Futures)": -0.0023,
   "WEEX (Futures)": 0.0001,
   "Tapbit (Futures)": 0.0064
  },
  "미결제약정 합계 USD(상위)": 28781430677
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 60.71,
  "CoinGecko 인기 검색 코인": [
   "BTC",
   "HYPE",
   "NEAR",
   "PEARL",
   "ETH",
   "LIT",
   "PENGU",
   "ZEC",
   "SOL",
   "ZAMA",
   "INJ",
   "LINK",
   "STRK",
   "MON",
   "PUMP"
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
  "기준일": "2026-11-05",
  "종가": 2238.01,
  "등락률(%)": {
   "1일": -7.7,
   "7일": -0.67,
   "30일": -17.03,
   "90일": 16.92
  },
  "이동평균": {
   "MA20": 2343.222,
   "MA60": 2499.601167,
   "MA120": 2278.94075
  },
  "종가와 이평선 거리(%)": {
   "MA20": -4.49,
   "MA60": -10.47,
   "MA120": -1.8
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 16
  },
  "RSI14": 39.4,
  "ATR14(%)": 4.22,
  "거래량(20일 평균 대비 배수)": 1.61,
  "30일 최고가": 2699.8,
  "30일 최저가": 2174.08,
  "최근 10일 종가": [
   2350.36,
   2359.68,
   2253.13,
   2245.54,
   2255.66,
   2275.31,
   2253.29,
   2274.77,
   2424.61,
   2238.01
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-05",
  "등락률(%)": {
   "1일": -1.06,
   "7일": -7.0,
   "30일": -0.78,
   "90일": -9.53
  },
  "종가와 이평선 거리(%)": {
   "MA20": -3.33,
   "MA60": -2.72,
   "MA120": -4.69
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 5
  },
  "RSI14": 39.3
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
 "시가총액(USD)": 272796753239,
 "완전희석가치 FDV(USD)": 272796753239,
 "24시간 거래대금(USD)": 17404098342,
 "유통량": 122192071.85523713,
 "총발행량": 122192071.85523713,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 4946.05,
 "역대 최고가 대비(%)": -54.86595,
 "가격 변화(%)": {
  "7d": 1.21362,
  "30d": -14.54281,
  "1y": -34.8032
 },
 "소개": "Ethereum is a global, open-source platform for decentralized applications. In other words, it is a decentralized blockchain platform that enables developers to build and deploy smart contracts and applications without central authority control. Unlike Bitcoin, which primarily functions as digital currency, Ethereum operates as a programmable global computer where developers can create any type of ",
 "체인 TVL (DefiLlama)": {
  "체인": "Ethereum",
  "TVL(USD)": 43376930075
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "ETH 관련 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Standard Chartered and SBI back crypto insurer Soter as funding reaches $23.5 million",
   "요약": "Soter also received backing of 500 BTC and 2000 ETH, worth another $43 million at current prices.",
   "시각(UTC)": "11-05 16:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin holds above $80,000 as Zcash jumps 12% in post-election crypto rebound",
   "요약": "Ether rose 8% as falling oil prices and a weaker dollar helped markets recover, even as traders weighed a tougher path for U.S. crypto legislation.",
   "시각(UTC)": "11-05 05:13"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Europe’s largest asset manager Amundi tokenizes equity index fund on Ethereum",
   "요약": "The new share class offers blockchain-based exposure to an index tracking 600 companies across European markets.",
   "시각(UTC)": "11-05 18:09"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin, Ether ETFs draw $128M as crypto rebounds after midterms",
   "요약": "Fidelity led Bitcoin ETF inflows, while BlackRock’s IBIT shed another $201 million, extending its outflow streak to four trading sessions.",
   "시각(UTC)": "11-05 08:22"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Trump-linked tokens lead crypto losses after Democrats sweep in the US midterms",
   "요약": "The official Trump and World Liberty Financial tokens were the two biggest losers among the top 100 cryptocurrencies on Wednesday, even as Bitcoin and Ether rallied.",
   "시각(UTC)": "11-04 19:15"
  }
 ],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Hyperliquid treasury firm seeking U.S. regulatory nod as a domestic futures platform",
   "요약": "The company said it's trying to establish a U.S. \"futures commission merchant\" with full compliance for activity with U.S. clients, though the timing is uncertain.",
   "시각(UTC)": "11-06 02:24"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin developer proposes ‘landmines’ to make quantum thieves lose their own BTC",
   "요약": "Anyone trying to move vulnerable bitcoin would have to put up matching collateral, giving prepared owners a chance to take both.",
   "시각(UTC)": "11-06 01:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. Justice Department assembles force to shield against foreign AI threats",
   "요약": "The new DOJ task force will aid the recently designated U.S. \"SI Force\" by warding off bad actors backed by other nations, criminal groups or corporate fraud.",
   "시각(UTC)": "11-05 18:59"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin tumbles to $76,000 as collapsing AI trade drags stocks sharply lower",
   "요약": "The post-election rally quickly reversed as AI stocks plunged, but cryptocurrencies held up relatively better despite a $1 billion liquidation wave.",
   "시각(UTC)": "11-05 18:48"
  },
  {
   "출처": "CoinDesk",
   "제목": "What is TraderTraitor, the hacking squad behind the $6.3 billion Binance heist?",
   "요약": "The hacking group has been behind some of the crypto industry's most recent high-profile thefts.",
   "시각(UTC)": "11-05 16:58"
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto for Advisors: Where investors stake crypto shapes how much of the reward they keep",
   "요약": "",
   "시각(UTC)": "11-05 16:13"
  },
  {
   "출처": "CoinDesk",
   "제목": "Gate CEO says crypto exchanges must prove they can survive a hack like Binance’s",
   "요약": "Lin Han says Gate holds enough assets in cold storage to cover customer balances even if its hot wallets are emptied. An independent audit is underway.",
   "시각(UTC)": "11-05 14:21"
  },
  {
   "출처": "CoinDesk",
   "제목": "Kraken parent Payward and its clients buy AAVE tokens in DeFi investment push",
   "요약": "The investment follows talks first reported by CoinDesk in June that included a proposed equity stake in Aave Group.",
   "시각(UTC)": "11-05 14:00"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "28 (Fear)",
  "최근 7일": [
   28,
   50,
   34,
   26,
   37,
   34,
   30
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.006,
   "WEEX (Futures)": 0.0001,
   "CoinW (Futures)": 0.006,
   "MEXC (Futures)": 0.0054,
   "Hyperliquid (Futures)": 0.0013
  },
  "미결제약정 합계 USD(상위)": 18671065110
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 77.55,
  "CoinGecko 인기 검색 코인": [
   "BTC",
   "HYPE",
   "NEAR",
   "PEARL",
   "ETH",
   "LIT",
   "PENGU",
   "ZEC",
   "SOL",
   "ZAMA",
   "INJ",
   "LINK",
   "STRK",
   "MON",
   "PUMP"
  ],
  "ETH가 인기 검색에 있음": true
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
  "기준일": "2026-11-05",
  "종가": 5e-06,
  "등락률(%)": {
   "1일": -3.42,
   "7일": 5.26,
   "30일": 12.15,
   "90일": 70.82
  },
  "이동평균": {
   "MA20": 5e-06,
   "MA60": 4e-06,
   "MA120": 4e-06
  },
  "종가와 이평선 거리(%)": {
   "MA20": 4.63,
   "MA60": 13.97,
   "MA120": 32.04
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 100
  },
  "RSI14": 55.4,
  "ATR14(%)": 11.4,
  "거래량(20일 평균 대비 배수)": 0.95,
  "30일 최고가": 6e-06,
  "30일 최저가": 4e-06,
  "최근 10일 종가": [
   5e-06,
   5e-06,
   5e-06,
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
  "기준일": "2026-11-05",
  "등락률(%)": {
   "1일": -0.62,
   "7일": -3.03,
   "30일": -4.0,
   "90일": 3.67
  },
  "종가와 이평선 거리(%)": {
   "MA20": -1.52,
   "MA60": -1.63,
   "MA120": 4.23
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 1
  },
  "RSI14": 46.2
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
 "시가총액(USD)": 2038421007,
 "완전희석가치 FDV(USD)": 2038421007,
 "24시간 거래대금(USD)": 437861595,
 "유통량": 420690000000000.0,
 "총발행량": 420690000000000.0,
 "최대발행량": 420690000000000.0,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 2.803e-05,
 "역대 최고가 대비(%)": -82.70946,
 "가격 변화(%)": {
  "7d": 2.42101,
  "30d": 17.8525,
  "1y": -15.54825
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
   "제목": "Hyperliquid treasury firm seeking U.S. regulatory nod as a domestic futures platform",
   "요약": "The company said it's trying to establish a U.S. \"futures commission merchant\" with full compliance for activity with U.S. clients, though the timing is uncertain.",
   "시각(UTC)": "11-06 02:24"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin developer proposes ‘landmines’ to make quantum thieves lose their own BTC",
   "요약": "Anyone trying to move vulnerable bitcoin would have to put up matching collateral, giving prepared owners a chance to take both.",
   "시각(UTC)": "11-06 01:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. Justice Department assembles force to shield against foreign AI threats",
   "요약": "The new DOJ task force will aid the recently designated U.S. \"SI Force\" by warding off bad actors backed by other nations, criminal groups or corporate fraud.",
   "시각(UTC)": "11-05 18:59"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin tumbles to $76,000 as collapsing AI trade drags stocks sharply lower",
   "요약": "The post-election rally quickly reversed as AI stocks plunged, but cryptocurrencies held up relatively better despite a $1 billion liquidation wave.",
   "시각(UTC)": "11-05 18:48"
  },
  {
   "출처": "CoinDesk",
   "제목": "What is TraderTraitor, the hacking squad behind the $6.3 billion Binance heist?",
   "요약": "The hacking group has been behind some of the crypto industry's most recent high-profile thefts.",
   "시각(UTC)": "11-05 16:58"
  },
  {
   "출처": "CoinDesk",
   "제목": "Standard Chartered and SBI back crypto insurer Soter as funding reaches $23.5 million",
   "요약": "Soter also received backing of 500 BTC and 2000 ETH, worth another $43 million at current prices.",
   "시각(UTC)": "11-05 16:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto for Advisors: Where investors stake crypto shapes how much of the reward they keep",
   "요약": "",
   "시각(UTC)": "11-05 16:13"
  },
  {
   "출처": "CoinDesk",
   "제목": "Gate CEO says crypto exchanges must prove they can survive a hack like Binance’s",
   "요약": "Lin Han says Gate holds enough assets in cold storage to cover customer balances even if its hot wallets are emptied. An independent audit is underway.",
   "시각(UTC)": "11-05 14:21"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "28 (Fear)",
  "최근 7일": [
   28,
   50,
   34,
   26,
   37,
   34,
   30
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "MEXC (Futures)": 0.01,
   "Gate (Futures)": 0.01,
   "Bitget Futures": 0.01,
   "OKX (Futures)": 0.01,
   "KCEX (Futures)": 0.01,
   "WhiteBIT Futures": 0.01
  },
  "미결제약정 합계 USD(상위)": 288253390
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 85.0,
  "CoinGecko 인기 검색 코인": [
   "BTC",
   "HYPE",
   "NEAR",
   "PEARL",
   "ETH",
   "LIT",
   "PENGU",
   "ZEC",
   "SOL",
   "ZAMA",
   "INJ",
   "LINK",
   "STRK",
   "MON",
   "PUMP"
  ],
  "PEPE가 인기 검색에 있음": false
 }
}
```

## INJ

**수집 실패**
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-05",
  "종가": 8.148,
  "등락률(%)": {
   "1일": 2.66,
   "7일": 11.05,
   "30일": 0.43,
   "90일": 80.55
  },
  "이동평균": {
   "MA20": 7.9101,
   "MA60": 7.4402,
   "MA120": 6.163392
  },
  "종가와 이평선 거리(%)": {
   "MA20": 3.01,
   "MA60": 9.51,
   "MA120": 32.2
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 64
  },
  "RSI14": 56.0,
  "ATR14(%)": 7.76,
  "거래량(20일 평균 대비 배수)": 1.61,
  "30일 최고가": 9.417,
  "30일 최저가": 6.417,
  "최근 10일 종가": [
   7.966,
   8.154,
   7.337,
   7.182,
   7.231,
   7.185,
   6.983,
   7.248,
   7.937,
   8.148
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-05",
  "등락률(%)": {
   "1일": -0.77,
   "7일": 3.98,
   "30일": 12.68,
   "90일": -5.48
  },
  "종가와 이평선 거리(%)": {
   "MA20": 7.37,
   "MA60": 8.06,
   "MA120": 3.29
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 0
  },
  "RSI14": 62.9
 }
}
```

### DIANA 자료 · 기본적 분석 (펀더멘털)

```json
{
 "이름": "Injective",
 "분류": [
  "Smart Contract Platform",
  "Decentralized Finance (DeFi)",
  "BNB Chain Ecosystem",
  "Cosmos Ecosystem",
  "Solana Ecosystem"
 ],
 "시가총액 순위": 81,
 "시가총액(USD)": 837565931,
 "완전희석가치 FDV(USD)": 837565931,
 "24시간 거래대금(USD)": 174331224,
 "유통량": 100000000.0,
 "총발행량": 100000000.0,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 52.62,
 "역대 최고가 대비(%)": -84.08295,
 "가격 변화(%)": {
  "7d": 18.36531,
  "30d": 13.14792,
  "1y": 27.16887
 },
 "소개": "Injective is an interoperable Layer 1 blockchain designed for DeFi applications. It provides developers with on-chain financial infrastructure modules to build dApps such as decentralized exchanges, prediction markets, and lending protocols. Its decentralized cross-chain bridging infrastructure offers compatibility with most blockchains, including EVM chains like Ethereum and non-EVM chains like S",
 "체인 TVL (DefiLlama)": {
  "체인": "Injective",
  "TVL(USD)": 22835890
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "INJ 관련 기사": [],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Hyperliquid treasury firm seeking U.S. regulatory nod as a domestic futures platform",
   "요약": "The company said it's trying to establish a U.S. \"futures commission merchant\" with full compliance for activity with U.S. clients, though the timing is uncertain.",
   "시각(UTC)": "11-06 02:24"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin developer proposes ‘landmines’ to make quantum thieves lose their own BTC",
   "요약": "Anyone trying to move vulnerable bitcoin would have to put up matching collateral, giving prepared owners a chance to take both.",
   "시각(UTC)": "11-06 01:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. Justice Department assembles force to shield against foreign AI threats",
   "요약": "The new DOJ task force will aid the recently designated U.S. \"SI Force\" by warding off bad actors backed by other nations, criminal groups or corporate fraud.",
   "시각(UTC)": "11-05 18:59"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin tumbles to $76,000 as collapsing AI trade drags stocks sharply lower",
   "요약": "The post-election rally quickly reversed as AI stocks plunged, but cryptocurrencies held up relatively better despite a $1 billion liquidation wave.",
   "시각(UTC)": "11-05 18:48"
  },
  {
   "출처": "CoinDesk",
   "제목": "What is TraderTraitor, the hacking squad behind the $6.3 billion Binance heist?",
   "요약": "The hacking group has been behind some of the crypto industry's most recent high-profile thefts.",
   "시각(UTC)": "11-05 16:58"
  },
  {
   "출처": "CoinDesk",
   "제목": "Standard Chartered and SBI back crypto insurer Soter as funding reaches $23.5 million",
   "요약": "Soter also received backing of 500 BTC and 2000 ETH, worth another $43 million at current prices.",
   "시각(UTC)": "11-05 16:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto for Advisors: Where investors stake crypto shapes how much of the reward they keep",
   "요약": "",
   "시각(UTC)": "11-05 16:13"
  },
  {
   "출처": "CoinDesk",
   "제목": "Gate CEO says crypto exchanges must prove they can survive a hack like Binance’s",
   "요약": "Lin Han says Gate holds enough assets in cold storage to cover customer balances even if its hot wallets are emptied. An independent audit is underway.",
   "시각(UTC)": "11-05 14:21"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "28 (Fear)",
  "최근 7일": [
   28,
   50,
   34,
   26,
   37,
   34,
   30
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Tapbit (Futures)": 0.01,
   "OrangeX Futures": -0.0226,
   "Binance (Futures)": 0.01,
   "Gate (Futures)": 0.0074,
   "MEXC (Futures)": 0.0288,
   "Bybit (Futures)": 0.01
  },
  "미결제약정 합계 USD(상위)": 337921689
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 92.0,
  "CoinGecko 인기 검색 코인": [
   "BTC",
   "HYPE",
   "NEAR",
   "PEARL",
   "ETH",
   "LIT",
   "PENGU",
   "ZEC",
   "SOL",
   "ZAMA",
   "INJ",
   "LINK",
   "STRK",
   "MON",
   "PUMP"
  ],
  "INJ가 인기 검색에 있음": true
 }
}
```

## INTCB

**수집 실패**
- VIBE/선물 포지션: ValueError: INTCB 무기한 선물 자료 없음
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-05",
  "종가": 51.41,
  "등락률(%)": {
   "1일": -11.48,
   "7일": -27.7,
   "30일": -54.4,
   "90일": -49.45
  },
  "이동평균": {
   "MA20": 78.993,
   "MA60": 99.527333,
   "MA120": 98.054583
  },
  "종가와 이평선 거리(%)": {
   "MA20": -34.92,
   "MA60": -48.35,
   "MA120": -47.57
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 15
  },
  "RSI14": 19.3,
  "ATR14(%)": 11.15,
  "거래량(20일 평균 대비 배수)": 1.59,
  "30일 최고가": 116.09,
  "30일 최저가": 50.42,
  "최근 10일 종가": [
   94.19,
   93.19,
   71.11,
   65.01,
   65.11,
   66.2,
   60.51,
   60.95,
   58.08,
   51.41
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-05",
  "등락률(%)": {
   "1일": -5.95,
   "7일": -11.53,
   "30일": -21.04,
   "90일": -43.49
  },
  "종가와 이평선 거리(%)": {
   "MA20": -12.04,
   "MA60": -27.91,
   "MA120": -36.02
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 39
  },
  "RSI14": 24.0
 }
}
```

### DIANA 자료 · 기본적 분석 (펀더멘털)

```json
{
 "이름": "Intel (bStocks Tokenized Stock)",
 "분류": [
  "Tokenized Assets",
  "BNB Chain Ecosystem",
  "Tokenized Stocks",
  "Real World Assets (RWA)",
  "bStocks Ecosystem"
 ],
 "시가총액 순위": 355,
 "시가총액(USD)": 65329625,
 "완전희석가치 FDV(USD)": 65329625,
 "24시간 거래대금(USD)": 19368005,
 "유통량": 1212989.76993557,
 "총발행량": 1212989.76993557,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 130.12,
 "역대 최고가 대비(%)": -58.60721,
 "가격 변화(%)": {
  "7d": -23.96354,
  "30d": -52.0176,
  "1y": null
 },
 "소개": ""
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "INTCB 관련 기사": [],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Hyperliquid treasury firm seeking U.S. regulatory nod as a domestic futures platform",
   "요약": "The company said it's trying to establish a U.S. \"futures commission merchant\" with full compliance for activity with U.S. clients, though the timing is uncertain.",
   "시각(UTC)": "11-06 02:24"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin developer proposes ‘landmines’ to make quantum thieves lose their own BTC",
   "요약": "Anyone trying to move vulnerable bitcoin would have to put up matching collateral, giving prepared owners a chance to take both.",
   "시각(UTC)": "11-06 01:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. Justice Department assembles force to shield against foreign AI threats",
   "요약": "The new DOJ task force will aid the recently designated U.S. \"SI Force\" by warding off bad actors backed by other nations, criminal groups or corporate fraud.",
   "시각(UTC)": "11-05 18:59"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin tumbles to $76,000 as collapsing AI trade drags stocks sharply lower",
   "요약": "The post-election rally quickly reversed as AI stocks plunged, but cryptocurrencies held up relatively better despite a $1 billion liquidation wave.",
   "시각(UTC)": "11-05 18:48"
  },
  {
   "출처": "CoinDesk",
   "제목": "What is TraderTraitor, the hacking squad behind the $6.3 billion Binance heist?",
   "요약": "The hacking group has been behind some of the crypto industry's most recent high-profile thefts.",
   "시각(UTC)": "11-05 16:58"
  },
  {
   "출처": "CoinDesk",
   "제목": "Standard Chartered and SBI back crypto insurer Soter as funding reaches $23.5 million",
   "요약": "Soter also received backing of 500 BTC and 2000 ETH, worth another $43 million at current prices.",
   "시각(UTC)": "11-05 16:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto for Advisors: Where investors stake crypto shapes how much of the reward they keep",
   "요약": "",
   "시각(UTC)": "11-05 16:13"
  },
  {
   "출처": "CoinDesk",
   "제목": "Gate CEO says crypto exchanges must prove they can survive a hack like Binance’s",
   "요약": "Lin Han says Gate holds enough assets in cold storage to cover customer balances even if its hot wallets are emptied. An independent audit is underway.",
   "시각(UTC)": "11-05 14:21"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "28 (Fear)",
  "최근 7일": [
   28,
   50,
   34,
   26,
   37,
   34,
   30
  ]
 },
 "선물 포지션": {
  "오류": "ValueError: INTCB 무기한 선물 자료 없음"
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": null,
  "CoinGecko 인기 검색 코인": [
   "BTC",
   "HYPE",
   "NEAR",
   "PEARL",
   "ETH",
   "LIT",
   "PENGU",
   "ZEC",
   "SOL",
   "ZAMA",
   "INJ",
   "LINK",
   "STRK",
   "MON",
   "PUMP"
  ],
  "INTCB가 인기 검색에 있음": false
 }
}
```
