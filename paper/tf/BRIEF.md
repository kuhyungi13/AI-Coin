# TF팀 회의 자료 (2026-11-07 00:24 KST)

GitHub Actions가 무료 공개 API로 모은 자료입니다. 회의 진행 방법은 `aicoin/tf_team/PLAYBOOK.md`.
자료에 없는 숫자는 쓰지 않습니다. 실패한 자료는 아래 '수집 실패'에 있습니다.

분석 대상: BTC, ETH, PEPE, INJ, INTCB

**지금까지 승률** ACE 40.9% (9/22), 채점 대기 0개 · 자세히는 `paper/tf/SCOREBOARD.md`, 교훈은 `aicoin/tf_team/LESSONS.md`

**TRAINER 모의 계좌** 총자산 10,027.16 USDT (+0.27%), 보유 PEPE · 자세히는 `paper/tf/trainer/TRAINER.md`

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
   "1일": 0.7,
   "7일": -5.24,
   "30일": -2.33,
   "90일": -6.85
  },
  "종가와 이평선 거리(%)": {
   "MA20": -2.25,
   "MA60": -2.99,
   "MA120": -4.83
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 76
  },
  "RSI14": 39.5
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
 "시가총액(USD)": 1520379267950,
 "완전희석가치 FDV(USD)": 1520406945081,
 "24시간 거래대금(USD)": 42502027452,
 "유통량": 20105365.0,
 "총발행량": 20105731.0,
 "최대발행량": 21000000.0,
 "유통 비율(%)": 95.7,
 "역대 최고가(USD)": 126080,
 "역대 최고가 대비(%)": -40.0217,
 "가격 변화(%)": {
  "7d": -2.02613,
  "30d": -8.83834,
  "1y": -25.90663
 },
 "소개": "Bitcoin is the world's first decentralized cryptocurrency, created in 2009 by the pseudonymous Satoshi Nakamoto. It enables peer-to-peer electronic cash transactions without intermediaries like banks or governments, operating on a blockchain secured by Proof of Work mining and the SHA-256 cryptographic algorithm. \n\nWith a fixed supply cap of 21 million coins and programmatic halvings every four ye",
 "체인 TVL (DefiLlama)": {
  "체인": "Bitcoin",
  "TVL(USD)": 4035940314
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "BTC 관련 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin slips further after blowout October jobs numbers",
   "요약": "Chip stocks were leading a rebound in the broader market on Friday following yesterday's washout.",
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
   "출처": "Cointelegraph",
   "제목": "Here’s what happened in crypto today",
   "요약": "Need to know what happened in crypto today? Here is the latest news on daily trends and events impacting Bitcoin price, blockchain, DeFi, Web3 and crypto regulation.",
   "시각(UTC)": "11-06 13:33"
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Zcash’s landmark NU7 upgrade goes live, speeding up private payments",
   "요약": "NU7 cuts the target time between blocks to 25 seconds, reduces the work wallets must do to find private payments and sets aside fees for future miners.",
   "시각(UTC)": "11-06 05:14"
  },
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
   "Binance (Futures)": 0.0083,
   "Bybit (Futures)": 0.0059,
   "MEXC (Futures)": 0.0082,
   "Gate (Futures)": 0.0036,
   "WEEX (Futures)": 0.0001,
   "Tapbit (Futures)": 0.0079
  },
  "미결제약정 합계 USD(상위)": 28773502167
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 52.17,
  "CoinGecko 인기 검색 코인": [
   "DENIM",
   "REBOOT",
   "BTC",
   "INJ",
   "LIT",
   "ZEC",
   "MON",
   "SOL",
   "HYPE",
   "ETH",
   "PENGU",
   "PEARL",
   "NEAR",
   "AERO",
   "VVV"
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
   "1일": 0.67,
   "7일": -7.13,
   "30일": -1.17,
   "90일": -6.52
  },
  "종가와 이평선 거리(%)": {
   "MA20": -2.96,
   "MA60": -2.29,
   "MA120": -4.24
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 8
  },
  "RSI14": 41.1
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
 "시가총액(USD)": 271681611599,
 "완전희석가치 FDV(USD)": 271681611599,
 "24시간 거래대금(USD)": 15907915832,
 "유통량": 122194930.21672837,
 "총발행량": 122194930.21672837,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 4946.05,
 "역대 최고가 대비(%)": -55.04801,
 "가격 변화(%)": {
  "7d": -0.56345,
  "30d": -13.22769,
  "1y": -33.30586
 },
 "소개": "Ethereum is a global, open-source platform for decentralized applications. In other words, it is a decentralized blockchain platform that enables developers to build and deploy smart contracts and applications without central authority control. Unlike Bitcoin, which primarily functions as digital currency, Ethereum operates as a programmable global computer where developers can create any type of ",
 "체인 TVL (DefiLlama)": {
  "체인": "Ethereum",
  "TVL(USD)": 43168127598
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
   "제목": "Live updates: Bitcoin slips further after blowout October jobs numbers",
   "요약": "Chip stocks were leading a rebound in the broader market on Friday following yesterday's washout.",
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
   "Binance (Futures)": -0.0016,
   "WEEX (Futures)": 0.0001,
   "CoinW (Futures)": 0.0034,
   "MEXC (Futures)": 0.0034,
   "Hyperliquid (Futures)": 0.0013
  },
  "미결제약정 합계 USD(상위)": 18738034216
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 80.43,
  "CoinGecko 인기 검색 코인": [
   "DENIM",
   "REBOOT",
   "BTC",
   "INJ",
   "LIT",
   "ZEC",
   "MON",
   "SOL",
   "HYPE",
   "ETH",
   "PENGU",
   "PEARL",
   "NEAR",
   "AERO",
   "VVV"
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
  "기준일": "2026-11-06",
  "등락률(%)": {
   "1일": 2.22,
   "7일": 2.63,
   "30일": 3.26,
   "90일": 12.92
  },
  "종가와 이평선 거리(%)": {
   "MA20": 3.26,
   "MA60": 3.19,
   "MA120": 9.52
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 4
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
 "시가총액 순위": 45,
 "시가총액(USD)": 2157515267,
 "완전희석가치 FDV(USD)": 2157515267,
 "24시간 거래대금(USD)": 494390219,
 "유통량": 420690000000000.0,
 "총발행량": 420690000000000.0,
 "최대발행량": 420690000000000.0,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 2.803e-05,
 "역대 최고가 대비(%)": -81.70229,
 "가격 변화(%)": {
  "7d": -0.52369,
  "30d": 27.64192,
  "1y": -6.55902
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
   "제목": "Live updates: Bitcoin slips further after blowout October jobs numbers",
   "요약": "Chip stocks were leading a rebound in the broader market on Friday following yesterday's washout.",
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
   "MEXC (Futures)": 0.0372,
   "Gate (Futures)": 0.01,
   "OKX (Futures)": 0.01,
   "Bitget Futures": 0.01,
   "KCEX (Futures)": 0.01,
   "WhiteBIT Futures": 0.01
  },
  "미결제약정 합계 USD(상위)": 324378148
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 73.08,
  "CoinGecko 인기 검색 코인": [
   "DENIM",
   "REBOOT",
   "BTC",
   "INJ",
   "LIT",
   "ZEC",
   "MON",
   "SOL",
   "HYPE",
   "ETH",
   "PENGU",
   "PEARL",
   "NEAR",
   "AERO",
   "VVV"
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
  "기준일": "2026-11-06",
  "등락률(%)": {
   "1일": 0.09,
   "7일": -0.2,
   "30일": 12.82,
   "90일": 0.74
  },
  "종가와 이평선 거리(%)": {
   "MA20": 5.06,
   "MA60": 8.1,
   "MA120": 3.8
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 3
  },
  "RSI14": 60.4
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
 "시가총액(USD)": 842824012,
 "완전희석가치 FDV(USD)": 842824012,
 "24시간 거래대금(USD)": 145911842,
 "유통량": 100000000.0,
 "총발행량": 100000000.0,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 52.62,
 "역대 최고가 대비(%)": -83.98302,
 "가격 변화(%)": {
  "7d": 18.20276,
  "30d": 16.45356,
  "1y": 34.06744
 },
 "소개": "Injective is an interoperable Layer 1 blockchain designed for DeFi applications. It provides developers with on-chain financial infrastructure modules to build dApps such as decentralized exchanges, prediction markets, and lending protocols. Its decentralized cross-chain bridging infrastructure offers compatibility with most blockchains, including EVM chains like Ethereum and non-EVM chains like S",
 "체인 TVL (DefiLlama)": {
  "체인": "Injective",
  "TVL(USD)": 22746574
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
   "제목": "Live updates: Bitcoin slips further after blowout October jobs numbers",
   "요약": "Chip stocks were leading a rebound in the broader market on Friday following yesterday's washout.",
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
   "Tapbit (Futures)": 0.01,
   "OrangeX Futures": -0.0543,
   "Binance (Futures)": 0.01,
   "Gate (Futures)": 0.01,
   "MEXC (Futures)": 0.0255,
   "Bybit (Futures)": 0.01
  },
  "미결제약정 합계 USD(상위)": 331188741
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 97.22,
  "CoinGecko 인기 검색 코인": [
   "DENIM",
   "REBOOT",
   "BTC",
   "INJ",
   "LIT",
   "ZEC",
   "MON",
   "SOL",
   "HYPE",
   "ETH",
   "PENGU",
   "PEARL",
   "NEAR",
   "AERO",
   "VVV"
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
   "1일": 2.76,
   "7일": -2.15,
   "30일": -16.13,
   "90일": -37.51
  },
  "종가와 이평선 거리(%)": {
   "MA20": -3.42,
   "MA60": -20.06,
   "MA120": -30.07
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 42
  },
  "RSI14": 39.4
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
 "시가총액 순위": 348,
 "시가총액(USD)": 68392122,
 "완전희석가치 FDV(USD)": 68392122,
 "24시간 거래대금(USD)": 17330900,
 "유통량": 1235820.5574752998,
 "총발행량": 1235820.5574752998,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 130.12,
 "역대 최고가 대비(%)": -57.46963,
 "가격 변화(%)": {
  "7d": -16.47381,
  "30d": -51.27661,
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
   "제목": "Live updates: Bitcoin slips further after blowout October jobs numbers",
   "요약": "Chip stocks were leading a rebound in the broader market on Friday following yesterday's washout.",
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
  "오류": "ValueError: INTCB 무기한 선물 자료 없음"
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": null,
  "CoinGecko 인기 검색 코인": [
   "DENIM",
   "REBOOT",
   "BTC",
   "INJ",
   "LIT",
   "ZEC",
   "MON",
   "SOL",
   "HYPE",
   "ETH",
   "PENGU",
   "PEARL",
   "NEAR",
   "AERO",
   "VVV"
  ],
  "INTCB가 인기 검색에 있음": false
 }
}
```
