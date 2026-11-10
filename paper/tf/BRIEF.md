# TF팀 회의 자료 (2026-11-11 07:20 KST)

GitHub Actions가 무료 공개 API로 모은 자료입니다. 회의 진행 방법은 `aicoin/tf_team/PLAYBOOK.md`.
자료에 없는 숫자는 쓰지 않습니다. 실패한 자료는 아래 '수집 실패'에 있습니다.

분석 대상: BTC, ETH, PEPE, INJ, TRUMP

**지금까지 승률** ACE 40.9% (9/22), 채점 대기 0개 · 자세히는 `paper/tf/SCOREBOARD.md`, 교훈은 `aicoin/tf_team/LESSONS.md`

**TRAINER 모의 계좌** 총자산 10,017.55 USDT (+0.18%), 보유 없음 · 자세히는 `paper/tf/trainer/TRAINER.md`

**전체 스캔 후보** (`paper/tf/SCAN.md`) 상승 추세: PEPE, INJ · 과매도 반등: TRUMP

## BTC

**수집 실패**
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-09",
  "종가": 75368.41,
  "등락률(%)": {
   "1일": 0.69,
   "7일": -1.88,
   "30일": -9.18,
   "90일": 18.5
  },
  "이동평균": {
   "MA20": 78711.751,
   "MA60": 81106.4445,
   "MA120": 75297.546417
  },
  "종가와 이평선 거리(%)": {
   "MA20": -4.25,
   "MA60": -7.07,
   "MA120": 0.09
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 10
  },
  "RSI14": 37.8,
  "ATR14(%)": 3.14,
  "거래량(20일 평균 대비 배수)": 1.09,
  "30일 최고가": 84898.0,
  "30일 최저가": 73510.0,
  "최근 10일 종가": [
   77582.02,
   78354.0,
   76816.0,
   77453.86,
   80504.01,
   76088.01,
   75844.0,
   75867.59,
   74851.44,
   75368.41
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-10",
  "등락률(%)": {
   "1일": 0.35,
   "7일": -2.73,
   "30일": -3.79,
   "90일": -8.18
  },
  "종가와 이평선 거리(%)": {
   "MA20": -2.14,
   "MA60": -4.24,
   "MA120": -6.39
  },
  "MA20>MA60": false,
  "최근 교차": null,
  "RSI14": 35.5
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
 "시가총액(USD)": 1486289906302,
 "완전희석가치 FDV(USD)": 1486295671024,
 "24시간 거래대금(USD)": 30514780851,
 "유통량": 20110356.0,
 "총발행량": 20110434.0,
 "최대발행량": 21000000.0,
 "유통 비율(%)": 95.8,
 "역대 최고가(USD)": 126080,
 "역대 최고가 대비(%)": -41.3962,
 "가격 변화(%)": {
  "7d": -5.06582,
  "30d": -11.43866,
  "1y": -30.04951
 },
 "소개": "Bitcoin is the world's first decentralized cryptocurrency, created in 2009 by the pseudonymous Satoshi Nakamoto. It enables peer-to-peer electronic cash transactions without intermediaries like banks or governments, operating on a blockchain secured by Proof of Work mining and the SHA-256 cryptographic algorithm. \n\nWith a fixed supply cap of 21 million coins and programmatic halvings every four ye",
 "체인 TVL (DefiLlama)": {
  "체인": "Bitcoin",
  "TVL(USD)": 3889193613
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "BTC 관련 기사": [
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
   "출처": "CoinDesk",
   "제목": "A Bitcoin block just neared a 2015 transaction record, but paid only $180 in fees",
   "요약": "The AntPool block came within 984 transactions of Bitcoin’s 2015 record, even as fees made up less than 0.1% of the miner’s payout.",
   "시각(UTC)": "11-09 16:19"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Here’s what happened in crypto today",
   "요약": "Need to know what happened in crypto today? Here is the latest news on daily trends and events impacting Bitcoin price, blockchain, DeFi, Web3 and crypto regulation.",
   "시각(UTC)": "11-10 22:04"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Mercado Bitcoin to resume cash withdrawals after $49M hack",
   "요약": "Starting next week, customers can deposit and withdraw money through Brazil’s instant payment system. Crypto transfers remain suspended.",
   "시각(UTC)": "11-10 18:12"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin nears 11-week low after ‘discouraging’ US CPI inflation beat",
   "요약": "Bitcoin and US stocks initially fall after October inflation tops forecasts, with traders expecting a quarter-point Fed rate hike in December.",
   "시각(UTC)": "11-10 16:25"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin’s ‘best buying opportunity ever’ has arrived: Mark Moss",
   "요약": "Bitcoin Opportunity Fund co-founder Mark Moss says that with banks and ETFs widening access to Bitcoin he expects a new record high in 2027.",
   "시각(UTC)": "11-10 13:30"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin may benefit as global tightening slows, Binance Research says",
   "요약": "Binance Research says Bitcoin could find support as global monetary tightening slows, even as markets price in a December Fed rate hike.",
   "시각(UTC)": "11-10 13:15"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin price eyes $74K as Fed rate-hike bets hit 96% after Waller speech",
   "요약": "Bitcoin price action and stock futures trended lower after Fed governor Christopher Waller said that he would vote to raise interest rates by 0.25% at the December FOMC meeting.",
   "시각(UTC)": "11-10 10:08"
  },
  {
   "출처": "Cointelegraph",
   "제목": "BlackRock Bitcoin ETF outflows hit $1.66B over seven trading sessions",
   "요약": "US spot Bitcoin ETFs shed $201 million Monday, with seven straight sessions of net withdrawals from BlackRock’s IBIT totaling $1.66 billion.",
   "시각(UTC)": "11-10 08:02"
  },
  {
   "출처": "Cointelegraph",
   "제목": "HIVE, MARA mine more Bitcoin but earn less as crypto prices fall",
   "요약": "Both miners reported higher Bitcoin production but lower mining revenue and rising electricity costs as they expanded their AI infrastructure businesses.",
   "시각(UTC)": "11-10 00:42"
  }
 ],
 "시장 전반 기사": [
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Will stablecoins survive once the banks catch up?",
   "요약": "As crypto firms and banks converge, it is fair to ask what lasting advantage stablecoins have, argues Alessandro Hatami, founder of Pacemakers and former COO of Digital Banking at Lloyds Banking Group.",
   "시각(UTC)": "11-10 14:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. CPI rose stronger than expected 0.4% in October; core rate rose 0.3%",
   "요약": "A December rate hike appears completely assured, with Fed Governor Chris Waller suggesting even a 50-basis-point move could be appropriate.",
   "시각(UTC)": "11-10 13:32"
  },
  {
   "출처": "CoinDesk",
   "제목": "Ripple Prime head Marc Asch to step down, Noel Kimmel named successor",
   "요약": "Asch is stepping down as head of the institutional prime brokerage.",
   "시각(UTC)": "11-10 12:38"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "32 (Fear)",
  "최근 7일": [
   32,
   29,
   28,
   25,
   28,
   50,
   34
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.0071,
   "OKX (Futures)": 0.0088,
   "Bybit (Futures)": 0.0099,
   "Deepcoin (Derivatives)": 0.0141,
   "MEXC (Futures)": 0.0071,
   "Gate (Futures)": 0.0081
  },
  "미결제약정 합계 USD(상위)": 19782176175
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 55.1,
  "CoinGecko 인기 검색 코인": [
   "DACITY",
   "SI",
   "PENGU",
   "LIT",
   "ZEC",
   "AVAX",
   "INIT",
   "HYPE",
   "PEARL",
   "BTC",
   "ETH",
   "MON",
   "GRAM",
   "VVV",
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
  "기준일": "2026-11-09",
  "종가": 2135.24,
  "등락률(%)": {
   "1일": 0.37,
   "7일": -5.24,
   "30일": -14.81,
   "90일": 13.42
  },
  "이동평균": {
   "MA20": 2296.7855,
   "MA60": 2480.601,
   "MA120": 2292.316083
  },
  "종가와 이평선 거리(%)": {
   "MA20": -7.03,
   "MA60": -13.92,
   "MA120": -6.85
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 20
  },
  "RSI14": 33.7,
  "ATR14(%)": 4.59,
  "거래량(20일 평균 대비 배수)": 1.31,
  "30일 최고가": 2579.88,
  "30일 최저가": 2060.0,
  "최근 10일 종가": [
   2255.66,
   2275.31,
   2253.29,
   2274.77,
   2424.61,
   2238.01,
   2238.67,
   2240.24,
   2127.46,
   2135.24
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-10",
  "등락률(%)": {
   "1일": 1.01,
   "7일": -4.79,
   "30일": -9.61,
   "90일": -11.8
  },
  "종가와 이평선 거리(%)": {
   "MA20": -5.32,
   "MA60": -8.9,
   "MA120": -10.72
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 16
  },
  "RSI14": 28.8
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
 "시가총액(USD)": 251499075929,
 "완전희석가치 FDV(USD)": 251499075929,
 "24시간 거래대금(USD)": 13667733396,
 "유통량": 122206811.20718135,
 "총발행량": 122206811.20718135,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 4946.05,
 "역대 최고가 대비(%)": -58.39607,
 "가격 변화(%)": {
  "7d": -10.23718,
  "30d": -18.54556,
  "1y": -41.96418
 },
 "소개": "Ethereum is a global, open-source platform for decentralized applications. In other words, it is a decentralized blockchain platform that enables developers to build and deploy smart contracts and applications without central authority control. Unlike Bitcoin, which primarily functions as digital currency, Ethereum operates as a programmable global computer where developers can create any type of ",
 "체인 TVL (DefiLlama)": {
  "체인": "Ethereum",
  "TVL(USD)": 40898168095
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
   "제목": "Ex-employee sues Ethereum Foundation and Vitalik Buterin over firing",
   "요약": "Kayleen Fulton alleges she was fired less than two weeks after disclosing a cancer diagnosis and helping organize a staff letter challenging a requirement to endorse the foundation’s new mandate.",
   "시각(UTC)": "11-10 10:56"
  },
  {
   "출처": "Cointelegraph",
   "제목": "PNC Bank tests turning USDC payments into dollar deposits",
   "요약": "The pilot lets eligible corporate and institutional clients accept USDC on Ethereum, with each token converted to one US dollar before deposit.",
   "시각(UTC)": "11-09 17:48"
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Will stablecoins survive once the banks catch up?",
   "요약": "As crypto firms and banks converge, it is fair to ask what lasting advantage stablecoins have, argues Alessandro Hatami, founder of Pacemakers and former COO of Digital Banking at Lloyds Banking Group.",
   "시각(UTC)": "11-10 14:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. CPI rose stronger than expected 0.4% in October; core rate rose 0.3%",
   "요약": "A December rate hike appears completely assured, with Fed Governor Chris Waller suggesting even a 50-basis-point move could be appropriate.",
   "시각(UTC)": "11-10 13:32"
  },
  {
   "출처": "CoinDesk",
   "제목": "Ripple Prime head Marc Asch to step down, Noel Kimmel named successor",
   "요약": "Asch is stepping down as head of the institutional prime brokerage.",
   "시각(UTC)": "11-10 12:38"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "32 (Fear)",
  "최근 7일": [
   32,
   29,
   28,
   25,
   28,
   50,
   34
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": -0.0061,
   "CoinW (Futures)": -0.005,
   "WEEX (Futures)": 0.0,
   "OKX (Futures)": -0.0063,
   "WhiteBIT Futures": 0.01
  },
  "미결제약정 합계 USD(상위)": 12642691660
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 73.81,
  "CoinGecko 인기 검색 코인": [
   "DACITY",
   "SI",
   "PENGU",
   "LIT",
   "ZEC",
   "AVAX",
   "INIT",
   "HYPE",
   "PEARL",
   "BTC",
   "ETH",
   "MON",
   "GRAM",
   "VVV",
   "NEAR"
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
  "기준일": "2026-11-09",
  "종가": 5e-06,
  "등락률(%)": {
   "1일": 3.23,
   "7일": 7.11,
   "30일": 26.73,
   "90일": 80.28
  },
  "이동평균": {
   "MA20": 5e-06,
   "MA60": 4e-06,
   "MA120": 4e-06
  },
  "종가와 이평선 거리(%)": {
   "MA20": 7.7,
   "MA60": 18.78,
   "MA120": 37.98
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 104
  },
  "RSI14": 60.5,
  "ATR14(%)": 10.39,
  "거래량(20일 평균 대비 배수)": 1.08,
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
  "기준일": "2026-11-10",
  "등락률(%)": {
   "1일": 0.0,
   "7일": -1.13,
   "30일": 8.9,
   "90일": 21.76
  },
  "종가와 이평선 거리(%)": {
   "MA20": 3.61,
   "MA60": 6.0,
   "MA120": 9.2
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 13
  },
  "RSI14": 59.0
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
 "시가총액(USD)": 2223544593,
 "완전희석가치 FDV(USD)": 2223544593,
 "24시간 거래대금(USD)": 638198139,
 "유통량": 420690000000000.0,
 "총발행량": 420690000000000.0,
 "최대발행량": 420690000000000.0,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 2.803e-05,
 "역대 최고가 대비(%)": -81.1461,
 "가격 변화(%)": {
  "7d": 7.36,
  "30d": 26.74693,
  "1y": -14.60685
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Will stablecoins survive once the banks catch up?",
   "요약": "As crypto firms and banks converge, it is fair to ask what lasting advantage stablecoins have, argues Alessandro Hatami, founder of Pacemakers and former COO of Digital Banking at Lloyds Banking Group.",
   "시각(UTC)": "11-10 14:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. CPI rose stronger than expected 0.4% in October; core rate rose 0.3%",
   "요약": "A December rate hike appears completely assured, with Fed Governor Chris Waller suggesting even a 50-basis-point move could be appropriate.",
   "시각(UTC)": "11-10 13:32"
  },
  {
   "출처": "CoinDesk",
   "제목": "Ripple Prime head Marc Asch to step down, Noel Kimmel named successor",
   "요약": "Asch is stepping down as head of the institutional prime brokerage.",
   "시각(UTC)": "11-10 12:38"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "32 (Fear)",
  "최근 7일": [
   32,
   29,
   28,
   25,
   28,
   50,
   34
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "MEXC (Futures)": 0.0053,
   "Gate (Futures)": -0.0091,
   "OKX (Futures)": 0.0059,
   "KCEX (Futures)": 0.0061,
   "Bitget Futures": 0.01,
   "WhiteBIT Futures": 0.01
  },
  "미결제약정 합계 USD(상위)": 222628956
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 86.54,
  "CoinGecko 인기 검색 코인": [
   "DACITY",
   "SI",
   "PENGU",
   "LIT",
   "ZEC",
   "AVAX",
   "INIT",
   "HYPE",
   "PEARL",
   "BTC",
   "ETH",
   "MON",
   "GRAM",
   "VVV",
   "NEAR"
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
  "기준일": "2026-11-09",
  "종가": 8.115,
  "등락률(%)": {
   "1일": 0.82,
   "7일": 16.21,
   "30일": 6.09,
   "90일": 73.95
  },
  "이동평균": {
   "MA20": 7.8032,
   "MA60": 7.5745,
   "MA120": 6.272292
  },
  "종가와 이평선 거리(%)": {
   "MA20": 4.0,
   "MA60": 7.14,
   "MA120": 29.38
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 68
  },
  "RSI14": 54.7,
  "ATR14(%)": 7.4,
  "거래량(20일 평균 대비 배수)": 1.3,
  "30일 최고가": 9.417,
  "30일 최저가": 6.823,
  "최근 10일 종가": [
   7.231,
   7.185,
   6.983,
   7.248,
   7.937,
   8.148,
   8.297,
   8.262,
   8.049,
   8.115
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-10",
  "등락률(%)": {
   "1일": 3.8,
   "7일": -1.85,
   "30일": -2.23,
   "90일": 0.15
  },
  "종가와 이평선 거리(%)": {
   "MA20": -0.81,
   "MA60": 3.05,
   "MA120": 3.22
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 29
  },
  "RSI14": 49.6
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
 "시가총액 순위": 82,
 "시가총액(USD)": 811757526,
 "완전희석가치 FDV(USD)": 811757526,
 "24시간 거래대금(USD)": 99758103,
 "유통량": 100000000.0,
 "총발행량": 100000000.0,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 52.62,
 "역대 최고가 대비(%)": -84.57469,
 "가격 변화(%)": {
  "7d": 11.7456,
  "30d": 5.20777,
  "1y": 0.81608
 },
 "소개": "Injective is an interoperable Layer 1 blockchain designed for DeFi applications. It provides developers with on-chain financial infrastructure modules to build dApps such as decentralized exchanges, prediction markets, and lending protocols. Its decentralized cross-chain bridging infrastructure offers compatibility with most blockchains, including EVM chains like Ethereum and non-EVM chains like S",
 "체인 TVL (DefiLlama)": {
  "체인": "Injective",
  "TVL(USD)": 21849687
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Will stablecoins survive once the banks catch up?",
   "요약": "As crypto firms and banks converge, it is fair to ask what lasting advantage stablecoins have, argues Alessandro Hatami, founder of Pacemakers and former COO of Digital Banking at Lloyds Banking Group.",
   "시각(UTC)": "11-10 14:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. CPI rose stronger than expected 0.4% in October; core rate rose 0.3%",
   "요약": "A December rate hike appears completely assured, with Fed Governor Chris Waller suggesting even a 50-basis-point move could be appropriate.",
   "시각(UTC)": "11-10 13:32"
  },
  {
   "출처": "CoinDesk",
   "제목": "Ripple Prime head Marc Asch to step down, Noel Kimmel named successor",
   "요약": "Asch is stepping down as head of the institutional prime brokerage.",
   "시각(UTC)": "11-10 12:38"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "32 (Fear)",
  "최근 7일": [
   32,
   29,
   28,
   25,
   28,
   50,
   34
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Tapbit (Futures)": 0.01,
   "Binance (Futures)": 0.0071,
   "OrangeX Futures": 0.01,
   "Gate (Futures)": 0.01,
   "Bybit (Futures)": 0.01,
   "Bitget Futures": -0.0001
  },
  "미결제약정 합계 USD(상위)": 158125388
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 85.71,
  "CoinGecko 인기 검색 코인": [
   "DACITY",
   "SI",
   "PENGU",
   "LIT",
   "ZEC",
   "AVAX",
   "INIT",
   "HYPE",
   "PEARL",
   "BTC",
   "ETH",
   "MON",
   "GRAM",
   "VVV",
   "NEAR"
  ],
  "INJ가 인기 검색에 있음": false
 }
}
```

## TRUMP

**수집 실패**
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-09",
  "종가": 1.121,
  "등락률(%)": {
   "1일": -1.32,
   "7일": -29.94,
   "30일": -40.78,
   "90일": -24.31
  },
  "이동평균": {
   "MA20": 1.52425,
   "MA60": 1.823917,
   "MA120": 1.81025
  },
  "종가와 이평선 거리(%)": {
   "MA20": -26.46,
   "MA60": -38.54,
   "MA120": -38.07
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 30
  },
  "RSI14": 24.9,
  "ATR14(%)": 11.74,
  "거래량(20일 평균 대비 배수)": 0.96,
  "30일 최고가": 1.959,
  "30일 최저가": 1.108,
  "최근 10일 종가": [
   1.576,
   1.705,
   1.6,
   1.586,
   1.27,
   1.182,
   1.204,
   1.188,
   1.136,
   1.121
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-10",
  "등락률(%)": {
   "1일": 1.34,
   "7일": -0.7,
   "30일": -6.43,
   "90일": -33.22
  },
  "종가와 이평선 거리(%)": {
   "MA20": -1.41,
   "MA60": -15.41,
   "MA120": -24.87
  },
  "MA20>MA60": false,
  "최근 교차": null,
  "RSI14": 37.1
 }
}
```

### DIANA 자료 · 기본적 분석 (펀더멘털)

```json
{
 "이름": "Official Trump",
 "분류": [
  "Solana Ecosystem",
  "Meme",
  "Solana Meme",
  "PolitiFi",
  "Made in USA"
 ],
 "시가총액 순위": 127,
 "시가총액(USD)": 321303171,
 "완전희석가치 FDV(USD)": 1139906782,
 "24시간 거래대금(USD)": 107931278,
 "유통량": 281867935.671502,
 "총발행량": 1000000000.0,
 "최대발행량": 1000000000.0,
 "유통 비율(%)": 28.2,
 "역대 최고가(USD)": 73.43,
 "역대 최고가 대비(%)": -98.44861,
 "가격 변화(%)": {
  "7d": -28.39722,
  "30d": -40.79949,
  "1y": -87.38491
 },
 "소개": "TRUMP is a politics-themed digital coin built on the Solana blockchain that uses the brand of Donald Trump to foster a community-driven ecosystem. As a community-focused asset, it is designed to bridge political support with web ownership, operating within the PolitiFi sector to blend political movements with decentralized finance tools. The project's main value proposition lies in its official ti"
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "TRUMP 관련 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Warren: What is White House doing to prevent a repeat of teleprompter's Trump bets?",
   "요약": "U.S. Senator Elizabeth Warren argued the administration is not doing enough about staff insider trading, questioning whether CFTC enforcement action was sufficient.",
   "시각(UTC)": "11-10 20:36"
  },
  {
   "출처": "Decrypt",
   "제목": "Trump Media Posts $410 Million Profit. Bitcoin Gains Did the Heavy Lifting",
   "요약": "Truth Social’s parent booked $409.7 million in quarterly income largely from crypto investments, even as its stock remained more than 94% below its March 2024 peak.",
   "시각(UTC)": "11-10 21:36"
  },
  {
   "출처": "Decrypt",
   "제목": "'Tough Questions' Ahead: Warren Targets Prediction Markets, Trump Crypto as Banking Chair",
   "요약": "An aide said Trump family crypto businesses should \"preserve their documents\" as Warren prepares to take over the Senate Banking Committee.",
   "시각(UTC)": "11-10 10:41"
  },
  {
   "출처": "Decrypt",
   "제목": "Trump Says He Knows 'Nothing' About World Liberty Financial as He Defends UAE Ties",
   "요약": "Pressed on why he doesn't divest from the family's crypto venture, Trump said his sons run the business and every president faces conflicts.",
   "시각(UTC)": "11-09 11:26"
  }
 ],
 "시장 전반 기사": [
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Will stablecoins survive once the banks catch up?",
   "요약": "As crypto firms and banks converge, it is fair to ask what lasting advantage stablecoins have, argues Alessandro Hatami, founder of Pacemakers and former COO of Digital Banking at Lloyds Banking Group.",
   "시각(UTC)": "11-10 14:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. CPI rose stronger than expected 0.4% in October; core rate rose 0.3%",
   "요약": "A December rate hike appears completely assured, with Fed Governor Chris Waller suggesting even a 50-basis-point move could be appropriate.",
   "시각(UTC)": "11-10 13:32"
  },
  {
   "출처": "CoinDesk",
   "제목": "Ripple Prime head Marc Asch to step down, Noel Kimmel named successor",
   "요약": "Asch is stepping down as head of the institutional prime brokerage.",
   "시각(UTC)": "11-10 12:38"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin breaks with stocks, declines as ETF outflows mount, MARA reduces holdings",
   "요약": "Your day-ahead look for Nov. 10, 2026",
   "시각(UTC)": "11-10 12:15"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "32 (Fear)",
  "최근 7일": [
   32,
   29,
   28,
   25,
   28,
   50,
   34
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.0017,
   "Gate (Futures)": 0.005,
   "OKX (Futures)": 0.0025,
   "Bybit (Futures)": 0.005,
   "WhiteBIT Futures": 0.0046,
   "Hyperliquid (Futures)": 0.0008
  },
  "미결제약정 합계 USD(상위)": 97345193
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 36.84,
  "CoinGecko 인기 검색 코인": [
   "DACITY",
   "SI",
   "PENGU",
   "LIT",
   "ZEC",
   "AVAX",
   "INIT",
   "HYPE",
   "PEARL",
   "BTC",
   "ETH",
   "MON",
   "GRAM",
   "VVV",
   "NEAR"
  ],
  "TRUMP가 인기 검색에 있음": false
 }
}
```
