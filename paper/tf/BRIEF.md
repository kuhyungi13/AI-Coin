# TF팀 회의 자료 (2026-11-14 09:15 KST)

GitHub Actions가 무료 공개 API로 모은 자료입니다. 회의 진행 방법은 `aicoin/tf_team/PLAYBOOK.md`.
자료에 없는 숫자는 쓰지 않습니다. 실패한 자료는 아래 '수집 실패'에 있습니다.

분석 대상: BTC, ETH, INJ, TSLAB, SOL

**지금까지 승률** ACE 40.9% (9/22), 채점 대기 0개 · 자세히는 `paper/tf/SCOREBOARD.md`, 교훈은 `aicoin/tf_team/LESSONS.md`

**TRAINER 모의 계좌** 총자산 10,017.55 USDT (+0.18%), 보유 없음 · 자세히는 `paper/tf/trainer/TRAINER.md`

**전체 스캔 후보** (`paper/tf/SCAN.md`) 상승 추세: INJ, TSLAB · 과매도 반등: SOL

## BTC

**수집 실패**
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-13",
  "종가": 68314.0,
  "등락률(%)": {
   "1일": -4.4,
   "7일": -9.93,
   "30일": -16.37,
   "90일": 8.29
  },
  "이동평균": {
   "MA20": 76711.6585,
   "MA60": 80740.6045,
   "MA120": 75561.048667
  },
  "종가와 이평선 거리(%)": {
   "MA20": -10.95,
   "MA60": -15.39,
   "MA120": -9.59
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 14
  },
  "RSI14": 24.5,
  "ATR14(%)": 3.63,
  "거래량(20일 평균 대비 배수)": 2.05,
  "30일 최고가": 84898.0,
  "30일 최저가": 67568.0,
  "최근 10일 종가": [
   80504.01,
   76088.01,
   75844.0,
   75867.59,
   74851.44,
   75368.41,
   73796.06,
   74015.19,
   71460.0,
   68314.0
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-13",
  "등락률(%)": {
   "1일": -1.08,
   "7일": -4.7,
   "30일": -8.73,
   "90일": -12.41
  },
  "종가와 이평선 거리(%)": {
   "MA20": -5.12,
   "MA60": -8.81,
   "MA120": -11.25
  },
  "MA20>MA60": false,
  "최근 교차": null,
  "RSI14": 22.4
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
 "시가총액(USD)": 1373328481421,
 "완전희석가치 FDV(USD)": 1373330188558,
 "24시간 거래대금(USD)": 43672631020,
 "유통량": 20111581.0,
 "총발행량": 20111606.0,
 "최대발행량": 21000000.0,
 "유통 비율(%)": 95.8,
 "역대 최고가(USD)": 126080,
 "역대 최고가 대비(%)": -45.83953,
 "가격 변화(%)": {
  "7d": -9.88426,
  "30d": -16.32059,
  "1y": -31.35782
 },
 "소개": "Bitcoin is the world's first decentralized cryptocurrency, created in 2009 by the pseudonymous Satoshi Nakamoto. It enables peer-to-peer electronic cash transactions without intermediaries like banks or governments, operating on a blockchain secured by Proof of Work mining and the SHA-256 cryptographic algorithm. \n\nWith a fixed supply cap of 21 million coins and programmatic halvings every four ye",
 "체인 TVL (DefiLlama)": {
  "체인": "Bitcoin",
  "TVL(USD)": 3585176993
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "BTC 관련 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin miners pay Paraguay $350 million a year, but AI is pushing them out",
   "요약": "Contracts that sell power to a 4% slice of the world’s bitcoin mining at $44 a megawatt-hour expire on Dec. 31, 2027. Paraguay’s state utility calls the date final, and it has just signed a 15-year deal to power a Founders Fund-backed AI ca",
   "시각(UTC)": "11-13 23:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin plunges to $68,000 as Anthropic IPO frenzy adds to market jitters",
   "요약": "Analysts see no direct link between Nvidia and bitcoin's decline, pointing instead to investor capital headed into Anthropic as well as a broader risk-off move.",
   "시각(UTC)": "11-13 18:39"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin heads for sixth weekly loss as Anthropic’s blockbuster IPO looms",
   "요약": "Bitcoin is down 21% this year as investors weigh Anthropic’s anticipated listing, Nvidia’s leadership upheaval and rising Fed rate hike expectations.",
   "시각(UTC)": "11-13 16:01"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin's momentum gauge is turning red, could send prices back below $60,000",
   "요약": "Your day-ahead look for Nov. 13, 2026",
   "시각(UTC)": "11-13 12:14"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin hits 12-week low as dollar rallies on interest-rate outlook, liquidations top $1.6 billion",
   "요약": "Bitcoin (BTC) fell below $70,000 for the first time since August and is down 3.5% since midnight UTC, as the dollar climbs and liquidations top $1.6 billion.",
   "시각(UTC)": "11-13 11:52"
  },
  {
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin eyes bear market lows as late summer rally mostly wiped out",
   "요약": "Equity markets are falling as well, with interest rates and the dollar surging amid an increasingly hawkish Federal Reserve.",
   "시각(UTC)": "11-13 09:16"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin firm Nakamoto owes Kraken $165 million, more than its entire market value",
   "요약": "About 70% of the bitcoin treasury firm’s coins are pledged to the exchange, bought at roughly $118,000 each, and bitcoin now trades under $69,000.",
   "시각(UTC)": "11-13 06:03"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin ETFs are now down over $1.5 billion in net outflows for the year",
   "요약": "Recent rapid redemptions explain the market swoon. Bitcoin's spot price fell below $70,000 on Friday, the lowest since August.",
   "시각(UTC)": "11-13 05:45"
  },
  {
   "출처": "CoinDesk",
   "제목": "SpaceX-Tesla merger talks put 30,000 bitcoin back in focus",
   "요약": "A deal could be announced as soon as December, putting $2.1 billion of bitcoin under one roof, a sliver of what the combined group would be worth.",
   "시각(UTC)": "11-13 05:08"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin dips below $70,000 as Dollar Index hits 19-month high",
   "요약": "The crypto market selloff gathered pace early Friday. Bitcoin dropped below $70,000 and ether traded below $2,000, triggering large liquidations in futures market.",
   "시각(UTC)": "11-13 03:37"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin weakness erases September's bullish signal",
   "요약": "Your day-ahead look for Nov. 12, 2026",
   "시각(UTC)": "11-12 12:15"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Here’s what happened in crypto today",
   "요약": "Need to know what happened in crypto today? Here is the latest news on daily trends and events impacting Bitcoin price, blockchain, DeFi, Web3 and crypto regulation.",
   "시각(UTC)": "11-13 22:08"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Adam Back makes case for simpler security as Blockstream launches Bitcoin custody system",
   "요약": "Blockstream’s new custody system, developed with Thales, uses dedicated hardware for transaction signing as Adam Back advocates for offline security to reduce cyber risks.",
   "시각(UTC)": "11-13 21:49"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Metaplanet swings to $170M loss as Bitcoin sale hits earnings",
   "요약": "Bitcoin sales, valuation losses and rising borrowing costs weighed on the Japanese company’s earnings despite higher revenue and operating profit.",
   "시각(UTC)": "11-13 18:28"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin holds below $70K as stocks slip despite a cooler US PPI print",
   "요약": "Bitcoin was down about 4% on the day amid a tepid market reaction to October’s US PPI reading, which came in below expected levels.",
   "시각(UTC)": "11-13 16:39"
  }
 ],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "U.S. Senate Banking Committee races toward hearing on new SEC nominations",
   "요약": "The committee that needs to advance President Donald Trump's nominees responded quickly to set his SEC picks for review next week.",
   "시각(UTC)": "11-13 17:05"
  },
  {
   "출처": "CoinDesk",
   "제목": "Kraken parent Payward says expansion outside crypto trading helps cushion revenue decline",
   "요약": "While earnings and the company’s newly introduced financial performance measure remained below year-earlier levels, there are signs of improvement from the second quarter.",
   "시각(UTC)": "11-13 14:02"
  },
  {
   "출처": "CoinDesk",
   "제목": "Ethereum treasury firm BTCS sold ether at a loss to keep $64 million Aave loan healthy",
   "요약": "The Nasdaq-listed company has 46,676 ETH backing its borrowings, and the loan could become eligible for liquidation if ether slides to around $1,700.",
   "시각(UTC)": "11-13 07:05"
  },
  {
   "출처": "CoinDesk",
   "제목": "North Korea's Binance hack faces U.S. crackdown as DOJ targets $1.2 billion in stolen crypto",
   "요약": "Federal authorities say they've taken infrastructure used in the FaceStealer scheme used to steal as much as $400 million in crypto assets.",
   "시각(UTC)": "11-12 22:55"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. President Trump names CFTC, SEC nominees for first time in a year",
   "요약": "U.S. President Donald Trump has named two potential commissioners each to the Securities and Exchange Commission and Commodity Futures Trading Commission.",
   "시각(UTC)": "11-12 22:47"
  },
  {
   "출처": "CoinDesk",
   "제목": "Kalshi ends Donald Trump Jr.’s advisory contract over 1789 Capital’s Polymarket investment",
   "요약": "Trump Jr. joined Kalshi as a strategic adviser in January 2025, helping the prediction market expand its customer base and strengthen its market presence.",
   "시각(UTC)": "11-12 21:07"
  },
  {
   "출처": "CoinDesk",
   "제목": "Illinois crypto tax is impossible to enforce as written, crypto industry tells court",
   "요약": "The legal battle to head off the crypto transaction tax in Illinois has drawn up a hefty roster of industry opposition, and they're saying the tax won't work.",
   "시각(UTC)": "11-12 16:45"
  },
  {
   "출처": "CoinDesk",
   "제목": "DTCC adds Solana to Wall Street tokenization plans, targeting 2027 rollout",
   "요약": "The securities infrastructure giant plans to bring tokenized stocks, ETFs and U.S. Treasuries to Solana as it expands next year's roadmap beyond Stellar and Arc.",
   "시각(UTC)": "11-12 15:45"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "13 (Extreme Fear)",
  "최근 7일": [
   13,
   20,
   28,
   29,
   32,
   29,
   28
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.0059,
   "Bybit (Futures)": 0.0087,
   "Deepcoin (Derivatives)": 0.0153,
   "OKX (Futures)": 0.004,
   "MEXC (Futures)": 0.0059,
   "Gate (Futures)": 0.0019
  },
  "미결제약정 합계 USD(상위)": 17994981506
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 55.27,
  "CoinGecko 인기 검색 코인": [
   "MIHAO",
   "BTC",
   "INJ",
   "SOL",
   "LINK",
   "AKE",
   "PENGU",
   "HYPE",
   "ETH",
   "KAS",
   "GRASS",
   "PEARL",
   "DRV",
   "ZEC",
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
  "기준일": "2026-11-13",
  "종가": 1929.88,
  "등락률(%)": {
   "1일": -4.45,
   "7일": -13.79,
   "30일": -20.31,
   "90일": 2.51
  },
  "이동평균": {
   "MA20": 2219.279,
   "MA60": 2447.667333,
   "MA120": 2297.383
  },
  "종가와 이평선 거리(%)": {
   "MA20": -13.04,
   "MA60": -21.15,
   "MA120": -16.0
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 24
  },
  "RSI14": 24.3,
  "ATR14(%)": 5.21,
  "거래량(20일 평균 대비 배수)": 1.64,
  "30일 최고가": 2526.62,
  "30일 최저가": 1895.95,
  "최근 10일 종가": [
   2424.61,
   2238.01,
   2238.67,
   2240.24,
   2127.46,
   2135.24,
   2053.21,
   2056.36,
   2019.74,
   1929.88
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-13",
  "등락률(%)": {
   "1일": -1.23,
   "7일": -4.35,
   "30일": -9.29,
   "90일": -14.35
  },
  "종가와 이평선 거리(%)": {
   "MA20": -4.27,
   "MA60": -10.77,
   "MA120": -13.47
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 35
  },
  "RSI14": 29.1
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
 "시가총액(USD)": 236082608957,
 "완전희석가치 FDV(USD)": 236082608957,
 "24시간 거래대금(USD)": 15079676714,
 "유통량": 122215668.80579185,
 "총발행량": 122215668.80579185,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 4946.05,
 "역대 최고가 대비(%)": -60.94479,
 "가격 변화(%)": {
  "7d": -13.62051,
  "30d": -20.16792,
  "1y": -40.06878
 },
 "소개": "Ethereum is a global, open-source platform for decentralized applications. In other words, it is a decentralized blockchain platform that enables developers to build and deploy smart contracts and applications without central authority control. Unlike Bitcoin, which primarily functions as digital currency, Ethereum operates as a programmable global computer where developers can create any type of ",
 "체인 TVL (DefiLlama)": {
  "체인": "Ethereum",
  "TVL(USD)": 39147001356
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "ETH 관련 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Ethereum treasury firm BTCS sold ether at a loss to keep $64 million Aave loan healthy",
   "요약": "The Nasdaq-listed company has 46,676 ETH backing its borrowings, and the loan could become eligible for liquidation if ether slides to around $1,700.",
   "시각(UTC)": "11-13 07:05"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin dips below $70,000 as Dollar Index hits 19-month high",
   "요약": "The crypto market selloff gathered pace early Friday. Bitcoin dropped below $70,000 and ether traded below $2,000, triggering large liquidations in futures market.",
   "시각(UTC)": "11-13 03:37"
  },
  {
   "출처": "CoinDesk",
   "제목": "Ethereum researchers drop faster blocks to race toward quantum defenses in 2027",
   "요약": "Ethlabs wants quantum-resistant accounts targeted for next year, even if wallet holders still have to switch signing methods themselves.",
   "시각(UTC)": "11-12 11:43"
  },
  {
   "출처": "Decrypt",
   "제목": "SoFi Brings Its Bank-Issued Stablecoin to Polygon’s Payments Stack",
   "요약": "SoFiUSD, the first stablecoin from a U.S. national bank, is now live on Polygon Open Money Stack alongside Ethereum and Solana.",
   "시각(UTC)": "11-12 14:01"
  },
  {
   "출처": "Decrypt",
   "제목": "Deutsche Bank Goes Live With Crypto Custody After a Five-Year Buildup",
   "요약": "Deutsche Bank’s custody service now holds Bitcoin, Ethereum and three stablecoins for institutional and corporate clients in Europe.",
   "시각(UTC)": "11-11 19:06"
  }
 ],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin miners pay Paraguay $350 million a year, but AI is pushing them out",
   "요약": "Contracts that sell power to a 4% slice of the world’s bitcoin mining at $44 a megawatt-hour expire on Dec. 31, 2027. Paraguay’s state utility calls the date final, and it has just signed a 15-year deal to power a Founders Fund-backed AI ca",
   "시각(UTC)": "11-13 23:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin plunges to $68,000 as Anthropic IPO frenzy adds to market jitters",
   "요약": "Analysts see no direct link between Nvidia and bitcoin's decline, pointing instead to investor capital headed into Anthropic as well as a broader risk-off move.",
   "시각(UTC)": "11-13 18:39"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. Senate Banking Committee races toward hearing on new SEC nominations",
   "요약": "The committee that needs to advance President Donald Trump's nominees responded quickly to set his SEC picks for review next week.",
   "시각(UTC)": "11-13 17:05"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin heads for sixth weekly loss as Anthropic’s blockbuster IPO looms",
   "요약": "Bitcoin is down 21% this year as investors weigh Anthropic’s anticipated listing, Nvidia’s leadership upheaval and rising Fed rate hike expectations.",
   "시각(UTC)": "11-13 16:01"
  },
  {
   "출처": "CoinDesk",
   "제목": "Kraken parent Payward says expansion outside crypto trading helps cushion revenue decline",
   "요약": "While earnings and the company’s newly introduced financial performance measure remained below year-earlier levels, there are signs of improvement from the second quarter.",
   "시각(UTC)": "11-13 14:02"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin's momentum gauge is turning red, could send prices back below $60,000",
   "요약": "Your day-ahead look for Nov. 13, 2026",
   "시각(UTC)": "11-13 12:14"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin hits 12-week low as dollar rallies on interest-rate outlook, liquidations top $1.6 billion",
   "요약": "Bitcoin (BTC) fell below $70,000 for the first time since August and is down 3.5% since midnight UTC, as the dollar climbs and liquidations top $1.6 billion.",
   "시각(UTC)": "11-13 11:52"
  },
  {
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin eyes bear market lows as late summer rally mostly wiped out",
   "요약": "Equity markets are falling as well, with interest rates and the dollar surging amid an increasingly hawkish Federal Reserve.",
   "시각(UTC)": "11-13 09:16"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "13 (Extreme Fear)",
  "최근 7일": [
   13,
   20,
   28,
   29,
   32,
   29,
   28
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.0007,
   "WEEX (Futures)": 0.0,
   "OKX (Futures)": 0.001,
   "CoinW (Futures)": 0.0012,
   "WhiteBIT Futures": 0.01
  },
  "미결제약정 합계 USD(상위)": 11681841295
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 55.17,
  "CoinGecko 인기 검색 코인": [
   "MIHAO",
   "BTC",
   "INJ",
   "SOL",
   "LINK",
   "AKE",
   "PENGU",
   "HYPE",
   "ETH",
   "KAS",
   "GRASS",
   "PEARL",
   "DRV",
   "ZEC",
   "VVV"
  ],
  "ETH가 인기 검색에 있음": true
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
  "기준일": "2026-11-13",
  "종가": 8.074,
  "등락률(%)": {
   "1일": 8.3,
   "7일": -2.69,
   "30일": 5.34,
   "90일": 93.48
  },
  "이동평균": {
   "MA20": 7.7545,
   "MA60": 7.693617,
   "MA120": 6.3671
  },
  "종가와 이평선 거리(%)": {
   "MA20": 4.12,
   "MA60": 4.94,
   "MA120": 26.81
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 72
  },
  "RSI14": 53.9,
  "ATR14(%)": 7.94,
  "거래량(20일 평균 대비 배수)": 1.86,
  "30일 최고가": 9.417,
  "30일 최저가": 6.823,
  "최근 10일 종가": [
   7.937,
   8.148,
   8.297,
   8.262,
   8.049,
   8.115,
   8.018,
   7.517,
   7.455,
   8.074
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-13",
  "등락률(%)": {
   "1일": -2.29,
   "7일": 8.67,
   "30일": 0.31,
   "90일": 10.04
  },
  "종가와 이평선 거리(%)": {
   "MA20": 3.63,
   "MA60": 1.14,
   "MA120": 4.14
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 7
  },
  "RSI14": 55.5
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
 "시가총액(USD)": 813612965,
 "완전희석가치 FDV(USD)": 813612965,
 "24시간 거래대금(USD)": 154971751,
 "유통량": 100000000.0,
 "총발행량": 100000000.0,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 52.62,
 "역대 최고가 대비(%)": -84.53815,
 "가격 변화(%)": {
  "7d": -1.84189,
  "30d": 6.19692,
  "1y": 17.09892
 },
 "소개": "Injective is an interoperable Layer 1 blockchain designed for DeFi applications. It provides developers with on-chain financial infrastructure modules to build dApps such as decentralized exchanges, prediction markets, and lending protocols. Its decentralized cross-chain bridging infrastructure offers compatibility with most blockchains, including EVM chains like Ethereum and non-EVM chains like S",
 "체인 TVL (DefiLlama)": {
  "체인": "Injective",
  "TVL(USD)": 21780315
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
   "제목": "Bitcoin miners pay Paraguay $350 million a year, but AI is pushing them out",
   "요약": "Contracts that sell power to a 4% slice of the world’s bitcoin mining at $44 a megawatt-hour expire on Dec. 31, 2027. Paraguay’s state utility calls the date final, and it has just signed a 15-year deal to power a Founders Fund-backed AI ca",
   "시각(UTC)": "11-13 23:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin plunges to $68,000 as Anthropic IPO frenzy adds to market jitters",
   "요약": "Analysts see no direct link between Nvidia and bitcoin's decline, pointing instead to investor capital headed into Anthropic as well as a broader risk-off move.",
   "시각(UTC)": "11-13 18:39"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. Senate Banking Committee races toward hearing on new SEC nominations",
   "요약": "The committee that needs to advance President Donald Trump's nominees responded quickly to set his SEC picks for review next week.",
   "시각(UTC)": "11-13 17:05"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin heads for sixth weekly loss as Anthropic’s blockbuster IPO looms",
   "요약": "Bitcoin is down 21% this year as investors weigh Anthropic’s anticipated listing, Nvidia’s leadership upheaval and rising Fed rate hike expectations.",
   "시각(UTC)": "11-13 16:01"
  },
  {
   "출처": "CoinDesk",
   "제목": "Kraken parent Payward says expansion outside crypto trading helps cushion revenue decline",
   "요약": "While earnings and the company’s newly introduced financial performance measure remained below year-earlier levels, there are signs of improvement from the second quarter.",
   "시각(UTC)": "11-13 14:02"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin's momentum gauge is turning red, could send prices back below $60,000",
   "요약": "Your day-ahead look for Nov. 13, 2026",
   "시각(UTC)": "11-13 12:14"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin hits 12-week low as dollar rallies on interest-rate outlook, liquidations top $1.6 billion",
   "요약": "Bitcoin (BTC) fell below $70,000 for the first time since August and is down 3.5% since midnight UTC, as the dollar climbs and liquidations top $1.6 billion.",
   "시각(UTC)": "11-13 11:52"
  },
  {
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin eyes bear market lows as late summer rally mostly wiped out",
   "요약": "Equity markets are falling as well, with interest rates and the dollar surging amid an increasingly hawkish Federal Reserve.",
   "시각(UTC)": "11-13 09:16"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "13 (Extreme Fear)",
  "최근 7일": [
   13,
   20,
   28,
   29,
   32,
   29,
   28
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Tapbit (Futures)": 0.01,
   "OrangeX Futures": 0.0101,
   "Binance (Futures)": 0.01,
   "Gate (Futures)": -0.0032,
   "MEXC (Futures)": -0.0026,
   "Bybit (Futures)": 0.01
  },
  "미결제약정 합계 USD(상위)": 181823952
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 80.0,
  "CoinGecko 인기 검색 코인": [
   "MIHAO",
   "BTC",
   "INJ",
   "SOL",
   "LINK",
   "AKE",
   "PENGU",
   "HYPE",
   "ETH",
   "KAS",
   "GRASS",
   "PEARL",
   "DRV",
   "ZEC",
   "VVV"
  ],
  "INJ가 인기 검색에 있음": true
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
  "기준일": "2026-11-13",
  "종가": 387.8,
  "등락률(%)": {
   "1일": -3.01,
   "7일": 7.87,
   "30일": 6.42,
   "90일": 13.0
  },
  "이동평균": {
   "MA20": 385.258,
   "MA60": 375.019833,
   "MA120": 359.735667
  },
  "종가와 이평선 거리(%)": {
   "MA20": 0.66,
   "MA60": 3.41,
   "MA120": 7.8
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 71
  },
  "RSI14": 53.2,
  "ATR14(%)": 4.23,
  "거래량(20일 평균 대비 배수)": 0.84,
  "30일 최고가": 414.93,
  "30일 최저가": 335.78,
  "최근 10일 종가": [
   382.63,
   338.62,
   359.51,
   358.49,
   355.33,
   379.2,
   381.33,
   386.72,
   399.84,
   387.8
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-13",
  "등락률(%)": {
   "1일": -1.16,
   "7일": -0.7,
   "30일": 9.14,
   "90일": -2.52
  },
  "종가와 이평선 거리(%)": {
   "MA20": -0.63,
   "MA60": 3.77,
   "MA120": 0.63
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 12
  },
  "RSI14": 51.4
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
 "시가총액 순위": 825,
 "시가총액(USD)": 18630651,
 "완전희석가치 FDV(USD)": 18630651,
 "24시간 거래대금(USD)": 8943691,
 "유통량": 48065.90931576,
 "총발행량": 48065.90931576,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 435.42,
 "역대 최고가 대비(%)": -10.97897,
 "가격 변화(%)": {
  "7d": 8.13336,
  "30d": 6.4473,
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
   "제목": "Bitcoin miners pay Paraguay $350 million a year, but AI is pushing them out",
   "요약": "Contracts that sell power to a 4% slice of the world’s bitcoin mining at $44 a megawatt-hour expire on Dec. 31, 2027. Paraguay’s state utility calls the date final, and it has just signed a 15-year deal to power a Founders Fund-backed AI ca",
   "시각(UTC)": "11-13 23:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin plunges to $68,000 as Anthropic IPO frenzy adds to market jitters",
   "요약": "Analysts see no direct link between Nvidia and bitcoin's decline, pointing instead to investor capital headed into Anthropic as well as a broader risk-off move.",
   "시각(UTC)": "11-13 18:39"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. Senate Banking Committee races toward hearing on new SEC nominations",
   "요약": "The committee that needs to advance President Donald Trump's nominees responded quickly to set his SEC picks for review next week.",
   "시각(UTC)": "11-13 17:05"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin heads for sixth weekly loss as Anthropic’s blockbuster IPO looms",
   "요약": "Bitcoin is down 21% this year as investors weigh Anthropic’s anticipated listing, Nvidia’s leadership upheaval and rising Fed rate hike expectations.",
   "시각(UTC)": "11-13 16:01"
  },
  {
   "출처": "CoinDesk",
   "제목": "Kraken parent Payward says expansion outside crypto trading helps cushion revenue decline",
   "요약": "While earnings and the company’s newly introduced financial performance measure remained below year-earlier levels, there are signs of improvement from the second quarter.",
   "시각(UTC)": "11-13 14:02"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin's momentum gauge is turning red, could send prices back below $60,000",
   "요약": "Your day-ahead look for Nov. 13, 2026",
   "시각(UTC)": "11-13 12:14"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin hits 12-week low as dollar rallies on interest-rate outlook, liquidations top $1.6 billion",
   "요약": "Bitcoin (BTC) fell below $70,000 for the first time since August and is down 3.5% since midnight UTC, as the dollar climbs and liquidations top $1.6 billion.",
   "시각(UTC)": "11-13 11:52"
  },
  {
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin eyes bear market lows as late summer rally mostly wiped out",
   "요약": "Equity markets are falling as well, with interest rates and the dollar surging amid an increasingly hawkish Federal Reserve.",
   "시각(UTC)": "11-13 09:16"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "13 (Extreme Fear)",
  "최근 7일": [
   13,
   20,
   28,
   29,
   32,
   29,
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
   "MIHAO",
   "BTC",
   "INJ",
   "SOL",
   "LINK",
   "AKE",
   "PENGU",
   "HYPE",
   "ETH",
   "KAS",
   "GRASS",
   "PEARL",
   "DRV",
   "ZEC",
   "VVV"
  ],
  "TSLAB가 인기 검색에 있음": false
 }
}
```

## SOL

**수집 실패**
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-13",
  "종가": 78.19,
  "등락률(%)": {
   "1일": -4.32,
   "7일": -13.25,
   "30일": -25.03,
   "90일": 3.77
  },
  "이동평균": {
   "MA20": 91.887,
   "MA60": 104.986,
   "MA120": 95.710833
  },
  "종가와 이평선 거리(%)": {
   "MA20": -14.91,
   "MA60": -25.52,
   "MA120": -18.31
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 20
  },
  "RSI14": 19.4,
  "ATR14(%)": 5.5,
  "거래량(20일 평균 대비 배수)": 2.03,
  "30일 최고가": 109.2,
  "30일 최저가": 77.19,
  "최근 10일 종가": [
   95.61,
   89.33,
   90.13,
   89.81,
   86.54,
   86.74,
   83.35,
   83.28,
   81.72,
   78.19
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-13",
  "등락률(%)": {
   "1일": -2.64,
   "7일": -4.23,
   "30일": -9.65,
   "90일": -18.25
  },
  "종가와 이평선 거리(%)": {
   "MA20": -4.72,
   "MA60": -10.43,
   "MA120": -15.55
  },
  "MA20>MA60": false,
  "최근 교차": null,
  "RSI14": 29.5
 }
}
```

### DIANA 자료 · 기본적 분석 (펀더멘털)

```json
{
 "이름": "Solana",
 "분류": [
  "Smart Contract Platform",
  "Solana Ecosystem",
  "Layer 1 (L1)",
  "FTX Holdings",
  "Multicoin Capital Portfolio"
 ],
 "시가총액 순위": 7,
 "시가총액(USD)": 46294211227,
 "완전희석가치 FDV(USD)": 49892882029,
 "24시간 거래대금(USD)": 3623091178,
 "유통량": 591512453.0987307,
 "총발행량": 637493549.6106703,
 "최대발행량": null,
 "유통 비율(%)": 92.8,
 "역대 최고가(USD)": 293.31,
 "역대 최고가 대비(%)": -73.31708,
 "가격 변화(%)": {
  "7d": -13.09791,
  "30d": -24.88602,
  "1y": -45.87625
 },
 "소개": "Solana is a high-performance Layer 1 blockchain designed for mass adoption by providing a fast, secure, and low-cost environment for decentralized applications. It distinguishes itself by scaling globally without the use of complex sharding or multiple layers, instead maintaining a single, unified ledger to avoid liquidity fragmentation. This architecture allows it to process thousands of transact",
 "체인 TVL (DefiLlama)": {
  "체인": "Solana",
  "TVL(USD)": 4904598904
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "SOL 관련 기사": [
  {
   "출처": "CoinDesk",
   "제목": "DTCC adds Solana to Wall Street tokenization plans, targeting 2027 rollout",
   "요약": "The securities infrastructure giant plans to bring tokenized stocks, ETFs and U.S. Treasuries to Solana as it expands next year's roadmap beyond Stellar and Arc.",
   "시각(UTC)": "11-12 15:45"
  },
  {
   "출처": "CoinDesk",
   "제목": "Jupiter adds Anchorage-backed USDGO to its $1 billion Solana lending platform",
   "요약": "OSL offers a yield on USDGO only to professional investors, but Jupiter said its market lets other holders earn onchain at rates set by borrower demand.",
   "시각(UTC)": "11-12 14:45"
  },
  {
   "출처": "Cointelegraph",
   "제목": "DTCC Plans Solana Expansion as Wallet Rules Limit Access",
   "요약": "The US securities clearinghouse plans to bring tokenized stocks to Solana in 2027, but analysts say restrictions could limit adoption.",
   "시각(UTC)": "11-12 20:07"
  },
  {
   "출처": "Decrypt",
   "제목": "SoFi Brings Its Bank-Issued Stablecoin to Polygon’s Payments Stack",
   "요약": "SoFiUSD, the first stablecoin from a U.S. national bank, is now live on Polygon Open Money Stack alongside Ethereum and Solana.",
   "시각(UTC)": "11-12 14:01"
  },
  {
   "출처": "Decrypt",
   "제목": "DTCC to Bring Tokenized Stocks and Treasuries to Solana in 2027",
   "요약": "Wall Street's main settlement firm will add Solana to its tokenization service, which went live last month on Canton and a private network.",
   "시각(UTC)": "11-12 13:25"
  },
  {
   "출처": "Decrypt",
   "제목": "What Are Solana Privacy Rings? Inside Helius’ Privacy Protocol for Solana",
   "요약": "Solana Privacy Rings encrypt balances and transfer amounts without leaving Solana. Here's how they work, and how they compare.",
   "시각(UTC)": "11-11 17:09"
  }
 ],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin miners pay Paraguay $350 million a year, but AI is pushing them out",
   "요약": "Contracts that sell power to a 4% slice of the world’s bitcoin mining at $44 a megawatt-hour expire on Dec. 31, 2027. Paraguay’s state utility calls the date final, and it has just signed a 15-year deal to power a Founders Fund-backed AI ca",
   "시각(UTC)": "11-13 23:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin plunges to $68,000 as Anthropic IPO frenzy adds to market jitters",
   "요약": "Analysts see no direct link between Nvidia and bitcoin's decline, pointing instead to investor capital headed into Anthropic as well as a broader risk-off move.",
   "시각(UTC)": "11-13 18:39"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. Senate Banking Committee races toward hearing on new SEC nominations",
   "요약": "The committee that needs to advance President Donald Trump's nominees responded quickly to set his SEC picks for review next week.",
   "시각(UTC)": "11-13 17:05"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin heads for sixth weekly loss as Anthropic’s blockbuster IPO looms",
   "요약": "Bitcoin is down 21% this year as investors weigh Anthropic’s anticipated listing, Nvidia’s leadership upheaval and rising Fed rate hike expectations.",
   "시각(UTC)": "11-13 16:01"
  },
  {
   "출처": "CoinDesk",
   "제목": "Kraken parent Payward says expansion outside crypto trading helps cushion revenue decline",
   "요약": "While earnings and the company’s newly introduced financial performance measure remained below year-earlier levels, there are signs of improvement from the second quarter.",
   "시각(UTC)": "11-13 14:02"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin's momentum gauge is turning red, could send prices back below $60,000",
   "요약": "Your day-ahead look for Nov. 13, 2026",
   "시각(UTC)": "11-13 12:14"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin hits 12-week low as dollar rallies on interest-rate outlook, liquidations top $1.6 billion",
   "요약": "Bitcoin (BTC) fell below $70,000 for the first time since August and is down 3.5% since midnight UTC, as the dollar climbs and liquidations top $1.6 billion.",
   "시각(UTC)": "11-13 11:52"
  },
  {
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin eyes bear market lows as late summer rally mostly wiped out",
   "요약": "Equity markets are falling as well, with interest rates and the dollar surging amid an increasingly hawkish Federal Reserve.",
   "시각(UTC)": "11-13 09:16"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "13 (Extreme Fear)",
  "최근 7일": [
   13,
   20,
   28,
   29,
   32,
   29,
   28
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.0064,
   "Gate (Futures)": -0.0128,
   "OKX (Futures)": 0.0041,
   "Toobit Futures": 0.0064,
   "Bybit (Futures)": 0.0021,
   "XT.COM (Derivatives)": 0.0184
  },
  "미결제약정 합계 USD(상위)": 2018571180
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 75.68,
  "CoinGecko 인기 검색 코인": [
   "MIHAO",
   "BTC",
   "INJ",
   "SOL",
   "LINK",
   "AKE",
   "PENGU",
   "HYPE",
   "ETH",
   "KAS",
   "GRASS",
   "PEARL",
   "DRV",
   "ZEC",
   "VVV"
  ],
  "SOL가 인기 검색에 있음": true
 }
}
```
