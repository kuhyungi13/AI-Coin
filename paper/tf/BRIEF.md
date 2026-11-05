# TF팀 회의 자료 (2026-11-06 03:19 KST)

GitHub Actions가 무료 공개 API로 모은 자료입니다. 회의 진행 방법은 `aicoin/tf_team/PLAYBOOK.md`.
자료에 없는 숫자는 쓰지 않습니다. 실패한 자료는 아래 '수집 실패'에 있습니다.

분석 대상: BTC, ETH, BMT, PEPE, INTCB

**지금까지 승률** ACE 40.9% (9/22), 채점 대기 0개 · 자세히는 `paper/tf/SCOREBOARD.md`, 교훈은 `aicoin/tf_team/LESSONS.md`

**TRAINER 모의 계좌** 총자산 9,995.42 USDT (-0.05%), 보유 PEPE · 자세히는 `paper/tf/trainer/TRAINER.md`

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
   "1일": -5.42,
   "7일": -3.12,
   "30일": -2.05,
   "90일": -10.07
  },
  "종가와 이평선 거리(%)": {
   "MA20": -2.79,
   "MA60": -3.54,
   "MA120": -5.25
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 71
  },
  "RSI14": 36.3
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
 "시가총액(USD)": 1525712265779,
 "완전희석가치 FDV(USD)": 1525712265779,
 "24시간 거래대금(USD)": 39820760192,
 "유통량": 20105365.0,
 "총발행량": 20105365.0,
 "최대발행량": 21000000.0,
 "유통 비율(%)": 95.7,
 "역대 최고가(USD)": 126080,
 "역대 최고가 대비(%)": -39.81131,
 "가격 변화(%)": {
  "7d": -6.08588,
  "30d": -11.4742,
  "1y": -26.91902
 },
 "소개": "Bitcoin is the world's first decentralized cryptocurrency, created in 2009 by the pseudonymous Satoshi Nakamoto. It enables peer-to-peer electronic cash transactions without intermediaries like banks or governments, operating on a blockchain secured by Proof of Work mining and the SHA-256 cryptographic algorithm. \n\nWith a fixed supply cap of 21 million coins and programmatic halvings every four ye",
 "체인 TVL (DefiLlama)": {
  "체인": "Bitcoin",
  "TVL(USD)": 4064497973
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "BTC 관련 기사": [
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
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin plunges as Nasdaq falls 4% in panicky selloff",
   "요약": "There's been no letup in the selling of the AI chip stocks, with Micron and AMD among those suffering double-digit percentage declines; Nvidia is down 8%.",
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
   "출처": "Cointelegraph",
   "제목": "Bitcoin crashes 6% to 7-week low as US stocks erase election gains",
   "요약": "Bitcoin saw sudden downside at the Wall Street open as stocks witnessed a snap sell-off, reversing post-election gains.",
   "시각(UTC)": "11-05 16:48"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Here’s what happened in crypto today",
   "요약": "Need to know what happened in crypto today? Here is the latest news on daily trends and events impacting Bitcoin price, blockchain, DeFi, Web3 and crypto regulation.",
   "시각(UTC)": "11-05 13:46"
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
  }
 ],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "What is TraderTraitor, the hacking squad behind the $6.3 billion Binance heist",
   "요약": "The hacking group has been behind some of the crypto industry's most recent high-profile thefts.",
   "시각(UTC)": "11-05 16:58"
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto for Advisors: Where investors stake crypto shapes how much of the reward they keep",
   "요약": "",
   "시각(UTC)": "11-05 16:13"
  },
  {
   "출처": "CoinDesk",
   "제목": "Gate CEO says crypto exchanges must prove they can survive a hack like Binance’s",
   "요약": "Lin Han says Gate holds enough assets in cold storage to cover customer balances even if its hot wallets are emptied. An independent audit is underway.",
   "시각(UTC)": "11-05 14:21"
  },
  {
   "출처": "CoinDesk",
   "제목": "Kraken parent Payward and its clients buy AAVE tokens in DeFi investment push",
   "요약": "The investment follows talks first reported by CoinDesk in June that included a proposed equity stake in Aave Group.",
   "시각(UTC)": "11-05 14:00"
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
   "제목": "Hong Kong passes law requiring crypto exchanges to report customer transactions to tax authorities",
   "요약": "Crypto firms must collect customer and transaction data from 2027, with Hong Kong sharing the information with overseas tax authorities from 2028.",
   "시각(UTC)": "11-05 08:35"
  },
  {
   "출처": "CoinDesk",
   "제목": "OpenAI says its AI can break into Linux at scale. Here's what it means for crypto",
   "요약": "OpenAI says its AI found 948 Linux flaws and wrote a working attack for each one. Crypto security voices say decentralization leaves the industry better placed than most to cope.",
   "시각(UTC)": "11-05 08:26"
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
   "Bybit (Futures)": 0.0063,
   "MEXC (Futures)": 0.01,
   "Gate (Futures)": 0.01,
   "WEEX (Futures)": 0.0001,
   "Tapbit (Futures)": 0.01
  },
  "미결제약정 합계 USD(상위)": 28527103348
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 66.67,
  "CoinGecko 인기 검색 코인": [
   "BTC",
   "LIT",
   "NEAR",
   "INJ",
   "HYPE",
   "TRUMP",
   "ZEC",
   "PENGU",
   "ETH",
   "SUI",
   "BP",
   "PEPE",
   "PEARL",
   "QTC",
   "AERO"
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
   "1일": -6.95,
   "7일": -3.23,
   "30일": 0.08,
   "90일": -10.34
  },
  "종가와 이평선 거리(%)": {
   "MA20": -2.82,
   "MA60": -2.18,
   "MA120": -4.18
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 3
  },
  "RSI14": 40.5
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
 "시가총액(USD)": 274875100199,
 "완전희석가치 FDV(USD)": 274875100199,
 "24시간 거래대금(USD)": 15547685540,
 "유통량": 122192071.85523713,
 "총발행량": 122192071.85523713,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 4946.05,
 "역대 최고가 대비(%)": -54.51855,
 "가격 변화(%)": {
  "7d": -3.8071,
  "30d": -16.66355,
  "1y": -34.49659
 },
 "소개": "Ethereum is a global, open-source platform for decentralized applications. In other words, it is a decentralized blockchain platform that enables developers to build and deploy smart contracts and applications without central authority control. Unlike Bitcoin, which primarily functions as digital currency, Ethereum operates as a programmable global computer where developers can create any type of ",
 "체인 TVL (DefiLlama)": {
  "체인": "Ethereum",
  "TVL(USD)": 43547355315
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
   "출처": "CoinDesk",
   "제목": "Bitcoin holds above $80,000 as Zcash jumps 12% in post-election crypto rebound",
   "요약": "Ether rose 8% as falling oil prices and a weaker dollar helped markets recover, even as traders weighed a tougher path for U.S. crypto legislation.",
   "시각(UTC)": "11-05 05:13"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Europe’s largest asset manager Amundi tokenizes equity index fund on Ethereum",
   "요약": "The new share class offers blockchain-based exposure to an index tracking 600 companies across European markets.",
   "시각(UTC)": "11-05 18:09"
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
  }
 ],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "What is TraderTraitor, the hacking squad behind the $6.3 billion Binance heist",
   "요약": "The hacking group has been behind some of the crypto industry's most recent high-profile thefts.",
   "시각(UTC)": "11-05 16:58"
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto for Advisors: Where investors stake crypto shapes how much of the reward they keep",
   "요약": "",
   "시각(UTC)": "11-05 16:13"
  },
  {
   "출처": "CoinDesk",
   "제목": "Gate CEO says crypto exchanges must prove they can survive a hack like Binance’s",
   "요약": "Lin Han says Gate holds enough assets in cold storage to cover customer balances even if its hot wallets are emptied. An independent audit is underway.",
   "시각(UTC)": "11-05 14:21"
  },
  {
   "출처": "CoinDesk",
   "제목": "Kraken parent Payward and its clients buy AAVE tokens in DeFi investment push",
   "요약": "The investment follows talks first reported by CoinDesk in June that included a proposed equity stake in Aave Group.",
   "시각(UTC)": "11-05 14:00"
  },
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
   "Binance (Futures)": 0.0014,
   "WEEX (Futures)": 0.0001,
   "CoinW (Futures)": 0.01,
   "MEXC (Futures)": 0.01,
   "Hyperliquid (Futures)": 0.0011
  },
  "미결제약정 합계 USD(상위)": 18650256541
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 83.08,
  "CoinGecko 인기 검색 코인": [
   "BTC",
   "LIT",
   "NEAR",
   "INJ",
   "HYPE",
   "TRUMP",
   "ZEC",
   "PENGU",
   "ETH",
   "SUI",
   "BP",
   "PEPE",
   "PEARL",
   "QTC",
   "AERO"
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
   "1일": -1.4,
   "7일": -17.17,
   "30일": 11.81,
   "90일": 15.0
  },
  "종가와 이평선 거리(%)": {
   "MA20": -0.94,
   "MA60": 0.17,
   "MA120": 3.51
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 1
  },
  "RSI14": 48.2
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
 "시가총액 순위": 843,
 "시가총액(USD)": 19273474,
 "완전희석가치 FDV(USD)": 25299442,
 "24시간 거래대금(USD)": 35725984,
 "유통량": 761814186.0,
 "총발행량": 1000000000.0,
 "최대발행량": 1000000000.0,
 "유통 비율(%)": 76.2,
 "역대 최고가(USD)": 0.317341,
 "역대 최고가 대비(%)": -92.02792,
 "가격 변화(%)": {
  "7d": -2.74577,
  "30d": 29.14629,
  "1y": -22.52278
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
   "제목": "What is TraderTraitor, the hacking squad behind the $6.3 billion Binance heist",
   "요약": "The hacking group has been behind some of the crypto industry's most recent high-profile thefts.",
   "시각(UTC)": "11-05 16:58"
  },
  {
   "출처": "CoinDesk",
   "제목": "Standard Chartered and SBI back crypto insurer Soter as funding reaches $23.5 million",
   "요약": "Soter also received backing of 500 BTC and 2000 ETH, worth another $43 million at current prices.",
   "시각(UTC)": "11-05 16:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto for Advisors: Where investors stake crypto shapes how much of the reward they keep",
   "요약": "",
   "시각(UTC)": "11-05 16:13"
  },
  {
   "출처": "CoinDesk",
   "제목": "Gate CEO says crypto exchanges must prove they can survive a hack like Binance’s",
   "요약": "Lin Han says Gate holds enough assets in cold storage to cover customer balances even if its hot wallets are emptied. An independent audit is underway.",
   "시각(UTC)": "11-05 14:21"
  },
  {
   "출처": "CoinDesk",
   "제목": "Kraken parent Payward and its clients buy AAVE tokens in DeFi investment push",
   "요약": "The investment follows talks first reported by CoinDesk in June that included a proposed equity stake in Aave Group.",
   "시각(UTC)": "11-05 14:00"
  },
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
   "Binance (Futures)": -0.0873,
   "Bybit (Futures)": -0.0349,
   "Toobit Futures": -0.0873,
   "Ourbit (Futures)": -0.0872,
   "KCEX (Futures)": -0.0872,
   "Gate (Futures)": -0.1122
  },
  "미결제약정 합계 USD(상위)": 12231776
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 33.33,
  "CoinGecko 인기 검색 코인": [
   "BTC",
   "LIT",
   "NEAR",
   "INJ",
   "HYPE",
   "TRUMP",
   "ZEC",
   "PENGU",
   "ETH",
   "SUI",
   "BP",
   "PEPE",
   "PEARL",
   "QTC",
   "AERO"
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
   "1일": -5.24,
   "7일": -6.56,
   "30일": -5.81,
   "90일": 0.21
  },
  "종가와 이평선 거리(%)": {
   "MA20": -3.47,
   "MA60": -3.36,
   "MA120": 2.35
  },
  "MA20>MA60": true,
  "최근 교차": null,
  "RSI14": 41.5
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
 "시가총액(USD)": 2005779842,
 "완전희석가치 FDV(USD)": 2005779842,
 "24시간 거래대금(USD)": 441550468,
 "유통량": 420690000000000.0,
 "총발행량": 420690000000000.0,
 "최대발행량": 420690000000000.0,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 2.803e-05,
 "역대 최고가 대비(%)": -82.98915,
 "가격 변화(%)": {
  "7d": -12.1752,
  "30d": 10.94216,
  "1y": -16.87561
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
   "제목": "What is TraderTraitor, the hacking squad behind the $6.3 billion Binance heist",
   "요약": "The hacking group has been behind some of the crypto industry's most recent high-profile thefts.",
   "시각(UTC)": "11-05 16:58"
  },
  {
   "출처": "CoinDesk",
   "제목": "Standard Chartered and SBI back crypto insurer Soter as funding reaches $23.5 million",
   "요약": "Soter also received backing of 500 BTC and 2000 ETH, worth another $43 million at current prices.",
   "시각(UTC)": "11-05 16:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto for Advisors: Where investors stake crypto shapes how much of the reward they keep",
   "요약": "",
   "시각(UTC)": "11-05 16:13"
  },
  {
   "출처": "CoinDesk",
   "제목": "Gate CEO says crypto exchanges must prove they can survive a hack like Binance’s",
   "요약": "Lin Han says Gate holds enough assets in cold storage to cover customer balances even if its hot wallets are emptied. An independent audit is underway.",
   "시각(UTC)": "11-05 14:21"
  },
  {
   "출처": "CoinDesk",
   "제목": "Kraken parent Payward and its clients buy AAVE tokens in DeFi investment push",
   "요약": "The investment follows talks first reported by CoinDesk in June that included a proposed equity stake in Aave Group.",
   "시각(UTC)": "11-05 14:00"
  },
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
   "Gate (Futures)": -0.0158,
   "Bitget Futures": 0.01,
   "OKX (Futures)": 0.01,
   "KCEX (Futures)": 0.01,
   "WhiteBIT Futures": 0.01
  },
  "미결제약정 합계 USD(상위)": 280514420
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 85.71,
  "CoinGecko 인기 검색 코인": [
   "BTC",
   "LIT",
   "NEAR",
   "INJ",
   "HYPE",
   "TRUMP",
   "ZEC",
   "PENGU",
   "ETH",
   "SUI",
   "BP",
   "PEPE",
   "PEARL",
   "QTC",
   "AERO"
  ],
  "PEPE가 인기 검색에 있음": true
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
   "1일": -6.75,
   "7일": -10.64,
   "30일": -17.78,
   "90일": -42.38
  },
  "종가와 이평선 거리(%)": {
   "MA20": -10.24,
   "MA60": -26.31,
   "MA120": -33.93
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 37
  },
  "RSI14": 23.7
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
 "시가총액 순위": 353,
 "시가총액(USD)": 66112265,
 "완전희석가치 FDV(USD)": 66112265,
 "24시간 거래대금(USD)": 17355687,
 "유통량": 1224172.32365121,
 "총발행량": 1224172.32365121,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 130.12,
 "역대 최고가 대비(%)": -58.49619,
 "가격 변화(%)": {
  "7d": -40.88701,
  "30d": -52.93767,
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
   "제목": "What is TraderTraitor, the hacking squad behind the $6.3 billion Binance heist",
   "요약": "The hacking group has been behind some of the crypto industry's most recent high-profile thefts.",
   "시각(UTC)": "11-05 16:58"
  },
  {
   "출처": "CoinDesk",
   "제목": "Standard Chartered and SBI back crypto insurer Soter as funding reaches $23.5 million",
   "요약": "Soter also received backing of 500 BTC and 2000 ETH, worth another $43 million at current prices.",
   "시각(UTC)": "11-05 16:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto for Advisors: Where investors stake crypto shapes how much of the reward they keep",
   "요약": "",
   "시각(UTC)": "11-05 16:13"
  },
  {
   "출처": "CoinDesk",
   "제목": "Gate CEO says crypto exchanges must prove they can survive a hack like Binance’s",
   "요약": "Lin Han says Gate holds enough assets in cold storage to cover customer balances even if its hot wallets are emptied. An independent audit is underway.",
   "시각(UTC)": "11-05 14:21"
  },
  {
   "출처": "CoinDesk",
   "제목": "Kraken parent Payward and its clients buy AAVE tokens in DeFi investment push",
   "요약": "The investment follows talks first reported by CoinDesk in June that included a proposed equity stake in Aave Group.",
   "시각(UTC)": "11-05 14:00"
  },
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
   "BTC",
   "LIT",
   "NEAR",
   "INJ",
   "HYPE",
   "TRUMP",
   "ZEC",
   "PENGU",
   "ETH",
   "SUI",
   "BP",
   "PEPE",
   "PEARL",
   "QTC",
   "AERO"
  ],
  "INTCB가 인기 검색에 있음": false
 }
}
```
