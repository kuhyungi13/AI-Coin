# TF팀 회의 자료 (2026-11-12 20:37 KST)

GitHub Actions가 무료 공개 API로 모은 자료입니다. 회의 진행 방법은 `aicoin/tf_team/PLAYBOOK.md`.
자료에 없는 숫자는 쓰지 않습니다. 실패한 자료는 아래 '수집 실패'에 있습니다.

분석 대상: BTC, ETH, ERA, TSLAB, NVDAB

**지금까지 승률** ACE 40.9% (9/22), 채점 대기 0개 · 자세히는 `paper/tf/SCOREBOARD.md`, 교훈은 `aicoin/tf_team/LESSONS.md`

**TRAINER 모의 계좌** 총자산 10,017.55 USDT (+0.18%), 보유 없음 · 자세히는 `paper/tf/trainer/TRAINER.md`

**전체 스캔 후보** (`paper/tf/SCAN.md`) 상승 추세: ERA, TSLAB · 과매도 반등: NVDAB

## BTC

**수집 실패**
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-11",
  "종가": 74015.19,
  "등락률(%)": {
   "1일": 0.3,
   "7일": -8.06,
   "30일": -9.57,
   "90일": 16.58
  },
  "이동평균": {
   "MA20": 77826.838,
   "MA60": 80994.8915,
   "MA120": 75467.819333
  },
  "종가와 이평선 거리(%)": {
   "MA20": -4.9,
   "MA60": -8.62,
   "MA120": -1.92
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 12
  },
  "RSI14": 35.0,
  "ATR14(%)": 3.3,
  "거래량(20일 평균 대비 배수)": 1.11,
  "30일 최고가": 84898.0,
  "30일 최저가": 72727.27,
  "최근 10일 종가": [
   76816.0,
   77453.86,
   80504.01,
   76088.01,
   75844.0,
   75867.59,
   74851.44,
   75368.41,
   73796.06,
   74015.19
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-12",
  "등락률(%)": {
   "1일": -0.2,
   "7일": -0.15,
   "30일": -3.2,
   "90일": -9.15
  },
  "종가와 이평선 거리(%)": {
   "MA20": -0.79,
   "MA60": -3.23,
   "MA120": -5.41
  },
  "MA20>MA60": false,
  "최근 교차": null,
  "RSI14": 39.3
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
 "시가총액(USD)": 1469172277135,
 "완전희석가치 FDV(USD)": 1469172934612,
 "24시간 거래대금(USD)": 22714753411,
 "유통량": 20111025.0,
 "총발행량": 20111034.0,
 "최대발행량": 21000000.0,
 "유통 비율(%)": 95.8,
 "역대 최고가(USD)": 126080,
 "역대 최고가 대비(%)": -42.06723,
 "가격 변화(%)": {
  "7d": -8.95028,
  "30d": -12.26452,
  "1y": -30.36326
 },
 "소개": "Bitcoin is the world's first decentralized cryptocurrency, created in 2009 by the pseudonymous Satoshi Nakamoto. It enables peer-to-peer electronic cash transactions without intermediaries like banks or governments, operating on a blockchain secured by Proof of Work mining and the SHA-256 cryptographic algorithm. \n\nWith a fixed supply cap of 21 million coins and programmatic halvings every four ye",
 "체인 TVL (DefiLlama)": {
  "체인": "Bitcoin",
  "TVL(USD)": 3861424690
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "BTC 관련 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin dips with Nvidia as ETF outflows reach day five",
   "요약": "Bitcoin slips 0.7% as Nvidia falls on reports its board may oust CEO Jensen Huang, while U.S. spot bitcoin ETFs lose another $299.9 million.",
   "시각(UTC)": "11-12 11:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin ETFs bleed $300 million as AI stocks slide again",
   "요약": "Nasdaq 100 futures retreat after Wednesday’s rally, while AI stocks slide, Strategy falls 4% and gold trades below $4,000.",
   "시각(UTC)": "11-12 09:15"
  },
  {
   "출처": "CoinDesk",
   "제목": "Canaan may sell more bitcoin for stock buybacks as mining-rig revenue falls 96%",
   "요약": "The Avalon maker has launched a $20 million repurchase program, while most of its bitcoin holdings were pledged or placed in a fixed-term product at September’s end.",
   "시각(UTC)": "11-12 07:41"
  },
  {
   "출처": "CoinDesk",
   "제목": "MSCI is dropping Strategy from its index, and the exclusion could hit its bitcoin-buying machine",
   "요약": "MSCI’s decision to exclude Strategy from its equity indexes could hamper the company’s ability to buy more bitcoin, according to some analysts.",
   "시각(UTC)": "11-12 07:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin Core reveals bug that made thousands of nodes trust any stranger on Tor",
   "요약": "The flaw was fixed in October 2025 and kept quiet until Tuesday. It came out alongside a high-severity bug that could stop a miner from producing blocks until someone restarted it.",
   "시각(UTC)": "11-12 05:22"
  },
  {
   "출처": "CoinDesk",
   "제목": "Nvidia perps crash 7% as CEO Jensen Huang reportedly faces the axe",
   "요약": "Nvidia perps are down 7% on Hyperliquid as traders react to reports that CEO Jensen Huang may be removed. Bitcoin continues to trade in a familiar price range.",
   "시각(UTC)": "11-12 04:03"
  },
  {
   "출처": "CoinDesk",
   "제목": "Live news: Bitcoin remains under pressure as CoreWeave, Nvidia lead AI rebound",
   "요약": "The DRAM ETF jumps 8% and semiconductor stocks gain more than 4%, while bitcoin continues to test its 200-day moving average.",
   "시각(UTC)": "11-11 12:21"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin barely flinches at hot CPI as ETF selling slows",
   "요약": "Your day-ahead look for Nov. 11, 2026",
   "시각(UTC)": "11-11 12:19"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin sits out stock rebound as ETF outflows extend to fourth day",
   "요약": "Bitcoin held steady near $74,000 as Tuesday's hot inflation figure lifted the odds on a U.S. interest-rate increase to around 90%. ETF outflows extended to a fourth day and liquidations jumped.",
   "시각(UTC)": "11-11 11:37"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin stuck under $74,000 as CoreWeave earnings revive AI outlook, Anthropic said to raise IPO valuation",
   "요약": "CoreWeave’s revenue surge lifted AI infrastructure stocks and Nasdaq futures, while bitcoin was little changed over 24 hours.",
   "시각(UTC)": "11-11 10:45"
  },
  {
   "출처": "Cointelegraph",
   "제목": "BlackRock Bitcoin ETF outflows hit $2B over nine sessions",
   "요약": "US spot Bitcoin ETF outflows rose to nearly $300 million on Wednesday, up from $95 million a day earlier, as five-session withdrawals reached $1.44 billion.",
   "시각(UTC)": "11-12 08:06"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Here’s what happened in crypto today",
   "요약": "Need to know what happened in crypto today? Here is the latest news on daily trends and events impacting Bitcoin price, blockchain, DeFi, Web3 and crypto regulation.",
   "시각(UTC)": "11-12 06:00"
  },
  {
   "출처": "Cointelegraph",
   "제목": "US data center restrictions could give Bitcoin miners an edge in AI, though challenges remain",
   "요약": "As US voters push back against new data centers, Bitcoin miners already expanding into AI could benefit from their existing facilities.",
   "시각(UTC)": "11-11 20:43"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin hovers near $74K as stocks rise despite US bond yield rebound",
   "요약": "Bitcoin traded in a narrow range as investors bought the dip in tech stocks and US bond yields climbed on high CPI inflation data.",
   "시각(UTC)": "11-11 16:26"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Deutsche Bank launches crypto custody for companies and institutions",
   "요약": "Clients can store and transfer Bitcoin, Ether and select stablecoins through the bank, which manages their wallets and private keys.",
   "시각(UTC)": "11-11 14:02"
  }
 ],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Polymarket trims workforce under investor pressure as Kalshi surges ahead",
   "요약": "More than half of those affected were contractors, a source told Reuters. The cuts follow investor pressure on founder Shayne Coplan.",
   "시각(UTC)": "11-12 10:42"
  },
  {
   "출처": "CoinDesk",
   "제목": "Nomura weighs Laser Digital sale as European losses hit four straight quarters",
   "요약": "The Japanese brokerage has held talks with potential buyers, including Marex, as its European business posts more losses.",
   "시각(UTC)": "11-12 10:32"
  },
  {
   "출처": "CoinDesk",
   "제목": "India’s financial crimes watchdog raids crypto exchanges CoinDCX and Delta over alleged illegal cross-border trades",
   "요약": "The Enforcement Directorate alleged illegal cross-border flows that violated India's foreign exchange laws.",
   "시각(UTC)": "11-12 10:10"
  },
  {
   "출처": "CoinDesk",
   "제목": "Gemini sells UK and European operations to stablecoin payments firm KAST for under $10 million",
   "요약": "The sale follows the Winklevoss-founded crypto exchange’s retreat from several overseas markets as it restructures its business.",
   "시각(UTC)": "11-12 09:07"
  },
  {
   "출처": "CoinDesk",
   "제목": "Zcash holders to vote on pulling 50,000 ZEC, worth $50 million, from grants treasury",
   "요약": "The proposal would remove more than half of Zcash Community Grants' ZEC holdings from circulation and redirect its future block rewards into a new development and legal-defense fund.",
   "시각(UTC)": "11-12 05:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Ripple’s bank-lending system moves closer to launch on the XRP Ledger",
   "요약": "Lending support among the ledger’s 35 validators has climbed from 19 to 22 since mid-October, and no public tracker shows which validators switched.",
   "시각(UTC)": "11-12 05:18"
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto Long & Short: The GENIUS Act’s guarantees don’t cover DeFi lending",
   "요약": "Institutions weighing DeFi lending tend to ask which markets are safest. Mike Hathaway and Joseph Quintilian of Ajna argue the better question is who can change a loan’s terms after the money is lent, and why a fully backed stablecoin offer",
   "시각(UTC)": "11-11 16:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "OKXICE to debut tokenized stock trading with Strategy, Coinbase, Circle this month",
   "요약": "After initial issuer pushback, the blockchain venue is set to start trading on Nov. 23 and said will list over 70 assets, including Strategy’s common and preferred shares and 59 of Direxion's ETFs.",
   "시각(UTC)": "11-11 13:00"
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
   29,
   32,
   29,
   28,
   25,
   28
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.0046,
   "OKX (Futures)": 0.0068,
   "Bybit (Futures)": 0.0046,
   "MEXC (Futures)": 0.0044,
   "Gate (Futures)": 0.0066,
   "CoinW (Futures)": 0.0044
  },
  "미결제약정 합계 USD(상위)": 18988678472
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 69.42,
  "CoinGecko 인기 검색 코인": [
   "SEPPUKU",
   "ZIG",
   "PENGU",
   "BTC",
   "ETH",
   "TAO",
   "ZEC",
   "UNI",
   "PEARL",
   "PI",
   "XRP",
   "HYPE",
   "EPIC",
   "ICP",
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
  "기준일": "2026-11-11",
  "종가": 2056.36,
  "등락률(%)": {
   "1일": 0.15,
   "7일": -15.19,
   "30일": -15.97,
   "90일": 9.02
  },
  "이동평균": {
   "MA20": 2259.119,
   "MA60": 2465.0545,
   "MA120": 2295.990917
  },
  "종가와 이평선 거리(%)": {
   "MA20": -8.98,
   "MA60": -16.58,
   "MA120": -10.44
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 22
  },
  "RSI14": 29.9,
  "ATR14(%)": 4.98,
  "거래량(20일 평균 대비 배수)": 0.83,
  "30일 최고가": 2538.52,
  "30일 최저가": 2006.0,
  "최근 10일 종가": [
   2253.29,
   2274.77,
   2424.61,
   2238.01,
   2238.67,
   2240.24,
   2127.46,
   2135.24,
   2053.21,
   2056.36
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-12",
  "등락률(%)": {
   "1일": -0.17,
   "7일": -0.54,
   "30일": -8.66,
   "90일": -13.12
  },
  "종가와 이평선 거리(%)": {
   "MA20": -1.64,
   "MA60": -7.28,
   "MA120": -9.38
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 25
  },
  "RSI14": 34.5
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
 "시가총액(USD)": 247792067534,
 "완전희석가치 FDV(USD)": 247792067534,
 "24시간 거래대금(USD)": 8357624053,
 "유통량": 122212724.4774798,
 "총발행량": 122212724.4774798,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 4946.05,
 "역대 최고가 대비(%)": -59.01556,
 "가격 변화(%)": {
  "7d": -16.11538,
  "30d": -18.78878,
  "1y": -42.63088
 },
 "소개": "Ethereum is a global, open-source platform for decentralized applications. In other words, it is a decentralized blockchain platform that enables developers to build and deploy smart contracts and applications without central authority control. Unlike Bitcoin, which primarily functions as digital currency, Ethereum operates as a programmable global computer where developers can create any type of ",
 "체인 TVL (DefiLlama)": {
  "체인": "Ethereum",
  "TVL(USD)": 41041532902
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "ETH 관련 기사": [
  {
   "출처": "Cointelegraph",
   "제목": "Ethlabs drops Hegotá slot proposal in push for 2027 quantum readiness",
   "요약": "Ethlabs’ roadmap aims to help Ethereum withstand quantum attacks and give users a way to protect their accounts by 2027.",
   "시각(UTC)": "11-12 10:30"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Deutsche Bank launches crypto custody for companies and institutions",
   "요약": "Clients can store and transfer Bitcoin, Ether and select stablecoins through the bank, which manages their wallets and private keys.",
   "시각(UTC)": "11-11 14:02"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitmine posts $6.3B net loss for fiscal 2026 as Ether prices slide",
   "요약": "Bitmine booked $6.2 billion in unrealized losses on digital assets. It held 6.07 million ETH on Sunday, or 4.97% of Ether’s supply.",
   "시각(UTC)": "11-11 09:58"
  },
  {
   "출처": "Decrypt",
   "제목": "Deutsche Bank Goes Live With Crypto Custody After a Five-Year Buildup",
   "요약": "Deutsche Bank’s custody service now holds Bitcoin, Ethereum and three stablecoins for institutional and corporate clients in Europe.",
   "시각(UTC)": "11-11 19:06"
  },
  {
   "출처": "Decrypt",
   "제목": "Morning Minute: Vitalik Recasts ETH as a Store of Value",
   "요약": "It’s a big shift for Ethereum from the “ultrasound money” days. But can ETH compete as a store-of-value play?",
   "시각(UTC)": "11-10 13:24"
  }
 ],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin dips with Nvidia as ETF outflows reach day five",
   "요약": "Bitcoin slips 0.7% as Nvidia falls on reports its board may oust CEO Jensen Huang, while U.S. spot bitcoin ETFs lose another $299.9 million.",
   "시각(UTC)": "11-12 11:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "Polymarket trims workforce under investor pressure as Kalshi surges ahead",
   "요약": "More than half of those affected were contractors, a source told Reuters. The cuts follow investor pressure on founder Shayne Coplan.",
   "시각(UTC)": "11-12 10:42"
  },
  {
   "출처": "CoinDesk",
   "제목": "Nomura weighs Laser Digital sale as European losses hit four straight quarters",
   "요약": "The Japanese brokerage has held talks with potential buyers, including Marex, as its European business posts more losses.",
   "시각(UTC)": "11-12 10:32"
  },
  {
   "출처": "CoinDesk",
   "제목": "India’s financial crimes watchdog raids crypto exchanges CoinDCX and Delta over alleged illegal cross-border trades",
   "요약": "The Enforcement Directorate alleged illegal cross-border flows that violated India's foreign exchange laws.",
   "시각(UTC)": "11-12 10:10"
  },
  {
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin ETFs bleed $300 million as AI stocks slide again",
   "요약": "Nasdaq 100 futures retreat after Wednesday’s rally, while AI stocks slide, Strategy falls 4% and gold trades below $4,000.",
   "시각(UTC)": "11-12 09:15"
  },
  {
   "출처": "CoinDesk",
   "제목": "Gemini sells UK and European operations to stablecoin payments firm KAST for under $10 million",
   "요약": "The sale follows the Winklevoss-founded crypto exchange’s retreat from several overseas markets as it restructures its business.",
   "시각(UTC)": "11-12 09:07"
  },
  {
   "출처": "CoinDesk",
   "제목": "Canaan may sell more bitcoin for stock buybacks as mining-rig revenue falls 96%",
   "요약": "The Avalon maker has launched a $20 million repurchase program, while most of its bitcoin holdings were pledged or placed in a fixed-term product at September’s end.",
   "시각(UTC)": "11-12 07:41"
  },
  {
   "출처": "CoinDesk",
   "제목": "MSCI is dropping Strategy from its index, and the exclusion could hit its bitcoin-buying machine",
   "요약": "MSCI’s decision to exclude Strategy from its equity indexes could hamper the company’s ability to buy more bitcoin, according to some analysts.",
   "시각(UTC)": "11-12 07:00"
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
   29,
   32,
   29,
   28,
   25,
   28
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.0037,
   "CoinW (Futures)": 0.0047,
   "WEEX (Futures)": 0.0001,
   "OKX (Futures)": 0.0038,
   "WhiteBIT Futures": 0.01
  },
  "미결제약정 합계 USD(상위)": 12788732984
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 85.37,
  "CoinGecko 인기 검색 코인": [
   "SEPPUKU",
   "ZIG",
   "PENGU",
   "BTC",
   "ETH",
   "TAO",
   "ZEC",
   "UNI",
   "PEARL",
   "PI",
   "XRP",
   "HYPE",
   "EPIC",
   "ICP",
   "NEAR"
  ],
  "ETH가 인기 검색에 있음": true
 }
}
```

## ERA

**수집 실패**
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-11",
  "종가": 0.0875,
  "등락률(%)": {
   "1일": 9.1,
   "7일": 27.55,
   "30일": 31.18,
   "90일": 37.58
  },
  "이동평균": {
   "MA20": 0.073465,
   "MA60": 0.068157,
   "MA120": 0.066981
  },
  "종가와 이평선 거리(%)": {
   "MA20": 19.1,
   "MA60": 28.38,
   "MA120": 30.63
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 45
  },
  "RSI14": 64.3,
  "ATR14(%)": 10.7,
  "거래량(20일 평균 대비 배수)": 2.04,
  "30일 최고가": 0.1031,
  "30일 최저가": 0.0564,
  "최근 10일 종가": [
   0.0614,
   0.064,
   0.0686,
   0.0703,
   0.0698,
   0.0724,
   0.0756,
   0.0704,
   0.0802,
   0.0875
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-12",
  "등락률(%)": {
   "1일": 5.31,
   "7일": 8.3,
   "30일": 26.81,
   "90일": 9.6
  },
  "종가와 이평선 거리(%)": {
   "MA20": 15.37,
   "MA60": 26.03,
   "MA120": 22.71
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 30
  },
  "RSI14": 72.4
 }
}
```

### DIANA 자료 · 기본적 분석 (펀더멘털)

```json
{
 "이름": "Caldera",
 "분류": [
  "BNB Chain Ecosystem",
  "Arbitrum Ecosystem",
  "Ethereum Ecosystem",
  "Base Ecosystem",
  "Rollups-as-a-Service (RaaS)"
 ],
 "시가총액 순위": 899,
 "시가총액(USD)": 16529517,
 "완전희석가치 FDV(USD)": 94589511,
 "24시간 거래대금(USD)": 43348496,
 "유통량": 174750000.0,
 "총발행량": 1000000000.0,
 "최대발행량": 1000000000.0,
 "유통 비율(%)": 17.5,
 "역대 최고가(USD)": 1.88,
 "역대 최고가 대비(%)": -94.98724,
 "가격 변화(%)": {
  "7d": 39.47512,
  "30d": 45.54032,
  "1y": -61.60594
 },
 "소개": "Caldera is a rollup platform on Ethereum that enables horizontal scaling and interoperability between rollups. Instead of optimizing a single blockchain, Caldera allows projects to launch customizable rollups while maintaining Ethereum's security and decentralization. The platform introduces the Metalayer, a unifying layer designed to connect rollups across Optimistic and Zero-Knowledge (ZK) frame",
 "체인 TVL (DefiLlama)": {
  "체인": "Eteria",
  "TVL(USD)": 0
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "ERA 관련 기사": [],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin dips with Nvidia as ETF outflows reach day five",
   "요약": "Bitcoin slips 0.7% as Nvidia falls on reports its board may oust CEO Jensen Huang, while U.S. spot bitcoin ETFs lose another $299.9 million.",
   "시각(UTC)": "11-12 11:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "Polymarket trims workforce under investor pressure as Kalshi surges ahead",
   "요약": "More than half of those affected were contractors, a source told Reuters. The cuts follow investor pressure on founder Shayne Coplan.",
   "시각(UTC)": "11-12 10:42"
  },
  {
   "출처": "CoinDesk",
   "제목": "Nomura weighs Laser Digital sale as European losses hit four straight quarters",
   "요약": "The Japanese brokerage has held talks with potential buyers, including Marex, as its European business posts more losses.",
   "시각(UTC)": "11-12 10:32"
  },
  {
   "출처": "CoinDesk",
   "제목": "India’s financial crimes watchdog raids crypto exchanges CoinDCX and Delta over alleged illegal cross-border trades",
   "요약": "The Enforcement Directorate alleged illegal cross-border flows that violated India's foreign exchange laws.",
   "시각(UTC)": "11-12 10:10"
  },
  {
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin ETFs bleed $300 million as AI stocks slide again",
   "요약": "Nasdaq 100 futures retreat after Wednesday’s rally, while AI stocks slide, Strategy falls 4% and gold trades below $4,000.",
   "시각(UTC)": "11-12 09:15"
  },
  {
   "출처": "CoinDesk",
   "제목": "Gemini sells UK and European operations to stablecoin payments firm KAST for under $10 million",
   "요약": "The sale follows the Winklevoss-founded crypto exchange’s retreat from several overseas markets as it restructures its business.",
   "시각(UTC)": "11-12 09:07"
  },
  {
   "출처": "CoinDesk",
   "제목": "Canaan may sell more bitcoin for stock buybacks as mining-rig revenue falls 96%",
   "요약": "The Avalon maker has launched a $20 million repurchase program, while most of its bitcoin holdings were pledged or placed in a fixed-term product at September’s end.",
   "시각(UTC)": "11-12 07:41"
  },
  {
   "출처": "CoinDesk",
   "제목": "MSCI is dropping Strategy from its index, and the exclusion could hit its bitcoin-buying machine",
   "요약": "MSCI’s decision to exclude Strategy from its equity indexes could hamper the company’s ability to buy more bitcoin, according to some analysts.",
   "시각(UTC)": "11-12 07:00"
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
   29,
   32,
   29,
   28,
   25,
   28
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "OrangeX Futures": -0.1398,
   "Binance (Futures)": -0.1068,
   "XT.COM (Derivatives)": -0.1068,
   "Ourbit (Futures)": -0.1071,
   "Bybit (Futures)": -0.0692,
   "Toobit Futures": -0.1071
  },
  "미결제약정 합계 USD(상위)": 52514515
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 50.0,
  "CoinGecko 인기 검색 코인": [
   "SEPPUKU",
   "ZIG",
   "PENGU",
   "BTC",
   "ETH",
   "TAO",
   "ZEC",
   "UNI",
   "PEARL",
   "PI",
   "XRP",
   "HYPE",
   "EPIC",
   "ICP",
   "NEAR"
  ],
  "ERA가 인기 검색에 있음": false
 }
}
```

## TSLAB

**수집 실패**
- VIBE/선물 포지션: ValueError: TSLAB 무기한 선물 자료 없음
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-11",
  "종가": 386.72,
  "등락률(%)": {
   "1일": 1.41,
   "7일": 1.07,
   "30일": 2.59,
   "90일": 13.15
  },
  "이동평균": {
   "MA20": 383.104,
   "MA60": 373.937833,
   "MA120": 359.702917
  },
  "종가와 이평선 거리(%)": {
   "MA20": 0.94,
   "MA60": 3.42,
   "MA120": 7.51
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 69
  },
  "RSI14": 53.8,
  "ATR14(%)": 4.1,
  "거래량(20일 평균 대비 배수)": 0.86,
  "30일 최고가": 414.93,
  "30일 최저가": 335.78,
  "최근 10일 종가": [
   404.93,
   396.29,
   382.63,
   338.62,
   359.51,
   358.49,
   355.33,
   379.2,
   381.33,
   386.72
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-12",
  "등락률(%)": {
   "1일": -0.02,
   "7일": 0.43,
   "30일": 7.84,
   "90일": -6.02
  },
  "종가와 이평선 거리(%)": {
   "MA20": 2.03,
   "MA60": 3.2,
   "MA120": 0.98
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 2
  },
  "RSI14": 61.7
 }
}
```

### DIANA 자료 · 기본적 분석 (펀더멘털)

```json
{
 "이름": "Tesla (bStocks Tokenized Stock)",
 "분류": [
  "Tokenized Assets",
  "BNB Chain Ecosystem",
  "Tokenized Stocks",
  "Real World Assets (RWA)",
  "bStocks Ecosystem"
 ],
 "시가총액 순위": 864,
 "시가총액(USD)": 17841134,
 "완전희석가치 FDV(USD)": 17844222,
 "24시간 거래대금(USD)": 8987007,
 "유통량": 45957.653100460004,
 "총발행량": 45965.60864547,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 435.42,
 "역대 최고가 대비(%)": -10.84386,
 "가격 변화(%)": {
  "7d": 2.71934,
  "30d": 3.55842,
  "1y": null
 },
 "소개": ""
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "TSLAB 관련 기사": [],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin dips with Nvidia as ETF outflows reach day five",
   "요약": "Bitcoin slips 0.7% as Nvidia falls on reports its board may oust CEO Jensen Huang, while U.S. spot bitcoin ETFs lose another $299.9 million.",
   "시각(UTC)": "11-12 11:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "Polymarket trims workforce under investor pressure as Kalshi surges ahead",
   "요약": "More than half of those affected were contractors, a source told Reuters. The cuts follow investor pressure on founder Shayne Coplan.",
   "시각(UTC)": "11-12 10:42"
  },
  {
   "출처": "CoinDesk",
   "제목": "Nomura weighs Laser Digital sale as European losses hit four straight quarters",
   "요약": "The Japanese brokerage has held talks with potential buyers, including Marex, as its European business posts more losses.",
   "시각(UTC)": "11-12 10:32"
  },
  {
   "출처": "CoinDesk",
   "제목": "India’s financial crimes watchdog raids crypto exchanges CoinDCX and Delta over alleged illegal cross-border trades",
   "요약": "The Enforcement Directorate alleged illegal cross-border flows that violated India's foreign exchange laws.",
   "시각(UTC)": "11-12 10:10"
  },
  {
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin ETFs bleed $300 million as AI stocks slide again",
   "요약": "Nasdaq 100 futures retreat after Wednesday’s rally, while AI stocks slide, Strategy falls 4% and gold trades below $4,000.",
   "시각(UTC)": "11-12 09:15"
  },
  {
   "출처": "CoinDesk",
   "제목": "Gemini sells UK and European operations to stablecoin payments firm KAST for under $10 million",
   "요약": "The sale follows the Winklevoss-founded crypto exchange’s retreat from several overseas markets as it restructures its business.",
   "시각(UTC)": "11-12 09:07"
  },
  {
   "출처": "CoinDesk",
   "제목": "Canaan may sell more bitcoin for stock buybacks as mining-rig revenue falls 96%",
   "요약": "The Avalon maker has launched a $20 million repurchase program, while most of its bitcoin holdings were pledged or placed in a fixed-term product at September’s end.",
   "시각(UTC)": "11-12 07:41"
  },
  {
   "출처": "CoinDesk",
   "제목": "MSCI is dropping Strategy from its index, and the exclusion could hit its bitcoin-buying machine",
   "요약": "MSCI’s decision to exclude Strategy from its equity indexes could hamper the company’s ability to buy more bitcoin, according to some analysts.",
   "시각(UTC)": "11-12 07:00"
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
   29,
   32,
   29,
   28,
   25,
   28
  ]
 },
 "선물 포지션": {
  "오류": "ValueError: TSLAB 무기한 선물 자료 없음"
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 0.0,
  "CoinGecko 인기 검색 코인": [
   "SEPPUKU",
   "ZIG",
   "PENGU",
   "BTC",
   "ETH",
   "TAO",
   "ZEC",
   "UNI",
   "PEARL",
   "PI",
   "XRP",
   "HYPE",
   "EPIC",
   "ICP",
   "NEAR"
  ],
  "TSLAB가 인기 검색에 있음": false
 }
}
```

## NVDAB

**수집 실패**
- VIBE/선물 포지션: ValueError: NVDAB 무기한 선물 자료 없음
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-11",
  "종가": 160.65,
  "등락률(%)": {
   "1일": -5.66,
   "7일": -20.18,
   "30일": -28.51,
   "90일": -28.84
  },
  "이동평균": {
   "MA20": 198.64,
   "MA60": 215.9945,
   "MA120": 215.770167
  },
  "종가와 이평선 거리(%)": {
   "MA20": -19.13,
   "MA60": -25.62,
   "MA120": -25.55
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 18
  },
  "RSI14": 20.7,
  "ATR14(%)": 6.65,
  "거래량(20일 평균 대비 배수)": 6.88,
  "30일 최고가": 230.1,
  "30일 최저가": 155.1,
  "최근 10일 종가": [
   203.91,
   208.3,
   201.26,
   180.91,
   188.27,
   187.54,
   179.43,
   180.29,
   170.28,
   160.65
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-12",
  "등락률(%)": {
   "1일": 0.09,
   "7일": -6.93,
   "30일": -14.06,
   "90일": -26.49
  },
  "종가와 이평선 거리(%)": {
   "MA20": -7.15,
   "MA60": -14.17,
   "MA120": -19.22
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 77
  },
  "RSI14": 29.1
 }
}
```

### DIANA 자료 · 기본적 분석 (펀더멘털)

```json
{
 "이름": "NVIDIA (bStocks Tokenized Stock)",
 "분류": [
  "Tokenized Assets",
  "BNB Chain Ecosystem",
  "Tokenized Stocks",
  "Real World Assets (RWA)",
  "bStocks Ecosystem"
 ],
 "시가총액 순위": 201,
 "시가총액(USD)": 145932654,
 "완전희석가치 FDV(USD)": 149518256,
 "24시간 거래대금(USD)": 168663646,
 "유통량": 905889.45305709,
 "총발행량": 928147.38369351,
 "최대발행량": null,
 "유통 비율(%)": 97.6,
 "역대 최고가(USD)": 242.78,
 "역대 최고가 대비(%)": -33.64668,
 "가격 변화(%)": {
  "7d": -19.15654,
  "30d": -28.12202,
  "1y": null
 },
 "소개": ""
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "NVDAB 관련 기사": [],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin dips with Nvidia as ETF outflows reach day five",
   "요약": "Bitcoin slips 0.7% as Nvidia falls on reports its board may oust CEO Jensen Huang, while U.S. spot bitcoin ETFs lose another $299.9 million.",
   "시각(UTC)": "11-12 11:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "Polymarket trims workforce under investor pressure as Kalshi surges ahead",
   "요약": "More than half of those affected were contractors, a source told Reuters. The cuts follow investor pressure on founder Shayne Coplan.",
   "시각(UTC)": "11-12 10:42"
  },
  {
   "출처": "CoinDesk",
   "제목": "Nomura weighs Laser Digital sale as European losses hit four straight quarters",
   "요약": "The Japanese brokerage has held talks with potential buyers, including Marex, as its European business posts more losses.",
   "시각(UTC)": "11-12 10:32"
  },
  {
   "출처": "CoinDesk",
   "제목": "India’s financial crimes watchdog raids crypto exchanges CoinDCX and Delta over alleged illegal cross-border trades",
   "요약": "The Enforcement Directorate alleged illegal cross-border flows that violated India's foreign exchange laws.",
   "시각(UTC)": "11-12 10:10"
  },
  {
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin ETFs bleed $300 million as AI stocks slide again",
   "요약": "Nasdaq 100 futures retreat after Wednesday’s rally, while AI stocks slide, Strategy falls 4% and gold trades below $4,000.",
   "시각(UTC)": "11-12 09:15"
  },
  {
   "출처": "CoinDesk",
   "제목": "Gemini sells UK and European operations to stablecoin payments firm KAST for under $10 million",
   "요약": "The sale follows the Winklevoss-founded crypto exchange’s retreat from several overseas markets as it restructures its business.",
   "시각(UTC)": "11-12 09:07"
  },
  {
   "출처": "CoinDesk",
   "제목": "Canaan may sell more bitcoin for stock buybacks as mining-rig revenue falls 96%",
   "요약": "The Avalon maker has launched a $20 million repurchase program, while most of its bitcoin holdings were pledged or placed in a fixed-term product at September’s end.",
   "시각(UTC)": "11-12 07:41"
  },
  {
   "출처": "CoinDesk",
   "제목": "MSCI is dropping Strategy from its index, and the exclusion could hit its bitcoin-buying machine",
   "요약": "MSCI’s decision to exclude Strategy from its equity indexes could hamper the company’s ability to buy more bitcoin, according to some analysts.",
   "시각(UTC)": "11-12 07:00"
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
   29,
   32,
   29,
   28,
   25,
   28
  ]
 },
 "선물 포지션": {
  "오류": "ValueError: NVDAB 무기한 선물 자료 없음"
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": null,
  "CoinGecko 인기 검색 코인": [
   "SEPPUKU",
   "ZIG",
   "PENGU",
   "BTC",
   "ETH",
   "TAO",
   "ZEC",
   "UNI",
   "PEARL",
   "PI",
   "XRP",
   "HYPE",
   "EPIC",
   "ICP",
   "NEAR"
  ],
  "NVDAB가 인기 검색에 있음": false
 }
}
```
