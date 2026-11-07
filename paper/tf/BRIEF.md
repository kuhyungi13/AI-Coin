# TF팀 회의 자료 (2026-11-08 00:16 KST)

GitHub Actions가 무료 공개 API로 모은 자료입니다. 회의 진행 방법은 `aicoin/tf_team/PLAYBOOK.md`.
자료에 없는 숫자는 쓰지 않습니다. 실패한 자료는 아래 '수집 실패'에 있습니다.

분석 대상: BTC, ETH, PEPE, INJ, SNDKB

**지금까지 승률** ACE 40.9% (9/22), 채점 대기 0개 · 자세히는 `paper/tf/SCOREBOARD.md`, 교훈은 `aicoin/tf_team/LESSONS.md`

**TRAINER 모의 계좌** 총자산 10,017.55 USDT (+0.18%), 보유 없음 · 자세히는 `paper/tf/trainer/TRAINER.md`

**전체 스캔 후보** (`paper/tf/SCAN.md`) 상승 추세: PEPE, INJ · 과매도 반등: SNDKB

## BTC

**수집 실패**
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-06",
  "종가": 75844.0,
  "등락률(%)": {
   "1일": -0.32,
   "7일": -1.97,
   "30일": -8.97,
   "90일": 16.75
  },
  "이동평균": {
   "MA20": 79761.5065,
   "MA60": 81227.169667,
   "MA120": 75011.490417
  },
  "종가와 이평선 거리(%)": {
   "MA20": -4.91,
   "MA60": -6.63,
   "MA120": 1.11
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 7
  },
  "RSI14": 37.9,
  "ATR14(%)": 3.07,
  "거래량(20일 평균 대비 배수)": 1.2,
  "30일 최고가": 84898.0,
  "30일 최저가": 74888.0,
  "최근 10일 종가": [
   81343.5,
   77991.89,
   77368.77,
   77582.02,
   78354.0,
   76816.0,
   77453.86,
   80504.01,
   76088.01,
   75844.0
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-07",
  "등락률(%)": {
   "1일": -0.15,
   "7일": 0.49,
   "30일": -2.45,
   "90일": -7.03
  },
  "종가와 이평선 거리(%)": {
   "MA20": -1.98,
   "MA60": -2.57,
   "MA120": -4.69
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 82
  },
  "RSI14": 39.7
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
 "시가총액(USD)": 1524525692211,
 "완전희석가치 FDV(USD)": 1524529027969,
 "24시간 거래대금(USD)": 16654044208,
 "유통량": 20109115.0,
 "총발행량": 20109159.0,
 "최대발행량": 21000000.0,
 "유통 비율(%)": 95.8,
 "역대 최고가(USD)": 126080,
 "역대 최고가 대비(%)": -39.87026,
 "가격 변화(%)": {
  "7d": -2.02362,
  "30d": -8.25661,
  "1y": -24.55096
 },
 "소개": "Bitcoin is the world's first decentralized cryptocurrency, created in 2009 by the pseudonymous Satoshi Nakamoto. It enables peer-to-peer electronic cash transactions without intermediaries like banks or governments, operating on a blockchain secured by Proof of Work mining and the SHA-256 cryptographic algorithm. \n\nWith a fixed supply cap of 21 million coins and programmatic halvings every four ye",
 "체인 TVL (DefiLlama)": {
  "체인": "Bitcoin",
  "TVL(USD)": 4036401806
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
   "시각(UTC)": "11-07 14:22"
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
  "오늘": "25 (Extreme Fear)",
  "최근 7일": [
   25,
   28,
   50,
   34,
   26,
   37,
   34
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.0014,
   "Bybit (Futures)": 0.0062,
   "MEXC (Futures)": 0.0012,
   "Gate (Futures)": 0.008,
   "WEEX (Futures)": 0.0001,
   "Tapbit (Futures)": 0.0014
  },
  "미결제약정 합계 USD(상위)": 28918419818
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 70.09,
  "CoinGecko 인기 검색 코인": [
   "REBOOT",
   "DACITY",
   "PENGU",
   "PEARL",
   "ZEC",
   "HYPE",
   "TAO",
   "ONE",
   "NEAR",
   "SOL",
   "BTC",
   "PI",
   "TRUMP",
   "AERO",
   "FET"
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
  "기준일": "2026-11-06",
  "종가": 2238.67,
  "등락률(%)": {
   "1일": 0.03,
   "7일": -0.31,
   "30일": -13.03,
   "90일": 16.8
  },
  "이동평균": {
   "MA20": 2335.0145,
   "MA60": 2495.409667,
   "MA120": 2283.053333
  },
  "종가와 이평선 거리(%)": {
   "MA20": -4.13,
   "MA60": -10.29,
   "MA120": -1.94
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 17
  },
  "RSI14": 39.5,
  "ATR14(%)": 4.15,
  "거래량(20일 평균 대비 배수)": 0.91,
  "30일 최고가": 2587.28,
  "30일 최저가": 2174.08,
  "최근 10일 종가": [
   2359.68,
   2253.13,
   2245.54,
   2255.66,
   2275.31,
   2253.29,
   2274.77,
   2424.61,
   2238.01,
   2238.67
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-07",
  "등락률(%)": {
   "1일": -0.03,
   "7일": 0.74,
   "30일": -1.81,
   "90일": -6.56
  },
  "종가와 이평선 거리(%)": {
   "MA20": -2.49,
   "MA60": -1.74,
   "MA120": -3.82
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 14
  },
  "RSI14": 42.5
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
 "시가총액(USD)": 273817446913,
 "완전희석가치 FDV(USD)": 273817446913,
 "24시간 거래대금(USD)": 5875414797,
 "유통량": 122197894.00927158,
 "총발행량": 122197894.00927158,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 4946.05,
 "역대 최고가 대비(%)": -54.69651,
 "가격 변화(%)": {
  "7d": -0.19524,
  "30d": -11.43291,
  "1y": -31.51136
 },
 "소개": "Ethereum is a global, open-source platform for decentralized applications. In other words, it is a decentralized blockchain platform that enables developers to build and deploy smart contracts and applications without central authority control. Unlike Bitcoin, which primarily functions as digital currency, Ethereum operates as a programmable global computer where developers can create any type of ",
 "체인 TVL (DefiLlama)": {
  "체인": "Ethereum",
  "TVL(USD)": 43471532714
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
  "오늘": "25 (Extreme Fear)",
  "최근 7일": [
   25,
   28,
   50,
   34,
   26,
   37,
   34
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.0059,
   "CoinW (Futures)": 0.008,
   "WEEX (Futures)": 0.0001,
   "MEXC (Futures)": 0.008,
   "Hyperliquid (Futures)": 0.0013
  },
  "미결제약정 합계 USD(상위)": 19614013468
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 80.0,
  "CoinGecko 인기 검색 코인": [
   "REBOOT",
   "DACITY",
   "PENGU",
   "PEARL",
   "ZEC",
   "HYPE",
   "TAO",
   "ONE",
   "NEAR",
   "SOL",
   "BTC",
   "PI",
   "TRUMP",
   "AERO",
   "FET"
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
  "기준일": "2026-11-06",
  "종가": 5e-06,
  "등락률(%)": {
   "1일": 3.96,
   "7일": 1.01,
   "30일": 21.71,
   "90일": 75.09
  },
  "이동평균": {
   "MA20": 5e-06,
   "MA60": 4e-06,
   "MA120": 4e-06
  },
  "종가와 이평선 거리(%)": {
   "MA20": 7.47,
   "MA60": 17.85,
   "MA120": 36.53
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 101
  },
  "RSI14": 58.8,
  "ATR14(%)": 10.51,
  "거래량(20일 평균 대비 배수)": 0.86,
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
  "기준일": "2026-11-07",
  "등락률(%)": {
   "1일": -0.81,
   "7일": -1.21,
   "30일": 1.03,
   "90일": -3.35
  },
  "종가와 이평선 거리(%)": {
   "MA20": -1.24,
   "MA60": -0.83,
   "MA120": 4.61
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 5
  },
  "RSI14": 48.1
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
 "시가총액(USD)": 2056982608,
 "완전희석가치 FDV(USD)": 2056982608,
 "24시간 거래대금(USD)": 236852538,
 "유통량": 420690000000000.0,
 "총발행량": 420690000000000.0,
 "최대발행량": 420690000000000.0,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 2.803e-05,
 "역대 최고가 대비(%)": -82.54824,
 "가격 변화(%)": {
  "7d": -2.34028,
  "30d": 21.62179,
  "1y": -13.83571
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
  "오늘": "25 (Extreme Fear)",
  "최근 7일": [
   25,
   28,
   50,
   34,
   26,
   37,
   34
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "MEXC (Futures)": 0.01,
   "Gate (Futures)": 0.0093,
   "OKX (Futures)": 0.01,
   "Bitget Futures": 0.0042,
   "WhiteBIT Futures": 0.01,
   "BloFin (Futures)": 0.022
  },
  "미결제약정 합계 USD(상위)": 279041145
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 92.59,
  "CoinGecko 인기 검색 코인": [
   "REBOOT",
   "DACITY",
   "PENGU",
   "PEARL",
   "ZEC",
   "HYPE",
   "TAO",
   "ONE",
   "NEAR",
   "SOL",
   "BTC",
   "PI",
   "TRUMP",
   "AERO",
   "FET"
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
  "기준일": "2026-11-06",
  "종가": 8.297,
  "등락률(%)": {
   "1일": 1.83,
   "7일": 15.52,
   "30일": 11.15,
   "90일": 88.06
  },
  "이동평균": {
   "MA20": 7.8951,
   "MA60": 7.475433,
   "MA120": 6.192258
  },
  "종가와 이평선 거리(%)": {
   "MA20": 5.09,
   "MA60": 10.99,
   "MA120": 33.99
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 65
  },
  "RSI14": 57.7,
  "ATR14(%)": 7.39,
  "거래량(20일 평균 대비 배수)": 1.12,
  "30일 최고가": 9.417,
  "30일 최저가": 6.417,
  "최근 10일 종가": [
   8.154,
   7.337,
   7.182,
   7.231,
   7.185,
   6.983,
   7.248,
   7.937,
   8.148,
   8.297
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-07",
  "등락률(%)": {
   "1일": -1.28,
   "7일": 0.31,
   "30일": 14.24,
   "90일": 2.67
  },
  "종가와 이평선 거리(%)": {
   "MA20": 0.99,
   "MA60": 7.94,
   "MA120": 4.21
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 9
  },
  "RSI14": 56.9
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
 "시가총액(USD)": 813473832,
 "완전희석가치 FDV(USD)": 813473832,
 "24시간 거래대금(USD)": 74998510,
 "유통량": 100000000.0,
 "총발행량": 100000000.0,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 52.62,
 "역대 최고가 대비(%)": -84.53746,
 "가격 변화(%)": {
  "7d": 13.93009,
  "30d": 11.30625,
  "1y": 19.98204
 },
 "소개": "Injective is an interoperable Layer 1 blockchain designed for DeFi applications. It provides developers with on-chain financial infrastructure modules to build dApps such as decentralized exchanges, prediction markets, and lending protocols. Its decentralized cross-chain bridging infrastructure offers compatibility with most blockchains, including EVM chains like Ethereum and non-EVM chains like S",
 "체인 TVL (DefiLlama)": {
  "체인": "Injective",
  "TVL(USD)": 22746646
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
  "오늘": "25 (Extreme Fear)",
  "최근 7일": [
   25,
   28,
   50,
   34,
   26,
   37,
   34
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Tapbit (Futures)": 0.01,
   "OrangeX Futures": -0.0149,
   "Binance (Futures)": 0.01,
   "Gate (Futures)": 0.01,
   "MEXC (Futures)": 0.0279,
   "Bybit (Futures)": 0.01
  },
  "미결제약정 합계 USD(상위)": 290214328
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 94.12,
  "CoinGecko 인기 검색 코인": [
   "REBOOT",
   "DACITY",
   "PENGU",
   "PEARL",
   "ZEC",
   "HYPE",
   "TAO",
   "ONE",
   "NEAR",
   "SOL",
   "BTC",
   "PI",
   "TRUMP",
   "AERO",
   "FET"
  ],
  "INJ가 인기 검색에 있음": false
 }
}
```

## SNDKB

**수집 실패**
- VIBE/선물 포지션: ValueError: SNDKB 무기한 선물 자료 없음
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-06",
  "종가": 838.07,
  "등락률(%)": {
   "1일": 3.38,
   "7일": -27.68,
   "30일": -50.79,
   "90일": -31.24
  },
  "이동평균": {
   "MA20": 1200.529,
   "MA60": 1500.621333,
   "MA120": 1497.500667
  },
  "종가와 이평선 거리(%)": {
   "MA20": -30.19,
   "MA60": -44.15,
   "MA120": -44.04
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 22
  },
  "RSI14": 24.9,
  "ATR14(%)": 11.87,
  "거래량(20일 평균 대비 배수)": 2.48,
  "30일 최고가": 1714.51,
  "30일 최저가": 794.03,
  "최근 10일 종가": [
   1365.94,
   1282.84,
   1158.78,
   1151.76,
   1172.1,
   1094.78,
   1134.62,
   1029.58,
   810.7,
   838.07
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-07",
  "등락률(%)": {
   "1일": -0.12,
   "7일": -3.0,
   "30일": -29.06,
   "90일": -35.24
  },
  "종가와 이평선 거리(%)": {
   "MA20": -9.82,
   "MA60": -24.74,
   "MA120": -30.82
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 41
  },
  "RSI14": 31.5
 }
}
```

### DIANA 자료 · 기본적 분석 (펀더멘털)

```json
{
 "이름": "SanDisk (bStocks Tokenized Stock)",
 "분류": [
  "Tokenized Assets",
  "BNB Chain Ecosystem",
  "Tokenized Stocks",
  "Real World Assets (RWA)",
  "bStocks Ecosystem"
 ],
 "시가총액 순위": 283,
 "시가총액(USD)": 92336227,
 "완전희석가치 FDV(USD)": 92336227,
 "24시간 거래대금(USD)": 35720988,
 "유통량": 110798.18748988,
 "총발행량": 110798.18748988,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 2369.74,
 "역대 최고가 대비(%)": -64.84279,
 "가격 변화(%)": {
  "7d": -27.63976,
  "30d": -49.30938,
  "1y": null
 },
 "소개": ""
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "SNDKB 관련 기사": [],
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
  "오늘": "25 (Extreme Fear)",
  "최근 7일": [
   25,
   28,
   50,
   34,
   26,
   37,
   34
  ]
 },
 "선물 포지션": {
  "오류": "ValueError: SNDKB 무기한 선물 자료 없음"
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": null,
  "CoinGecko 인기 검색 코인": [
   "REBOOT",
   "DACITY",
   "PENGU",
   "PEARL",
   "ZEC",
   "HYPE",
   "TAO",
   "ONE",
   "NEAR",
   "SOL",
   "BTC",
   "PI",
   "TRUMP",
   "AERO",
   "FET"
  ],
  "SNDKB가 인기 검색에 있음": false
 }
}
```
