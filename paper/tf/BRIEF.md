# TF팀 회의 자료 (2026-11-10 13:29 KST)

GitHub Actions가 무료 공개 API로 모은 자료입니다. 회의 진행 방법은 `aicoin/tf_team/PLAYBOOK.md`.
자료에 없는 숫자는 쓰지 않습니다. 실패한 자료는 아래 '수집 실패'에 있습니다.

분석 대상: BTC, ETH, PEPE, INJ, TRUMP

**지금까지 승률** ACE 40.9% (9/22), 채점 대기 0개 · 자세히는 `paper/tf/SCOREBOARD.md`, 교훈은 `aicoin/tf_team/LESSONS.md`

**TRAINER 모의 계좌** 총자산 10,017.55 USDT (+0.18%), 보유 없음 · 자세히는 `paper/tf/trainer/TRAINER.md`

**전체 스캔 후보** (`paper/tf/SCAN.md`) 상승 추세: PEPE, INJ · 과매도 반등: TRUMP

## BTC

**수집 실패**
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-09",
  "종가": 75368.41,
  "등락률(%)": {
   "1일": 0.69,
   "7일": -1.88,
   "30일": -9.18,
   "90일": 18.5
  },
  "이동평균": {
   "MA20": 78711.751,
   "MA60": 81106.4445,
   "MA120": 75297.546417
  },
  "종가와 이평선 거리(%)": {
   "MA20": -4.25,
   "MA60": -7.07,
   "MA120": 0.09
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 10
  },
  "RSI14": 37.8,
  "ATR14(%)": 3.14,
  "거래량(20일 평균 대비 배수)": 1.09,
  "30일 최고가": 84898.0,
  "30일 최저가": 73510.0,
  "최근 10일 종가": [
   77582.02,
   78354.0,
   76816.0,
   77453.86,
   80504.01,
   76088.01,
   75844.0,
   75867.59,
   74851.44,
   75368.41
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-10",
  "등락률(%)": {
   "1일": -1.07,
   "7일": -0.39,
   "30일": -7.43,
   "90일": -6.33
  },
  "종가와 이평선 거리(%)": {
   "MA20": -1.2,
   "MA60": -3.12,
   "MA120": -5.4
  },
  "MA20>MA60": false,
  "최근 교차": null,
  "RSI14": 39.9
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
 "시가총액(USD)": 1501827206251,
 "완전희석가치 FDV(USD)": 1501827206251,
 "24시간 거래대금(USD)": 28658466715,
 "유통량": 20110078.0,
 "총발행량": 20110078.0,
 "최대발행량": 21000000.0,
 "유통 비율(%)": 95.8,
 "역대 최고가(USD)": 126080,
 "역대 최고가 대비(%)": -40.76745,
 "가격 변화(%)": {
  "7d": -2.79725,
  "30d": -9.7665,
  "1y": -29.64004
 },
 "소개": "Bitcoin is the world's first decentralized cryptocurrency, created in 2009 by the pseudonymous Satoshi Nakamoto. It enables peer-to-peer electronic cash transactions without intermediaries like banks or governments, operating on a blockchain secured by Proof of Work mining and the SHA-256 cryptographic algorithm. \n\nWith a fixed supply cap of 21 million coins and programmatic halvings every four ye",
 "체인 TVL (DefiLlama)": {
  "체인": "Bitcoin",
  "TVL(USD)": 3945539354
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "BTC 관련 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin faces U.S. CPI test as analysts warn inflation relief may not be enough",
   "요약": "Bitcoin trades below $75,000 ahead of the October inflation data. Analysts warning that sustainable recovery depends on improving liquidity and spot ETF demand rather than temporary macro relief.",
   "시각(UTC)": "11-10 03:22"
  },
  {
   "출처": "CoinDesk",
   "제목": "A Bitcoin block just neared a 2015 transaction record, but paid only $180 in fees",
   "요약": "The AntPool block came within 984 transactions of Bitcoin’s 2015 record, even as fees made up less than 0.1% of the miner’s payout.",
   "시각(UTC)": "11-09 16:19"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin bulls can't rely on ETF flows",
   "요약": "Your day-ahead look for Nov. 9, 2026",
   "시각(UTC)": "11-09 12:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "SpaceX proposes a $24 billion Texas supercomputer and a gas plant",
   "요약": "The $24 billion project, which includes an AI supercomputer in Texas with its own gas-fired power plant, is about 17 times the value of SpaceX's bitcoin holdings.",
   "시각(UTC)": "11-09 06:54"
  },
  {
   "출처": "CoinDesk",
   "제목": "Binance's bitcoin mining pool finds just one block in a week as shutdown nears",
   "요약": "The exchange's once significant mining operation has nearly disappeared from Bitcoin's block-production rankings ahead of its November 10 closure.",
   "시각(UTC)": "11-09 04:54"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin drops as Nvidia cheating scandal and failed Iran talks trigger volatility",
   "요약": "Volatile price action has once again liquidated leveraged bullish plays worth millions.",
   "시각(UTC)": "11-09 03:21"
  },
  {
   "출처": "CoinDesk",
   "제목": "These Finland homes get free heat from bitcoin miners (as long as BTC stays above $70,000)",
   "요약": "A Finnish startup has 30 bitcoin mining systems working as central heating, and at today’s prices each one earns slightly more than the electricity it burns.",
   "시각(UTC)": "11-08 12:55"
  },
  {
   "출처": "Cointelegraph",
   "제목": "HIVE, MARA mine more Bitcoin but earn less as crypto prices fall",
   "요약": "Both miners reported higher Bitcoin production but lower mining revenue and rising electricity costs as they expanded their AI infrastructure businesses.",
   "시각(UTC)": "11-10 00:42"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Here’s what happened in crypto today",
   "요약": "Need to know what happened in crypto today? Here is the latest news on daily trends and events impacting Bitcoin price, blockchain, DeFi, Web3 and crypto regulation.",
   "시각(UTC)": "11-09 22:06"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Mercado Bitcoin begins post-hack reopening without a timeline for withdrawals",
   "요약": "Customers can view their pre-hack balances as access returns in phases. The exchange has yet to say when withdrawals will resume.",
   "시각(UTC)": "11-09 18:25"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin, tech stocks brush off Nvidia nerves as analyst mulls $68K target",
   "요약": "Bitcoin rebounded from an 11-week low near $73,500 as the Nasdaq Composite rallied despite sell-off in Nvidia shares.",
   "시각(UTC)": "11-09 17:13"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Strategy buys 1,036 Bitcoin as BTC holdings climb to 850,364",
   "요약": "Strategy bought $81.9 million in Bitcoin last week while spending $188.3 million repurchasing STRC preferred shares, according to its latest SEC filing.",
   "시각(UTC)": "11-09 13:29"
  },
  {
   "출처": "Cointelegraph",
   "제목": "BTC price eyes $73K amid Nvidia volatility: Three things to know in Bitcoin this week",
   "요약": "Bitcoin price action fell to its lowest levels since mid-August as Nvidia reports added to sell-side pressure across stock-market futures.",
   "시각(UTC)": "11-09 10:03"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin ETFs shed $1.3B in biggest weekly outflow since late June",
   "요약": "Investors pulled a net $1.21 billion from BlackRock’s IBIT last week as Bitcoin fell below $76,000 and US technology stocks sold off.",
   "시각(UTC)": "11-09 08:17"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Vitalik ‘pivots’ ETH to store of value, crypto suffers after US midterms: Hodler’s Digest",
   "요약": "Vitalik Buterin wants Ethereum to embrace a store of value narrative, upsetting Bitcoin maxis. The crypto industry faces an uncertain future following the US elections.",
   "시각(UTC)": "11-08 22:59"
  }
 ],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Securitize pushes into $6 trillion asset-backed finance market with River One acquisition",
   "요약": "The tokenization firm unveiled an acquisition and a $50 million stock buyback as quarterly revenue rose 13%. SECZ shares jumped 10% after hours.",
   "시각(UTC)": "11-09 22:56"
  },
  {
   "출처": "CoinDesk",
   "제목": "Robinhood backs tokenization of its stock on OKX–ICE platform even as most companies opt out",
   "요약": "The brokerage firm said it would rather help build tokenized markets than sit on the sidelines, following a wave of early corporate pushback to the Intercontinental Exchange and OKX joint venture.",
   "시각(UTC)": "11-09 19:36"
  },
  {
   "출처": "CoinDesk",
   "제목": "Google’s AI chip push adds more pressure on Nvidia",
   "요약": "Google’s specialised AI chips threaten greater competition as Nvidia faces a leadership investigation.",
   "시각(UTC)": "11-09 15:20"
  },
  {
   "출처": "CoinDesk",
   "제목": "North Korean hackers are creating memecoins to wash loot from $6.3 billion Binance hack",
   "요약": "North Korean hackers used six homemade memecoins to launder 117,000 NEAR, worth about $430,000, from the $6.3 billion Binance hack, Elliptic says.",
   "시각(UTC)": "11-09 15:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "NYSE picks Avalanche to settle tokenized stocks amid Wall Street's blockchain race",
   "요약": "Avalanche will serve as the core settlement ledger for the exchange's planned blockchain stock market",
   "시각(UTC)": "11-09 13:40"
  },
  {
   "출처": "CoinDesk",
   "제목": "Solana set for its first tokenized stock venue under SEC framework, listing Galaxy",
   "요약": "Formation Securities plans to launch in early 2027 with Galaxy, Exodus and Forward Industries shares, expanding the U.S. regulator's experiment in blockchain-based stock trading.",
   "시각(UTC)": "11-09 12:41"
  },
  {
   "출처": "CoinDesk",
   "제목": "Trump says he knows ‘nothing’ about World Liberty’s UAE ties as Justin Sun challenges filings",
   "요약": "Trump confirmed he co-owns World Liberty, whose UAE ownership could derail Justin Sun’s federal lawsuit over frozen WLFI tokens",
   "시각(UTC)": "11-09 12:37"
  },
  {
   "출처": "CoinDesk",
   "제목": "Nvidia-led tech selloff weighs on crypto majors",
   "요약": "Only five of the top 100 cryptocurrencies by market value are up 1% or more over the past 24 hours. That is the state of the market today.",
   "시각(UTC)": "11-09 11:42"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "32 (Fear)",
  "최근 7일": [
   32,
   29,
   28,
   25,
   28,
   50,
   34
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "WEEX (Futures)": 0.0001,
   "Hyperliquid (Futures)": 0.0013,
   "OKX (Futures)": 0.0044,
   "Bybit (Futures)": 0.0018,
   "MEXC (Futures)": 0.01,
   "Gate (Futures)": 0.01
  },
  "미결제약정 합계 USD(상위)": 18605322704
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 65.66,
  "CoinGecko 인기 검색 코인": [
   "DACITY",
   "AVAX",
   "PIEVERSE",
   "AERO",
   "BTC",
   "XRP",
   "INIT",
   "BP",
   "JUP",
   "HYPE",
   "KNTQ",
   "PENGU",
   "ZEC",
   "JCT",
   "SOL"
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
  "기준일": "2026-11-09",
  "종가": 2135.24,
  "등락률(%)": {
   "1일": 0.37,
   "7일": -5.24,
   "30일": -14.81,
   "90일": 13.42
  },
  "이동평균": {
   "MA20": 2296.7855,
   "MA60": 2480.601,
   "MA120": 2292.316083
  },
  "종가와 이평선 거리(%)": {
   "MA20": -7.03,
   "MA60": -13.92,
   "MA120": -6.85
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 20
  },
  "RSI14": 33.7,
  "ATR14(%)": 4.59,
  "거래량(20일 평균 대비 배수)": 1.31,
  "30일 최고가": 2579.88,
  "30일 최저가": 2060.0,
  "최근 10일 종가": [
   2255.66,
   2275.31,
   2253.29,
   2274.77,
   2424.61,
   2238.01,
   2238.67,
   2240.24,
   2127.46,
   2135.24
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-10",
  "등락률(%)": {
   "1일": -0.96,
   "7일": -0.6,
   "30일": -12.77,
   "90일": -8.18
  },
  "종가와 이평선 거리(%)": {
   "MA20": -3.62,
   "MA60": -6.28,
   "MA120": -8.22
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 12
  },
  "RSI14": 33.2
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
 "시가총액(USD)": 259254813086,
 "완전희석가치 FDV(USD)": 259254813211,
 "24시간 거래대금(USD)": 12289424236,
 "유통량": 122206811.20718135,
 "총발행량": 122206811.26598936,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 4946.05,
 "역대 최고가 대비(%)": -57.10829,
 "가격 변화(%)": {
  "7d": -5.72755,
  "30d": -15.06527,
  "1y": -41.49578
 },
 "소개": "Ethereum is a global, open-source platform for decentralized applications. In other words, it is a decentralized blockchain platform that enables developers to build and deploy smart contracts and applications without central authority control. Unlike Bitcoin, which primarily functions as digital currency, Ethereum operates as a programmable global computer where developers can create any type of ",
 "체인 TVL (DefiLlama)": {
  "체인": "Ethereum",
  "TVL(USD)": 41866732422
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "ETH 관련 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Two rival Ethereum proposals aim to stop Glamsterdam breaking old contracts",
   "요약": "The proposals aim to keep Ethereum’s planned gas changes from breaking existing contracts, using different approaches to what contracts see and what users pay.",
   "시각(UTC)": "11-09 05:16"
  },
  {
   "출처": "Cointelegraph",
   "제목": "PNC Bank tests turning USDC payments into dollar deposits",
   "요약": "The pilot lets eligible corporate and institutional clients accept USDC on Ethereum, with each token converted to one US dollar before deposit.",
   "시각(UTC)": "11-09 17:48"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Vitalik ‘pivots’ ETH to store of value, crypto suffers after US midterms: Hodler’s Digest",
   "요약": "Vitalik Buterin wants Ethereum to embrace a store of value narrative, upsetting Bitcoin maxis. The crypto industry faces an uncertain future following the US elections.",
   "시각(UTC)": "11-08 22:59"
  },
  {
   "출처": "Decrypt",
   "제목": "Vitalik Buterin Moves On From ‘Ultrasound Money,’ Says ETH’s Value Is Stability",
   "요약": "The Ethereum co-founder says ETH's value comes from stability, not fee burns, citing its decentralization, censorship resistance and security.",
   "시각(UTC)": "11-09 17:14"
  },
  {
   "출처": "Decrypt",
   "제목": "Tom Lee’s Bitmine Adds $20M in Ethereum, Seizing on Vitalik’s 'ETH Is Money' Declaration",
   "요약": "The firm’s stash reached 6.07 million ETH—4.97% of supply and 99% of the way to its “Alchemy of 5%” goal—as chairman Tom Lee called Vitalik Buterin’s “ETH is money” comments a “seismic shift.”",
   "시각(UTC)": "11-09 17:08"
  }
 ],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin faces U.S. CPI test as analysts warn inflation relief may not be enough",
   "요약": "Bitcoin trades below $75,000 ahead of the October inflation data. Analysts warning that sustainable recovery depends on improving liquidity and spot ETF demand rather than temporary macro relief.",
   "시각(UTC)": "11-10 03:22"
  },
  {
   "출처": "CoinDesk",
   "제목": "Securitize pushes into $6 trillion asset-backed finance market with River One acquisition",
   "요약": "The tokenization firm unveiled an acquisition and a $50 million stock buyback as quarterly revenue rose 13%. SECZ shares jumped 10% after hours.",
   "시각(UTC)": "11-09 22:56"
  },
  {
   "출처": "CoinDesk",
   "제목": "Robinhood backs tokenization of its stock on OKX–ICE platform even as most companies opt out",
   "요약": "The brokerage firm said it would rather help build tokenized markets than sit on the sidelines, following a wave of early corporate pushback to the Intercontinental Exchange and OKX joint venture.",
   "시각(UTC)": "11-09 19:36"
  },
  {
   "출처": "CoinDesk",
   "제목": "A Bitcoin block just neared a 2015 transaction record, but paid only $180 in fees",
   "요약": "The AntPool block came within 984 transactions of Bitcoin’s 2015 record, even as fees made up less than 0.1% of the miner’s payout.",
   "시각(UTC)": "11-09 16:19"
  },
  {
   "출처": "CoinDesk",
   "제목": "Google’s AI chip push adds more pressure on Nvidia",
   "요약": "Google’s specialised AI chips threaten greater competition as Nvidia faces a leadership investigation.",
   "시각(UTC)": "11-09 15:20"
  },
  {
   "출처": "CoinDesk",
   "제목": "North Korean hackers are creating memecoins to wash loot from $6.3 billion Binance hack",
   "요약": "North Korean hackers used six homemade memecoins to launder 117,000 NEAR, worth about $430,000, from the $6.3 billion Binance hack, Elliptic says.",
   "시각(UTC)": "11-09 15:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "NYSE picks Avalanche to settle tokenized stocks amid Wall Street's blockchain race",
   "요약": "Avalanche will serve as the core settlement ledger for the exchange's planned blockchain stock market",
   "시각(UTC)": "11-09 13:40"
  },
  {
   "출처": "CoinDesk",
   "제목": "Solana set for its first tokenized stock venue under SEC framework, listing Galaxy",
   "요약": "Formation Securities plans to launch in early 2027 with Galaxy, Exodus and Forward Industries shares, expanding the U.S. regulator's experiment in blockchain-based stock trading.",
   "시각(UTC)": "11-09 12:41"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "32 (Fear)",
  "최근 7일": [
   32,
   29,
   28,
   25,
   28,
   50,
   34
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "WEEX (Futures)": 0.0,
   "CoinW (Futures)": 0.0015,
   "Hyperliquid (Futures)": -0.0001,
   "OKX (Futures)": 0.0028,
   "MEXC (Futures)": 0.0015,
   "OrangeX Futures": 0.0061
  },
  "미결제약정 합계 USD(상위)": 9820363718
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 78.18,
  "CoinGecko 인기 검색 코인": [
   "DACITY",
   "AVAX",
   "PIEVERSE",
   "AERO",
   "BTC",
   "XRP",
   "INIT",
   "BP",
   "JUP",
   "HYPE",
   "KNTQ",
   "PENGU",
   "ZEC",
   "JCT",
   "SOL"
  ],
  "ETH가 인기 검색에 있음": false
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
  "기준일": "2026-11-09",
  "종가": 5e-06,
  "등락률(%)": {
   "1일": 3.23,
   "7일": 7.11,
   "30일": 26.73,
   "90일": 80.28
  },
  "이동평균": {
   "MA20": 5e-06,
   "MA60": 4e-06,
   "MA120": 4e-06
  },
  "종가와 이평선 거리(%)": {
   "MA20": 7.7,
   "MA60": 18.78,
   "MA120": 37.98
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 104
  },
  "RSI14": 60.5,
  "ATR14(%)": 10.39,
  "거래량(20일 평균 대비 배수)": 1.08,
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
  "기준일": "2026-11-10",
  "등락률(%)": {
   "1일": 0.78,
   "7일": 4.03,
   "30일": 3.41,
   "90일": 20.28
  },
  "종가와 이평선 거리(%)": {
   "MA20": 3.05,
   "MA60": 4.34,
   "MA120": 7.62
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 9
  },
  "RSI14": 57.2
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
 "시가총액 순위": 42,
 "시가총액(USD)": 2212735144,
 "완전희석가치 FDV(USD)": 2212735144,
 "24시간 거래대금(USD)": 485538171,
 "유통량": 420690000000000.0,
 "총발행량": 420690000000000.0,
 "최대발행량": 420690000000000.0,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 2.803e-05,
 "역대 최고가 대비(%)": -81.23397,
 "가격 변화(%)": {
  "7d": 12.16518,
  "30d": 32.15909,
  "1y": -14.4431
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
   "제목": "Bitcoin faces U.S. CPI test as analysts warn inflation relief may not be enough",
   "요약": "Bitcoin trades below $75,000 ahead of the October inflation data. Analysts warning that sustainable recovery depends on improving liquidity and spot ETF demand rather than temporary macro relief.",
   "시각(UTC)": "11-10 03:22"
  },
  {
   "출처": "CoinDesk",
   "제목": "Securitize pushes into $6 trillion asset-backed finance market with River One acquisition",
   "요약": "The tokenization firm unveiled an acquisition and a $50 million stock buyback as quarterly revenue rose 13%. SECZ shares jumped 10% after hours.",
   "시각(UTC)": "11-09 22:56"
  },
  {
   "출처": "CoinDesk",
   "제목": "Robinhood backs tokenization of its stock on OKX–ICE platform even as most companies opt out",
   "요약": "The brokerage firm said it would rather help build tokenized markets than sit on the sidelines, following a wave of early corporate pushback to the Intercontinental Exchange and OKX joint venture.",
   "시각(UTC)": "11-09 19:36"
  },
  {
   "출처": "CoinDesk",
   "제목": "A Bitcoin block just neared a 2015 transaction record, but paid only $180 in fees",
   "요약": "The AntPool block came within 984 transactions of Bitcoin’s 2015 record, even as fees made up less than 0.1% of the miner’s payout.",
   "시각(UTC)": "11-09 16:19"
  },
  {
   "출처": "CoinDesk",
   "제목": "Google’s AI chip push adds more pressure on Nvidia",
   "요약": "Google’s specialised AI chips threaten greater competition as Nvidia faces a leadership investigation.",
   "시각(UTC)": "11-09 15:20"
  },
  {
   "출처": "CoinDesk",
   "제목": "North Korean hackers are creating memecoins to wash loot from $6.3 billion Binance hack",
   "요약": "North Korean hackers used six homemade memecoins to launder 117,000 NEAR, worth about $430,000, from the $6.3 billion Binance hack, Elliptic says.",
   "시각(UTC)": "11-09 15:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "NYSE picks Avalanche to settle tokenized stocks amid Wall Street's blockchain race",
   "요약": "Avalanche will serve as the core settlement ledger for the exchange's planned blockchain stock market",
   "시각(UTC)": "11-09 13:40"
  },
  {
   "출처": "CoinDesk",
   "제목": "Solana set for its first tokenized stock venue under SEC framework, listing Galaxy",
   "요약": "Formation Securities plans to launch in early 2027 with Galaxy, Exodus and Forward Industries shares, expanding the U.S. regulator's experiment in blockchain-based stock trading.",
   "시각(UTC)": "11-09 12:41"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "32 (Fear)",
  "최근 7일": [
   32,
   29,
   28,
   25,
   28,
   50,
   34
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "MEXC (Futures)": 0.01,
   "Gate (Futures)": 0.0047,
   "OKX (Futures)": 0.01,
   "Bitget Futures": 0.01,
   "KCEX (Futures)": 0.01,
   "WhiteBIT Futures": 0.01
  },
  "미결제약정 합계 USD(상위)": 205369533
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 84.09,
  "CoinGecko 인기 검색 코인": [
   "DACITY",
   "AVAX",
   "PIEVERSE",
   "AERO",
   "BTC",
   "XRP",
   "INIT",
   "BP",
   "JUP",
   "HYPE",
   "KNTQ",
   "PENGU",
   "ZEC",
   "JCT",
   "SOL"
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
  "기준일": "2026-11-09",
  "종가": 8.115,
  "등락률(%)": {
   "1일": 0.82,
   "7일": 16.21,
   "30일": 6.09,
   "90일": 73.95
  },
  "이동평균": {
   "MA20": 7.8032,
   "MA60": 7.5745,
   "MA120": 6.272292
  },
  "종가와 이평선 거리(%)": {
   "MA20": 4.0,
   "MA60": 7.14,
   "MA120": 29.38
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 68
  },
  "RSI14": 54.7,
  "ATR14(%)": 7.4,
  "거래량(20일 평균 대비 배수)": 1.3,
  "30일 최고가": 9.417,
  "30일 최저가": 6.823,
  "최근 10일 종가": [
   7.231,
   7.185,
   6.983,
   7.248,
   7.937,
   8.148,
   8.297,
   8.262,
   8.049,
   8.115
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-10",
  "등락률(%)": {
   "1일": -1.4,
   "7일": -0.6,
   "30일": -0.58,
   "90일": 4.48
  },
  "종가와 이평선 거리(%)": {
   "MA20": -1.89,
   "MA60": 3.35,
   "MA120": 2.54
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 25
  },
  "RSI14": 47.4
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
 "시가총액(USD)": 803869370,
 "완전희석가치 FDV(USD)": 803869370,
 "24시간 거래대금(USD)": 101011042,
 "유통량": 100000000.0,
 "총발행량": 100000000.0,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 52.62,
 "역대 최고가 대비(%)": -84.72332,
 "가격 변화(%)": {
  "7d": 15.52783,
  "30d": 7.17523,
  "1y": 1.8839
 },
 "소개": "Injective is an interoperable Layer 1 blockchain designed for DeFi applications. It provides developers with on-chain financial infrastructure modules to build dApps such as decentralized exchanges, prediction markets, and lending protocols. Its decentralized cross-chain bridging infrastructure offers compatibility with most blockchains, including EVM chains like Ethereum and non-EVM chains like S",
 "체인 TVL (DefiLlama)": {
  "체인": "Injective",
  "TVL(USD)": 21822243
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
   "제목": "Bitcoin faces U.S. CPI test as analysts warn inflation relief may not be enough",
   "요약": "Bitcoin trades below $75,000 ahead of the October inflation data. Analysts warning that sustainable recovery depends on improving liquidity and spot ETF demand rather than temporary macro relief.",
   "시각(UTC)": "11-10 03:22"
  },
  {
   "출처": "CoinDesk",
   "제목": "Securitize pushes into $6 trillion asset-backed finance market with River One acquisition",
   "요약": "The tokenization firm unveiled an acquisition and a $50 million stock buyback as quarterly revenue rose 13%. SECZ shares jumped 10% after hours.",
   "시각(UTC)": "11-09 22:56"
  },
  {
   "출처": "CoinDesk",
   "제목": "Robinhood backs tokenization of its stock on OKX–ICE platform even as most companies opt out",
   "요약": "The brokerage firm said it would rather help build tokenized markets than sit on the sidelines, following a wave of early corporate pushback to the Intercontinental Exchange and OKX joint venture.",
   "시각(UTC)": "11-09 19:36"
  },
  {
   "출처": "CoinDesk",
   "제목": "A Bitcoin block just neared a 2015 transaction record, but paid only $180 in fees",
   "요약": "The AntPool block came within 984 transactions of Bitcoin’s 2015 record, even as fees made up less than 0.1% of the miner’s payout.",
   "시각(UTC)": "11-09 16:19"
  },
  {
   "출처": "CoinDesk",
   "제목": "Google’s AI chip push adds more pressure on Nvidia",
   "요약": "Google’s specialised AI chips threaten greater competition as Nvidia faces a leadership investigation.",
   "시각(UTC)": "11-09 15:20"
  },
  {
   "출처": "CoinDesk",
   "제목": "North Korean hackers are creating memecoins to wash loot from $6.3 billion Binance hack",
   "요약": "North Korean hackers used six homemade memecoins to launder 117,000 NEAR, worth about $430,000, from the $6.3 billion Binance hack, Elliptic says.",
   "시각(UTC)": "11-09 15:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "NYSE picks Avalanche to settle tokenized stocks amid Wall Street's blockchain race",
   "요약": "Avalanche will serve as the core settlement ledger for the exchange's planned blockchain stock market",
   "시각(UTC)": "11-09 13:40"
  },
  {
   "출처": "CoinDesk",
   "제목": "Solana set for its first tokenized stock venue under SEC framework, listing Galaxy",
   "요약": "Formation Securities plans to launch in early 2027 with Galaxy, Exodus and Forward Industries shares, expanding the U.S. regulator's experiment in blockchain-based stock trading.",
   "시각(UTC)": "11-09 12:41"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "32 (Fear)",
  "최근 7일": [
   32,
   29,
   28,
   25,
   28,
   50,
   34
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Tapbit (Futures)": 0.01,
   "OrangeX Futures": -0.0194,
   "WEEX (Futures)": 0.0001,
   "Gate (Futures)": 0.01,
   "BingX (Futures)": 0.01,
   "MEXC (Futures)": -0.0055
  },
  "미결제약정 합계 USD(상위)": 178696856
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 75.0,
  "CoinGecko 인기 검색 코인": [
   "DACITY",
   "AVAX",
   "PIEVERSE",
   "AERO",
   "BTC",
   "XRP",
   "INIT",
   "BP",
   "JUP",
   "HYPE",
   "KNTQ",
   "PENGU",
   "ZEC",
   "JCT",
   "SOL"
  ],
  "INJ가 인기 검색에 있음": false
 }
}
```

## TRUMP

**수집 실패**
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-09",
  "종가": 1.121,
  "등락률(%)": {
   "1일": -1.32,
   "7일": -29.94,
   "30일": -40.78,
   "90일": -24.31
  },
  "이동평균": {
   "MA20": 1.52425,
   "MA60": 1.823917,
   "MA120": 1.81025
  },
  "종가와 이평선 거리(%)": {
   "MA20": -26.46,
   "MA60": -38.54,
   "MA120": -38.07
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 30
  },
  "RSI14": 24.9,
  "ATR14(%)": 11.74,
  "거래량(20일 평균 대비 배수)": 0.96,
  "30일 최고가": 1.959,
  "30일 최저가": 1.108,
  "최근 10일 종가": [
   1.576,
   1.705,
   1.6,
   1.586,
   1.27,
   1.182,
   1.204,
   1.188,
   1.136,
   1.121
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-10",
  "등락률(%)": {
   "1일": 0.27,
   "7일": -1.06,
   "30일": -11.36,
   "90일": -30.96
  },
  "종가와 이평선 거리(%)": {
   "MA20": -3.54,
   "MA60": -18.14,
   "MA120": -26.83
  },
  "MA20>MA60": false,
  "최근 교차": null,
  "RSI14": 31.2
 }
}
```

### DIANA 자료 · 기본적 분석 (펀더멘털)

```json
{
 "이름": "Official Trump",
 "분류": [
  "Solana Ecosystem",
  "Meme",
  "Solana Meme",
  "PolitiFi",
  "Made in USA"
 ],
 "시가총액 순위": 129,
 "시가총액(USD)": 316591896,
 "완전희석가치 FDV(USD)": 1123192305,
 "24시간 거래대금(USD)": 102895650,
 "유통량": 281867935.671502,
 "총발행량": 1000000000.0,
 "최대발행량": 1000000000.0,
 "유통 비율(%)": 28.2,
 "역대 최고가(USD)": 73.43,
 "역대 최고가 대비(%)": -98.4704,
 "가격 변화(%)": {
  "7d": -29.76971,
  "30d": -39.7504,
  "1y": -85.60092
 },
 "소개": "TRUMP is a politics-themed digital coin built on the Solana blockchain that uses the brand of Donald Trump to foster a community-driven ecosystem. As a community-focused asset, it is designed to bridge political support with web ownership, operating within the PolitiFi sector to blend political movements with decentralized finance tools. The project's main value proposition lies in its official ti"
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "TRUMP 관련 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Trump says he knows ‘nothing’ about World Liberty’s UAE ties as Justin Sun challenges filings",
   "요약": "Trump confirmed he co-owns World Liberty, whose UAE ownership could derail Justin Sun’s federal lawsuit over frozen WLFI tokens",
   "시각(UTC)": "11-09 12:37"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Binance, Tether and Trump crypto firms face Senate records deadline",
   "요약": "Sen. Richard Blumenthal asked four crypto firms to start sending records by Nov. 30 and warned of further action if they miss the Jan. 4 deadline.",
   "시각(UTC)": "11-09 09:00"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Nvidia may face a more hostile post-election Washington: Report",
   "요약": "CEO Jensen Huang’s relationship with President Donald Trump probably won’t save the company from a more adversarial Washington, Semafor says.",
   "시각(UTC)": "11-07 07:45"
  },
  {
   "출처": "Decrypt",
   "제목": "Trump Says He Knows 'Nothing' About World Liberty Financial as He Defends UAE Ties",
   "요약": "Pressed on why he doesn't divest from the family's crypto venture, Trump said his sons run the business and every president faces conflicts.",
   "시각(UTC)": "11-09 11:26"
  }
 ],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin faces U.S. CPI test as analysts warn inflation relief may not be enough",
   "요약": "Bitcoin trades below $75,000 ahead of the October inflation data. Analysts warning that sustainable recovery depends on improving liquidity and spot ETF demand rather than temporary macro relief.",
   "시각(UTC)": "11-10 03:22"
  },
  {
   "출처": "CoinDesk",
   "제목": "Securitize pushes into $6 trillion asset-backed finance market with River One acquisition",
   "요약": "The tokenization firm unveiled an acquisition and a $50 million stock buyback as quarterly revenue rose 13%. SECZ shares jumped 10% after hours.",
   "시각(UTC)": "11-09 22:56"
  },
  {
   "출처": "CoinDesk",
   "제목": "Robinhood backs tokenization of its stock on OKX–ICE platform even as most companies opt out",
   "요약": "The brokerage firm said it would rather help build tokenized markets than sit on the sidelines, following a wave of early corporate pushback to the Intercontinental Exchange and OKX joint venture.",
   "시각(UTC)": "11-09 19:36"
  },
  {
   "출처": "CoinDesk",
   "제목": "A Bitcoin block just neared a 2015 transaction record, but paid only $180 in fees",
   "요약": "The AntPool block came within 984 transactions of Bitcoin’s 2015 record, even as fees made up less than 0.1% of the miner’s payout.",
   "시각(UTC)": "11-09 16:19"
  },
  {
   "출처": "CoinDesk",
   "제목": "Google’s AI chip push adds more pressure on Nvidia",
   "요약": "Google’s specialised AI chips threaten greater competition as Nvidia faces a leadership investigation.",
   "시각(UTC)": "11-09 15:20"
  },
  {
   "출처": "CoinDesk",
   "제목": "North Korean hackers are creating memecoins to wash loot from $6.3 billion Binance hack",
   "요약": "North Korean hackers used six homemade memecoins to launder 117,000 NEAR, worth about $430,000, from the $6.3 billion Binance hack, Elliptic says.",
   "시각(UTC)": "11-09 15:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "NYSE picks Avalanche to settle tokenized stocks amid Wall Street's blockchain race",
   "요약": "Avalanche will serve as the core settlement ledger for the exchange's planned blockchain stock market",
   "시각(UTC)": "11-09 13:40"
  },
  {
   "출처": "CoinDesk",
   "제목": "Solana set for its first tokenized stock venue under SEC framework, listing Galaxy",
   "요약": "Formation Securities plans to launch in early 2027 with Galaxy, Exodus and Forward Industries shares, expanding the U.S. regulator's experiment in blockchain-based stock trading.",
   "시각(UTC)": "11-09 12:41"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "32 (Fear)",
  "최근 7일": [
   32,
   29,
   28,
   25,
   28,
   50,
   34
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "WEEX (Futures)": -0.0002,
   "Gate (Futures)": -0.0097,
   "OKX (Futures)": -0.0004,
   "CoinUp.io (Futures)": -0.007,
   "Hyperliquid (Futures)": 0.0006,
   "Bybit (Futures)": 0.005
  },
  "미결제약정 합계 USD(상위)": 551259939
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 42.31,
  "CoinGecko 인기 검색 코인": [
   "DACITY",
   "AVAX",
   "PIEVERSE",
   "AERO",
   "BTC",
   "XRP",
   "INIT",
   "BP",
   "JUP",
   "HYPE",
   "KNTQ",
   "PENGU",
   "ZEC",
   "JCT",
   "SOL"
  ],
  "TRUMP가 인기 검색에 있음": false
 }
}
```
