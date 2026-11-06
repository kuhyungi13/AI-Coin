# TF팀 회의 자료 (2026-11-07 08:17 KST)

GitHub Actions가 무료 공개 API로 모은 자료입니다. 회의 진행 방법은 `aicoin/tf_team/PLAYBOOK.md`.
자료에 없는 숫자는 쓰지 않습니다. 실패한 자료는 아래 '수집 실패'에 있습니다.

분석 대상: BTC, ETH, PEPE, INJ, INTCB

**지금까지 승률** ACE 40.9% (9/22), 채점 대기 0개 · 자세히는 `paper/tf/SCOREBOARD.md`, 교훈은 `aicoin/tf_team/LESSONS.md`

**TRAINER 모의 계좌** 총자산 10,013.80 USDT (+0.14%), 보유 PEPE · 자세히는 `paper/tf/trainer/TRAINER.md`

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
  "기준일": "2026-11-06",
  "등락률(%)": {
   "1일": 0.03,
   "7일": -0.19,
   "30일": -2.46,
   "90일": -6.88
  },
  "종가와 이평선 거리(%)": {
   "MA20": -2.45,
   "MA60": -3.12,
   "MA120": -5.04
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 78
  },
  "RSI14": 38.3
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
 "시가총액(USD)": 1524820185393,
 "완전희석가치 FDV(USD)": 1524847941054,
 "24시간 거래대금(USD)": 30551339778,
 "유통량": 20107040.0,
 "총발행량": 20107406.0,
 "최대발행량": 21000000.0,
 "유통 비율(%)": 95.7,
 "역대 최고가(USD)": 126080,
 "역대 최고가 대비(%)": -39.85152,
 "가격 변화(%)": {
  "7d": -1.34849,
  "30d": -8.84647,
  "1y": -25.13901
 },
 "소개": "Bitcoin is the world's first decentralized cryptocurrency, created in 2009 by the pseudonymous Satoshi Nakamoto. It enables peer-to-peer electronic cash transactions without intermediaries like banks or governments, operating on a blockchain secured by Proof of Work mining and the SHA-256 cryptographic algorithm. \n\nWith a fixed supply cap of 21 million coins and programmatic halvings every four ye",
 "체인 TVL (DefiLlama)": {
  "체인": "Bitcoin",
  "TVL(USD)": 4041541659
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "BTC 관련 기사": [
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
   "출처": "Cointelegraph",
   "제목": "Here’s what happened in crypto today",
   "요약": "Need to know what happened in crypto today? Here is the latest news on daily trends and events impacting Bitcoin price, blockchain, DeFi, Web3 and crypto regulation.",
   "시각(UTC)": "11-06 22:00"
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
   "출처": "Cointelegraph",
   "제목": "Core Scientific to quit Bitcoin mining by year-end as AI business surges",
   "요약": "The former Bitcoin mining heavyweight plans to become a pure-play data center provider in 2027, with mining now accounting for just 7.5% of quarterly revenue.",
   "시각(UTC)": "11-06 00:19"
  }
 ],
 "시장 전반 기사": [
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Thailand moves to block Bitget as crypto exchange's local acquisition faces uncertainty",
   "요약": "Thailand’s SEC filed a criminal complaint against Bitget’s operator, alleging it ran an unlicensed crypto exchange for Thai users from 2022 to 2025.",
   "시각(UTC)": "11-06 14:33"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. added 165,000 jobs in October, blowing past 65,000 estimate",
   "요약": "The unemployment rate unexpectedly fell to 4.1%. The strong showing surely puts a December rate hike in play, but next week's inflation numbers and the fate of the stock market could prove more important.",
   "시각(UTC)": "11-06 13:31"
  },
  {
   "출처": "CoinDesk",
   "제목": "Over $1 billion in bullish bets liquidated while ETF flows suggest no help in spot market",
   "요약": "Your day-ahead look for Nov. 6, 2026",
   "시각(UTC)": "11-06 12:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "Greece approves 10% tax on crypto gains and 15% levy on DeFi income",
   "요약": "Investors will have 12 months to declare past crypto gains without late-filing penalties, though questions remain over crypto-to-crypto swaps.",
   "시각(UTC)": "11-06 08:47"
  },
  {
   "출처": "CoinDesk",
   "제목": "Trump-backed World Liberty Financial plans token buyback after 66% year-to-date slide",
   "요약": "The crypto venture may use fees from its USD1 stablecoin reserves to fund token purchases as it seeks to boost governance.",
   "시각(UTC)": "11-06 08:04"
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
   "Binance (Futures)": 0.01,
   "Bybit (Futures)": 0.0077,
   "MEXC (Futures)": 0.01,
   "Gate (Futures)": 0.01,
   "WEEX (Futures)": 0.0001,
   "Tapbit (Futures)": 0.01
  },
  "미결제약정 합계 USD(상위)": 28769046342
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 57.06,
  "CoinGecko 인기 검색 코인": [
   "PENGU",
   "DENIM",
   "PEARL",
   "REBOOT",
   "BTC",
   "HYPE",
   "KNTQ",
   "XRP",
   "AERO",
   "PEPE",
   "INJ",
   "VVV",
   "TAO",
   "LINK",
   "AKE"
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
  "기준일": "2026-11-06",
  "등락률(%)": {
   "1일": 0.23,
   "7일": -0.75,
   "30일": -1.04,
   "90일": -6.34
  },
  "종가와 이평선 거리(%)": {
   "MA20": -3.19,
   "MA60": -2.48,
   "MA120": -4.46
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 10
  },
  "RSI14": 40.4
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
 "시가총액(USD)": 273096839452,
 "완전희석가치 FDV(USD)": 273096839452,
 "24시간 거래대금(USD)": 11059977428,
 "유통량": 122194930.21672837,
 "총발행량": 122194930.21672837,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 4946.05,
 "역대 최고가 대비(%)": -54.81385,
 "가격 변화(%)": {
  "7d": 0.06065,
  "30d": -12.99954,
  "1y": -32.59506
 },
 "소개": "Ethereum is a global, open-source platform for decentralized applications. In other words, it is a decentralized blockchain platform that enables developers to build and deploy smart contracts and applications without central authority control. Unlike Bitcoin, which primarily functions as digital currency, Ethereum operates as a programmable global computer where developers can create any type of ",
 "체인 TVL (DefiLlama)": {
  "체인": "Ethereum",
  "TVL(USD)": 43130120832
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
   "출처": "Cointelegraph",
   "제목": "Europe’s largest asset manager Amundi tokenizes equity index fund on Ethereum",
   "요약": "The new share class offers blockchain-based exposure to an index tracking 600 companies across European markets.",
   "시각(UTC)": "11-05 18:09"
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Thailand moves to block Bitget as crypto exchange's local acquisition faces uncertainty",
   "요약": "Thailand’s SEC filed a criminal complaint against Bitget’s operator, alleging it ran an unlicensed crypto exchange for Thai users from 2022 to 2025.",
   "시각(UTC)": "11-06 14:33"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. added 165,000 jobs in October, blowing past 65,000 estimate",
   "요약": "The unemployment rate unexpectedly fell to 4.1%. The strong showing surely puts a December rate hike in play, but next week's inflation numbers and the fate of the stock market could prove more important.",
   "시각(UTC)": "11-06 13:31"
  },
  {
   "출처": "CoinDesk",
   "제목": "Over $1 billion in bullish bets liquidated while ETF flows suggest no help in spot market",
   "요약": "Your day-ahead look for Nov. 6, 2026",
   "시각(UTC)": "11-06 12:30"
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
   "Binance (Futures)": 0.0079,
   "CoinW (Futures)": 0.01,
   "WEEX (Futures)": 0.0001,
   "MEXC (Futures)": 0.01,
   "Hyperliquid (Futures)": 0.0013
  },
  "미결제약정 합계 USD(상위)": 19419418946
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 85.29,
  "CoinGecko 인기 검색 코인": [
   "PENGU",
   "DENIM",
   "PEARL",
   "REBOOT",
   "BTC",
   "HYPE",
   "KNTQ",
   "XRP",
   "AERO",
   "PEPE",
   "INJ",
   "VVV",
   "TAO",
   "LINK",
   "AKE"
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
  "기준일": "2026-11-06",
  "등락률(%)": {
   "1일": -0.39,
   "7일": 7.87,
   "30일": 3.47,
   "90일": 15.23
  },
  "종가와 이평선 거리(%)": {
   "MA20": 2.55,
   "MA60": 2.76,
   "MA120": 9.06
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 1
  },
  "RSI14": 56.9
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
 "시가총액(USD)": 2088745578,
 "완전희석가치 FDV(USD)": 2088745578,
 "24시간 거래대금(USD)": 413805742,
 "유통량": 420690000000000.0,
 "총발행량": 420690000000000.0,
 "최대발행량": 420690000000000.0,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 2.803e-05,
 "역대 최고가 대비(%)": -82.28552,
 "가격 변화(%)": {
  "7d": -0.40756,
  "30d": 21.62967,
  "1y": -10.39872
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Thailand moves to block Bitget as crypto exchange's local acquisition faces uncertainty",
   "요약": "Thailand’s SEC filed a criminal complaint against Bitget’s operator, alleging it ran an unlicensed crypto exchange for Thai users from 2022 to 2025.",
   "시각(UTC)": "11-06 14:33"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. added 165,000 jobs in October, blowing past 65,000 estimate",
   "요약": "The unemployment rate unexpectedly fell to 4.1%. The strong showing surely puts a December rate hike in play, but next week's inflation numbers and the fate of the stock market could prove more important.",
   "시각(UTC)": "11-06 13:31"
  },
  {
   "출처": "CoinDesk",
   "제목": "Over $1 billion in bullish bets liquidated while ETF flows suggest no help in spot market",
   "요약": "Your day-ahead look for Nov. 6, 2026",
   "시각(UTC)": "11-06 12:30"
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
  "미결제약정 합계 USD(상위)": 308782382
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 87.5,
  "CoinGecko 인기 검색 코인": [
   "PENGU",
   "DENIM",
   "PEARL",
   "REBOOT",
   "BTC",
   "HYPE",
   "KNTQ",
   "XRP",
   "AERO",
   "PEPE",
   "INJ",
   "VVV",
   "TAO",
   "LINK",
   "AKE"
  ],
  "PEPE가 인기 검색에 있음": true
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
  "기준일": "2026-11-06",
  "등락률(%)": {
   "1일": 1.47,
   "7일": 6.56,
   "30일": 19.4,
   "90일": 4.93
  },
  "종가와 이평선 거리(%)": {
   "MA20": 6.73,
   "MA60": 11.43,
   "MA120": 7.15
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 5
  },
  "RSI14": 65.4
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
 "시가총액 순위": 80,
 "시가총액(USD)": 834262754,
 "완전희석가치 FDV(USD)": 834262754,
 "24시간 거래대금(USD)": 116152340,
 "유통량": 100000000.0,
 "총발행량": 100000000.0,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 52.62,
 "역대 최고가 대비(%)": -84.14572,
 "가격 변화(%)": {
  "7d": 17.26987,
  "30d": 12.17187,
  "1y": 31.67666
 },
 "소개": "Injective is an interoperable Layer 1 blockchain designed for DeFi applications. It provides developers with on-chain financial infrastructure modules to build dApps such as decentralized exchanges, prediction markets, and lending protocols. Its decentralized cross-chain bridging infrastructure offers compatibility with most blockchains, including EVM chains like Ethereum and non-EVM chains like S",
 "체인 TVL (DefiLlama)": {
  "체인": "Injective",
  "TVL(USD)": 23176519
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Thailand moves to block Bitget as crypto exchange's local acquisition faces uncertainty",
   "요약": "Thailand’s SEC filed a criminal complaint against Bitget’s operator, alleging it ran an unlicensed crypto exchange for Thai users from 2022 to 2025.",
   "시각(UTC)": "11-06 14:33"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. added 165,000 jobs in October, blowing past 65,000 estimate",
   "요약": "The unemployment rate unexpectedly fell to 4.1%. The strong showing surely puts a December rate hike in play, but next week's inflation numbers and the fate of the stock market could prove more important.",
   "시각(UTC)": "11-06 13:31"
  },
  {
   "출처": "CoinDesk",
   "제목": "Over $1 billion in bullish bets liquidated while ETF flows suggest no help in spot market",
   "요약": "Your day-ahead look for Nov. 6, 2026",
   "시각(UTC)": "11-06 12:30"
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
   "OrangeX Futures": -0.0253,
   "Binance (Futures)": 0.01,
   "Gate (Futures)": 0.01,
   "MEXC (Futures)": 0.0206,
   "Bybit (Futures)": 0.01
  },
  "미결제약정 합계 USD(상위)": 315416567
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 94.29,
  "CoinGecko 인기 검색 코인": [
   "PENGU",
   "DENIM",
   "PEARL",
   "REBOOT",
   "BTC",
   "HYPE",
   "KNTQ",
   "XRP",
   "AERO",
   "PEPE",
   "INJ",
   "VVV",
   "TAO",
   "LINK",
   "AKE"
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
  "기준일": "2026-11-06",
  "등락률(%)": {
   "1일": 1.97,
   "7일": 6.51,
   "30일": -13.45,
   "90일": -33.39
  },
  "종가와 이평선 거리(%)": {
   "MA20": -0.18,
   "MA60": -16.54,
   "MA120": -27.81
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 44
  },
  "RSI14": 44.2
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
 "시가총액 순위": 343,
 "시가총액(USD)": 70471468,
 "완전희석가치 FDV(USD)": 70471468,
 "24시간 거래대금(USD)": 14400946,
 "유통량": 1243011.50686961,
 "총발행량": 1243011.50686961,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 130.12,
 "역대 최고가 대비(%)": -56.43169,
 "가격 변화(%)": {
  "7d": -12.58901,
  "30d": -49.87597,
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Thailand moves to block Bitget as crypto exchange's local acquisition faces uncertainty",
   "요약": "Thailand’s SEC filed a criminal complaint against Bitget’s operator, alleging it ran an unlicensed crypto exchange for Thai users from 2022 to 2025.",
   "시각(UTC)": "11-06 14:33"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. added 165,000 jobs in October, blowing past 65,000 estimate",
   "요약": "The unemployment rate unexpectedly fell to 4.1%. The strong showing surely puts a December rate hike in play, but next week's inflation numbers and the fate of the stock market could prove more important.",
   "시각(UTC)": "11-06 13:31"
  },
  {
   "출처": "CoinDesk",
   "제목": "Over $1 billion in bullish bets liquidated while ETF flows suggest no help in spot market",
   "요약": "Your day-ahead look for Nov. 6, 2026",
   "시각(UTC)": "11-06 12:30"
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
   "PENGU",
   "DENIM",
   "PEARL",
   "REBOOT",
   "BTC",
   "HYPE",
   "KNTQ",
   "XRP",
   "AERO",
   "PEPE",
   "INJ",
   "VVV",
   "TAO",
   "LINK",
   "AKE"
  ],
  "INTCB가 인기 검색에 있음": false
 }
}
```
