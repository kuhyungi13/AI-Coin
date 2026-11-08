# TF팀 회의 자료 (2026-11-09 04:22 KST)

GitHub Actions가 무료 공개 API로 모은 자료입니다. 회의 진행 방법은 `aicoin/tf_team/PLAYBOOK.md`.
자료에 없는 숫자는 쓰지 않습니다. 실패한 자료는 아래 '수집 실패'에 있습니다.

분석 대상: BTC, ETH, QNT, PEPE, SNDKB

**지금까지 승률** ACE 40.9% (9/22), 채점 대기 0개 · 자세히는 `paper/tf/SCOREBOARD.md`, 교훈은 `aicoin/tf_team/LESSONS.md`

**TRAINER 모의 계좌** 총자산 10,017.55 USDT (+0.18%), 보유 없음 · 자세히는 `paper/tf/trainer/TRAINER.md`

**전체 스캔 후보** (`paper/tf/SCAN.md`) 상승 추세: QNT, PEPE · 과매도 반등: SNDKB

## BTC

**수집 실패**
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-07",
  "종가": 75867.59,
  "등락률(%)": {
   "1일": 0.03,
   "7일": -2.21,
   "30일": -7.2,
   "90일": 16.9
  },
  "이동평균": {
   "MA20": 79449.086,
   "MA60": 81184.032833,
   "MA120": 75109.039333
  },
  "종가와 이평선 거리(%)": {
   "MA20": -4.51,
   "MA60": -6.55,
   "MA120": 1.01
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 8
  },
  "RSI14": 38.0,
  "ATR14(%)": 2.94,
  "거래량(20일 평균 대비 배수)": 0.35,
  "30일 최고가": 84898.0,
  "30일 최저가": 74888.0,
  "최근 10일 종가": [
   77991.89,
   77368.77,
   77582.02,
   78354.0,
   76816.0,
   77453.86,
   80504.01,
   76088.01,
   75844.0,
   75867.59
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-08",
  "등락률(%)": {
   "1일": 0.12,
   "7일": 0.12,
   "30일": -2.08,
   "90일": -4.67
  },
  "종가와 이평선 거리(%)": {
   "MA20": -0.13,
   "MA60": -1.74,
   "MA120": -4.15
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 89
  },
  "RSI14": 42.4
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
 "시가총액(USD)": 1524131658869,
 "완전희석가치 FDV(USD)": 1524132340991,
 "24시간 거래대금(USD)": 10631161442,
 "유통량": 20109603.0,
 "총발행량": 20109612.0,
 "최대발행량": 21000000.0,
 "유통 비율(%)": 95.8,
 "역대 최고가(USD)": 126080,
 "역대 최고가 대비(%)": -39.88582,
 "가격 변화(%)": {
  "7d": -2.59113,
  "30d": -7.99074,
  "1y": -25.77079
 },
 "소개": "Bitcoin is the world's first decentralized cryptocurrency, created in 2009 by the pseudonymous Satoshi Nakamoto. It enables peer-to-peer electronic cash transactions without intermediaries like banks or governments, operating on a blockchain secured by Proof of Work mining and the SHA-256 cryptographic algorithm. \n\nWith a fixed supply cap of 21 million coins and programmatic halvings every four ye",
 "체인 TVL (DefiLlama)": {
  "체인": "Bitcoin",
  "TVL(USD)": 4043329259
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "BTC 관련 기사": [
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
   "출처": "CoinDesk",
   "제목": "Bitcoin developer proposes ‘landmines’ to make quantum thieves lose their own BTC",
   "요약": "Anyone trying to move vulnerable bitcoin would have to put up matching collateral, giving prepared owners a chance to take both.",
   "시각(UTC)": "11-06 01:30"
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
  },
  {
   "출처": "Decrypt",
   "제목": "Crypto Liquidations Top $1 Billion as Bitcoin Tests 11-Week Low",
   "요약": "Bitcoin fell toward $75,500 after AI stocks plunged, and over $1 billion in the crypto derivatives market has been wiped out.",
   "시각(UTC)": "11-06 16:34"
  }
 ],
 "시장 전반 기사": [
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Thailand moves to block Bitget as crypto exchange's local acquisition faces uncertainty",
   "요약": "Thailand’s SEC filed a criminal complaint against Bitget’s operator, alleging it ran an unlicensed crypto exchange for Thai users from 2022 to 2025.",
   "시각(UTC)": "11-06 14:33"
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
   25,
   28,
   50,
   34,
   26,
   37
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.0038,
   "CoinW (Futures)": 0.0038,
   "Bybit (Futures)": 0.0086,
   "MEXC (Futures)": 0.0044,
   "Gate (Futures)": 0.01,
   "WEEX (Futures)": 0.0001
  },
  "미결제약정 합계 USD(상위)": 31091156096
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 68.89,
  "CoinGecko 인기 검색 코인": [
   "JOSÉ",
   "WASTED",
   "DACITY",
   "JCT",
   "BTC",
   "PONS",
   "ONDO",
   "PENGU",
   "PUMP",
   "STONK",
   "ZEC",
   "MON",
   "TAO",
   "SUI",
   "KNTQ"
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
  "기준일": "2026-11-07",
  "종가": 2240.24,
  "등락률(%)": {
   "1일": 0.07,
   "7일": -0.68,
   "30일": -9.48,
   "90일": 17.25
  },
  "이동평균": {
   "MA20": 2326.511,
   "MA60": 2491.329333,
   "MA120": 2286.74825
  },
  "종가와 이평선 거리(%)": {
   "MA20": -3.71,
   "MA60": -10.08,
   "MA120": -2.03
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 18
  },
  "RSI14": 39.6,
  "ATR14(%)": 3.9,
  "거래량(20일 평균 대비 배수)": 0.28,
  "30일 최고가": 2579.88,
  "30일 최저가": 2174.08,
  "최근 10일 종가": [
   2253.13,
   2245.54,
   2255.66,
   2275.31,
   2253.29,
   2274.77,
   2424.61,
   2238.01,
   2238.67,
   2240.24
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-08",
  "등락률(%)": {
   "1일": 0.07,
   "7일": -0.15,
   "30일": -2.5,
   "90일": -2.79
  },
  "종가와 이평선 거리(%)": {
   "MA20": -0.35,
   "MA60": -1.38,
   "MA120": -3.57
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 3
  },
  "RSI14": 43.0
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
 "시가총액(USD)": 272594708816,
 "완전희석가치 FDV(USD)": 272594708816,
 "24시간 거래대금(USD)": 3841778043,
 "유통량": 122200877.25744775,
 "총발행량": 122200877.25744775,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 4946.05,
 "역대 최고가 대비(%)": -54.90226,
 "가격 변화(%)": {
  "7d": -1.35103,
  "30d": -10.09347,
  "1y": -34.44841
 },
 "소개": "Ethereum is a global, open-source platform for decentralized applications. In other words, it is a decentralized blockchain platform that enables developers to build and deploy smart contracts and applications without central authority control. Unlike Bitcoin, which primarily functions as digital currency, Ethereum operates as a programmable global computer where developers can create any type of ",
 "체인 TVL (DefiLlama)": {
  "체인": "Ethereum",
  "TVL(USD)": 43041683904
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "ETH 관련 기사": [
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
  "오늘": "28 (Fear)",
  "최근 7일": [
   28,
   25,
   28,
   50,
   34,
   26,
   37
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "CoinW (Futures)": 0.0046,
   "Binance (Futures)": 0.003,
   "WEEX (Futures)": 0.0001,
   "MEXC (Futures)": 0.0052,
   "Hyperliquid (Futures)": 0.0013
  },
  "미결제약정 합계 USD(상위)": 21315175824
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 85.29,
  "CoinGecko 인기 검색 코인": [
   "JOSÉ",
   "WASTED",
   "DACITY",
   "JCT",
   "BTC",
   "PONS",
   "ONDO",
   "PENGU",
   "PUMP",
   "STONK",
   "ZEC",
   "MON",
   "TAO",
   "SUI",
   "KNTQ"
  ],
  "ETH가 인기 검색에 있음": false
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
  "기준일": "2026-11-07",
  "종가": 196.17,
  "등락률(%)": {
   "1일": 1.09,
   "7일": -2.46,
   "30일": -17.13,
   "90일": 236.43
  },
  "이동평균": {
   "MA20": 194.289,
   "MA60": 174.217833,
   "MA120": 118.196
  },
  "종가와 이평선 거리(%)": {
   "MA20": 0.97,
   "MA60": 12.6,
   "MA120": 65.97
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 63
  },
  "RSI14": 50.3,
  "ATR14(%)": 9.22,
  "거래량(20일 평균 대비 배수)": 0.58,
  "30일 최고가": 256.5,
  "30일 최저가": 173.56,
  "최근 10일 종가": [
   182.89,
   192.27,
   201.11,
   201.73,
   194.13,
   192.26,
   204.15,
   188.77,
   194.06,
   196.17
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-08",
  "등락률(%)": {
   "1일": 0.39,
   "7일": 1.47,
   "30일": 2.68,
   "90일": 13.74
  },
  "종가와 이평선 거리(%)": {
   "MA20": 3.0,
   "MA60": 2.38,
   "MA120": 3.01
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 3
  },
  "RSI14": 57.0
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
 "시가총액(USD)": 2931646942,
 "완전희석가치 FDV(USD)": 2942988876,
 "24시간 거래대금(USD)": 31498706,
 "유통량": 14556178.164081175,
 "총발행량": 14612493.0,
 "최대발행량": 14612493.0,
 "유통 비율(%)": 99.6,
 "역대 최고가(USD)": 427.42,
 "역대 최고가 대비(%)": -52.87851,
 "가격 변화(%)": {
  "7d": 1.91213,
  "30d": -17.23502,
  "1y": 137.07431
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
  "오늘": "28 (Fear)",
  "최근 7일": [
   28,
   25,
   28,
   50,
   34,
   26,
   37
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.01,
   "OrangeX Futures": 0.01,
   "Toobit Futures": 0.01,
   "WEEX (Futures)": 0.0001,
   "MEXC (Futures)": 0.01,
   "Bybit (Futures)": 0.001
  },
  "미결제약정 합계 USD(상위)": 110870989
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 77.27,
  "CoinGecko 인기 검색 코인": [
   "JOSÉ",
   "WASTED",
   "DACITY",
   "JCT",
   "BTC",
   "PONS",
   "ONDO",
   "PENGU",
   "PUMP",
   "STONK",
   "ZEC",
   "MON",
   "TAO",
   "SUI",
   "KNTQ"
  ],
  "QNT가 인기 검색에 있음": false
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
  "기준일": "2026-11-07",
  "종가": 5e-06,
  "등락률(%)": {
   "1일": -2.4,
   "7일": -2.6,
   "30일": 27.15,
   "90일": 69.1
  },
  "이동평균": {
   "MA20": 5e-06,
   "MA60": 4e-06,
   "MA120": 4e-06
  },
  "종가와 이평선 거리(%)": {
   "MA20": 3.93,
   "MA60": 14.47,
   "MA120": 32.61
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 102
  },
  "RSI14": 55.9,
  "ATR14(%)": 10.56,
  "거래량(20일 평균 대비 배수)": 0.26,
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
  "기준일": "2026-11-08",
  "등락률(%)": {
   "1일": 1.6,
   "7일": 3.47,
   "30일": 3.68,
   "90일": 18.18
  },
  "종가와 이평선 거리(%)": {
   "MA20": 2.77,
   "MA60": 2.84,
   "MA120": 7.01
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 0
  },
  "RSI14": 59.3
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
 "시가총액 순위": 43,
 "시가총액(USD)": 2125886371,
 "완전희석가치 FDV(USD)": 2125886371,
 "24시간 거래대금(USD)": 262002935,
 "유통량": 420690000000000.0,
 "총발행량": 420690000000000.0,
 "최대발행량": 420690000000000.0,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 2.803e-05,
 "역대 최고가 대비(%)": -81.96579,
 "가격 변화(%)": {
  "7d": 3.50061,
  "30d": 29.02889,
  "1y": -16.5131
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
  "오늘": "28 (Fear)",
  "최근 7일": [
   28,
   25,
   28,
   50,
   34,
   26,
   37
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
  "미결제약정 합계 USD(상위)": 287601077
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 86.21,
  "CoinGecko 인기 검색 코인": [
   "JOSÉ",
   "WASTED",
   "DACITY",
   "JCT",
   "BTC",
   "PONS",
   "ONDO",
   "PENGU",
   "PUMP",
   "STONK",
   "ZEC",
   "MON",
   "TAO",
   "SUI",
   "KNTQ"
  ],
  "PEPE가 인기 검색에 있음": false
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
  "기준일": "2026-11-07",
  "종가": 836.63,
  "등락률(%)": {
   "1일": -0.17,
   "7일": -27.36,
   "30일": -48.19,
   "90일": -31.47
  },
  "이동평균": {
   "MA20": 1177.4815,
   "MA60": 1485.5165,
   "MA120": 1488.38125
  },
  "종가와 이평선 거리(%)": {
   "MA20": -28.95,
   "MA60": -43.68,
   "MA120": -43.79
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 23
  },
  "RSI14": 24.9,
  "ATR14(%)": 11.66,
  "거래량(20일 평균 대비 배수)": 0.17,
  "30일 최고가": 1648.7,
  "30일 최저가": 794.03,
  "최근 10일 종가": [
   1282.84,
   1158.78,
   1151.76,
   1172.1,
   1094.78,
   1134.62,
   1029.58,
   810.7,
   838.07,
   836.63
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-08",
  "등락률(%)": {
   "1일": -0.05,
   "7일": 0.03,
   "30일": -26.5,
   "90일": -31.67
  },
  "종가와 이평선 거리(%)": {
   "MA20": -1.69,
   "MA60": -20.22,
   "MA120": -29.13
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 48
  },
  "RSI14": 32.6
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
 "시가총액 순위": 280,
 "시가총액(USD)": 94045556,
 "완전희석가치 FDV(USD)": 94045556,
 "24시간 거래대금(USD)": 10090210,
 "유통량": 110764.00954523,
 "총발행량": 110764.00954523,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 2369.74,
 "역대 최고가 대비(%)": -64.17069,
 "가격 변화(%)": {
  "7d": -26.78332,
  "30d": -46.54693,
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
  "오늘": "28 (Fear)",
  "최근 7일": [
   28,
   25,
   28,
   50,
   34,
   26,
   37
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
   "JOSÉ",
   "WASTED",
   "DACITY",
   "JCT",
   "BTC",
   "PONS",
   "ONDO",
   "PENGU",
   "PUMP",
   "STONK",
   "ZEC",
   "MON",
   "TAO",
   "SUI",
   "KNTQ"
  ],
  "SNDKB가 인기 검색에 있음": false
 }
}
```
