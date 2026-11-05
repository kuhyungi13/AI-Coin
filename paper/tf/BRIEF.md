# TF팀 회의 자료 (2026-11-05 22:53 KST)

GitHub Actions가 무료 공개 API로 모은 자료입니다. 회의 진행 방법은 `aicoin/tf_team/PLAYBOOK.md`.
자료에 없는 숫자는 쓰지 않습니다. 실패한 자료는 아래 '수집 실패'에 있습니다.

분석 대상: BTC, ETH, BMT, PEPE, INTCB

**지금까지 승률** ACE 40.9% (9/22), 채점 대기 0개 · 자세히는 `paper/tf/SCOREBOARD.md`, 교훈은 `aicoin/tf_team/LESSONS.md`

**TRAINER 모의 계좌** 총자산 10,009.62 USDT (+0.10%), 보유 PEPE · 자세히는 `paper/tf/trainer/TRAINER.md`

**전체 스캔 후보** (`paper/tf/SCAN.md`) 상승 추세: BMT, PEPE · 과매도 반등: INTCB

## BTC

**수집 실패**
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-04",
  "종가": 80504.01,
  "등락률(%)": {
   "1일": 3.94,
   "7일": -1.03,
   "30일": -6.14,
   "90일": 25.15
  },
  "이동평균": {
   "MA20": 80320.24,
   "MA60": 81352.5335,
   "MA120": 74791.390333
  },
  "종가와 이평선 거리(%)": {
   "MA20": 0.23,
   "MA60": -1.04,
   "MA120": 7.64
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 5
  },
  "RSI14": 50.6,
  "ATR14(%)": 2.69,
  "거래량(20일 평균 대비 배수)": 1.61,
  "30일 최고가": 86698.99,
  "30일 최저가": 75736.38,
  "최근 10일 종가": [
   80150.56,
   80909.77,
   81343.5,
   77991.89,
   77368.77,
   77582.02,
   78354.0,
   76816.0,
   77453.86,
   80504.01
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-05",
  "등락률(%)": {
   "1일": 0.04,
   "7일": 2.88,
   "30일": 3.57,
   "90일": -3.72
  },
  "종가와 이평선 거리(%)": {
   "MA20": 2.65,
   "MA60": 1.9,
   "MA120": 0.13
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 70
  },
  "RSI14": 64.8
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
 "시가총액(USD)": 1604043950928,
 "완전희석가치 FDV(USD)": 1604043950928,
 "24시간 거래대금(USD)": 35506712320,
 "유통량": 20105365.0,
 "총발행량": 20105365.0,
 "최대발행량": 21000000.0,
 "유통 비율(%)": 95.7,
 "역대 최고가(USD)": 126080,
 "역대 최고가 대비(%)": -36.71807,
 "가격 변화(%)": {
  "7d": -0.23233,
  "30d": -7.41695,
  "1y": -22.26451
 },
 "소개": "Bitcoin is the world's first decentralized cryptocurrency, created in 2009 by the pseudonymous Satoshi Nakamoto. It enables peer-to-peer electronic cash transactions without intermediaries like banks or governments, operating on a blockchain secured by Proof of Work mining and the SHA-256 cryptographic algorithm. \n\nWith a fixed supply cap of 21 million coins and programmatic halvings every four ye",
 "체인 TVL (DefiLlama)": {
  "체인": "Bitcoin",
  "TVL(USD)": 4263171762
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "BTC 관련 기사": [
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
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin edges lower as markets cool following yesterday's rally",
   "요약": "There's been no letup in selling of the AI chip stocks, sending Nasdaq 100 futures nearly 1% lower.",
   "시각(UTC)": "11-05 10:57"
  },
  {
   "출처": "CoinDesk",
   "제목": "Mercado Bitcoin hack continued hours after exchange said attack was contained, report finds",
   "요약": "The same attacker took about $391,000, mostly from wallets Bitquery ties to BitMart, whose founder confirmed a Nov. 2 hack and suspects a link.",
   "시각(UTC)": "11-05 10:44"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin miner Riot could pay Anthropic 12% interest under $28 billion AI deal",
   "요약": "Riot has sold most of its bitcoin to fund its move into data centers. Its latest agreement gives Anthropic a way to finance part of the build and collect interest through rent deductions.",
   "시각(UTC)": "11-05 09:36"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin holds above $80,000 as Zcash jumps 12% in post-election crypto rebound",
   "요약": "Ether rose 8% as falling oil prices and a weaker dollar helped markets recover, even as traders weighed a tougher path for U.S. crypto legislation.",
   "시각(UTC)": "11-05 05:13"
  },
  {
   "출처": "CoinDesk",
   "제목": "Trump Media moves $342 million in bitcoin to Crypto.com, blockchain data show",
   "요약": "A wallet supposedly linked to Trump Media has made a large BTC transfer to Crypto.com, data tracked by Arkham show.",
   "시각(UTC)": "11-05 04:11"
  },
  {
   "출처": "CoinDesk",
   "제목": "Wall Street rethinks AI data center boom as Texas election raises new risks",
   "요약": "Bitcoin miners pivoting to AI face new uncertainty over power access and construction permits, while companies with approved projects could benefit from tighter supply.",
   "시각(UTC)": "11-04 16:08"
  },
  {
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin rises above $80,000 as stocks gain following Blue Wave",
   "요약": "The biggest losers were the AI data center stocks following victories for several candidates who campaigned expressly against the sector.",
   "시각(UTC)": "11-04 14:00"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin win rate vs. S&P 500 recovers as post-midterm history favors stocks",
   "요약": "Bitcoin outperformed the S&P 500 in half of the past 90 US trading sessions, while historical midterm data highlights gains for stocks.",
   "시각(UTC)": "11-05 10:28"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin, Ether ETFs draw $128M as crypto rebounds after midterms",
   "요약": "Fidelity led Bitcoin ETF inflows, while BlackRock’s IBIT shed another $201 million, extending its outflow streak to four trading sessions.",
   "시각(UTC)": "11-05 08:22"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Here’s what happened in crypto today",
   "요약": "Need to know what happened in crypto today? Here is the latest news on daily trends and events impacting Bitcoin price, blockchain, DeFi, Web3 and crypto regulation.",
   "시각(UTC)": "11-05 06:21"
  }
 ],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Binance cuts SignalPlus access after security warning, urges users to check accounts",
   "요약": "The exchange says its systems are unaffected but has removed trading connections to the third-party platform as a precaution.",
   "시각(UTC)": "11-05 12:55"
  },
  {
   "출처": "CoinDesk",
   "제목": "Ukraine’s central bank opposes crypto bill, citing monetary sovereignty concerns",
   "요약": "Ukraine’s central bank won’t back a crypto legalization bill in its current form and wants lawmakers to revise it before a final vote.",
   "시각(UTC)": "11-05 12:50"
  },
  {
   "출처": "CoinDesk",
   "제목": "Hong Kong passes law requiring crypto exchanges to report customer transactions to tax authorities",
   "요약": "Crypto firms must collect customer and transaction data from 2027, with Hong Kong sharing the information with overseas tax authorities from 2028.",
   "시각(UTC)": "11-05 08:35"
  },
  {
   "출처": "CoinDesk",
   "제목": "OpenAI says its AI can break into Linux at scale. Here's what it means for crypto",
   "요약": "OpenAI says its AI found 948 Linux flaws and wrote a working attack for each one. Crypto security voices say decentralization leaves the industry better placed than most to cope.",
   "시각(UTC)": "11-05 08:26"
  },
  {
   "출처": "CoinDesk",
   "제목": "Zcash is about to freeze $16 million in its oldest privacy pool",
   "요약": "About 12,200 ZEC remains in Sprout, the privacy pool Zcash launched in 2016. Roughly 10,000 coins have left over the past week, but only about 40 moved out Wednesday.",
   "시각(UTC)": "11-05 05:47"
  },
  {
   "출처": "CoinDesk",
   "제목": "The pile of lawsuits against Kalshi just grew by one",
   "요약": "Arkansas has accused the prediction market of running illegal gambling, joining Utah and several other U.S. states that have filed criminal or civil charges.",
   "시각(UTC)": "11-05 05:28"
  },
  {
   "출처": "CoinDesk",
   "제목": "XRP Ledger fixes a disclosed bug that could have led to the creation of new tokens",
   "요약": "The fix went live Wednesday after validator support reset the activation clock in October. XRP itself was unaffected.",
   "시각(UTC)": "11-05 05:25"
  },
  {
   "출처": "CoinDesk",
   "제목": "Tokenization and stablecoins may weather Democrats' sweep as broader crypto rules face uncertainty",
   "요약": "Wall Street's push to bring finance onto blockchain rails may continue under existing laws, though the SEC and CFTC face tougher oversight and questions over how long their rules will last, experts said.",
   "시각(UTC)": "11-04 22:55"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "50 (Neutral)",
  "최근 7일": [
   50,
   34,
   26,
   37,
   34,
   30,
   30
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.01,
   "Bybit (Futures)": 0.01,
   "MEXC (Futures)": 0.01,
   "Gate (Futures)": 0.01,
   "Tapbit (Futures)": 0.01,
   "WEEX (Futures)": 0.0
  },
  "미결제약정 합계 USD(상위)": 29505524244
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 78.98,
  "CoinGecko 인기 검색 코인": [
   "TRUMP",
   "PEARL",
   "SOL",
   "CARDS",
   "PENGU",
   "ETH",
   "DOT",
   "BTC",
   "HYPE",
   "INJ",
   "AERO",
   "SUI",
   "PI",
   "PUMP",
   "LIT"
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
  "기준일": "2026-11-04",
  "종가": 2424.61,
  "등락률(%)": {
   "1일": 6.59,
   "7일": 2.75,
   "30일": -10.53,
   "90일": 27.34
  },
  "이동평균": {
   "MA20": 2352.4985,
   "MA60": 2504.209,
   "MA120": 2274.820167
  },
  "종가와 이평선 거리(%)": {
   "MA20": 3.07,
   "MA60": -3.18,
   "MA120": 6.58
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 15
  },
  "RSI14": 54.1,
  "ATR14(%)": 3.58,
  "거래량(20일 평균 대비 배수)": 1.48,
  "30일 최고가": 2725.13,
  "30일 최저가": 2174.08,
  "최근 10일 종가": [
   2324.55,
   2350.36,
   2359.68,
   2253.13,
   2245.54,
   2255.66,
   2275.31,
   2253.29,
   2274.77,
   2424.61
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-05",
  "등락률(%)": {
   "1일": 0.2,
   "7일": 5.1,
   "30일": 7.67,
   "90일": -1.96
  },
  "종가와 이평선 거리(%)": {
   "MA20": 4.37,
   "MA60": 5.07,
   "MA120": 2.92
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 2
  },
  "RSI14": 68.9
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
 "시가총액(USD)": 291988202370,
 "완전희석가치 FDV(USD)": 291988202370,
 "24시간 거래대금(USD)": 15261203395,
 "유통량": 122192071.85523713,
 "총발행량": 122192071.85523713,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 4946.05,
 "역대 최고가 대비(%)": -51.68698,
 "가격 변화(%)": {
  "7d": 2.9799,
  "30d": -11.97406,
  "1y": -28.51767
 },
 "소개": "Ethereum is a global, open-source platform for decentralized applications. In other words, it is a decentralized blockchain platform that enables developers to build and deploy smart contracts and applications without central authority control. Unlike Bitcoin, which primarily functions as digital currency, Ethereum operates as a programmable global computer where developers can create any type of ",
 "체인 TVL (DefiLlama)": {
  "체인": "Ethereum",
  "TVL(USD)": 45651414034
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "ETH 관련 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin holds above $80,000 as Zcash jumps 12% in post-election crypto rebound",
   "요약": "Ether rose 8% as falling oil prices and a weaker dollar helped markets recover, even as traders weighed a tougher path for U.S. crypto legislation.",
   "시각(UTC)": "11-05 05:13"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin, Ether ETFs draw $128M as crypto rebounds after midterms",
   "요약": "Fidelity led Bitcoin ETF inflows, while BlackRock’s IBIT shed another $201 million, extending its outflow streak to four trading sessions.",
   "시각(UTC)": "11-05 08:22"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Trump-linked tokens lead crypto losses after Democrats sweep in the US midterms",
   "요약": "The official Trump and World Liberty Financial tokens were the two biggest losers among the top 100 cryptocurrencies on Wednesday, even as Bitcoin and Ether rallied.",
   "시각(UTC)": "11-04 19:15"
  },
  {
   "출처": "Decrypt",
   "제목": "Ethereum Privacy Network Aztec Rolls Out Major Security and Speed Upgrade",
   "요약": "The “Tierra” upgrade resolves a critical bug from the prior version, adds formal verification, and an AI-powered testing harness.",
   "시각(UTC)": "11-03 14:01"
  }
 ],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Google could take stake in bitcoin miner TeraWulf’s $19 billion AI project if Anthropic defaults",
   "요약": "A $19 billion data-center agreement includes an unusual provision allowing Google to acquire part of the project if Anthropic fails to pay its rent.",
   "시각(UTC)": "11-05 13:29"
  },
  {
   "출처": "CoinDesk",
   "제목": "Binance cuts SignalPlus access after security warning, urges users to check accounts",
   "요약": "The exchange says its systems are unaffected but has removed trading connections to the third-party platform as a precaution.",
   "시각(UTC)": "11-05 12:55"
  },
  {
   "출처": "CoinDesk",
   "제목": "Ukraine’s central bank opposes crypto bill, citing monetary sovereignty concerns",
   "요약": "Ukraine’s central bank won’t back a crypto legalization bill in its current form and wants lawmakers to revise it before a final vote.",
   "시각(UTC)": "11-05 12:50"
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
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin edges lower as markets cool following yesterday's rally",
   "요약": "There's been no letup in selling of the AI chip stocks, sending Nasdaq 100 futures nearly 1% lower.",
   "시각(UTC)": "11-05 10:57"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "50 (Neutral)",
  "최근 7일": [
   50,
   34,
   26,
   37,
   34,
   30,
   30
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.01,
   "WEEX (Futures)": -0.0,
   "Hyperliquid (Futures)": 0.0013,
   "MEXC (Futures)": 0.01,
   "CoinW (Futures)": 0.01
  },
  "미결제약정 합계 USD(상위)": 19278106410
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 86.36,
  "CoinGecko 인기 검색 코인": [
   "TRUMP",
   "PEARL",
   "SOL",
   "CARDS",
   "PENGU",
   "ETH",
   "DOT",
   "BTC",
   "HYPE",
   "INJ",
   "AERO",
   "SUI",
   "PI",
   "PUMP",
   "LIT"
  ],
  "ETH가 인기 검색에 있음": true
 }
}
```

## BMT

**수집 실패**
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-04",
  "종가": 0.02873,
  "등락률(%)": {
   "1일": 8.33,
   "7일": -0.21,
   "30일": 47.79,
   "90일": 126.58
  },
  "이동평균": {
   "MA20": 0.024167,
   "MA60": 0.020622,
   "MA120": 0.017996
  },
  "종가와 이평선 거리(%)": {
   "MA20": 18.88,
   "MA60": 39.32,
   "MA120": 59.64
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 11
  },
  "RSI14": 58.8,
  "ATR14(%)": 26.51,
  "거래량(20일 평균 대비 배수)": 1.49,
  "30일 최고가": 0.05144,
  "30일 최저가": 0.01564,
  "최근 10일 종가": [
   0.02959,
   0.02809,
   0.02879,
   0.02382,
   0.02336,
   0.02267,
   0.02197,
   0.021,
   0.02652,
   0.02873
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-05",
  "등락률(%)": {
   "1일": -0.77,
   "7일": -15.36,
   "30일": 12.95,
   "90일": 2.55
  },
  "종가와 이평선 거리(%)": {
   "MA20": 1.3,
   "MA60": 1.32,
   "MA120": 5.27
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 0
  },
  "RSI14": 49.7
 }
}
```

### DIANA 자료 · 기본적 분석 (펀더멘털)

```json
{
 "이름": "Bubblemaps",
 "분류": [
  "Analytics",
  "BNB Chain Ecosystem",
  "Solana Ecosystem",
  "Binance HODLer Airdrops",
  "Binance Wallet IDO"
 ],
 "시가총액 순위": 840,
 "시가총액(USD)": 20106141,
 "완전희석가치 FDV(USD)": 26392447,
 "24시간 거래대금(USD)": 43528936,
 "유통량": 761814186.0,
 "총발행량": 1000000000.0,
 "최대발행량": 1000000000.0,
 "유통 비율(%)": 76.2,
 "역대 최고가(USD)": 0.317341,
 "역대 최고가 대비(%)": -91.68324,
 "가격 변화(%)": {
  "7d": 0.26421,
  "30d": 33.86145,
  "1y": -17.27008
 },
 "소개": "Blockchain data is inherently cluttered, noisy, and highly technical. \n\nBubblemaps transforms this complexity into a visual experience, making analysis engaging and efficient —allowing users to address modern crypto challenges:\n\n- Tokenomics being difficult to analyse and understand\n- Memecoins bundling their supply and dumping on the retail\n- Celebrities launching tokens while secretly holding ma"
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "BMT 관련 기사": [],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Google could take stake in bitcoin miner TeraWulf’s $19 billion AI project if Anthropic defaults",
   "요약": "A $19 billion data-center agreement includes an unusual provision allowing Google to acquire part of the project if Anthropic fails to pay its rent.",
   "시각(UTC)": "11-05 13:29"
  },
  {
   "출처": "CoinDesk",
   "제목": "Binance cuts SignalPlus access after security warning, urges users to check accounts",
   "요약": "The exchange says its systems are unaffected but has removed trading connections to the third-party platform as a precaution.",
   "시각(UTC)": "11-05 12:55"
  },
  {
   "출처": "CoinDesk",
   "제목": "Ukraine’s central bank opposes crypto bill, citing monetary sovereignty concerns",
   "요약": "Ukraine’s central bank won’t back a crypto legalization bill in its current form and wants lawmakers to revise it before a final vote.",
   "시각(UTC)": "11-05 12:50"
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
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin edges lower as markets cool following yesterday's rally",
   "요약": "There's been no letup in selling of the AI chip stocks, sending Nasdaq 100 futures nearly 1% lower.",
   "시각(UTC)": "11-05 10:57"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "50 (Neutral)",
  "최근 7일": [
   50,
   34,
   26,
   37,
   34,
   30,
   30
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": -0.1822,
   "Bybit (Futures)": -0.1559,
   "Toobit Futures": -0.1822,
   "Ourbit (Futures)": -0.1822,
   "KCEX (Futures)": -0.1822,
   "Gate (Futures)": -0.1713
  },
  "미결제약정 합계 USD(상위)": 14511658
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 33.33,
  "CoinGecko 인기 검색 코인": [
   "TRUMP",
   "PEARL",
   "SOL",
   "CARDS",
   "PENGU",
   "ETH",
   "DOT",
   "BTC",
   "HYPE",
   "INJ",
   "AERO",
   "SUI",
   "PI",
   "PUMP",
   "LIT"
  ],
  "BMT가 인기 검색에 있음": false
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
  "기준일": "2026-11-04",
  "종가": 5e-06,
  "등락률(%)": {
   "1일": 2.05,
   "7일": -1.19,
   "30일": 13.21,
   "90일": 76.87
  },
  "이동평균": {
   "MA20": 5e-06,
   "MA60": 4e-06,
   "MA120": 4e-06
  },
  "종가와 이평선 거리(%)": {
   "MA20": 9.25,
   "MA60": 18.55,
   "MA120": 37.41
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 99
  },
  "RSI14": 59.5,
  "ATR14(%)": 10.78,
  "거래량(20일 평균 대비 배수)": 1.15,
  "30일 최고가": 6e-06,
  "30일 최저가": 4e-06,
  "최근 10일 종가": [
   4e-06,
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
  "기준일": "2026-11-05",
  "등락률(%)": {
   "1일": 0.4,
   "7일": -0.8,
   "30일": -2.36,
   "90일": 8.06
  },
  "종가와 이평선 거리(%)": {
   "MA20": 1.74,
   "MA60": 2.11,
   "MA120": 8.15
  },
  "MA20>MA60": true,
  "최근 교차": null,
  "RSI14": 52.4
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
 "시가총액(USD)": 2066940293,
 "완전희석가치 FDV(USD)": 2066940293,
 "24시간 거래대금(USD)": 475583629,
 "유통량": 420690000000000.0,
 "총발행량": 420690000000000.0,
 "최대발행량": 420690000000000.0,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 2.803e-05,
 "역대 최고가 대비(%)": -82.47045,
 "가격 변화(%)": {
  "7d": 0.49509,
  "30d": 12.98134,
  "1y": -13.39087
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
   "제목": "Google could take stake in bitcoin miner TeraWulf’s $19 billion AI project if Anthropic defaults",
   "요약": "A $19 billion data-center agreement includes an unusual provision allowing Google to acquire part of the project if Anthropic fails to pay its rent.",
   "시각(UTC)": "11-05 13:29"
  },
  {
   "출처": "CoinDesk",
   "제목": "Binance cuts SignalPlus access after security warning, urges users to check accounts",
   "요약": "The exchange says its systems are unaffected but has removed trading connections to the third-party platform as a precaution.",
   "시각(UTC)": "11-05 12:55"
  },
  {
   "출처": "CoinDesk",
   "제목": "Ukraine’s central bank opposes crypto bill, citing monetary sovereignty concerns",
   "요약": "Ukraine’s central bank won’t back a crypto legalization bill in its current form and wants lawmakers to revise it before a final vote.",
   "시각(UTC)": "11-05 12:50"
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
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin edges lower as markets cool following yesterday's rally",
   "요약": "There's been no letup in selling of the AI chip stocks, sending Nasdaq 100 futures nearly 1% lower.",
   "시각(UTC)": "11-05 10:57"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "50 (Neutral)",
  "최근 7일": [
   50,
   34,
   26,
   37,
   34,
   30,
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
  "미결제약정 합계 USD(상위)": 299531092
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 87.5,
  "CoinGecko 인기 검색 코인": [
   "TRUMP",
   "PEARL",
   "SOL",
   "CARDS",
   "PENGU",
   "ETH",
   "DOT",
   "BTC",
   "HYPE",
   "INJ",
   "AERO",
   "SUI",
   "PI",
   "PUMP",
   "LIT"
  ],
  "PEPE가 인기 검색에 있음": false
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
  "기준일": "2026-11-04",
  "종가": 58.08,
  "등락률(%)": {
   "1일": -4.71,
   "7일": -37.68,
   "30일": -50.09,
   "90일": -42.08
  },
  "이동평균": {
   "MA20": 80.896,
   "MA60": 100.303833,
   "MA120": 98.544417
  },
  "종가와 이평선 거리(%)": {
   "MA20": -28.2,
   "MA60": -42.1,
   "MA120": -41.06
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 14
  },
  "RSI14": 22.1,
  "ATR14(%)": 9.8,
  "거래량(20일 평균 대비 배수)": 1.52,
  "30일 최고가": 118.16,
  "30일 최저가": 56.72,
  "최근 10일 종가": [
   91.6,
   94.19,
   93.19,
   71.11,
   65.01,
   65.11,
   66.2,
   60.51,
   60.95,
   58.08
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-05",
  "등락률(%)": {
   "1일": 1.0,
   "7일": -4.08,
   "30일": -11.3,
   "90일": -38.89
  },
  "종가와 이평선 거리(%)": {
   "MA20": -4.78,
   "MA60": -21.65,
   "MA120": -29.43
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 36
  },
  "RSI14": 30.9
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
 "시가총액 순위": 352,
 "시가총액(USD)": 69319217,
 "완전희석가치 FDV(USD)": 69319217,
 "24시간 거래대금(USD)": 16928475,
 "유통량": 1220081.53142126,
 "총발행량": 1220081.53142126,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 130.12,
 "역대 최고가 대비(%)": -56.32655,
 "가격 변화(%)": {
  "7d": -38.75075,
  "30d": -51.41082,
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
   "제목": "Google could take stake in bitcoin miner TeraWulf’s $19 billion AI project if Anthropic defaults",
   "요약": "A $19 billion data-center agreement includes an unusual provision allowing Google to acquire part of the project if Anthropic fails to pay its rent.",
   "시각(UTC)": "11-05 13:29"
  },
  {
   "출처": "CoinDesk",
   "제목": "Binance cuts SignalPlus access after security warning, urges users to check accounts",
   "요약": "The exchange says its systems are unaffected but has removed trading connections to the third-party platform as a precaution.",
   "시각(UTC)": "11-05 12:55"
  },
  {
   "출처": "CoinDesk",
   "제목": "Ukraine’s central bank opposes crypto bill, citing monetary sovereignty concerns",
   "요약": "Ukraine’s central bank won’t back a crypto legalization bill in its current form and wants lawmakers to revise it before a final vote.",
   "시각(UTC)": "11-05 12:50"
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
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin edges lower as markets cool following yesterday's rally",
   "요약": "There's been no letup in selling of the AI chip stocks, sending Nasdaq 100 futures nearly 1% lower.",
   "시각(UTC)": "11-05 10:57"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "50 (Neutral)",
  "최근 7일": [
   50,
   34,
   26,
   37,
   34,
   30,
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
   "TRUMP",
   "PEARL",
   "SOL",
   "CARDS",
   "PENGU",
   "ETH",
   "DOT",
   "BTC",
   "HYPE",
   "INJ",
   "AERO",
   "SUI",
   "PI",
   "PUMP",
   "LIT"
  ],
  "INTCB가 인기 검색에 있음": false
 }
}
```
