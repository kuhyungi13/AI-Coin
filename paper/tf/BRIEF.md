# TF팀 회의 자료 (2026-11-05 13:36 KST)

GitHub Actions가 무료 공개 API로 모은 자료입니다. 회의 진행 방법은 `aicoin/tf_team/PLAYBOOK.md`.
자료에 없는 숫자는 쓰지 않습니다. 실패한 자료는 아래 '수집 실패'에 있습니다.

분석 대상: BTC, ETH, BMT, PEPE, INTCB

**지금까지 승률** ACE 52.9% (9/17), 채점 대기 5개 · 자세히는 `paper/tf/SCOREBOARD.md`, 교훈은 `aicoin/tf_team/LESSONS.md`

**TRAINER 모의 계좌** 총자산 10,016.30 USDT (+0.16%), 보유 PEPE · 자세히는 `paper/tf/trainer/TRAINER.md`

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
   "1일": 0.05,
   "7일": 3.99,
   "30일": 4.37,
   "90일": -2.65
  },
  "종가와 이평선 거리(%)": {
   "MA20": 3.09,
   "MA60": 2.1,
   "MA120": 0.28
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 68
  },
  "RSI14": 66.5
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
 "시가총액(USD)": 1618697916481,
 "완전희석가치 FDV(USD)": 1618697916481,
 "24시간 거래대금(USD)": 36871289835,
 "유통량": 20105365.0,
 "총발행량": 20105365.0,
 "최대발행량": 21000000.0,
 "유통 비율(%)": 95.7,
 "역대 최고가(USD)": 126080,
 "역대 최고가 대비(%)": -36.14307,
 "가격 변화(%)": {
  "7d": 0.93918,
  "30d": -5.83568,
  "1y": -21.15974
 },
 "소개": "Bitcoin is the world's first decentralized cryptocurrency, created in 2009 by the pseudonymous Satoshi Nakamoto. It enables peer-to-peer electronic cash transactions without intermediaries like banks or governments, operating on a blockchain secured by Proof of Work mining and the SHA-256 cryptographic algorithm. \n\nWith a fixed supply cap of 21 million coins and programmatic halvings every four ye",
 "체인 TVL (DefiLlama)": {
  "체인": "Bitcoin",
  "TVL(USD)": 4278762841
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "BTC 관련 기사": [
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
   "출처": "CoinDesk",
   "제목": "Jack Dorsey's Block faces $764 million DOJ settlement as bitcoin profit plunges 50%",
   "요약": "The proposed agreement would resolve a federal anti-money-laundering investigation, while lower Cash App trading fees halved Block's quarterly bitcoin gross profit.",
   "시각(UTC)": "11-04 06:06"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S.-sanctioned Moscow Exchange to list bitcoin and Tether’s USDT in December",
   "요약": "Russia’s main bourse wants back the crypto trading Russians do abroad, and one of the coins it's listing is issued by a company that freezes wallets on the U.S. sanctions list.",
   "시각(UTC)": "11-04 05:14"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin briefly sinks to $75,700 as bets on a Democratic sweep rattle markets",
   "요약": "Stock futures and the dollar slid and Treasuries rallied as early U.S. midterm returns pointed to Democrats taking both chambers of Congress.",
   "시각(UTC)": "11-04 04:48"
  },
  {
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin and stocks reverse overnight plunge following Blue Wave landslide",
   "요약": "The biggest losers, so far, are the AI data center stocks following victories for several candidates who campaigned expressly against the sector.",
   "시각(UTC)": "11-04 00:00"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Mercado Bitcoin says phased reopening to begin Monday, will cover losses",
   "요약": "Customers will initially be able to view their holdings, while withdrawals and trading remain suspended pending security checks.",
   "시각(UTC)": "11-04 23:20"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Here’s what happened in crypto today",
   "요약": "Need to know what happened in crypto today? Here is the latest news on daily trends and events impacting Bitcoin price, blockchain, DeFi, Web3 and crypto regulation.",
   "시각(UTC)": "11-04 22:54"
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
  }
 ],
 "시장 전반 기사": [
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
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. Democratic sweep could be the final nail in the ‘Clarity Act’s coffin’",
   "요약": "Industry experts warn the Clarity Act is likely dead in its current form as incoming Democratic majorities eye tighter scrutiny of crypto markets and tokenized stocks.",
   "시각(UTC)": "11-04 16:11"
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto Long & Short: ICE is betting on retail’s appetite for quick outcomes",
   "요약": "Retail traders increasingly want trades that resolve fast, from prediction markets to same-day options. Andy Baehr of GSR argues perpetual futures belong in that group, and that ICE’s deal to bring Trade[XYZ]’s Hyperliquid markets onshore i",
   "시각(UTC)": "11-04 15:27"
  },
  {
   "출처": "CoinDesk",
   "제목": "The election changes Washington. The work on crypto continues",
   "요약": "The next Congress inherits an unfinished assignment: establishing clear, lasting rules for digital assets that protect consumers and ensure American innovation continues to thrive, writes Blockchain Association's Lindsay Fraser.",
   "시각(UTC)": "11-04 14:25"
  },
  {
   "출처": "CoinDesk",
   "제목": "Global asset manager Schroders brings emerging market bond fund to Solana",
   "요약": "The global asset manager, which oversees $1.1 trillion in assets, is bringing an actively managed bond strategy onchain through tokenization specialist Centrifuge.",
   "시각(UTC)": "11-04 13:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "Circle beats earnings expectations on strong revenue, but cuts 5% of its workforce",
   "요약": "Circle’s net income for continuing operations of $226 million grew 5% year-over-year to $226 million in the third quarter.",
   "시각(UTC)": "11-04 12:33"
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
   "Binance (Futures)": 0.0079,
   "Bybit (Futures)": 0.01,
   "Gate (Futures)": 0.01,
   "MEXC (Futures)": 0.0078,
   "Tapbit (Futures)": 0.0079,
   "WEEX (Futures)": 0.0001
  },
  "미결제약정 합계 USD(상위)": 29697077410
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 77.72,
  "CoinGecko 인기 검색 코인": [
   "PENGU",
   "TRUMP",
   "BTC",
   "NEAR",
   "ZEC",
   "UNI",
   "ENA",
   "PEARL",
   "LIT",
   "VVV",
   "LINK",
   "BEAM",
   "SUI",
   "ADA",
   "ZRO"
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
   "1일": -0.01,
   "7일": 6.58,
   "30일": 8.23,
   "90일": -0.81
  },
  "종가와 이평선 거리(%)": {
   "MA20": 5.09,
   "MA60": 5.36,
   "MA120": 3.03
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 0
  },
  "RSI14": 70.5
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
 "시가총액(USD)": 296585717934,
 "완전희석가치 FDV(USD)": 296585718289,
 "24시간 거래대금(USD)": 16287979190,
 "유통량": 122192071.85523713,
 "총발행량": 122192072.00183041,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 4946.05,
 "역대 최고가 대비(%)": -50.92627,
 "가격 변화(%)": {
  "7d": 5.24828,
  "30d": -10.06881,
  "1y": -27.2903
 },
 "소개": "Ethereum is a global, open-source platform for decentralized applications. In other words, it is a decentralized blockchain platform that enables developers to build and deploy smart contracts and applications without central authority control. Unlike Bitcoin, which primarily functions as digital currency, Ethereum operates as a programmable global computer where developers can create any type of ",
 "체인 TVL (DefiLlama)": {
  "체인": "Ethereum",
  "TVL(USD)": 45931196809
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "ETH 관련 기사": [
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
   "출처": "Cointelegraph",
   "제목": "Wall Street killed Bitcoin’s wild rallies: 10x’s Markus Thielen",
   "요약": "Markus Thielen sees Bitcoin reaching $90,000 by year-end, questions institutional ETF demand and says Ethereum must do more for holders.",
   "시각(UTC)": "11-03 16:47"
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto's powerhouse super PAC suffers costly setback as Democrats sweep Congress",
   "요약": "The industry's primary campaign arm had cultivated a reputation as an unstoppable force, but more than a third of its spending failed to hit the mark, especially in Ohio.",
   "시각(UTC)": "11-04 20:29"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. Democratic sweep could be the final nail in the ‘Clarity Act’s coffin’",
   "요약": "Industry experts warn the Clarity Act is likely dead in its current form as incoming Democratic majorities eye tighter scrutiny of crypto markets and tokenized stocks.",
   "시각(UTC)": "11-04 16:11"
  },
  {
   "출처": "CoinDesk",
   "제목": "Wall Street rethinks AI data center boom as Texas election raises new risks",
   "요약": "Bitcoin miners pivoting to AI face new uncertainty over power access and construction permits, while companies with approved projects could benefit from tighter supply.",
   "시각(UTC)": "11-04 16:08"
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto Long & Short: ICE is betting on retail’s appetite for quick outcomes",
   "요약": "Retail traders increasingly want trades that resolve fast, from prediction markets to same-day options. Andy Baehr of GSR argues perpetual futures belong in that group, and that ICE’s deal to bring Trade[XYZ]’s Hyperliquid markets onshore i",
   "시각(UTC)": "11-04 15:27"
  },
  {
   "출처": "CoinDesk",
   "제목": "The election changes Washington. The work on crypto continues",
   "요약": "The next Congress inherits an unfinished assignment: establishing clear, lasting rules for digital assets that protect consumers and ensure American innovation continues to thrive, writes Blockchain Association's Lindsay Fraser.",
   "시각(UTC)": "11-04 14:25"
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
   "Binance (Futures)": 0.0078,
   "WEEX (Futures)": 0.0001,
   "Hyperliquid (Futures)": 0.0013,
   "MEXC (Futures)": 0.0034,
   "Bitget Futures": 0.0005
  },
  "미결제약정 합계 USD(상위)": 18819897142
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 90.16,
  "CoinGecko 인기 검색 코인": [
   "PENGU",
   "TRUMP",
   "BTC",
   "NEAR",
   "ZEC",
   "UNI",
   "ENA",
   "PEARL",
   "LIT",
   "VVV",
   "LINK",
   "BEAM",
   "SUI",
   "ADA",
   "ZRO"
  ],
  "ETH가 인기 검색에 있음": false
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
   "1일": -5.46,
   "7일": 2.41,
   "30일": 17.93,
   "90일": 32.81
  },
  "종가와 이평선 거리(%)": {
   "MA20": 8.66,
   "MA60": 6.28,
   "MA120": 11.75
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 36
  },
  "RSI14": 55.6
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
 "시가총액 순위": 825,
 "시가총액(USD)": 21178087,
 "완전희석가치 FDV(USD)": 27823052,
 "24시간 거래대금(USD)": 71320568,
 "유통량": 761170523.0,
 "총발행량": 1000000000.0,
 "최대발행량": 1000000000.0,
 "유통 비율(%)": 76.1,
 "역대 최고가(USD)": 0.317341,
 "역대 최고가 대비(%)": -91.23243,
 "가격 변화(%)": {
  "7d": 2.45954,
  "30d": 45.33486,
  "1y": -11.70464
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto's powerhouse super PAC suffers costly setback as Democrats sweep Congress",
   "요약": "The industry's primary campaign arm had cultivated a reputation as an unstoppable force, but more than a third of its spending failed to hit the mark, especially in Ohio.",
   "시각(UTC)": "11-04 20:29"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. Democratic sweep could be the final nail in the ‘Clarity Act’s coffin’",
   "요약": "Industry experts warn the Clarity Act is likely dead in its current form as incoming Democratic majorities eye tighter scrutiny of crypto markets and tokenized stocks.",
   "시각(UTC)": "11-04 16:11"
  },
  {
   "출처": "CoinDesk",
   "제목": "Wall Street rethinks AI data center boom as Texas election raises new risks",
   "요약": "Bitcoin miners pivoting to AI face new uncertainty over power access and construction permits, while companies with approved projects could benefit from tighter supply.",
   "시각(UTC)": "11-04 16:08"
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto Long & Short: ICE is betting on retail’s appetite for quick outcomes",
   "요약": "Retail traders increasingly want trades that resolve fast, from prediction markets to same-day options. Andy Baehr of GSR argues perpetual futures belong in that group, and that ICE’s deal to bring Trade[XYZ]’s Hyperliquid markets onshore i",
   "시각(UTC)": "11-04 15:27"
  },
  {
   "출처": "CoinDesk",
   "제목": "The election changes Washington. The work on crypto continues",
   "요약": "The next Congress inherits an unfinished assignment: establishing clear, lasting rules for digital assets that protect consumers and ensure American innovation continues to thrive, writes Blockchain Association's Lindsay Fraser.",
   "시각(UTC)": "11-04 14:25"
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
   "Binance (Futures)": -0.6883,
   "Ourbit (Futures)": -0.6866,
   "Toobit Futures": -0.6883,
   "Bybit (Futures)": -1.0627,
   "KCEX (Futures)": -0.6866,
   "Gate (Futures)": -0.9051
  },
  "미결제약정 합계 USD(상위)": 22141358
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 33.33,
  "CoinGecko 인기 검색 코인": [
   "PENGU",
   "TRUMP",
   "BTC",
   "NEAR",
   "ZEC",
   "UNI",
   "ENA",
   "PEARL",
   "LIT",
   "VVV",
   "LINK",
   "BEAM",
   "SUI",
   "ADA",
   "ZRO"
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
   "7일": 2.46,
   "30일": 1.22,
   "90일": 10.89
  },
  "종가와 이평선 거리(%)": {
   "MA20": 2.46,
   "MA60": 3.12,
   "MA120": 9.14
  },
  "MA20>MA60": true,
  "최근 교차": null,
  "RSI14": 53.8
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
 "시가총액(USD)": 2118552664,
 "완전희석가치 FDV(USD)": 2118552664,
 "24시간 거래대금(USD)": 559922657,
 "유통량": 420690000000000.0,
 "총발행량": 420690000000000.0,
 "최대발행량": 420690000000000.0,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 2.803e-05,
 "역대 최고가 대비(%)": -82.03273,
 "가격 변화(%)": {
  "7d": 1.72496,
  "30d": 17.22973,
  "1y": -11.4427
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto's powerhouse super PAC suffers costly setback as Democrats sweep Congress",
   "요약": "The industry's primary campaign arm had cultivated a reputation as an unstoppable force, but more than a third of its spending failed to hit the mark, especially in Ohio.",
   "시각(UTC)": "11-04 20:29"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. Democratic sweep could be the final nail in the ‘Clarity Act’s coffin’",
   "요약": "Industry experts warn the Clarity Act is likely dead in its current form as incoming Democratic majorities eye tighter scrutiny of crypto markets and tokenized stocks.",
   "시각(UTC)": "11-04 16:11"
  },
  {
   "출처": "CoinDesk",
   "제목": "Wall Street rethinks AI data center boom as Texas election raises new risks",
   "요약": "Bitcoin miners pivoting to AI face new uncertainty over power access and construction permits, while companies with approved projects could benefit from tighter supply.",
   "시각(UTC)": "11-04 16:08"
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto Long & Short: ICE is betting on retail’s appetite for quick outcomes",
   "요약": "Retail traders increasingly want trades that resolve fast, from prediction markets to same-day options. Andy Baehr of GSR argues perpetual futures belong in that group, and that ICE’s deal to bring Trade[XYZ]’s Hyperliquid markets onshore i",
   "시각(UTC)": "11-04 15:27"
  },
  {
   "출처": "CoinDesk",
   "제목": "The election changes Washington. The work on crypto continues",
   "요약": "The next Congress inherits an unfinished assignment: establishing clear, lasting rules for digital assets that protect consumers and ensure American innovation continues to thrive, writes Blockchain Association's Lindsay Fraser.",
   "시각(UTC)": "11-04 14:25"
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
   "Gate (Futures)": 0.004,
   "OKX (Futures)": 0.01,
   "Bitget Futures": 0.01,
   "KCEX (Futures)": 0.01,
   "WhiteBIT Futures": 0.01
  },
  "미결제약정 합계 USD(상위)": 288405556
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 86.21,
  "CoinGecko 인기 검색 코인": [
   "PENGU",
   "TRUMP",
   "BTC",
   "NEAR",
   "ZEC",
   "UNI",
   "ENA",
   "PEARL",
   "LIT",
   "VVV",
   "LINK",
   "BEAM",
   "SUI",
   "ADA",
   "ZRO"
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
   "1일": -1.33,
   "7일": -5.97,
   "30일": -11.83,
   "90일": -39.64
  },
  "종가와 이평선 거리(%)": {
   "MA20": -6.34,
   "MA60": -22.77,
   "MA120": -30.03
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 34
  },
  "RSI14": 28.9
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
 "시가총액 순위": 360,
 "시가총액(USD)": 68331592,
 "완전희석가치 FDV(USD)": 68331592,
 "24시간 거래대금(USD)": 17310609,
 "유통량": 1195659.98008406,
 "총발행량": 1195659.98008406,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 130.12,
 "역대 최고가 대비(%)": -56.08,
 "가격 변화(%)": {
  "7d": -37.71882,
  "30d": -50.78381,
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto's powerhouse super PAC suffers costly setback as Democrats sweep Congress",
   "요약": "The industry's primary campaign arm had cultivated a reputation as an unstoppable force, but more than a third of its spending failed to hit the mark, especially in Ohio.",
   "시각(UTC)": "11-04 20:29"
  },
  {
   "출처": "CoinDesk",
   "제목": "U.S. Democratic sweep could be the final nail in the ‘Clarity Act’s coffin’",
   "요약": "Industry experts warn the Clarity Act is likely dead in its current form as incoming Democratic majorities eye tighter scrutiny of crypto markets and tokenized stocks.",
   "시각(UTC)": "11-04 16:11"
  },
  {
   "출처": "CoinDesk",
   "제목": "Wall Street rethinks AI data center boom as Texas election raises new risks",
   "요약": "Bitcoin miners pivoting to AI face new uncertainty over power access and construction permits, while companies with approved projects could benefit from tighter supply.",
   "시각(UTC)": "11-04 16:08"
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto Long & Short: ICE is betting on retail’s appetite for quick outcomes",
   "요약": "Retail traders increasingly want trades that resolve fast, from prediction markets to same-day options. Andy Baehr of GSR argues perpetual futures belong in that group, and that ICE’s deal to bring Trade[XYZ]’s Hyperliquid markets onshore i",
   "시각(UTC)": "11-04 15:27"
  },
  {
   "출처": "CoinDesk",
   "제목": "The election changes Washington. The work on crypto continues",
   "요약": "The next Congress inherits an unfinished assignment: establishing clear, lasting rules for digital assets that protect consumers and ensure American innovation continues to thrive, writes Blockchain Association's Lindsay Fraser.",
   "시각(UTC)": "11-04 14:25"
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
   "TRUMP",
   "BTC",
   "NEAR",
   "ZEC",
   "UNI",
   "ENA",
   "PEARL",
   "LIT",
   "VVV",
   "LINK",
   "BEAM",
   "SUI",
   "ADA",
   "ZRO"
  ],
  "INTCB가 인기 검색에 있음": false
 }
}
```
