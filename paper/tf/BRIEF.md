# TF팀 회의 자료 (2026-11-11 22:54 KST)

GitHub Actions가 무료 공개 API로 모은 자료입니다. 회의 진행 방법은 `aicoin/tf_team/PLAYBOOK.md`.
자료에 없는 숫자는 쓰지 않습니다. 실패한 자료는 아래 '수집 실패'에 있습니다.

분석 대상: BTC, ETH, PEPE, INJ, XRP

**지금까지 승률** ACE 40.9% (9/22), 채점 대기 0개 · 자세히는 `paper/tf/SCOREBOARD.md`, 교훈은 `aicoin/tf_team/LESSONS.md`

**TRAINER 모의 계좌** 총자산 10,017.55 USDT (+0.18%), 보유 없음 · 자세히는 `paper/tf/trainer/TRAINER.md`

**전체 스캔 후보** (`paper/tf/SCAN.md`) 상승 추세: PEPE, INJ · 과매도 반등: XRP

## BTC

**수집 실패**
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-10",
  "종가": 73796.06,
  "등락률(%)": {
   "1일": -2.09,
   "7일": -4.72,
   "30일": -11.91,
   "90일": 16.25
  },
  "이동평균": {
   "MA20": 78196.883,
   "MA60": 81049.283833,
   "MA120": 75393.05925
  },
  "종가와 이평선 거리(%)": {
   "MA20": -5.63,
   "MA60": -8.95,
   "MA120": -2.12
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 11
  },
  "RSI14": 34.0,
  "ATR14(%)": 3.29,
  "거래량(20일 평균 대비 배수)": 1.14,
  "30일 최고가": 84898.0,
  "30일 최저가": 72727.27,
  "최근 10일 종가": [
   78354.0,
   76816.0,
   77453.86,
   80504.01,
   76088.01,
   75844.0,
   75867.59,
   74851.44,
   75368.41,
   73796.06
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-11",
  "등락률(%)": {
   "1일": -0.13,
   "7일": -1.14,
   "30일": -2.83,
   "90일": -7.41
  },
  "종가와 이평선 거리(%)": {
   "MA20": -0.94,
   "MA60": -3.24,
   "MA120": -5.37
  },
  "MA20>MA60": false,
  "최근 교차": null,
  "RSI14": 41.0
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
 "시가총액(USD)": 1483130907662,
 "완전희석가치 FDV(USD)": 1483133193864,
 "24시간 거래대금(USD)": 30784232818,
 "유통량": 20110675.0,
 "총발행량": 20110706.0,
 "최대발행량": 21000000.0,
 "유통 비율(%)": 95.8,
 "역대 최고가(USD)": 126080,
 "역대 최고가 대비(%)": -41.50673,
 "가격 변화(%)": {
  "7d": -5.70949,
  "30d": -10.82431,
  "1y": -29.50651
 },
 "소개": "Bitcoin is the world's first decentralized cryptocurrency, created in 2009 by the pseudonymous Satoshi Nakamoto. It enables peer-to-peer electronic cash transactions without intermediaries like banks or governments, operating on a blockchain secured by Proof of Work mining and the SHA-256 cryptographic algorithm. \n\nWith a fixed supply cap of 21 million coins and programmatic halvings every four ye",
 "체인 TVL (DefiLlama)": {
  "체인": "Bitcoin",
  "TVL(USD)": 3897300877
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "BTC 관련 기사": [
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
   "출처": "CoinDesk",
   "제목": "Bitcoin miner MARA sold 13,597 BTC for $1.1 billion in six weeks, plans to sell more",
   "요약": "MARA paid off every loan backed by its bitcoin and says the rest of its coins can fund AI datacenters.",
   "시각(UTC)": "11-10 05:18"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin faces U.S. CPI test as analysts warn inflation relief may not be enough",
   "요약": "Bitcoin trades below $75,000 ahead of the October inflation data. Analysts warning that sustainable recovery depends on improving liquidity and spot ETF demand rather than temporary macro relief.",
   "시각(UTC)": "11-10 03:22"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Here’s what happened in crypto today",
   "요약": "Need to know what happened in crypto today? Here is the latest news on daily trends and events impacting Bitcoin price, blockchain, DeFi, Web3 and crypto regulation.",
   "시각(UTC)": "11-11 13:38"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin Covenants Part 5: MATT and OP_CHECKCONTRACTVERIFY — How Bitcoin could carry state across transactions",
   "요약": "OP_CCV embeds contract state directly into Taproot output keys and enforces valid state transitions onchain. This makes it possible to achieve stateful contracts and compact fraud proofs.",
   "시각(UTC)": "11-11 13:26"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Barclays boosts BlackRock Bitcoin ETF stake 48% as banks expand holdings",
   "요약": "Barclays reported a $187 million stake as of Sept. 30, while Citigroup disclosed a new $119 million position in Fidelity’s Bitcoin ETF.",
   "시각(UTC)": "11-11 11:56"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin short-term holders send 47K BTC to exchanges at a loss",
   "요약": "Bitcoin fell to an 11-week low of $72,670 after slipping below short-term holders’ average cost basis of about $75,700, according to CryptoQuant.",
   "시각(UTC)": "11-11 11:05"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Stock ETF buyers pounce on dip as Bitcoin funds bleed $1.6 billion",
   "요약": "US spot Bitcoin ETFs have lost $1.6 billion in November, while stock funds attracted billions of dollars from investors buying the dip.",
   "시각(UTC)": "11-11 08:55"
  }
 ],
 "시장 전반 기사": [
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Goldman Sachs, Citi among banks said to commit $270 million to stablecoin venture",
   "요약": "The venture, known as Project Faro, plans to issue a dollar-denominated stablecoin and is expected to be incorporated in the U.S.",
   "시각(UTC)": "11-10 17:32"
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto is now teamed up with U.S. government in two legal battles over perps",
   "요약": "Twice now, crypto firms have found themselves on the side of the U.S. Commodity Futures Trading Commission in holding that perpetual futures aren't swaps.",
   "시각(UTC)": "11-10 17:07"
  },
  {
   "출처": "CoinDesk",
   "제목": "Plume affiliate lands broker-dealer license to bring real U.S. assets onchain",
   "요약": "Kimber Digital Securities secured SEC and Finra approvals, a regulatory milestone paving the way for the delivery of legally binding claims, dividends, and yield-bearing products directly to self-custodial wallets and stablecoin application",
   "시각(UTC)": "11-10 15:51"
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
   32,
   29,
   28,
   25,
   28,
   50
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.0062,
   "OKX (Futures)": 0.0035,
   "Bybit (Futures)": 0.0066,
   "MEXC (Futures)": 0.0061,
   "Gate (Futures)": 0.0039,
   "WEEX (Futures)": 0.0001
  },
  "미결제약정 합계 USD(상위)": 19210952662
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 54.49,
  "CoinGecko 인기 검색 코인": [
   "DOGE",
   "GRAM",
   "ZEC",
   "BTC",
   "XRP",
   "HYPE",
   "PEARL",
   "KNTQ",
   "AVAX",
   "LIT",
   "PUMP",
   "ARIA",
   "QTC",
   "SHIB",
   "PI"
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
  "기준일": "2026-11-10",
  "종가": 2053.21,
  "등락률(%)": {
   "1일": -3.84,
   "7일": -9.74,
   "30일": -19.07,
   "90일": 9.22
  },
  "이동평균": {
   "MA20": 2275.758,
   "MA60": 2472.880667,
   "MA120": 2294.620167
  },
  "종가와 이평선 거리(%)": {
   "MA20": -9.78,
   "MA60": -16.97,
   "MA120": -10.52
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 21
  },
  "RSI14": 29.6,
  "ATR14(%)": 4.99,
  "거래량(20일 평균 대비 배수)": 1.44,
  "30일 최고가": 2579.88,
  "30일 최저가": 2006.0,
  "최근 10일 종가": [
   2275.31,
   2253.29,
   2274.77,
   2424.61,
   2238.01,
   2238.67,
   2240.24,
   2127.46,
   2135.24,
   2053.21
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-11",
  "등락률(%)": {
   "1일": -0.61,
   "7일": -2.78,
   "30일": -8.32,
   "90일": -11.18
  },
  "종가와 이평선 거리(%)": {
   "MA20": -3.15,
   "MA60": -7.78,
   "MA120": -9.68
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 20
  },
  "RSI14": 33.3
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
 "시가총액(USD)": 250731478414,
 "완전희석가치 FDV(USD)": 250731478414,
 "24시간 거래대금(USD)": 12045613338,
 "유통량": 122209757.95344049,
 "총발행량": 122209757.95344049,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 4946.05,
 "역대 최고가 대비(%)": -58.52054,
 "가격 변화(%)": {
  "7d": -11.26445,
  "30d": -18.90618,
  "1y": -42.08282
 },
 "소개": "Ethereum is a global, open-source platform for decentralized applications. In other words, it is a decentralized blockchain platform that enables developers to build and deploy smart contracts and applications without central authority control. Unlike Bitcoin, which primarily functions as digital currency, Ethereum operates as a programmable global computer where developers can create any type of ",
 "체인 TVL (DefiLlama)": {
  "체인": "Ethereum",
  "TVL(USD)": 40927782301
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "ETH 관련 기사": [
  {
   "출처": "CoinDesk",
   "제목": "An 11-year-old Ethereum wallet moved $4.6 million and dodged a scam set up in minutes",
   "요약": "Bots spotted a wallet from Ethereum’s 2015 launch the moment it stirred and planted lookalike addresses in its history, but the owner sent the money to the right place anyway.",
   "시각(UTC)": "11-10 07:01"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitmine posts $6.3B net loss for fiscal 2026 as Ether prices slide",
   "요약": "Bitmine booked $6.2 billion in unrealized losses on digital assets. It held 6.07 million ETH on Sunday, or 4.97% of Ether’s supply.",
   "시각(UTC)": "11-11 09:58"
  },
  {
   "출처": "Decrypt",
   "제목": "Morning Minute: Vitalik Recasts ETH as a Store of Value",
   "요약": "It’s a big shift for Ethereum from the “ultrasound money” days. But can ETH compete as a store-of-value play?",
   "시각(UTC)": "11-10 13:24"
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
   "제목": "Kraken's xStocks adds 200 UK and EU shares as its assets top $1.1 billion",
   "요약": "Payward says xStocks holds over $1.1 billion. Each token is backed by a share but gives no ownership of the underlying company.",
   "시각(UTC)": "11-11 10:51"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin stuck under $74,000 as CoreWeave earnings revive AI outlook, Anthropic said to raise IPO valuation",
   "요약": "CoreWeave’s revenue surge lifted AI infrastructure stocks and Nasdaq futures, while bitcoin was little changed over 24 hours.",
   "시각(UTC)": "11-11 10:45"
  },
  {
   "출처": "CoinDesk",
   "제목": "Warren: What is White House doing to prevent a repeat of teleprompter's Trump bets?",
   "요약": "U.S. Senator Elizabeth Warren argued the administration is not doing enough about staff insider trading, questioning whether CFTC enforcement action was sufficient.",
   "시각(UTC)": "11-10 20:36"
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
   32,
   29,
   28,
   25,
   28,
   50
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.0046,
   "CoinW (Futures)": 0.0071,
   "WEEX (Futures)": -0.0,
   "OKX (Futures)": 0.0077,
   "WhiteBIT Futures": 0.01
  },
  "미결제약정 합계 USD(상위)": 12807617628
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 80.39,
  "CoinGecko 인기 검색 코인": [
   "DOGE",
   "GRAM",
   "ZEC",
   "BTC",
   "XRP",
   "HYPE",
   "PEARL",
   "KNTQ",
   "AVAX",
   "LIT",
   "PUMP",
   "ARIA",
   "QTC",
   "SHIB",
   "PI"
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
  "기준일": "2026-11-10",
  "종가": 5e-06,
  "등락률(%)": {
   "1일": 5.08,
   "7일": 10.47,
   "30일": 27.49,
   "90일": 100.75
  },
  "이동평균": {
   "MA20": 5e-06,
   "MA60": 4e-06,
   "MA120": 4e-06
  },
  "종가와 이평선 거리(%)": {
   "MA20": 12.28,
   "MA60": 23.83,
   "MA120": 44.13
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 105
  },
  "RSI14": 64.7,
  "ATR14(%)": 10.1,
  "거래량(20일 평균 대비 배수)": 1.28,
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
  "기준일": "2026-11-11",
  "등락률(%)": {
   "1일": -5.13,
   "7일": -6.73,
   "30일": -1.58,
   "90일": 16.59
  },
  "종가와 이평선 거리(%)": {
   "MA20": -3.14,
   "MA60": 0.21,
   "MA120": 3.08
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 17
  },
  "RSI14": 44.0
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
 "시가총액(USD)": 2096434845,
 "완전희석가치 FDV(USD)": 2096434845,
 "24시간 거래대금(USD)": 791751334,
 "유통량": 420690000000000.0,
 "총발행량": 420690000000000.0,
 "최대발행량": 420690000000000.0,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 2.803e-05,
 "역대 최고가 대비(%)": -82.22092,
 "가격 변화(%)": {
  "7d": 0.09009,
  "30d": 19.76689,
  "1y": -16.87926
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
   "제목": "Kraken's xStocks adds 200 UK and EU shares as its assets top $1.1 billion",
   "요약": "Payward says xStocks holds over $1.1 billion. Each token is backed by a share but gives no ownership of the underlying company.",
   "시각(UTC)": "11-11 10:51"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin stuck under $74,000 as CoreWeave earnings revive AI outlook, Anthropic said to raise IPO valuation",
   "요약": "CoreWeave’s revenue surge lifted AI infrastructure stocks and Nasdaq futures, while bitcoin was little changed over 24 hours.",
   "시각(UTC)": "11-11 10:45"
  },
  {
   "출처": "CoinDesk",
   "제목": "Warren: What is White House doing to prevent a repeat of teleprompter's Trump bets?",
   "요약": "U.S. Senator Elizabeth Warren argued the administration is not doing enough about staff insider trading, questioning whether CFTC enforcement action was sufficient.",
   "시각(UTC)": "11-10 20:36"
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
   32,
   29,
   28,
   25,
   28,
   50
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "MEXC (Futures)": -0.0245,
   "Gate (Futures)": -0.0245,
   "OKX (Futures)": -0.0098,
   "Bitget Futures": 0.0017,
   "WhiteBIT Futures": 0.01,
   "BloFin (Futures)": -0.0068
  },
  "미결제약정 합계 USD(상위)": 201308132
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 86.96,
  "CoinGecko 인기 검색 코인": [
   "DOGE",
   "GRAM",
   "ZEC",
   "BTC",
   "XRP",
   "HYPE",
   "PEARL",
   "KNTQ",
   "AVAX",
   "LIT",
   "PUMP",
   "ARIA",
   "QTC",
   "SHIB",
   "PI"
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
  "기준일": "2026-11-10",
  "종가": 8.018,
  "등락률(%)": {
   "1일": -1.2,
   "7일": 10.62,
   "30일": 3.3,
   "90일": 73.36
  },
  "이동평균": {
   "MA20": 7.7731,
   "MA60": 7.612483,
   "MA120": 6.300133
  },
  "종가와 이평선 거리(%)": {
   "MA20": 3.15,
   "MA60": 5.33,
   "MA120": 27.27
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 69
  },
  "RSI14": 53.0,
  "ATR14(%)": 7.48,
  "거래량(20일 평균 대비 배수)": 1.19,
  "30일 최고가": 9.417,
  "30일 최저가": 6.823,
  "최근 10일 종가": [
   7.185,
   6.983,
   7.248,
   7.937,
   8.148,
   8.297,
   8.262,
   8.049,
   8.115,
   8.018
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-11",
  "등락률(%)": {
   "1일": -4.52,
   "7일": -2.19,
   "30일": -3.14,
   "90일": 1.33
  },
  "종가와 이평선 거리(%)": {
   "MA20": -2.15,
   "MA60": 0.85,
   "MA120": 1.84
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 33
  },
  "RSI14": 46.1
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
 "시가총액 순위": 83,
 "시가총액(USD)": 787259030,
 "완전희석가치 FDV(USD)": 787259030,
 "24시간 거래대금(USD)": 102783926,
 "유통량": 100000000.0,
 "총발행량": 100000000.0,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 52.62,
 "역대 최고가 대비(%)": -85.04048,
 "가격 변화(%)": {
  "7d": 2.89898,
  "30d": -0.39007,
  "1y": 2.60697
 },
 "소개": "Injective is an interoperable Layer 1 blockchain designed for DeFi applications. It provides developers with on-chain financial infrastructure modules to build dApps such as decentralized exchanges, prediction markets, and lending protocols. Its decentralized cross-chain bridging infrastructure offers compatibility with most blockchains, including EVM chains like Ethereum and non-EVM chains like S",
 "체인 TVL (DefiLlama)": {
  "체인": "Injective",
  "TVL(USD)": 21725879
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
   "제목": "Kraken's xStocks adds 200 UK and EU shares as its assets top $1.1 billion",
   "요약": "Payward says xStocks holds over $1.1 billion. Each token is backed by a share but gives no ownership of the underlying company.",
   "시각(UTC)": "11-11 10:51"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin stuck under $74,000 as CoreWeave earnings revive AI outlook, Anthropic said to raise IPO valuation",
   "요약": "CoreWeave’s revenue surge lifted AI infrastructure stocks and Nasdaq futures, while bitcoin was little changed over 24 hours.",
   "시각(UTC)": "11-11 10:45"
  },
  {
   "출처": "CoinDesk",
   "제목": "Warren: What is White House doing to prevent a repeat of teleprompter's Trump bets?",
   "요약": "U.S. Senator Elizabeth Warren argued the administration is not doing enough about staff insider trading, questioning whether CFTC enforcement action was sufficient.",
   "시각(UTC)": "11-10 20:36"
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
   32,
   29,
   28,
   25,
   28,
   50
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Tapbit (Futures)": -0.0293,
   "Bitrue (Futures)": -0.0077,
   "OrangeX Futures": -0.01,
   "Binance (Futures)": -0.0075,
   "Gate (Futures)": -0.0132,
   "Bybit (Futures)": -0.0231
  },
  "미결제약정 합계 USD(상위)": 219054521
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 100.0,
  "CoinGecko 인기 검색 코인": [
   "DOGE",
   "GRAM",
   "ZEC",
   "BTC",
   "XRP",
   "HYPE",
   "PEARL",
   "KNTQ",
   "AVAX",
   "LIT",
   "PUMP",
   "ARIA",
   "QTC",
   "SHIB",
   "PI"
  ],
  "INJ가 인기 검색에 있음": false
 }
}
```

## XRP

**수집 실패**
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-10",
  "종가": 1.0565,
  "등락률(%)": {
   "1일": -3.86,
   "7일": -17.25,
   "30일": -25.09,
   "90일": 5.07
  },
  "이동평균": {
   "MA20": 1.24073,
   "MA60": 1.359502,
   "MA120": 1.277241
  },
  "종가와 이평선 거리(%)": {
   "MA20": -14.85,
   "MA60": -22.29,
   "MA120": -17.28
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 23
  },
  "RSI14": 23.7,
  "ATR14(%)": 5.67,
  "거래량(20일 평균 대비 배수)": 1.73,
  "30일 최고가": 1.4214,
  "30일 최저가": 1.0311,
  "최근 10일 종가": [
   1.2507,
   1.2502,
   1.2767,
   1.3052,
   1.2072,
   1.179,
   1.164,
   1.1132,
   1.0989,
   1.0565
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-11",
  "등락률(%)": {
   "1일": -0.09,
   "7일": -3.4,
   "30일": -11.64,
   "90일": -18.74
  },
  "종가와 이평선 거리(%)": {
   "MA20": -3.52,
   "MA60": -11.14,
   "MA120": -14.67
  },
  "MA20>MA60": false,
  "최근 교차": null,
  "RSI14": 31.7
 }
}
```

### DIANA 자료 · 기본적 분석 (펀더멘털)

```json
{
 "이름": "XRP",
 "분류": [
  "Smart Contract Platform",
  "Layer 1 (L1)",
  "FTX Holdings",
  "Pantera Capital Portfolio",
  "Andreessen Horowitz (a16z) Portfolio"
 ],
 "시가총액 순위": 6,
 "시가총액(USD)": 67235249539,
 "완전희석가치 FDV(USD)": 105839338140,
 "24시간 거래대금(USD)": 1958987567,
 "유통량": 63516606953.0,
 "총발행량": 99985583260.0,
 "최대발행량": 100000000000.0,
 "유통 비율(%)": 63.5,
 "역대 최고가(USD)": 3.65,
 "역대 최고가 대비(%)": -70.96077,
 "가격 변화(%)": {
  "7d": -17.07168,
  "30d": -23.77196,
  "1y": -56.92428
 },
 "소개": "XRP is a decentralized digital asset and the native token of the XRP Ledger, a Layer 1 blockchain designed for high-performance global payments. Its primary value proposition is offering a fast, cost-effective alternative to traditional banking systems by enabling near-instant cross-border settlements that finalize in three to five seconds. By serving as a neutral bridge asset between different fi",
 "체인 TVL (DefiLlama)": {
  "체인": "XRPL",
  "TVL(USD)": 32489010
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "XRP 관련 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Ripple Prime head Marc Asch to step down, Noel Kimmel named successor",
   "요약": "Asch is stepping down as head of the institutional prime brokerage.",
   "시각(UTC)": "11-10 12:38"
  },
  {
   "출처": "CoinDesk",
   "제목": "XRP Ledger maps out quantum-proof accounts, with no extra fees for users",
   "요약": "The XRP Ledger Foundation’s design lets owners add a quantum-resistant key and switch off the old one, part of a roadmap that puts the network on track for a full transition by 2028.",
   "시각(UTC)": "11-10 04:51"
  },
  {
   "출처": "Decrypt",
   "제목": "Coinbase Joins Circle, Ripple With Final OCC Approval for Federal Trust Bank Charter",
   "요약": "The exchange will move its institutional crypto custody business under federal oversight, building on its 2018 New York trust charter.",
   "시각(UTC)": "11-09 11:50"
  }
 ],
 "시장 전반 기사": [
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
   "제목": "Kraken's xStocks adds 200 UK and EU shares as its assets top $1.1 billion",
   "요약": "Payward says xStocks holds over $1.1 billion. Each token is backed by a share but gives no ownership of the underlying company.",
   "시각(UTC)": "11-11 10:51"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin stuck under $74,000 as CoreWeave earnings revive AI outlook, Anthropic said to raise IPO valuation",
   "요약": "CoreWeave’s revenue surge lifted AI infrastructure stocks and Nasdaq futures, while bitcoin was little changed over 24 hours.",
   "시각(UTC)": "11-11 10:45"
  },
  {
   "출처": "CoinDesk",
   "제목": "Warren: What is White House doing to prevent a repeat of teleprompter's Trump bets?",
   "요약": "U.S. Senator Elizabeth Warren argued the administration is not doing enough about staff insider trading, questioning whether CFTC enforcement action was sufficient.",
   "시각(UTC)": "11-10 20:36"
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
   32,
   29,
   28,
   25,
   28,
   50
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.01,
   "OrangeX Futures": 0.0175,
   "XT.COM (Derivatives)": 0.0098,
   "CoinW (Futures)": 0.01,
   "Bybit (Futures)": 0.007,
   "Gate (Futures)": 0.0081
  },
  "미결제약정 합계 USD(상위)": 1045602686
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 71.74,
  "CoinGecko 인기 검색 코인": [
   "DOGE",
   "GRAM",
   "ZEC",
   "BTC",
   "XRP",
   "HYPE",
   "PEARL",
   "KNTQ",
   "AVAX",
   "LIT",
   "PUMP",
   "ARIA",
   "QTC",
   "SHIB",
   "PI"
  ],
  "XRP가 인기 검색에 있음": true
 }
}
```
