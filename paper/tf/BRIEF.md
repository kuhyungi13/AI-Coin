# TF팀 회의 자료 (2026-11-14 06:27 KST)

GitHub Actions가 무료 공개 API로 모은 자료입니다. 회의 진행 방법은 `aicoin/tf_team/PLAYBOOK.md`.
자료에 없는 숫자는 쓰지 않습니다. 실패한 자료는 아래 '수집 실패'에 있습니다.

분석 대상: BTC, ETH, ERA, TSLAB, SOL

**지금까지 승률** ACE 40.9% (9/22), 채점 대기 0개 · 자세히는 `paper/tf/SCOREBOARD.md`, 교훈은 `aicoin/tf_team/LESSONS.md`

**TRAINER 모의 계좌** 총자산 10,017.55 USDT (+0.18%), 보유 없음 · 자세히는 `paper/tf/trainer/TRAINER.md`

**전체 스캔 후보** (`paper/tf/SCAN.md`) 상승 추세: ERA, TSLAB · 과매도 반등: SOL

## BTC

**수집 실패**
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-12",
  "종가": 71460.0,
  "등락률(%)": {
   "1일": -3.45,
   "7일": -6.08,
   "30일": -14.08,
   "90일": 13.35
  },
  "이동평균": {
   "MA20": 77340.3665,
   "MA60": 80905.191333,
   "MA120": 75523.683667
  },
  "종가와 이평선 거리(%)": {
   "MA20": -7.6,
   "MA60": -11.67,
   "MA120": -5.38
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 13
  },
  "RSI14": 29.5,
  "ATR14(%)": 3.32,
  "거래량(20일 평균 대비 배수)": 1.06,
  "30일 최고가": 84898.0,
  "30일 최저가": 71113.06,
  "최근 10일 종가": [
   77453.86,
   80504.01,
   76088.01,
   75844.0,
   75867.59,
   74851.44,
   75368.41,
   73796.06,
   74015.19,
   71460.0
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-13",
  "등락률(%)": {
   "1일": 0.23,
   "7일": -3.69,
   "30일": -9.05,
   "90일": -14.58
  },
  "종가와 이평선 거리(%)": {
   "MA20": -4.41,
   "MA60": -8.0,
   "MA120": -10.4
  },
  "MA20>MA60": false,
  "최근 교차": null,
  "RSI14": 24.9
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
 "시가총액(USD)": 1375324321483,
 "완전희석가치 FDV(USD)": 1375329450361,
 "24시간 거래대금(USD)": 42625594789,
 "유통량": 20111481.0,
 "총발행량": 20111556.0,
 "최대발행량": 21000000.0,
 "유통 비율(%)": 95.8,
 "역대 최고가(USD)": 126080,
 "역대 최고가 대비(%)": -45.76055,
 "가격 변화(%)": {
  "7d": -9.78295,
  "30d": -16.30388,
  "1y": -30.35523
 },
 "소개": "Bitcoin is the world's first decentralized cryptocurrency, created in 2009 by the pseudonymous Satoshi Nakamoto. It enables peer-to-peer electronic cash transactions without intermediaries like banks or governments, operating on a blockchain secured by Proof of Work mining and the SHA-256 cryptographic algorithm. \n\nWith a fixed supply cap of 21 million coins and programmatic halvings every four ye",
 "체인 TVL (DefiLlama)": {
  "체인": "Bitcoin",
  "TVL(USD)": 3631909794
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "BTC 관련 기사": [
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
   "출처": "CoinDesk",
   "제목": "Bitcoin dips with Nvidia as ETF outflows reach day five",
   "요약": "Bitcoin slips 0.7% as Nvidia falls on reports its board may oust CEO Jensen Huang, while U.S. spot bitcoin ETFs lose another $299.9 million.",
   "시각(UTC)": "11-12 11:30"
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
  },
  {
   "출처": "Cointelegraph",
   "제목": "Here’s what happened in crypto today",
   "요약": "Need to know what happened in crypto today? Here is the latest news on daily trends and events impacting Bitcoin price, blockchain, DeFi, Web3 and crypto regulation.",
   "시각(UTC)": "11-13 13:49"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Nakamoto shares fall 6% premarket after Q3 revenue turns negative",
   "요약": "A $5.8 million Bitcoin options loss pushed Nakamoto’s quarterly operating revenue below zero, while the company extended repayment of $60 million in Kraken debt to 2027.",
   "시각(UTC)": "11-13 13:04"
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
  "오늘": "20 (Extreme Fear)",
  "최근 7일": [
   20,
   28,
   29,
   32,
   29,
   28,
   25
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.0081,
   "Bybit (Futures)": 0.0067,
   "OKX (Futures)": 0.0079,
   "Deepcoin (Derivatives)": 0.0153,
   "MEXC (Futures)": 0.0079,
   "Gate (Futures)": 0.0091
  },
  "미결제약정 합계 USD(상위)": 18118778010
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 55.02,
  "CoinGecko 인기 검색 코인": [
   "MIHAO",
   "SEPPUKU",
   "MIHAO",
   "PEARL",
   "PENGU",
   "AVAX",
   "ADA",
   "AKE",
   "EDGE",
   "HYPE",
   "BTC",
   "SOL",
   "ENA",
   "XRP",
   "TAO"
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
  "기준일": "2026-11-12",
  "종가": 2019.74,
  "등락률(%)": {
   "1일": -1.78,
   "7일": -9.75,
   "30일": -19.14,
   "90일": 7.31
  },
  "이동평균": {
   "MA20": 2240.726,
   "MA60": 2457.431833,
   "MA120": 2296.839917
  },
  "종가와 이평선 거리(%)": {
   "MA20": -9.86,
   "MA60": -17.81,
   "MA120": -12.06
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 23
  },
  "RSI14": 28.1,
  "ATR14(%)": 4.85,
  "거래량(20일 평균 대비 배수)": 1.05,
  "30일 최고가": 2530.44,
  "30일 최저가": 1983.82,
  "최근 10일 종가": [
   2274.77,
   2424.61,
   2238.01,
   2238.67,
   2240.24,
   2127.46,
   2135.24,
   2053.21,
   2056.36,
   2019.74
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-13",
  "등락률(%)": {
   "1일": 0.98,
   "7일": -2.74,
   "30일": -12.47,
   "90일": -16.39
  },
  "종가와 이평선 거리(%)": {
   "MA20": -3.3,
   "MA60": -9.89,
   "MA120": -12.53
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 34
  },
  "RSI14": 31.9
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
 "시가총액(USD)": 236077583020,
 "완전희석가치 FDV(USD)": 236077583020,
 "24시간 거래대금(USD)": 14636502842,
 "유통량": 122215668.80579185,
 "총발행량": 122215668.80579185,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 4946.05,
 "역대 최고가 대비(%)": -60.94562,
 "가격 변화(%)": {
  "7d": -13.26757,
  "30d": -19.99334,
  "1y": -39.26632
 },
 "소개": "Ethereum is a global, open-source platform for decentralized applications. In other words, it is a decentralized blockchain platform that enables developers to build and deploy smart contracts and applications without central authority control. Unlike Bitcoin, which primarily functions as digital currency, Ethereum operates as a programmable global computer where developers can create any type of ",
 "체인 TVL (DefiLlama)": {
  "체인": "Ethereum",
  "TVL(USD)": 39488568458
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
   "출처": "Cointelegraph",
   "제목": "Are Alt-L1s over? Security, costs drive smaller chains to Ethereum",
   "요약": "L1 blockchains Zilliqa, Gnosis and Ronin join the Ethereum ecosystem as the costs of going it alone grow, and the security and liquidity advantages become too hard to resist.",
   "시각(UTC)": "11-12 13:30"
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin firm Nakamoto owes Kraken $165 million, more than its entire market value",
   "요약": "About 70% of the bitcoin treasury firm’s coins are pledged to the exchange, bought at roughly $118,000 each, and bitcoin now trades under $69,000.",
   "시각(UTC)": "11-13 06:03"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "20 (Extreme Fear)",
  "최근 7일": [
   20,
   28,
   29,
   32,
   29,
   28,
   25
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": -0.001,
   "WEEX (Futures)": 0.0,
   "OKX (Futures)": 0.0034,
   "CoinW (Futures)": 0.0019,
   "WhiteBIT Futures": 0.01
  },
  "미결제약정 합계 USD(상위)": 11733695166
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 58.06,
  "CoinGecko 인기 검색 코인": [
   "MIHAO",
   "SEPPUKU",
   "MIHAO",
   "PEARL",
   "PENGU",
   "AVAX",
   "ADA",
   "AKE",
   "EDGE",
   "HYPE",
   "BTC",
   "SOL",
   "ENA",
   "XRP",
   "TAO"
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
  "기준일": "2026-11-12",
  "종가": 0.0799,
  "등락률(%)": {
   "1일": -8.69,
   "7일": 13.66,
   "30일": 23.88,
   "90일": 31.85
  },
  "이동평균": {
   "MA20": 0.07365,
   "MA60": 0.068515,
   "MA120": 0.066973
  },
  "종가와 이평선 거리(%)": {
   "MA20": 8.49,
   "MA60": 16.62,
   "MA120": 19.3
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 46
  },
  "RSI14": 56.4,
  "ATR14(%)": 12.65,
  "거래량(20일 평균 대비 배수)": 1.84,
  "30일 최고가": 0.1031,
  "30일 최저가": 0.0564,
  "최근 10일 종가": [
   0.064,
   0.0686,
   0.0703,
   0.0698,
   0.0724,
   0.0756,
   0.0704,
   0.0802,
   0.0875,
   0.0799
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-13",
  "등락률(%)": {
   "1일": -2.25,
   "7일": -22.99,
   "30일": -2.64,
   "90일": -0.41
  },
  "종가와 이평선 거리(%)": {
   "MA20": -11.71,
   "MA60": -2.12,
   "MA120": -1.08
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 39
  },
  "RSI14": 40.8
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
 "시가총액 순위": 1019,
 "시가총액(USD)": 12852138,
 "완전희석가치 FDV(USD)": 73545853,
 "24시간 거래대금(USD)": 20700901,
 "유통량": 174750000.0,
 "총발행량": 1000000000.0,
 "최대발행량": 1000000000.0,
 "유통 비율(%)": 17.5,
 "역대 최고가(USD)": 1.88,
 "역대 최고가 대비(%)": -96.07956,
 "가격 변화(%)": {
  "7d": 5.04767,
  "30d": 20.20582,
  "1y": -68.66812
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Ethereum treasury firm BTCS sold ether at a loss to keep $64 million Aave loan healthy",
   "요약": "The Nasdaq-listed company has 46,676 ETH backing its borrowings, and the loan could become eligible for liquidation if ether slides to around $1,700.",
   "시각(UTC)": "11-13 07:05"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "20 (Extreme Fear)",
  "최근 7일": [
   20,
   28,
   29,
   32,
   29,
   28,
   25
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "OrangeX Futures": -0.0669,
   "XT.COM (Derivatives)": -0.0321,
   "Binance (Futures)": -0.0846,
   "Bybit (Futures)": -0.112,
   "KCEX (Futures)": -0.0844,
   "Ourbit (Futures)": -0.0844
  },
  "미결제약정 합계 USD(상위)": 24285249
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 100.0,
  "CoinGecko 인기 검색 코인": [
   "MIHAO",
   "SEPPUKU",
   "MIHAO",
   "PEARL",
   "PENGU",
   "AVAX",
   "ADA",
   "AKE",
   "EDGE",
   "HYPE",
   "BTC",
   "SOL",
   "ENA",
   "XRP",
   "TAO"
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
  "기준일": "2026-11-12",
  "종가": 399.84,
  "등락률(%)": {
   "1일": 3.39,
   "7일": 18.08,
   "30일": 6.64,
   "90일": 16.97
  },
  "이동평균": {
   "MA20": 384.471,
   "MA60": 374.556167,
   "MA120": 359.74425
  },
  "종가와 이평선 거리(%)": {
   "MA20": 4.0,
   "MA60": 6.75,
   "MA120": 11.15
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 70
  },
  "RSI14": 58.6,
  "ATR14(%)": 4.07,
  "거래량(20일 평균 대비 배수)": 0.78,
  "30일 최고가": 414.93,
  "30일 최저가": 335.78,
  "최근 10일 종가": [
   396.29,
   382.63,
   338.62,
   359.51,
   358.49,
   355.33,
   379.2,
   381.33,
   386.72,
   399.84
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-13",
  "등락률(%)": {
   "1일": 0.56,
   "7일": 0.04,
   "30일": 9.21,
   "90일": -2.82
  },
  "종가와 이평선 거리(%)": {
   "MA20": 0.67,
   "MA60": 4.95,
   "MA120": 1.85
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 11
  },
  "RSI14": 56.9
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
 "시가총액 순위": 834,
 "시가총액(USD)": 18388635,
 "완전희석가치 FDV(USD)": 18388635,
 "24시간 거래대금(USD)": 8633666,
 "유통량": 47330.21875512,
 "총발행량": 47330.21875512,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 435.42,
 "역대 최고가 대비(%)": -10.77272,
 "가격 변화(%)": {
  "7d": 8.50716,
  "30d": 5.88694,
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Ethereum treasury firm BTCS sold ether at a loss to keep $64 million Aave loan healthy",
   "요약": "The Nasdaq-listed company has 46,676 ETH backing its borrowings, and the loan could become eligible for liquidation if ether slides to around $1,700.",
   "시각(UTC)": "11-13 07:05"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "20 (Extreme Fear)",
  "최근 7일": [
   20,
   28,
   29,
   32,
   29,
   28,
   25
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
   "SEPPUKU",
   "MIHAO",
   "PEARL",
   "PENGU",
   "AVAX",
   "ADA",
   "AKE",
   "EDGE",
   "HYPE",
   "BTC",
   "SOL",
   "ENA",
   "XRP",
   "TAO"
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
  "기준일": "2026-11-12",
  "종가": 81.72,
  "등락률(%)": {
   "1일": -1.87,
   "7일": -8.52,
   "30일": -23.5,
   "90일": 8.38
  },
  "이동평균": {
   "MA20": 93.0965,
   "MA60": 105.391667,
   "MA120": 95.686917
  },
  "종가와 이평선 거리(%)": {
   "MA20": -12.22,
   "MA60": -22.46,
   "MA120": -14.6
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 19
  },
  "RSI14": 22.4,
  "ATR14(%)": 5.36,
  "거래량(20일 평균 대비 배수)": 0.99,
  "30일 최고가": 109.2,
  "30일 최저가": 80.46,
  "최근 10일 종가": [
   92.83,
   95.61,
   89.33,
   90.13,
   89.81,
   86.54,
   86.74,
   83.35,
   83.28,
   81.72
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-13",
  "등락률(%)": {
   "1일": 0.35,
   "7일": -1.71,
   "30일": -10.37,
   "90일": -19.55
  },
  "종가와 이평선 거리(%)": {
   "MA20": -2.38,
   "MA60": -8.26,
   "MA120": -13.44
  },
  "MA20>MA60": false,
  "최근 교차": null,
  "RSI14": 35.6
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
 "시가총액(USD)": 46792154125,
 "완전희석가치 FDV(USD)": 50429672680,
 "24시간 거래대금(USD)": 3286765393,
 "유통량": 591510873.1532179,
 "총발행량": 637493619.9801579,
 "최대발행량": null,
 "유통 비율(%)": 92.8,
 "역대 최고가(USD)": 293.31,
 "역대 최고가 대비(%)": -73.02834,
 "가격 변화(%)": {
  "7d": -11.92935,
  "30d": -23.95084,
  "1y": -44.53465
 },
 "소개": "Solana is a high-performance Layer 1 blockchain designed for mass adoption by providing a fast, secure, and low-cost environment for decentralized applications. It distinguishes itself by scaling globally without the use of complex sharding or multiple layers, instead maintaining a single, unified ledger to avoid liquidity fragmentation. This architecture allows it to process thousands of transact",
 "체인 TVL (DefiLlama)": {
  "체인": "Solana",
  "TVL(USD)": 4970556831
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Ethereum treasury firm BTCS sold ether at a loss to keep $64 million Aave loan healthy",
   "요약": "The Nasdaq-listed company has 46,676 ETH backing its borrowings, and the loan could become eligible for liquidation if ether slides to around $1,700.",
   "시각(UTC)": "11-13 07:05"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "20 (Extreme Fear)",
  "최근 7일": [
   20,
   28,
   29,
   32,
   29,
   28,
   25
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.0082,
   "Gate (Futures)": 0.0046,
   "OKX (Futures)": 0.0093,
   "Bybit (Futures)": -0.0034,
   "CoinUp.io (Futures)": -0.009,
   "Toobit Futures": 0.0083
  },
  "미결제약정 합계 USD(상위)": 2042585576
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 70.27,
  "CoinGecko 인기 검색 코인": [
   "MIHAO",
   "SEPPUKU",
   "MIHAO",
   "PEARL",
   "PENGU",
   "AVAX",
   "ADA",
   "AKE",
   "EDGE",
   "HYPE",
   "BTC",
   "SOL",
   "ENA",
   "XRP",
   "TAO"
  ],
  "SOL가 인기 검색에 있음": true
 }
}
```
