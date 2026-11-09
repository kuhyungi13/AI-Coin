# TF팀 회의 자료 (2026-11-10 01:42 KST)

GitHub Actions가 무료 공개 API로 모은 자료입니다. 회의 진행 방법은 `aicoin/tf_team/PLAYBOOK.md`.
자료에 없는 숫자는 쓰지 않습니다. 실패한 자료는 아래 '수집 실패'에 있습니다.

분석 대상: BTC, ETH, PEPE, QNT, AI

**지금까지 승률** ACE 40.9% (9/22), 채점 대기 0개 · 자세히는 `paper/tf/SCOREBOARD.md`, 교훈은 `aicoin/tf_team/LESSONS.md`

**TRAINER 모의 계좌** 총자산 10,017.55 USDT (+0.18%), 보유 없음 · 자세히는 `paper/tf/trainer/TRAINER.md`

**전체 스캔 후보** (`paper/tf/SCAN.md`) 상승 추세: PEPE, QNT · 과매도 반등: AI

## BTC

**수집 실패**
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-08",
  "종가": 74851.44,
  "등락률(%)": {
   "1일": -1.34,
   "7일": -4.47,
   "30일": -9.42,
   "90일": 17.01
  },
  "이동평균": {
   "MA20": 79094.738,
   "MA60": 81126.449667,
   "MA120": 75200.976333
  },
  "종가와 이평선 거리(%)": {
   "MA20": -5.36,
   "MA60": -7.73,
   "MA120": -0.46
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 9
  },
  "RSI14": 35.6,
  "ATR14(%)": 3.12,
  "거래량(20일 평균 대비 배수)": 0.65,
  "30일 최고가": 84898.0,
  "30일 최저가": 73510.0,
  "최근 10일 종가": [
   77368.77,
   77582.02,
   78354.0,
   76816.0,
   77453.86,
   80504.01,
   76088.01,
   75844.0,
   75867.59,
   74851.44
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-09",
  "등락률(%)": {
   "1일": 1.56,
   "7일": -0.59,
   "30일": -5.93,
   "90일": -6.33
  },
  "종가와 이평선 거리(%)": {
   "MA20": -0.12,
   "MA60": -2.0,
   "MA120": -4.41
  },
  "MA20>MA60": false,
  "최근 교차": null,
  "RSI14": 45.7
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
 "시가총액(USD)": 1505511306237,
 "완전희석가치 FDV(USD)": 1505513177841,
 "24시간 거래대금(USD)": 33942564220,
 "유통량": 20109909.0,
 "총발행량": 20109934.0,
 "최대발행량": 21000000.0,
 "유통 비율(%)": 95.8,
 "역대 최고가(USD)": 126080,
 "역대 최고가 대비(%)": -40.62165,
 "가격 변화(%)": {
  "7d": -3.29798,
  "30d": -9.7698,
  "1y": -27.82424
 },
 "소개": "Bitcoin is the world's first decentralized cryptocurrency, created in 2009 by the pseudonymous Satoshi Nakamoto. It enables peer-to-peer electronic cash transactions without intermediaries like banks or governments, operating on a blockchain secured by Proof of Work mining and the SHA-256 cryptographic algorithm. \n\nWith a fixed supply cap of 21 million coins and programmatic halvings every four ye",
 "체인 TVL (DefiLlama)": {
  "체인": "Bitcoin",
  "TVL(USD)": 3935435233
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "BTC 관련 기사": [
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
   "제목": "Live news: Bitcoin narrows loss as Nasdaq surges more than 2%",
   "요약": "The Nasdaq and S&P 500 are both sharply higher even as Nvidia declines following CEO Jensen Huang's issues.",
   "시각(UTC)": "11-09 10:51"
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
   "제목": "Here’s what happened in crypto today",
   "요약": "Need to know what happened in crypto today? Here is the latest news on daily trends and events impacting Bitcoin price, blockchain, DeFi, Web3 and crypto regulation.",
   "시각(UTC)": "11-09 13:36"
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
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin holders have received eCash — What can you do with it?",
   "요약": "Bitcoin’s eCash fork gives eligible holders an equivalent balance of ECX, but questions remain over where they can trade the tokens and what they can do with them.",
   "시각(UTC)": "11-07 13:30"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Russia finalizes crypto trading rules ahead of Nov. 17 rollout",
   "요약": "The rules allow retail investors to trade BTC, ETH and USDT through regulated intermediaries, with Moscow Exchange planning to launch crypto trading in December.",
   "시각(UTC)": "11-06 18:47"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Strive buys 15,124 Bitcoin in October, closes in on top treasury holders",
   "요약": "Bitcoin treasury company Strive reported $509 million in third-quarter net income and purchased 15,124 BTC in October, bringing its total holdings to 43,124 BTC.",
   "시각(UTC)": "11-06 18:22"
  }
 ],
 "시장 전반 기사": [
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Zcash developers want 20-second blocks just days after major speed upgrade",
   "요약": "Early data shows Zcash's orphan-block rate holding close to pre-upgrade levels despite blocks arriving three times faster, encouraging developers to push for another reduction.",
   "시각(UTC)": "11-09 10:52"
  },
  {
   "출처": "CoinDesk",
   "제목": "Coinbase gets full U.S. trust charter from federal banking regulator",
   "요약": "The Office of the Comptroller of the Currency elevated the biggest U.S. exchange's trust status from conditional to a full-fledged charter, the company said.",
   "시각(UTC)": "11-09 10:00"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "29 (Fear)",
  "최근 7일": [
   29,
   28,
   25,
   28,
   50,
   34,
   26
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.01,
   "Bybit (Futures)": 0.0095,
   "MEXC (Futures)": 0.01,
   "Gate (Futures)": 0.01,
   "WEEX (Futures)": 0.0001,
   "Toobit Futures": 0.01
  },
  "미결제약정 합계 USD(상위)": 28589751213
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 63.19,
  "CoinGecko 인기 검색 코인": [
   "DACITY",
   "AVAX",
   "KNTQ",
   "BTC",
   "ONDO",
   "HYPE",
   "PEARL",
   "NEAR",
   "LIT",
   "INJ",
   "AERO",
   "ETH",
   "XRP",
   "ARB",
   "SUI"
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
  "기준일": "2026-11-08",
  "종가": 2127.46,
  "등락률(%)": {
   "1일": -5.03,
   "7일": -6.5,
   "30일": -14.48,
   "90일": 13.58
  },
  "이동평균": {
   "MA20": 2312.4835,
   "MA60": 2485.6515,
   "MA120": 2289.579083
  },
  "종가와 이평선 거리(%)": {
   "MA20": -8.0,
   "MA60": -14.41,
   "MA120": -7.08
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 19
  },
  "RSI14": 32.9,
  "ATR14(%)": 4.52,
  "거래량(20일 평균 대비 배수)": 0.84,
  "30일 최고가": 2579.88,
  "30일 최저가": 2060.0,
  "최근 10일 종가": [
   2245.54,
   2255.66,
   2275.31,
   2253.29,
   2274.77,
   2424.61,
   2238.01,
   2238.67,
   2240.24,
   2127.46
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-09",
  "등락률(%)": {
   "1일": 1.62,
   "7일": -4.15,
   "30일": -11.48,
   "90일": -8.4
  },
  "종가와 이평선 거리(%)": {
   "MA20": -2.86,
   "MA60": -5.06,
   "MA120": -7.11
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 9
  },
  "RSI14": 36.8
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
 "시가총액(USD)": 259986998570,
 "완전희석가치 FDV(USD)": 259986998570,
 "24시간 거래대금(USD)": 16822468777,
 "유통량": 122203846.69715354,
 "총발행량": 122203846.69715354,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 4946.05,
 "역대 최고가 대비(%)": -56.98612,
 "가격 변화(%)": {
  "7d": -6.2881,
  "30d": -15.2131,
  "1y": -39.46592
 },
 "소개": "Ethereum is a global, open-source platform for decentralized applications. In other words, it is a decentralized blockchain platform that enables developers to build and deploy smart contracts and applications without central authority control. Unlike Bitcoin, which primarily functions as digital currency, Ethereum operates as a programmable global computer where developers can create any type of ",
 "체인 TVL (DefiLlama)": {
  "체인": "Ethereum",
  "TVL(USD)": 41908283667
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
   "제목": "Vitalik ‘pivots’ ETH to store of value, crypto suffers after US midterms: Hodler’s Digest",
   "요약": "Vitalik Buterin wants Ethereum to embrace a store of value narrative, upsetting Bitcoin maxis. The crypto industry faces an uncertain future following the US elections.",
   "시각(UTC)": "11-08 22:59"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Russia finalizes crypto trading rules ahead of Nov. 17 rollout",
   "요약": "The rules allow retail investors to trade BTC, ETH and USDT through regulated intermediaries, with Moscow Exchange planning to launch crypto trading in December.",
   "시각(UTC)": "11-06 18:47"
  }
 ],
 "시장 전반 기사": [
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Trump says he knows ‘nothing’ about World Liberty’s UAE ties as Justin Sun challenges filings",
   "요약": "Trump confirmed he co-owns World Liberty, whose UAE ownership could derail Justin Sun’s federal lawsuit over frozen WLFI tokens",
   "시각(UTC)": "11-09 12:37"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin bulls can't rely on ETF flows",
   "요약": "Your day-ahead look for Nov. 9, 2026",
   "시각(UTC)": "11-09 12:30"
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
  "오늘": "29 (Fear)",
  "최근 7일": [
   29,
   28,
   25,
   28,
   50,
   34,
   26
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.0033,
   "WEEX (Futures)": -0.0,
   "CoinW (Futures)": 0.0033,
   "MEXC (Futures)": 0.0033,
   "Toobit Futures": 0.0034
  },
  "미결제약정 합계 USD(상위)": 17594233402
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 68.66,
  "CoinGecko 인기 검색 코인": [
   "DACITY",
   "AVAX",
   "KNTQ",
   "BTC",
   "ONDO",
   "HYPE",
   "PEARL",
   "NEAR",
   "LIT",
   "INJ",
   "AERO",
   "ETH",
   "XRP",
   "ARB",
   "SUI"
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
  "기준일": "2026-11-08",
  "종가": 5e-06,
  "등락률(%)": {
   "1일": 1.85,
   "7일": 1.64,
   "30일": 25.25,
   "90일": 72.82
  },
  "이동평균": {
   "MA20": 5e-06,
   "MA60": 4e-06,
   "MA120": 4e-06
  },
  "종가와 이평선 거리(%)": {
   "MA20": 4.95,
   "MA60": 15.91,
   "MA120": 34.38
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 103
  },
  "RSI14": 57.6,
  "ATR14(%)": 10.43,
  "거래량(20일 평균 대비 배수)": 0.68,
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
  "기준일": "2026-11-09",
  "등락률(%)": {
   "1일": 5.98,
   "7일": 6.61,
   "30일": 2.9,
   "90일": 21.18
  },
  "종가와 이평선 거리(%)": {
   "MA20": 6.43,
   "MA60": 7.74,
   "MA120": 11.29
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 6
  },
  "RSI14": 66.7
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
 "시가총액(USD)": 2220166271,
 "완전희석가치 FDV(USD)": 2220166271,
 "24시간 거래대금(USD)": 594183641,
 "유통량": 420690000000000.0,
 "총발행량": 420690000000000.0,
 "최대발행량": 420690000000000.0,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 2.803e-05,
 "역대 최고가 대비(%)": -81.17095,
 "가격 변화(%)": {
  "7d": 13.02147,
  "30d": 30.80248,
  "1y": -13.28258
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Trump says he knows ‘nothing’ about World Liberty’s UAE ties as Justin Sun challenges filings",
   "요약": "Trump confirmed he co-owns World Liberty, whose UAE ownership could derail Justin Sun’s federal lawsuit over frozen WLFI tokens",
   "시각(UTC)": "11-09 12:37"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin bulls can't rely on ETF flows",
   "요약": "Your day-ahead look for Nov. 9, 2026",
   "시각(UTC)": "11-09 12:30"
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
  "오늘": "29 (Fear)",
  "최근 7일": [
   29,
   28,
   25,
   28,
   50,
   34,
   26
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "MEXC (Futures)": 0.01,
   "Gate (Futures)": 0.01,
   "OKX (Futures)": 0.01,
   "Bitget Futures": 0.01,
   "KCEX (Futures)": 0.01,
   "WhiteBIT Futures": 0.01
  },
  "미결제약정 합계 USD(상위)": 324849392
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 85.71,
  "CoinGecko 인기 검색 코인": [
   "DACITY",
   "AVAX",
   "KNTQ",
   "BTC",
   "ONDO",
   "HYPE",
   "PEARL",
   "NEAR",
   "LIT",
   "INJ",
   "AERO",
   "ETH",
   "XRP",
   "ARB",
   "SUI"
  ],
  "PEPE가 인기 검색에 있음": false
 }
}
```

## QNT

**수집 실패**
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-08",
  "종가": 194.9,
  "등락률(%)": {
   "1일": -0.65,
   "7일": -3.39,
   "30일": -21.5,
   "90일": 235.46
  },
  "이동평균": {
   "MA20": 194.294,
   "MA60": 176.347,
   "MA120": 119.271167
  },
  "종가와 이평선 거리(%)": {
   "MA20": 0.31,
   "MA60": 10.52,
   "MA120": 63.41
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 64
  },
  "RSI14": 49.8,
  "ATR14(%)": 8.92,
  "거래량(20일 평균 대비 배수)": 0.6,
  "30일 최고가": 255.0,
  "30일 최저가": 173.56,
  "최근 10일 종가": [
   192.27,
   201.11,
   201.73,
   194.13,
   192.26,
   204.15,
   188.77,
   194.06,
   196.17,
   194.9
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-09",
  "등락률(%)": {
   "1일": -1.44,
   "7일": 0.05,
   "30일": -2.03,
   "90일": 6.75
  },
  "종가와 이평선 거리(%)": {
   "MA20": 1.69,
   "MA60": 1.58,
   "MA120": 2.55
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 9
  },
  "RSI14": 53.3
 }
}
```

### DIANA 자료 · 기본적 분석 (펀더멘털)

```json
{
 "이름": "Quant",
 "분류": [
  "Infrastructure",
  "Ethereum Ecosystem",
  "Real World Assets (RWA)",
  "Energi Ecosystem",
  "Coinbase 50 Index"
 ],
 "시가총액 순위": 34,
 "시가총액(USD)": 2870264447,
 "완전희석가치 FDV(USD)": 2881368905,
 "24시간 거래대금(USD)": 64333901,
 "유통량": 14556178.164081175,
 "총발행량": 14612493.0,
 "최대발행량": 14612493.0,
 "유통 비율(%)": 99.6,
 "역대 최고가(USD)": 427.42,
 "역대 최고가 대비(%)": -53.86641,
 "가격 변화(%)": {
  "7d": -2.56901,
  "30d": -19.58945,
  "1y": 132.71317
 },
 "소개": "London-based Quant Network is set to revolutionise blockchain technology with the development of their blockchain operating system Overledger. The experienced team are determined to fulfil the original vision of the internet by creating an open trusted network for people, machines, and data to operate securely and safely.\n\nOverledger -the first interoperable blockchain operating system that facili"
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "QNT 관련 기사": [],
 "시장 전반 기사": [
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Trump says he knows ‘nothing’ about World Liberty’s UAE ties as Justin Sun challenges filings",
   "요약": "Trump confirmed he co-owns World Liberty, whose UAE ownership could derail Justin Sun’s federal lawsuit over frozen WLFI tokens",
   "시각(UTC)": "11-09 12:37"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin bulls can't rely on ETF flows",
   "요약": "Your day-ahead look for Nov. 9, 2026",
   "시각(UTC)": "11-09 12:30"
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
  "오늘": "29 (Fear)",
  "최근 7일": [
   29,
   28,
   25,
   28,
   50,
   34,
   26
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "OrangeX Futures": 0.01,
   "Binance (Futures)": 0.01,
   "WEEX (Futures)": 0.0001,
   "Bybit (Futures)": 0.01,
   "MEXC (Futures)": 0.01,
   "Toobit Futures": 0.01
  },
  "미결제약정 합계 USD(상위)": 120181944
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 95.65,
  "CoinGecko 인기 검색 코인": [
   "DACITY",
   "AVAX",
   "KNTQ",
   "BTC",
   "ONDO",
   "HYPE",
   "PEARL",
   "NEAR",
   "LIT",
   "INJ",
   "AERO",
   "ETH",
   "XRP",
   "ARB",
   "SUI"
  ],
  "QNT가 인기 검색에 있음": false
 }
}
```

## AI

**수집 실패**
- DIANA: ValueError: CoinGecko에서 AI을 찾지 못했습니다
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15
- VIBE/군중 심리(CoinGecko): ValueError: CoinGecko에서 AI을 찾지 못했습니다

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-08",
  "종가": 0.015,
  "등락률(%)": {
   "1일": -5.66,
   "7일": -15.73,
   "30일": -25.74,
   "90일": -15.25
  },
  "이동평균": {
   "MA20": 0.01813,
   "MA60": 0.018788,
   "MA120": 0.018658
  },
  "종가와 이평선 거리(%)": {
   "MA20": -17.26,
   "MA60": -20.16,
   "MA120": -19.61
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 5
  },
  "RSI14": 23.7,
  "ATR14(%)": 7.71,
  "거래량(20일 평균 대비 배수)": 0.03,
  "30일 최고가": 0.0233,
  "30일 최저가": 0.0147,
  "최근 10일 종가": [
   0.0178,
   0.0179,
   0.0178,
   0.0174,
   0.0175,
   0.0173,
   0.016,
   0.0161,
   0.0159,
   0.015
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-09",
  "등락률(%)": {
   "1일": 1.99,
   "7일": -1.91,
   "30일": -12.99,
   "90일": -20.62
  },
  "종가와 이평선 거리(%)": {
   "MA20": -2.13,
   "MA60": -8.62,
   "MA120": -15.16
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 64
  },
  "RSI14": 41.5
 }
}
```

### DIANA 자료 · 기본적 분석 (펀더멘털)

```json
{
 "오류": "ValueError: CoinGecko에서 AI을 찾지 못했습니다"
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "AI 관련 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Google’s AI chip push adds more pressure on Nvidia",
   "요약": "Google’s specialised AI chips threaten greater competition as Nvidia faces a leadership investigation.",
   "시각(UTC)": "11-09 15:20"
  },
  {
   "출처": "CoinDesk",
   "제목": "SpaceX proposes a $24 billion Texas supercomputer and a gas plant",
   "요약": "The $24 billion project, which includes an AI supercomputer in Texas with its own gas-fired power plant, is about 17 times the value of SpaceX's bitcoin holdings.",
   "시각(UTC)": "11-09 06:54"
  },
  {
   "출처": "Decrypt",
   "제목": "Microsoft-Backed Space and Time Launches Platform to Let AI Agents Verify Private Data",
   "요약": "Space and Time Enterprise uses Proof of SQL to prove calculations on private business data without exposing the records to AI agents.",
   "시각(UTC)": "11-09 13:01"
  },
  {
   "출처": "Decrypt",
   "제목": "AI Chip Stocks Bounce After Global Rout—But Is the Bubble Starting to Burst?",
   "요약": "A Friday rebound offered relief after a historic selloff. The question now is whether politics and mounting debt could turn an AI correction into something much worse.",
   "시각(UTC)": "11-07 16:01"
  }
 ],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "A Bitcoin block just neared a 2015 transaction record, but paid only $180 in fees",
   "요약": "The AntPool block came within 984 transactions of Bitcoin’s 2015 record, even as fees made up less than 0.1% of the miner’s payout.",
   "시각(UTC)": "11-09 16:19"
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
   "제목": "Bitcoin bulls can't rely on ETF flows",
   "요약": "Your day-ahead look for Nov. 9, 2026",
   "시각(UTC)": "11-09 12:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "Nvidia-led tech selloff weighs on crypto majors",
   "요약": "Only five of the top 100 cryptocurrencies by market value are up 1% or more over the past 24 hours. That is the state of the market today.",
   "시각(UTC)": "11-09 11:42"
  },
  {
   "출처": "CoinDesk",
   "제목": "Zcash developers want 20-second blocks just days after major speed upgrade",
   "요약": "Early data shows Zcash's orphan-block rate holding close to pre-upgrade levels despite blocks arriving three times faster, encouraging developers to push for another reduction.",
   "시각(UTC)": "11-09 10:52"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "29 (Fear)",
  "최근 7일": [
   29,
   28,
   25,
   28,
   50,
   34,
   26
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "OKX (Futures)": -0.0036,
   "OrangeX Futures": 0.01,
   "Lighter": 0.0012,
   "Aster (Futures)": 0.0013,
   "Robinhood Chain Lighter (Futures)": 0.0012
  },
  "미결제약정 합계 USD(상위)": 1052872
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "오류": "ValueError: CoinGecko에서 AI을 찾지 못했습니다"
 }
}
```
