# TF팀 회의 자료 (2026-11-05 17:39 KST)

GitHub Actions가 무료 공개 API로 모은 자료입니다. 회의 진행 방법은 `aicoin/tf_team/PLAYBOOK.md`.
자료에 없는 숫자는 쓰지 않습니다. 실패한 자료는 아래 '수집 실패'에 있습니다.

분석 대상: BTC, ETH, BMT, PEPE, INTCB

**지금까지 승률** ACE 40.9% (9/22), 채점 대기 0개 · 자세히는 `paper/tf/SCOREBOARD.md`, 교훈은 `aicoin/tf_team/LESSONS.md`

**TRAINER 모의 계좌** 총자산 10,012.13 USDT (+0.12%), 보유 PEPE · 자세히는 `paper/tf/trainer/TRAINER.md`

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
   "1일": -0.23,
   "7일": 5.05,
   "30일": 3.88,
   "90일": -3.36
  },
  "종가와 이평선 거리(%)": {
   "MA20": 2.73,
   "MA60": 1.86,
   "MA120": 0.07
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 69
  },
  "RSI14": 64.6
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
 "시가총액(USD)": 1619974959665,
 "완전희석가치 FDV(USD)": 1619974959665,
 "24시간 거래대금(USD)": 35146534361,
 "유통량": 20105365.0,
 "총발행량": 20105365.0,
 "최대발행량": 21000000.0,
 "유통 비율(%)": 95.7,
 "역대 최고가(USD)": 126080,
 "역대 최고가 대비(%)": -36.09269,
 "가격 변화(%)": {
  "7d": 0.99258,
  "30d": -5.84031,
  "1y": -20.85049
 },
 "소개": "Bitcoin is the world's first decentralized cryptocurrency, created in 2009 by the pseudonymous Satoshi Nakamoto. It enables peer-to-peer electronic cash transactions without intermediaries like banks or governments, operating on a blockchain secured by Proof of Work mining and the SHA-256 cryptographic algorithm. \n\nWith a fixed supply cap of 21 million coins and programmatic halvings every four ye",
 "체인 TVL (DefiLlama)": {
  "체인": "Bitcoin",
  "TVL(USD)": 4267783873
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "BTC 관련 기사": [
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
   "출처": "CoinDesk",
   "제목": "THORChain's RUNE jumps 10% as North Korean hackers resume laundering Binance loot",
   "요약": "North Korea’s TraderTraitor is routing Binance hack proceeds through THORChain, swapping ether for bitcoin after an earlier wave of conversions from Tron.",
   "시각(UTC)": "11-04 12:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin rebounds from midterm dip as DeFi leads gains",
   "요약": "Bitcoin recovered from a dip to around $75,600 as Democrats won Congress, while DeFi tokens led gains and Trump-linked coins fell.",
   "시각(UTC)": "11-04 10:38"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin rises to $78,300 in V-shaped comeback as midterm election uncertainty fades",
   "요약": "Crypto prices reversed overnight losses following the Blue Wave landslide for the Democratic Party.",
   "시각(UTC)": "11-04 06:16"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Here’s what happened in crypto today",
   "요약": "Need to know what happened in crypto today? Here is the latest news on daily trends and events impacting Bitcoin price, blockchain, DeFi, Web3 and crypto regulation.",
   "시각(UTC)": "11-05 06:21"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Mercado Bitcoin says phased reopening to begin Monday, will cover losses",
   "요약": "Customers will initially be able to view their holdings, while withdrawals and trading remain suspended pending security checks.",
   "시각(UTC)": "11-04 23:20"
  },
  {
   "출처": "Cointelegraph",
   "제목": "BitMart founder says security team ‘severely understaffed’ after new hack",
   "요약": "The crypto exchange’s founder warned of security staffing shortages amid restructuring as analysts flagged suspicious transfers potentially linked to the Mercado Bitcoin hack.",
   "시각(UTC)": "11-04 22:31"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Trump-linked tokens lead crypto losses after Democrats sweep in the US midterms",
   "요약": "The official Trump and World Liberty Financial tokens were the two biggest losers among the top 100 cryptocurrencies on Wednesday, even as Bitcoin and Ether rallied.",
   "시각(UTC)": "11-04 19:15"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Riot shares surge on $28B AI lease as Hut 8 sinks on revenue miss",
   "요약": "Bitcoin miner Riot sold BTC to finance its AI expansion, while Hut 8 reported falling revenue and rising costs before its major data center leases generate income.",
   "시각(UTC)": "11-04 18:47"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin hits $80.5K as US stocks rally on midterm election results",
   "요약": "Bitcoin climbed toward $80,500 as risk assets rallied on Democrats’ midterm election gains and oil prices fell.",
   "시각(UTC)": "11-04 15:29"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin ETFs lose $1.16B as Bitwise calls selling ‘short-term’",
   "요약": "Bitwise’s André Dragosch attributed Bitcoin ETF outflows to weaker market sentiment, saying institutions have largely maintained their exposure.",
   "시각(UTC)": "11-04 09:38"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin bounces from 7-week low under $76K as Democrats sweep Congress",
   "요약": "Bitcoin price downside reached a seven-week-low of $75,618 as 24-hour crypto long liquidations neared $300 million.",
   "시각(UTC)": "11-04 07:25"
  }
 ],
 "시장 전반 기사": [
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto's Washington hopes fade, but Grayscale and BlackRock see growth ahead",
   "요약": "The asset manager says global demand and institutional adoption will sustain the industry despite a political setback, while BlackRock sees little impact on its crypto business.",
   "시각(UTC)": "11-04 22:51"
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto's powerhouse super PAC suffers costly setback as Democrats sweep Congress",
   "요약": "The industry's primary campaign arm had cultivated a reputation as an unstoppable force, but more than a third of its spending failed to hit the mark, especially in Ohio.",
   "시각(UTC)": "11-04 20:29"
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
   "WEEX (Futures)": 0.0,
   "Tapbit (Futures)": 0.01
  },
  "미결제약정 합계 USD(상위)": 29938379208
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 80.65,
  "CoinGecko 인기 검색 코인": [
   "PENGU",
   "CARDS",
   "TRUMP",
   "PEARL",
   "KNTQ",
   "MON",
   "BTC",
   "BP",
   "DRV",
   "VVV",
   "SOL",
   "INJ",
   "NEAR",
   "QTC",
   "ETH"
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
   "1일": -0.34,
   "7일": 7.42,
   "30일": 7.67,
   "90일": -1.63
  },
  "종가와 이평선 거리(%)": {
   "MA20": 4.41,
   "MA60": 4.93,
   "MA120": 2.69
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 1
  },
  "RSI14": 68.3
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
 "시가총액(USD)": 296337320314,
 "완전희석가치 FDV(USD)": 296337320314,
 "24시간 거래대금(USD)": 15255268436,
 "유통량": 122192071.85523713,
 "총발행량": 122192071.85523713,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 4946.05,
 "역대 최고가 대비(%)": -50.96737,
 "가격 변화(%)": {
  "7d": 5.07437,
  "30d": -10.46631,
  "1y": -27.00971
 },
 "소개": "Ethereum is a global, open-source platform for decentralized applications. In other words, it is a decentralized blockchain platform that enables developers to build and deploy smart contracts and applications without central authority control. Unlike Bitcoin, which primarily functions as digital currency, Ethereum operates as a programmable global computer where developers can create any type of ",
 "체인 TVL (DefiLlama)": {
  "체인": "Ethereum",
  "TVL(USD)": 45857373645
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
   "출처": "CoinDesk",
   "제목": "THORChain's RUNE jumps 10% as North Korean hackers resume laundering Binance loot",
   "요약": "North Korea’s TraderTraitor is routing Binance hack proceeds through THORChain, swapping ether for bitcoin after an earlier wave of conversions from Tron.",
   "시각(UTC)": "11-04 12:49"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Trump-linked tokens lead crypto losses after Democrats sweep in the US midterms",
   "요약": "The official Trump and World Liberty Financial tokens were the two biggest losers among the top 100 cryptocurrencies on Wednesday, even as Bitcoin and Ether rallied.",
   "시각(UTC)": "11-04 19:15"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Ethereum dev targets 2028 for quantum resistance, a year early",
   "요약": "Ethereum researcher Justin Drake said it is their “hope” that Ethereum will achieve its post-quantum and post-AI transition by December 2028.",
   "시각(UTC)": "11-04 05:46"
  },
  {
   "출처": "Cointelegraph",
   "제목": "RUNE rallies 15% as THORChain restarts most swaps after halt",
   "요약": "THORChain has restored trading on Bitcoin, Ethereum and several other networks following a refund bug, while three chains remain paused.",
   "시각(UTC)": "11-03 23:56"
  },
  {
   "출처": "Decrypt",
   "제목": "Ethereum Privacy Network Aztec Rolls Out Major Security and Speed Upgrade",
   "요약": "The “Tierra” upgrade resolves a critical bug from the prior version, adds formal verification, and an AI-powered testing harness.",
   "시각(UTC)": "11-03 14:01"
  },
  {
   "출처": "Decrypt",
   "제목": "Morning Minute: Tom Lee Calls the Binance Hack Bullish for Ethereum",
   "요약": "Meanwhile, both the BTC ETFs and ETH ETFs bleed outflows in the Binance hack aftermath, dragging down prices.",
   "시각(UTC)": "11-03 13:11"
  }
 ],
 "시장 전반 기사": [
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
   "제목": "Trump Media moves $342 million in bitcoin to Crypto.com, blockchain data show",
   "요약": "A wallet supposedly linked to Trump Media has made a large BTC transfer to Crypto.com, data tracked by Arkham show.",
   "시각(UTC)": "11-05 04:11"
  },
  {
   "출처": "CoinDesk",
   "제목": "Tokenization and stablecoins may weather Democrats' sweep as broader crypto rules face uncertainty",
   "요약": "Wall Street's push to bring finance onto blockchain rails may continue under existing laws, though the SEC and CFTC face tougher oversight and questions over how long their rules will last, experts said.",
   "시각(UTC)": "11-04 22:55"
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto's Washington hopes fade, but Grayscale and BlackRock see growth ahead",
   "요약": "The asset manager says global demand and institutional adoption will sustain the industry despite a political setback, while BlackRock sees little impact on its crypto business.",
   "시각(UTC)": "11-04 22:51"
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
   "MEXC (Futures)": 0.009,
   "CoinW (Futures)": 0.0079
  },
  "미결제약정 합계 USD(상위)": 19128544438
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 87.5,
  "CoinGecko 인기 검색 코인": [
   "PENGU",
   "CARDS",
   "TRUMP",
   "PEARL",
   "KNTQ",
   "MON",
   "BTC",
   "BP",
   "DRV",
   "VVV",
   "SOL",
   "INJ",
   "NEAR",
   "QTC",
   "ETH"
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
   "1일": -4.53,
   "7일": -13.19,
   "30일": 15.76,
   "90일": 29.33
  },
  "종가와 이평선 거리(%)": {
   "MA20": 2.92,
   "MA60": 1.89,
   "MA120": 6.39
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 37
  },
  "RSI14": 50.5
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
 "시가총액 순위": 855,
 "시가총액(USD)": 19898183,
 "완전희석가치 FDV(USD)": 26141557,
 "24시간 거래대금(USD)": 56015987,
 "유통량": 761170523.0,
 "총발행량": 1000000000.0,
 "최대발행량": 1000000000.0,
 "유통 비율(%)": 76.1,
 "역대 최고가(USD)": 0.317341,
 "역대 최고가 대비(%)": -91.7623,
 "가격 변화(%)": {
  "7d": -1.56076,
  "30d": 33.54021,
  "1y": -18.42753
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
   "Binance (Futures)": -0.2473,
   "Bybit (Futures)": -0.1772,
   "Toobit Futures": -0.2487,
   "Ourbit (Futures)": -0.2486,
   "KCEX (Futures)": -0.2486,
   "Gate (Futures)": -0.209
  },
  "미결제약정 합계 USD(상위)": 15806945
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 33.33,
  "CoinGecko 인기 검색 코인": [
   "PENGU",
   "CARDS",
   "TRUMP",
   "PEARL",
   "KNTQ",
   "MON",
   "BTC",
   "BP",
   "DRV",
   "VVV",
   "SOL",
   "INJ",
   "NEAR",
   "QTC",
   "ETH"
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
   "1일": -1.0,
   "7일": 2.49,
   "30일": -2.56,
   "90일": 8.1
  },
  "종가와 이평선 거리(%)": {
   "MA20": 1.37,
   "MA60": 1.9,
   "MA120": 7.89
  },
  "MA20>MA60": true,
  "최근 교차": null,
  "RSI14": 51.5
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
 "시가총액(USD)": 2121896568,
 "완전희석가치 FDV(USD)": 2121896568,
 "24시간 거래대금(USD)": 515267415,
 "유통량": 420690000000000.0,
 "총발행량": 420690000000000.0,
 "최대발행량": 420690000000000.0,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 2.803e-05,
 "역대 최고가 대비(%)": -81.9972,
 "가격 변화(%)": {
  "7d": 2.84794,
  "30d": 16.43325,
  "1y": -10.72333
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
   "MEXC (Futures)": 0.0059,
   "Gate (Futures)": 0.01,
   "OKX (Futures)": 0.01,
   "Bitget Futures": 0.01,
   "KCEX (Futures)": 0.01,
   "WhiteBIT Futures": 0.01
  },
  "미결제약정 합계 USD(상위)": 295730117
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 90.32,
  "CoinGecko 인기 검색 코인": [
   "PENGU",
   "CARDS",
   "TRUMP",
   "PEARL",
   "KNTQ",
   "MON",
   "BTC",
   "BP",
   "DRV",
   "VVV",
   "SOL",
   "INJ",
   "NEAR",
   "QTC",
   "ETH"
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
   "1일": -0.91,
   "7일": -1.8,
   "30일": -12.12,
   "90일": -40.23
  },
  "종가와 이평선 거리(%)": {
   "MA20": -6.47,
   "MA60": -22.96,
   "MA120": -30.39
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 35
  },
  "RSI14": 27.9
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
 "시가총액 순위": 356,
 "시가총액(USD)": 68982184,
 "완전희석가치 FDV(USD)": 68982184,
 "24시간 거래대금(USD)": 18182378,
 "유통량": 1210366.80979207,
 "총발행량": 1210366.80979207,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 130.12,
 "역대 최고가 대비(%)": -56.20057,
 "가격 변화(%)": {
  "7d": -37.97356,
  "30d": -51.05232,
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
  "오류": "ValueError: INTCB 무기한 선물 자료 없음"
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": null,
  "CoinGecko 인기 검색 코인": [
   "PENGU",
   "CARDS",
   "TRUMP",
   "PEARL",
   "KNTQ",
   "MON",
   "BTC",
   "BP",
   "DRV",
   "VVV",
   "SOL",
   "INJ",
   "NEAR",
   "QTC",
   "ETH"
  ],
  "INTCB가 인기 검색에 있음": false
 }
}
```
