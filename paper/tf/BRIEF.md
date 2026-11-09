# TF팀 회의 자료 (2026-11-09 13:41 KST)

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
   "1일": 0.0,
   "7일": -1.34,
   "30일": -2.15,
   "90일": -7.43
  },
  "종가와 이평선 거리(%)": {
   "MA20": -1.27,
   "MA60": -3.08,
   "MA120": -5.49
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
 "이름": "Bitcoin",
 "분류": [
  "Smart Contract Platform",
  "Layer 1 (L1)",
  "FTX Holdings",
  "Proof of Work (PoW)",
  "Bitcoin Ecosystem"
 ],
 "시가총액 순위": 1,
 "시가총액(USD)": 1506682509196,
 "완전희석가치 FDV(USD)": 1506682509196,
 "24시간 거래대금(USD)": 20612534956,
 "유통량": 20109740.0,
 "총발행량": 20109740.0,
 "최대발행량": 21000000.0,
 "유통 비율(%)": 95.8,
 "역대 최고가(USD)": 126080,
 "역대 최고가 대비(%)": -40.57682,
 "가격 변화(%)": {
  "7d": -4.62834,
  "30d": -9.21911,
  "1y": -26.29191
 },
 "소개": "Bitcoin is the world's first decentralized cryptocurrency, created in 2009 by the pseudonymous Satoshi Nakamoto. It enables peer-to-peer electronic cash transactions without intermediaries like banks or governments, operating on a blockchain secured by Proof of Work mining and the SHA-256 cryptographic algorithm. \n\nWith a fixed supply cap of 21 million coins and programmatic halvings every four ye",
 "체인 TVL (DefiLlama)": {
  "체인": "Bitcoin",
  "TVL(USD)": 3967440983
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "BTC 관련 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin drops, then pops as Nvidia cheating scandal and failed Iran talks trigger volatility",
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
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin flatlines under $76,000 as stock bounce loses steam into the close",
   "요약": "The Nasdaq gained just 1.1%, while the S&P 500 only edged higher, and the DJIA lost more ground.",
   "시각(UTC)": "11-06 11:58"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin steadies after AI-led selloff as eyes turn to latest U.S. jobs figures",
   "요약": "Bitcoin bounced from around $75,200 after Thursday’s AI-led selloff, which drove more than $1 billion in liquidations, as traders await the U.S. jobs report.",
   "시각(UTC)": "11-06 11:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin recovers $76,000 level as ETFs shed $430 million after tech rout",
   "요약": "Bitcoin recovered above $76,000 Friday after dropping below that level during Thursday's tech-driven market rout.",
   "시각(UTC)": "11-06 09:53"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Vitalik ‘pivots’ ETH to store of value, crypto suffers after US midterms: Hodler’s Digest",
   "요약": "Vitalik Buterin wants Ethereum to embrace a store of value narrative, upsetting Bitcoin maxis. The crypto industry faces an uncertain future following the US elections.",
   "시각(UTC)": "11-08 22:59"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Here’s what happened in crypto today",
   "요약": "Need to know what happened in crypto today? Here is the latest news on daily trends and events impacting Bitcoin price, blockchain, DeFi, Web3 and crypto regulation.",
   "시각(UTC)": "11-08 13:33"
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
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin price dips under $75K as crypto markets miss tech-stock rebound",
   "요약": "BTC price action stayed weak after US nonfarm payrolls data significantly beat forecasts, increasing bets of a December interest-rate hike.",
   "시각(UTC)": "11-06 17:49"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin holds $75K as AI regulation fears see KOSPI halted after 8% crash",
   "요약": "Bitcoin consolidated as fears over US AI regulation spread to Asia, causing South Korea to announce measures to calm stock-market volatility.",
   "시각(UTC)": "11-06 11:16"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin, Ether ETFs post $530M outflows as election gains evaporate",
   "요약": "US spot Bitcoin and Ether ETFs shed a combined $530 million Thursday as Bitcoin fell below $76,000 and US stocks tumbled.",
   "시각(UTC)": "11-06 08:19"
  },
  {
   "출처": "Decrypt",
   "제목": "This Bitcoin Developer’s Idea Would Make Quantum Attacks a Losing Bet",
   "요약": "Cory Fields wants future quantum attackers to post Bitcoin as collateral before touching vulnerable wallets, giving prepared owners a chance to recover their coins and collect a potentially costly penalty.",
   "시각(UTC)": "11-08 14:01"
  },
  {
   "출처": "Decrypt",
   "제목": "Bitcoin ETFs Bleed $430 Million as Tech Rout Tests Wall Street Buyers",
   "요약": "Fidelity and BlackRock led Thursday's Bitcoin ETF withdrawals as a technology-stock selloff rattled risk assets.",
   "시각(UTC)": "11-06 18:36"
  }
 ],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "What the election results mean for crypto: State of Crypto",
   "요약": "Democrats had an astoundingly good night, smashing all expectations. Is that actually bad news for the industry?",
   "시각(UTC)": "11-08 19:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "Stablecoin growth has stalled. The payments boom hasn't",
   "요약": "Stablecoin supply has barely grown this year, even as payments using the tokens surge. Circle's latest earnings offer another example of the divergence between dollars outstanding and activity on blockchain networks.",
   "시각(UTC)": "11-08 19:16"
  },
  {
   "출처": "CoinDesk",
   "제목": "Binance users in some European countries told to pull crypto before fees kick in, with accounts closing by year end",
   "요약": "Affected accounts are reportedly set to close on Dec. 31. Users in Spain, France, and Poland say they've received similar notices.",
   "시각(UTC)": "11-07 19:13"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. Treasury moves to cut off crypto exchange MEXC over $16 billion in alleged illicit flows",
   "요약": "Treasury billed the move as part of its campaign against Iran, but the order rests on MEXC's alleged role in Russian illicit finance.",
   "시각(UTC)": "11-07 17:36"
  },
  {
   "출처": "CoinDesk",
   "제목": "Gnosis Pay breach exposes card numbers, home addresses and linked crypto wallets",
   "요약": "One user said the exposed data tied his home address and card number to every crypto wallet linked to his account, raising the risk of targeted scams.",
   "시각(UTC)": "11-07 16:51"
  },
  {
   "출처": "CoinDesk",
   "제목": "Apple, Meta reject OKX–ICE tokenized stock plans, leaving crypto firms as the ones to watch",
   "요약": "Strategy, Coinbase, Circle and Robinhood are among six companies from the venture’s initial selection with no disclosed objection, after 90% of issuers opted out.",
   "시각(UTC)": "11-06 20:09"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. prediction markets regulator issues demand that clashes directly with courts",
   "요약": "The Commodity Futures Trading Commission said regulated exchanges can't cut off customers state-by-state, but firms like Kalshi are under court orders to do so.",
   "시각(UTC)": "11-06 17:42"
  },
  {
   "출처": "CoinDesk",
   "제목": "The crypto industry has found new ways to grow. Making money from them is another story",
   "요약": "Coinbase, Robinhood and Circle are expanding into stablecoins, payments and prediction markets, but their latest earnings show how hard it is to escape crypto's boom-and-bust cycles.",
   "시각(UTC)": "11-06 15:26"
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
   "Bybit (Futures)": 0.01,
   "MEXC (Futures)": 0.01,
   "Gate (Futures)": 0.0073,
   "WEEX (Futures)": 0.0,
   "Tapbit (Futures)": 0.01
  },
  "미결제약정 합계 USD(상위)": 28347904440
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 67.94,
  "CoinGecko 인기 검색 코인": [
   "PENGU",
   "BTC",
   "HYPE",
   "LIT",
   "PEPE",
   "JCT",
   "ZEC",
   "PEARL",
   "XRP",
   "PUMP",
   "PI",
   "TRUMP",
   "INJ",
   "PONS",
   "NEAR"
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
   "1일": 0.63,
   "7일": -4.44,
   "30일": -4.83,
   "90일": -9.4
  },
  "종가와 이평선 거리(%)": {
   "MA20": -3.92,
   "MA60": -5.6,
   "MA120": -7.69
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 6
  },
  "RSI14": 27.5
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
 "시가총액(USD)": 261471896432,
 "완전희석가치 FDV(USD)": 261471896614,
 "24시간 거래대금(USD)": 10376016254,
 "유통량": 122203846.69715354,
 "총발행량": 122203846.78214265,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 4946.05,
 "역대 최고가 대비(%)": -56.74045,
 "가격 변화(%)": {
  "7d": -7.25217,
  "30d": -14.05632,
  "1y": -36.59224
 },
 "소개": "Ethereum is a global, open-source platform for decentralized applications. In other words, it is a decentralized blockchain platform that enables developers to build and deploy smart contracts and applications without central authority control. Unlike Bitcoin, which primarily functions as digital currency, Ethereum operates as a programmable global computer where developers can create any type of ",
 "체인 TVL (DefiLlama)": {
  "체인": "Ethereum",
  "TVL(USD)": 42245904417
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "ETH 관련 기사": [
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
  },
  {
   "출처": "Cointelegraph",
   "제목": "Ethereum devs won’t fork Glamsterdam on Hoodi until smart contract risks resolved",
   "요약": "Ethereum developers are investigating concerns tied to eight smart contract invariants tied to Glamsterdam’s EIP-8037 and EIP-8038.",
   "시각(UTC)": "11-06 13:23"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin, Ether ETFs post $530M outflows as election gains evaporate",
   "요약": "US spot Bitcoin and Ether ETFs shed a combined $530 million Thursday as Bitcoin fell below $76,000 and US stocks tumbled.",
   "시각(UTC)": "11-06 08:19"
  },
  {
   "출처": "Decrypt",
   "제목": "$3.1B in Stolen Binance Crypto Has Yet to Be Laundered: Elliptic",
   "요약": "The attackers have used more than 20,000 wallets on 16 blockchains so far, but the bulk of the stolen ETH and Bitcoin hasn't moved.",
   "시각(UTC)": "11-06 14:04"
  }
 ],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin drops, then pops as Nvidia cheating scandal and failed Iran talks trigger volatility",
   "요약": "Volatile price action has once again liquidated leveraged bullish plays worth millions.",
   "시각(UTC)": "11-09 03:21"
  },
  {
   "출처": "CoinDesk",
   "제목": "What the election results mean for crypto: State of Crypto",
   "요약": "Democrats had an astoundingly good night, smashing all expectations. Is that actually bad news for the industry?",
   "시각(UTC)": "11-08 19:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "Stablecoin growth has stalled. The payments boom hasn't",
   "요약": "Stablecoin supply has barely grown this year, even as payments using the tokens surge. Circle's latest earnings offer another example of the divergence between dollars outstanding and activity on blockchain networks.",
   "시각(UTC)": "11-08 19:16"
  },
  {
   "출처": "CoinDesk",
   "제목": "These Finland homes get free heat from bitcoin miners (as long as BTC stays above $70,000)",
   "요약": "A Finnish startup has 30 bitcoin mining systems working as central heating, and at today’s prices each one earns slightly more than the electricity it burns.",
   "시각(UTC)": "11-08 12:55"
  },
  {
   "출처": "CoinDesk",
   "제목": "Binance users in some European countries told to pull crypto before fees kick in, with accounts closing by year end",
   "요약": "Affected accounts are reportedly set to close on Dec. 31. Users in Spain, France, and Poland say they've received similar notices.",
   "시각(UTC)": "11-07 19:13"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. Treasury moves to cut off crypto exchange MEXC over $16 billion in alleged illicit flows",
   "요약": "Treasury billed the move as part of its campaign against Iran, but the order rests on MEXC's alleged role in Russian illicit finance.",
   "시각(UTC)": "11-07 17:36"
  },
  {
   "출처": "CoinDesk",
   "제목": "Gnosis Pay breach exposes card numbers, home addresses and linked crypto wallets",
   "요약": "One user said the exposed data tied his home address and card number to every crypto wallet linked to his account, raising the risk of targeted scams.",
   "시각(UTC)": "11-07 16:51"
  },
  {
   "출처": "CoinDesk",
   "제목": "Apple, Meta reject OKX–ICE tokenized stock plans, leaving crypto firms as the ones to watch",
   "요약": "Strategy, Coinbase, Circle and Robinhood are among six companies from the venture’s initial selection with no disclosed objection, after 90% of issuers opted out.",
   "시각(UTC)": "11-06 20:09"
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
   "Binance (Futures)": -0.0084,
   "WEEX (Futures)": 0.0001,
   "CoinW (Futures)": -0.0057,
   "MEXC (Futures)": -0.0055,
   "Hyperliquid (Futures)": -0.0024
  },
  "미결제약정 합계 USD(상위)": 17265017988
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 71.11,
  "CoinGecko 인기 검색 코인": [
   "PENGU",
   "BTC",
   "HYPE",
   "LIT",
   "PEPE",
   "JCT",
   "ZEC",
   "PEARL",
   "XRP",
   "PUMP",
   "PI",
   "TRUMP",
   "INJ",
   "PONS",
   "NEAR"
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
   "1일": 2.22,
   "7일": 4.11,
   "30일": 5.19,
   "90일": 12.92
  },
  "종가와 이평선 거리(%)": {
   "MA20": 2.13,
   "MA60": 2.7,
   "MA120": 6.51
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 3
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
 "시가총액(USD)": 2122915253,
 "완전희석가치 FDV(USD)": 2122915253,
 "24시간 거래대금(USD)": 409202702,
 "유통량": 420690000000000.0,
 "총발행량": 420690000000000.0,
 "최대발행량": 420690000000000.0,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 2.803e-05,
 "역대 최고가 대비(%)": -81.99573,
 "가격 변화(%)": {
  "7d": 2.72544,
  "30d": 25.25727,
  "1y": -14.01678
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
   "제목": "Bitcoin drops, then pops as Nvidia cheating scandal and failed Iran talks trigger volatility",
   "요약": "Volatile price action has once again liquidated leveraged bullish plays worth millions.",
   "시각(UTC)": "11-09 03:21"
  },
  {
   "출처": "CoinDesk",
   "제목": "What the election results mean for crypto: State of Crypto",
   "요약": "Democrats had an astoundingly good night, smashing all expectations. Is that actually bad news for the industry?",
   "시각(UTC)": "11-08 19:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "Stablecoin growth has stalled. The payments boom hasn't",
   "요약": "Stablecoin supply has barely grown this year, even as payments using the tokens surge. Circle's latest earnings offer another example of the divergence between dollars outstanding and activity on blockchain networks.",
   "시각(UTC)": "11-08 19:16"
  },
  {
   "출처": "CoinDesk",
   "제목": "These Finland homes get free heat from bitcoin miners (as long as BTC stays above $70,000)",
   "요약": "A Finnish startup has 30 bitcoin mining systems working as central heating, and at today’s prices each one earns slightly more than the electricity it burns.",
   "시각(UTC)": "11-08 12:55"
  },
  {
   "출처": "CoinDesk",
   "제목": "Binance users in some European countries told to pull crypto before fees kick in, with accounts closing by year end",
   "요약": "Affected accounts are reportedly set to close on Dec. 31. Users in Spain, France, and Poland say they've received similar notices.",
   "시각(UTC)": "11-07 19:13"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. Treasury moves to cut off crypto exchange MEXC over $16 billion in alleged illicit flows",
   "요약": "Treasury billed the move as part of its campaign against Iran, but the order rests on MEXC's alleged role in Russian illicit finance.",
   "시각(UTC)": "11-07 17:36"
  },
  {
   "출처": "CoinDesk",
   "제목": "Gnosis Pay breach exposes card numbers, home addresses and linked crypto wallets",
   "요약": "One user said the exposed data tied his home address and card number to every crypto wallet linked to his account, raising the risk of targeted scams.",
   "시각(UTC)": "11-07 16:51"
  },
  {
   "출처": "CoinDesk",
   "제목": "Apple, Meta reject OKX–ICE tokenized stock plans, leaving crypto firms as the ones to watch",
   "요약": "Strategy, Coinbase, Circle and Robinhood are among six companies from the venture’s initial selection with no disclosed objection, after 90% of issuers opted out.",
   "시각(UTC)": "11-06 20:09"
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
   "Bitget Futures": 0.0054,
   "KCEX (Futures)": 0.01,
   "WhiteBIT Futures": 0.01
  },
  "미결제약정 합계 USD(상위)": 291596598
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 87.5,
  "CoinGecko 인기 검색 코인": [
   "PENGU",
   "BTC",
   "HYPE",
   "LIT",
   "PEPE",
   "JCT",
   "ZEC",
   "PEARL",
   "XRP",
   "PUMP",
   "PI",
   "TRUMP",
   "INJ",
   "PONS",
   "NEAR"
  ],
  "PEPE가 인기 검색에 있음": true
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
   "1일": 1.91,
   "7일": 1.25,
   "30일": 4.71,
   "90일": 8.48
  },
  "종가와 이평선 거리(%)": {
   "MA20": 1.68,
   "MA60": 0.97,
   "MA120": 1.86
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 6
  },
  "RSI14": 52.6
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
 "시가총액 순위": 33,
 "시가총액(USD)": 2900022827,
 "완전희석가치 FDV(USD)": 2911242415,
 "24시간 거래대금(USD)": 47574621,
 "유통량": 14556178.164081175,
 "총발행량": 14612493.0,
 "최대발행량": 14612493.0,
 "유통 비율(%)": 99.6,
 "역대 최고가(USD)": 427.42,
 "역대 최고가 대비(%)": -53.39103,
 "가격 변화(%)": {
  "7d": -1.18684,
  "30d": -19.30686,
  "1y": 144.79186
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
   "제목": "Bitcoin drops, then pops as Nvidia cheating scandal and failed Iran talks trigger volatility",
   "요약": "Volatile price action has once again liquidated leveraged bullish plays worth millions.",
   "시각(UTC)": "11-09 03:21"
  },
  {
   "출처": "CoinDesk",
   "제목": "What the election results mean for crypto: State of Crypto",
   "요약": "Democrats had an astoundingly good night, smashing all expectations. Is that actually bad news for the industry?",
   "시각(UTC)": "11-08 19:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "Stablecoin growth has stalled. The payments boom hasn't",
   "요약": "Stablecoin supply has barely grown this year, even as payments using the tokens surge. Circle's latest earnings offer another example of the divergence between dollars outstanding and activity on blockchain networks.",
   "시각(UTC)": "11-08 19:16"
  },
  {
   "출처": "CoinDesk",
   "제목": "These Finland homes get free heat from bitcoin miners (as long as BTC stays above $70,000)",
   "요약": "A Finnish startup has 30 bitcoin mining systems working as central heating, and at today’s prices each one earns slightly more than the electricity it burns.",
   "시각(UTC)": "11-08 12:55"
  },
  {
   "출처": "CoinDesk",
   "제목": "Binance users in some European countries told to pull crypto before fees kick in, with accounts closing by year end",
   "요약": "Affected accounts are reportedly set to close on Dec. 31. Users in Spain, France, and Poland say they've received similar notices.",
   "시각(UTC)": "11-07 19:13"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. Treasury moves to cut off crypto exchange MEXC over $16 billion in alleged illicit flows",
   "요약": "Treasury billed the move as part of its campaign against Iran, but the order rests on MEXC's alleged role in Russian illicit finance.",
   "시각(UTC)": "11-07 17:36"
  },
  {
   "출처": "CoinDesk",
   "제목": "Gnosis Pay breach exposes card numbers, home addresses and linked crypto wallets",
   "요약": "One user said the exposed data tied his home address and card number to every crypto wallet linked to his account, raising the risk of targeted scams.",
   "시각(UTC)": "11-07 16:51"
  },
  {
   "출처": "CoinDesk",
   "제목": "Apple, Meta reject OKX–ICE tokenized stock plans, leaving crypto firms as the ones to watch",
   "요약": "Strategy, Coinbase, Circle and Robinhood are among six companies from the venture’s initial selection with no disclosed objection, after 90% of issuers opted out.",
   "시각(UTC)": "11-06 20:09"
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
   "OrangeX Futures": -0.01,
   "Binance (Futures)": 0.01,
   "WEEX (Futures)": 0.0001,
   "MEXC (Futures)": 0.01,
   "Bybit (Futures)": -0.0019,
   "Toobit Futures": 0.01
  },
  "미결제약정 합계 USD(상위)": 106858436
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 83.33,
  "CoinGecko 인기 검색 코인": [
   "PENGU",
   "BTC",
   "HYPE",
   "LIT",
   "PEPE",
   "JCT",
   "ZEC",
   "PEARL",
   "XRP",
   "PUMP",
   "PI",
   "TRUMP",
   "INJ",
   "PONS",
   "NEAR"
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
   "1일": 0.0,
   "7일": -5.66,
   "30일": -11.24,
   "90일": -22.68
  },
  "종가와 이평선 거리(%)": {
   "MA20": -5.54,
   "MA60": -11.69,
   "MA120": -17.8
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 61
  },
  "RSI14": 26.6
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
   "제목": "Bitcoin steadies after AI-led selloff as eyes turn to latest U.S. jobs figures",
   "요약": "Bitcoin bounced from around $75,200 after Thursday’s AI-led selloff, which drove more than $1 billion in liquidations, as traders await the U.S. jobs report.",
   "시각(UTC)": "11-06 11:49"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin holds $75K as AI regulation fears see KOSPI halted after 8% crash",
   "요약": "Bitcoin consolidated as fears over US AI regulation spread to Asia, causing South Korea to announce measures to calm stock-market volatility.",
   "시각(UTC)": "11-06 11:16"
  },
  {
   "출처": "Decrypt",
   "제목": "AI Chip Stocks Bounce After Global Rout—But Is the Bubble Starting to Burst?",
   "요약": "A Friday rebound offered relief after a historic selloff. The question now is whether politics and mounting debt could turn an AI correction into something much worse.",
   "시각(UTC)": "11-07 16:01"
  },
  {
   "출처": "Decrypt",
   "제목": "Crypto Liquidations Top $1 Billion as Bitcoin Tests 11-Week Low",
   "요약": "Bitcoin fell toward $75,500 after AI stocks plunged, and over $1 billion in the crypto derivatives market has been wiped out.",
   "시각(UTC)": "11-06 16:34"
  },
  {
   "출처": "Decrypt",
   "제목": "Anthropic IPO Valuation Could Be Slashed in Half to $1T After AI Stock Rout: Report",
   "요약": "Investors told The Wall Street Journal that the $1.5 trillion target now looks too high, as prediction markets bet on a December listing.",
   "시각(UTC)": "11-06 16:28"
  },
  {
   "출처": "Decrypt",
   "제목": "Tesla to Wind Down Cybertruck Production as Elon Musk Pivots to Robotaxis and AI",
   "요약": "The Tesla CEO said the Texas plant will make room for the Cybercab, as sales of the stainless-steel pickup run far below capacity.",
   "시각(UTC)": "11-06 13:53"
  },
  {
   "출처": "Decrypt",
   "제목": "Morning Minute: Bitcoin Erases Election Rally as AI Stocks Crater",
   "요약": "Thursday marked a massive reversal and historic selloff for AI stocks, and crypto was not immune. What held up the strongest?",
   "시각(UTC)": "11-06 13:29"
  }
 ],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin drops, then pops as Nvidia cheating scandal and failed Iran talks trigger volatility",
   "요약": "Volatile price action has once again liquidated leveraged bullish plays worth millions.",
   "시각(UTC)": "11-09 03:21"
  },
  {
   "출처": "CoinDesk",
   "제목": "What the election results mean for crypto: State of Crypto",
   "요약": "Democrats had an astoundingly good night, smashing all expectations. Is that actually bad news for the industry?",
   "시각(UTC)": "11-08 19:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "Stablecoin growth has stalled. The payments boom hasn't",
   "요약": "Stablecoin supply has barely grown this year, even as payments using the tokens surge. Circle's latest earnings offer another example of the divergence between dollars outstanding and activity on blockchain networks.",
   "시각(UTC)": "11-08 19:16"
  },
  {
   "출처": "CoinDesk",
   "제목": "These Finland homes get free heat from bitcoin miners (as long as BTC stays above $70,000)",
   "요약": "A Finnish startup has 30 bitcoin mining systems working as central heating, and at today’s prices each one earns slightly more than the electricity it burns.",
   "시각(UTC)": "11-08 12:55"
  },
  {
   "출처": "CoinDesk",
   "제목": "Binance users in some European countries told to pull crypto before fees kick in, with accounts closing by year end",
   "요약": "Affected accounts are reportedly set to close on Dec. 31. Users in Spain, France, and Poland say they've received similar notices.",
   "시각(UTC)": "11-07 19:13"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. Treasury moves to cut off crypto exchange MEXC over $16 billion in alleged illicit flows",
   "요약": "Treasury billed the move as part of its campaign against Iran, but the order rests on MEXC's alleged role in Russian illicit finance.",
   "시각(UTC)": "11-07 17:36"
  },
  {
   "출처": "CoinDesk",
   "제목": "Gnosis Pay breach exposes card numbers, home addresses and linked crypto wallets",
   "요약": "One user said the exposed data tied his home address and card number to every crypto wallet linked to his account, raising the risk of targeted scams.",
   "시각(UTC)": "11-07 16:51"
  },
  {
   "출처": "CoinDesk",
   "제목": "Apple, Meta reject OKX–ICE tokenized stock plans, leaving crypto firms as the ones to watch",
   "요약": "Strategy, Coinbase, Circle and Robinhood are among six companies from the venture’s initial selection with no disclosed objection, after 90% of issuers opted out.",
   "시각(UTC)": "11-06 20:09"
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
   "OKX (Futures)": 0.005,
   "OrangeX Futures": 0.01,
   "Lighter": 0.0012,
   "Aster (Futures)": 0.0013,
   "Robinhood Chain Lighter (Futures)": 0.0012
  },
  "미결제약정 합계 USD(상위)": 1029812
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "오류": "ValueError: CoinGecko에서 AI을 찾지 못했습니다"
 }
}
```
