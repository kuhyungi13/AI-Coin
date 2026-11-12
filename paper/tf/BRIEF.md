# TF팀 회의 자료 (2026-11-12 15:43 KST)

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
   "1일": -0.28,
   "7일": 0.02,
   "30일": -2.75,
   "90일": -9.04
  },
  "종가와 이평선 거리(%)": {
   "MA20": -0.67,
   "MA60": -3.13,
   "MA120": -5.31
  },
  "MA20>MA60": false,
  "최근 교차": null,
  "RSI14": 40.5
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
 "시가총액(USD)": 1479152835001,
 "완전희석가치 FDV(USD)": 1479152835001,
 "24시간 거래대금(USD)": 25008525914,
 "유통량": 20110993.0,
 "총발행량": 20110993.0,
 "최대발행량": 21000000.0,
 "유통 비율(%)": 95.8,
 "역대 최고가(USD)": 126080,
 "역대 최고가 대비(%)": -41.66439,
 "가격 변화(%)": {
  "7d": -8.4686,
  "30d": -12.0294,
  "1y": -28.82703
 },
 "소개": "Bitcoin is the world's first decentralized cryptocurrency, created in 2009 by the pseudonymous Satoshi Nakamoto. It enables peer-to-peer electronic cash transactions without intermediaries like banks or governments, operating on a blockchain secured by Proof of Work mining and the SHA-256 cryptographic algorithm. \n\nWith a fixed supply cap of 21 million coins and programmatic halvings every four ye",
 "체인 TVL (DefiLlama)": {
  "체인": "Bitcoin",
  "TVL(USD)": 3871470496
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "BTC 관련 기사": [
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
   "출처": "CoinDesk",
   "제목": "Bitcoin breaks with stocks, declines as ETF outflows mount, MARA reduces holdings",
   "요약": "Your day-ahead look for Nov. 10, 2026",
   "시각(UTC)": "11-10 12:15"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin lags stock rebound in advance of U.S. inflation report",
   "요약": "Bitcoin slipped despite a Monday rebound in U.S. stocks, with spot ETFs losing $201 million as traders await October inflation data later today.",
   "시각(UTC)": "11-10 11:24"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin slips before U.S. inflation report as traders price in Fed rate increase",
   "요약": "Fed Governor Waller backs December tightening even if inflation cools, while falling oil prices offer some relief and Anthropic withdraws IPO pricing details.",
   "시각(UTC)": "11-10 10:48"
  },
  {
   "출처": "CoinDesk",
   "제목": "Live news: Bitcoin falls to nearly three-month low after disappointing inflation data",
   "요약": "A rate hike in December appears totally assured now, with Fed Governor Chris Waller suggesting even a 50-basis-point move could be appropriate.",
   "시각(UTC)": "11-10 10:41"
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
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin Covenants Part 5: MATT and OP_CHECKCONTRACTVERIFY — How Bitcoin could carry state across transactions",
   "요약": "OP_CCV embeds contract state directly into Taproot output keys and enforces valid state transitions onchain. This makes it possible to achieve stateful contracts and compact fraud proofs.",
   "시각(UTC)": "11-11 13:26"
  }
 ],
 "시장 전반 기사": [
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Meet Spiko, the largest tokenized fund in the world you’ve probably never heard about",
   "요약": "The firm’s flagship Spiko Amundi Overnight Swap Fund (SAFO) held $2.39 billion in assets under management as of late last month.",
   "시각(UTC)": "11-11 12:57"
  },
  {
   "출처": "CoinDesk",
   "제목": "Kraken's xStocks adds 200 UK and EU shares as its assets top $1.1 billion",
   "요약": "Payward says xStocks holds over $1.1 billion. Each token is backed by a share but gives no ownership of the underlying company.",
   "시각(UTC)": "11-11 10:51"
  },
  {
   "출처": "CoinDesk",
   "제목": "Warren: What is White House doing to prevent a repeat of teleprompter's Trump bets?",
   "요약": "U.S. Senator Elizabeth Warren argued the administration is not doing enough about staff insider trading, questioning whether CFTC enforcement action was sufficient.",
   "시각(UTC)": "11-10 20:36"
  },
  {
   "출처": "CoinDesk",
   "제목": "Former NYSE president says stock issuers hold the key to tokenization as Bullish builds its platform",
   "요약": "Stacey Cunningham, who recently joined digital asset platform Bullish as President, sees the company’s planned Equiniti acquisition and focus on stock issuers as key to its tokenization ambitions.",
   "시각(UTC)": "11-10 20:15"
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
   "Binance (Futures)": 0.0077,
   "OKX (Futures)": 0.01,
   "Bybit (Futures)": 0.0063,
   "MEXC (Futures)": 0.0077,
   "Gate (Futures)": 0.01,
   "CoinW (Futures)": 0.0077
  },
  "미결제약정 합계 USD(상위)": 18814291203
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 66.67,
  "CoinGecko 인기 검색 코인": [
   "ZIG",
   "GRAM",
   "PENGU",
   "BTC",
   "ZEC",
   "PEARL",
   "ZRO",
   "INIT",
   "HYPE",
   "XRP",
   "SOL",
   "PEPE",
   "TAO",
   "SUI",
   "STRK"
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
   "1일": -0.06,
   "7일": 0.09,
   "30일": -8.46,
   "90일": -12.94
  },
  "종가와 이평선 거리(%)": {
   "MA20": -1.64,
   "MA60": -7.28,
   "MA120": -9.33
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 24
  },
  "RSI14": 35.1
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
 "시가총액(USD)": 250089851554,
 "완전희석가치 FDV(USD)": 250089851554,
 "24시간 거래대금(USD)": 8904505424,
 "유통량": 122212724.4774798,
 "총발행량": 122212724.4774798,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 4946.05,
 "역대 최고가 대비(%)": -58.62657,
 "가격 변화(%)": {
  "7d": -15.36135,
  "30d": -19.0949,
  "1y": -40.64153
 },
 "소개": "Ethereum is a global, open-source platform for decentralized applications. In other words, it is a decentralized blockchain platform that enables developers to build and deploy smart contracts and applications without central authority control. Unlike Bitcoin, which primarily functions as digital currency, Ethereum operates as a programmable global computer where developers can create any type of ",
 "체인 TVL (DefiLlama)": {
  "체인": "Ethereum",
  "TVL(USD)": 41164158133
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "ETH 관련 기사": [
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
   "제목": "Zcash holders to vote on pulling 50,000 ZEC, worth $50 million, from grants treasury",
   "요약": "The proposal would remove more than half of Zcash Community Grants' ZEC holdings from circulation and redirect its future block rewards into a new development and legal-defense fund.",
   "시각(UTC)": "11-12 05:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin Core reveals bug that made thousands of nodes trust any stranger on Tor",
   "요약": "The flaw was fixed in October 2025 and kept quiet until Tuesday. It came out alongside a high-severity bug that could stop a miner from producing blocks until someone restarted it.",
   "시각(UTC)": "11-12 05:22"
  },
  {
   "출처": "CoinDesk",
   "제목": "Ripple’s bank-lending system moves closer to launch on the XRP Ledger",
   "요약": "Lending support among the ledger’s 35 validators has climbed from 19 to 22 since mid-October, and no public tracker shows which validators switched.",
   "시각(UTC)": "11-12 05:18"
  },
  {
   "출처": "CoinDesk",
   "제목": "Nvidia perps crash 7% as CEO Jensen Huang reportedly faces the axe",
   "요약": "Nvidia perps are down 7% on Hyperliquid as traders react to reports that CEO Jensen Huang may be removed. Bitcoin continues to trade in a familiar price range.",
   "시각(UTC)": "11-12 04:03"
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Meet Spiko, the largest tokenized fund in the world you’ve probably never heard about",
   "요약": "The firm’s flagship Spiko Amundi Overnight Swap Fund (SAFO) held $2.39 billion in assets under management as of late last month.",
   "시각(UTC)": "11-11 12:57"
  },
  {
   "출처": "CoinDesk",
   "제목": "Live news: Bitcoin remains under pressure as CoreWeave, Nvidia lead AI rebound",
   "요약": "The DRAM ETF jumps 8% and semiconductor stocks gain more than 4%, while bitcoin continues to test its 200-day moving average.",
   "시각(UTC)": "11-11 12:21"
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
   "Binance (Futures)": 0.0065,
   "CoinW (Futures)": 0.0057,
   "WEEX (Futures)": 0.0001,
   "OKX (Futures)": 0.0042,
   "WhiteBIT Futures": 0.01
  },
  "미결제약정 합계 USD(상위)": 12779182598
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 84.09,
  "CoinGecko 인기 검색 코인": [
   "ZIG",
   "GRAM",
   "PENGU",
   "BTC",
   "ZEC",
   "PEARL",
   "ZRO",
   "INIT",
   "HYPE",
   "XRP",
   "SOL",
   "PEPE",
   "TAO",
   "SUI",
   "STRK"
  ],
  "ETH가 인기 검색에 있음": false
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
   "1일": -0.91,
   "7일": 8.1,
   "30일": 20.92,
   "90일": 11.44
  },
  "종가와 이평선 거리(%)": {
   "MA20": 10.65,
   "MA60": 20.47,
   "MA120": 16.78
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 29
  },
  "RSI14": 67.0
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
 "시가총액 순위": 898,
 "시가총액(USD)": 16395655,
 "완전희석가치 FDV(USD)": 93823488,
 "24시간 거래대금(USD)": 54637213,
 "유통량": 174750000.0,
 "총발행량": 1000000000.0,
 "최대발행량": 1000000000.0,
 "유통 비율(%)": 17.5,
 "역대 최고가(USD)": 1.88,
 "역대 최고가 대비(%)": -94.99864,
 "가격 변화(%)": {
  "7d": 39.21809,
  "30d": 38.3637,
  "1y": -60.94835
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
   "제목": "Zcash holders to vote on pulling 50,000 ZEC, worth $50 million, from grants treasury",
   "요약": "The proposal would remove more than half of Zcash Community Grants' ZEC holdings from circulation and redirect its future block rewards into a new development and legal-defense fund.",
   "시각(UTC)": "11-12 05:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin Core reveals bug that made thousands of nodes trust any stranger on Tor",
   "요약": "The flaw was fixed in October 2025 and kept quiet until Tuesday. It came out alongside a high-severity bug that could stop a miner from producing blocks until someone restarted it.",
   "시각(UTC)": "11-12 05:22"
  },
  {
   "출처": "CoinDesk",
   "제목": "Ripple’s bank-lending system moves closer to launch on the XRP Ledger",
   "요약": "Lending support among the ledger’s 35 validators has climbed from 19 to 22 since mid-October, and no public tracker shows which validators switched.",
   "시각(UTC)": "11-12 05:18"
  },
  {
   "출처": "CoinDesk",
   "제목": "Nvidia perps crash 7% as CEO Jensen Huang reportedly faces the axe",
   "요약": "Nvidia perps are down 7% on Hyperliquid as traders react to reports that CEO Jensen Huang may be removed. Bitcoin continues to trade in a familiar price range.",
   "시각(UTC)": "11-12 04:03"
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Meet Spiko, the largest tokenized fund in the world you’ve probably never heard about",
   "요약": "The firm’s flagship Spiko Amundi Overnight Swap Fund (SAFO) held $2.39 billion in assets under management as of late last month.",
   "시각(UTC)": "11-11 12:57"
  },
  {
   "출처": "CoinDesk",
   "제목": "Live news: Bitcoin remains under pressure as CoreWeave, Nvidia lead AI rebound",
   "요약": "The DRAM ETF jumps 8% and semiconductor stocks gain more than 4%, while bitcoin continues to test its 200-day moving average.",
   "시각(UTC)": "11-11 12:21"
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
   "OrangeX Futures": -0.3162,
   "Binance (Futures)": -0.138,
   "XT.COM (Derivatives)": -0.1418,
   "Ourbit (Futures)": -0.1399,
   "Toobit Futures": -0.1393,
   "Bybit (Futures)": -0.2666
  },
  "미결제약정 합계 USD(상위)": 51512342
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 100.0,
  "CoinGecko 인기 검색 코인": [
   "ZIG",
   "GRAM",
   "PENGU",
   "BTC",
   "ZEC",
   "PEARL",
   "ZRO",
   "INIT",
   "HYPE",
   "XRP",
   "SOL",
   "PEPE",
   "TAO",
   "SUI",
   "STRK"
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
   "1일": 0.17,
   "7일": 1.58,
   "30일": 7.79,
   "90일": -5.14
  },
  "종가와 이평선 거리(%)": {
   "MA20": 2.48,
   "MA60": 3.16,
   "MA120": 1.02
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 1
  },
  "RSI14": 61.8
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
 "시가총액 순위": 867,
 "시가총액(USD)": 17742716,
 "완전희석가치 FDV(USD)": 17742716,
 "24시간 거래대금(USD)": 9182172,
 "유통량": 45948.25516576,
 "총발행량": 45948.25516576,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 435.42,
 "역대 최고가 대비(%)": -11.31754,
 "가격 변화(%)": {
  "7d": 2.48055,
  "30d": 3.04971,
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
   "제목": "Zcash holders to vote on pulling 50,000 ZEC, worth $50 million, from grants treasury",
   "요약": "The proposal would remove more than half of Zcash Community Grants' ZEC holdings from circulation and redirect its future block rewards into a new development and legal-defense fund.",
   "시각(UTC)": "11-12 05:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin Core reveals bug that made thousands of nodes trust any stranger on Tor",
   "요약": "The flaw was fixed in October 2025 and kept quiet until Tuesday. It came out alongside a high-severity bug that could stop a miner from producing blocks until someone restarted it.",
   "시각(UTC)": "11-12 05:22"
  },
  {
   "출처": "CoinDesk",
   "제목": "Ripple’s bank-lending system moves closer to launch on the XRP Ledger",
   "요약": "Lending support among the ledger’s 35 validators has climbed from 19 to 22 since mid-October, and no public tracker shows which validators switched.",
   "시각(UTC)": "11-12 05:18"
  },
  {
   "출처": "CoinDesk",
   "제목": "Nvidia perps crash 7% as CEO Jensen Huang reportedly faces the axe",
   "요약": "Nvidia perps are down 7% on Hyperliquid as traders react to reports that CEO Jensen Huang may be removed. Bitcoin continues to trade in a familiar price range.",
   "시각(UTC)": "11-12 04:03"
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Meet Spiko, the largest tokenized fund in the world you’ve probably never heard about",
   "요약": "The firm’s flagship Spiko Amundi Overnight Swap Fund (SAFO) held $2.39 billion in assets under management as of late last month.",
   "시각(UTC)": "11-11 12:57"
  },
  {
   "출처": "CoinDesk",
   "제목": "Live news: Bitcoin remains under pressure as CoreWeave, Nvidia lead AI rebound",
   "요약": "The DRAM ETF jumps 8% and semiconductor stocks gain more than 4%, while bitcoin continues to test its 200-day moving average.",
   "시각(UTC)": "11-11 12:21"
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
  "CoinGecko 이용자 투표 상승(%)": null,
  "CoinGecko 인기 검색 코인": [
   "ZIG",
   "GRAM",
   "PENGU",
   "BTC",
   "ZEC",
   "PEARL",
   "ZRO",
   "INIT",
   "HYPE",
   "XRP",
   "SOL",
   "PEPE",
   "TAO",
   "SUI",
   "STRK"
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
   "1일": 0.3,
   "7일": -5.37,
   "30일": -14.12,
   "90일": -26.36
  },
  "종가와 이평선 거리(%)": {
   "MA20": -7.71,
   "MA60": -14.6,
   "MA120": -19.47
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 76
  },
  "RSI14": 28.8
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
 "시가총액 순위": 205,
 "시가총액(USD)": 141987472,
 "완전희석가치 FDV(USD)": 141987472,
 "24시간 거래대금(USD)": 165426109,
 "유통량": 882049.72679092,
 "총발행량": 882049.72679092,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 242.78,
 "역대 최고가 대비(%)": -33.6956,
 "가격 변화(%)": {
  "7d": -18.50114,
  "30d": -28.23825,
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
   "제목": "Zcash holders to vote on pulling 50,000 ZEC, worth $50 million, from grants treasury",
   "요약": "The proposal would remove more than half of Zcash Community Grants' ZEC holdings from circulation and redirect its future block rewards into a new development and legal-defense fund.",
   "시각(UTC)": "11-12 05:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin Core reveals bug that made thousands of nodes trust any stranger on Tor",
   "요약": "The flaw was fixed in October 2025 and kept quiet until Tuesday. It came out alongside a high-severity bug that could stop a miner from producing blocks until someone restarted it.",
   "시각(UTC)": "11-12 05:22"
  },
  {
   "출처": "CoinDesk",
   "제목": "Ripple’s bank-lending system moves closer to launch on the XRP Ledger",
   "요약": "Lending support among the ledger’s 35 validators has climbed from 19 to 22 since mid-October, and no public tracker shows which validators switched.",
   "시각(UTC)": "11-12 05:18"
  },
  {
   "출처": "CoinDesk",
   "제목": "Nvidia perps crash 7% as CEO Jensen Huang reportedly faces the axe",
   "요약": "Nvidia perps are down 7% on Hyperliquid as traders react to reports that CEO Jensen Huang may be removed. Bitcoin continues to trade in a familiar price range.",
   "시각(UTC)": "11-12 04:03"
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Meet Spiko, the largest tokenized fund in the world you’ve probably never heard about",
   "요약": "The firm’s flagship Spiko Amundi Overnight Swap Fund (SAFO) held $2.39 billion in assets under management as of late last month.",
   "시각(UTC)": "11-11 12:57"
  },
  {
   "출처": "CoinDesk",
   "제목": "Live news: Bitcoin remains under pressure as CoreWeave, Nvidia lead AI rebound",
   "요약": "The DRAM ETF jumps 8% and semiconductor stocks gain more than 4%, while bitcoin continues to test its 200-day moving average.",
   "시각(UTC)": "11-11 12:21"
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
   "ZIG",
   "GRAM",
   "PENGU",
   "BTC",
   "ZEC",
   "PEARL",
   "ZRO",
   "INIT",
   "HYPE",
   "XRP",
   "SOL",
   "PEPE",
   "TAO",
   "SUI",
   "STRK"
  ],
  "NVDAB가 인기 검색에 있음": false
 }
}
```
