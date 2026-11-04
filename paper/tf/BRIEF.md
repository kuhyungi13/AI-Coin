# TF팀 회의 자료 (2026-11-05 01:31 KST)

GitHub Actions가 무료 공개 API로 모은 자료입니다. 회의 진행 방법은 `aicoin/tf_team/PLAYBOOK.md`.
자료에 없는 숫자는 쓰지 않습니다. 실패한 자료는 아래 '수집 실패'에 있습니다.

분석 대상: BTC, ETH, BMT, PEPE, GOOGLB

**지금까지 승률** ACE 85.7% (6/7), 채점 대기 15개 · 자세히는 `paper/tf/SCOREBOARD.md`, 교훈은 `aicoin/tf_team/LESSONS.md`

**TRAINER 모의 계좌** 총자산 10,031.33 USDT (+0.31%), 보유 PEPE · 자세히는 `paper/tf/trainer/TRAINER.md`

**전체 스캔 후보** (`paper/tf/SCAN.md`) 상승 추세: BMT, PEPE · 과매도 반등: GOOGLB

## BTC

**수집 실패**
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-03",
  "종가": 77453.86,
  "등락률(%)": {
   "1일": 0.83,
   "7일": -4.27,
   "30일": -10.49,
   "90일": 19.78
  },
  "이동평균": {
   "MA20": 80407.336,
   "MA60": 81341.329167,
   "MA120": 74648.556833
  },
  "종가와 이평선 거리(%)": {
   "MA20": -3.67,
   "MA60": -4.78,
   "MA120": 3.76
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 4
  },
  "RSI14": 38.1,
  "ATR14(%)": 2.5,
  "거래량(20일 평균 대비 배수)": 0.89,
  "30일 최고가": 86999.11,
  "30일 최저가": 76325.98,
  "최근 10일 종가": [
   80154.09,
   80150.56,
   80909.77,
   81343.5,
   77991.89,
   77368.77,
   77582.02,
   78354.0,
   76816.0,
   77453.86
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-04",
  "등락률(%)": {
   "1일": 2.32,
   "7일": 4.13,
   "30일": 3.44,
   "90일": -2.81
  },
  "종가와 이평선 거리(%)": {
   "MA20": 3.26,
   "MA60": 1.8,
   "MA120": -0.09
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 65
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
 "시가총액(USD)": 1618866070809,
 "완전희석가치 FDV(USD)": 1618866070809,
 "24시간 거래대금(USD)": 37077173758,
 "유통량": 20105365.0,
 "총발행량": 20105365.0,
 "최대발행량": 21000000.0,
 "유통 비율(%)": 95.7,
 "역대 최고가(USD)": 126080,
 "역대 최고가 대비(%)": -36.1394,
 "가격 변화(%)": {
  "7d": 0.08039,
  "30d": -5.55975,
  "1y": -22.10895
 },
 "소개": "Bitcoin is the world's first decentralized cryptocurrency, created in 2009 by the pseudonymous Satoshi Nakamoto. It enables peer-to-peer electronic cash transactions without intermediaries like banks or governments, operating on a blockchain secured by Proof of Work mining and the SHA-256 cryptographic algorithm. \n\nWith a fixed supply cap of 21 million coins and programmatic halvings every four ye",
 "체인 TVL (DefiLlama)": {
  "체인": "Bitcoin",
  "TVL(USD)": 4185211898
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "BTC 관련 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Wall Street rethinks AI data center boom as Texas election raises new risks",
   "요약": "Bitcoin miners pivoting to AI face new uncertainty over power access and construction permits, while companies with approved projects could benefit from tighter supply.",
   "시각(UTC)": "11-04 16:08"
  },
  {
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin and stocks post big gains, reversing overnight plunge following Blue Wave landslide",
   "요약": "The biggest losers, so far, are the AI data center stocks following victories for several candidates who campaigned expressly against the sector.",
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
   "제목": "Bitcoin hits $80.5K as US stocks rally on midterm election results",
   "요약": "Bitcoin climbed toward $80,500 as risk assets rallied on Democrats’ midterm election gains and oil prices fell.",
   "시각(UTC)": "11-04 15:29"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Here’s what happened in crypto today",
   "요약": "Need to know what happened in crypto today? Here is the latest news on daily trends and events impacting Bitcoin price, blockchain, DeFi, Web3 and crypto regulation.",
   "시각(UTC)": "11-04 13:47"
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
  }
 ],
 "시장 전반 기사": [
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Here's how analysts are reacting to the new blue Congress",
   "요약": "Your day-ahead look for Nov. 4, 2026",
   "시각(UTC)": "11-04 12:14"
  },
  {
   "출처": "CoinDesk",
   "제목": "ZachXBT names French bank Crédit Mutuel Arkéa as suspected victim of $133 million crypto theft",
   "요약": "Blockchain sleuth ZachXBT says the French bank may have lost more than $133 million from crypto exchange accounts. Crypto.com confirms it has blocked funds linked to the theft.",
   "시각(UTC)": "11-04 10:18"
  },
  {
   "출처": "CoinDesk",
   "제목": "Elon Musk floats space data centers as Democratic sweep puts pressure on AI trade",
   "요약": "Texas election result raises fears of data centre restrictions, while Musk and Palihapitiya draw attention to the space economy.",
   "시각(UTC)": "11-04 10:03"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "34 (Fear)",
  "최근 7일": [
   34,
   26,
   37,
   34,
   30,
   30,
   51
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.01,
   "Bybit (Futures)": 0.01,
   "Gate (Futures)": 0.01,
   "MEXC (Futures)": 0.01,
   "WEEX (Futures)": 0.0001,
   "Tapbit (Futures)": 0.01
  },
  "미결제약정 합계 USD(상위)": 29908629401
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 72.09,
  "CoinGecko 인기 검색 코인": [
   "PEARL",
   "ETH",
   "NEAR",
   "DACITYCOIN",
   "BTC",
   "PENGU",
   "XMR",
   "TRUMP",
   "QTC",
   "AERO",
   "PUMP",
   "HYPE",
   "PEPE",
   "SUI",
   "ZEC"
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
  "기준일": "2026-11-03",
  "종가": 2274.77,
  "등락률(%)": {
   "1일": 0.95,
   "7일": -3.22,
   "30일": -16.58,
   "90일": 19.17
  },
  "이동평균": {
   "MA20": 2353.372,
   "MA60": 2505.137833,
   "MA120": 2269.377167
  },
  "종가와 이평선 거리(%)": {
   "MA20": -3.34,
   "MA60": -9.2,
   "MA120": 0.24
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 14
  },
  "RSI14": 36.4,
  "ATR14(%)": 3.39,
  "거래량(20일 평균 대비 배수)": 0.61,
  "30일 최고가": 2738.0,
  "30일 최저가": 2174.08,
  "최근 10일 종가": [
   2329.87,
   2324.55,
   2350.36,
   2359.68,
   2253.13,
   2245.54,
   2255.66,
   2275.31,
   2253.29,
   2274.77
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-04",
  "등락률(%)": {
   "1일": 4.21,
   "7일": 7.01,
   "30일": 8.91,
   "90일": -0.62
  },
  "종가와 이평선 거리(%)": {
   "MA20": 6.22,
   "MA60": 5.64,
   "MA120": 3.07
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 66
  },
  "RSI14": 73.3
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
 "시가총액(USD)": 296898769450,
 "완전희석가치 FDV(USD)": 296898769450,
 "24시간 거래대금(USD)": 15653070895,
 "유통량": 122189135.08807562,
 "총발행량": 122189135.08807562,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 4946.05,
 "역대 최고가 대비(%)": -50.88691,
 "가격 변화(%)": {
  "7d": 4.18427,
  "30d": -9.92732,
  "1y": -30.82536
 },
 "소개": "Ethereum is a global, open-source platform for decentralized applications. In other words, it is a decentralized blockchain platform that enables developers to build and deploy smart contracts and applications without central authority control. Unlike Bitcoin, which primarily functions as digital currency, Ethereum operates as a programmable global computer where developers can create any type of ",
 "체인 TVL (DefiLlama)": {
  "체인": "Ethereum",
  "TVL(USD)": 45458476953
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
   "출처": "Cointelegraph",
   "제목": "Moscow Exchange to launch Bitcoin, Ether and USDT trading in December",
   "요약": "Moscow Exchange plans to launch crypto trading on Dec. 1 under Russia’s new law, with annual purchase limits for non-qualified investors.",
   "시각(UTC)": "11-03 13:15"
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
  },
  {
   "출처": "Decrypt",
   "제목": "Bitmine Buys More Ethereum as Tom Lee Calls the Binance Hack Bullish",
   "요약": "The chairman laid out six reasons the market’s “muted” 4% ETH drop after the record Binance theft shows crypto is “increasingly resilient,” as the firm’s stash neared its 5% supply goal.",
   "시각(UTC)": "11-02 16:23"
  }
 ],
 "시장 전반 기사": [
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin and stocks post big gains, reversing overnight plunge following Blue Wave landslide",
   "요약": "The biggest losers, so far, are the AI data center stocks following victories for several candidates who campaigned expressly against the sector.",
   "시각(UTC)": "11-04 14:00"
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Here's how analysts are reacting to the new blue Congress",
   "요약": "Your day-ahead look for Nov. 4, 2026",
   "시각(UTC)": "11-04 12:14"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "34 (Fear)",
  "최근 7일": [
   34,
   26,
   37,
   34,
   30,
   30,
   51
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.01,
   "WEEX (Futures)": 0.0001,
   "Hyperliquid (Futures)": 0.0013,
   "MEXC (Futures)": 0.01,
   "Toobit Futures": 0.01
  },
  "미결제약정 합계 USD(상위)": 19253958304
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 88.89,
  "CoinGecko 인기 검색 코인": [
   "PEARL",
   "ETH",
   "NEAR",
   "DACITYCOIN",
   "BTC",
   "PENGU",
   "XMR",
   "TRUMP",
   "QTC",
   "AERO",
   "PUMP",
   "HYPE",
   "PEPE",
   "SUI",
   "ZEC"
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
  "기준일": "2026-11-03",
  "종가": 0.02652,
  "등락률(%)": {
   "1일": 26.29,
   "7일": -5.59,
   "30일": 38.27,
   "90일": 116.49
  },
  "이동평균": {
   "MA20": 0.023617,
   "MA60": 0.020446,
   "MA120": 0.017859
  },
  "종가와 이평선 거리(%)": {
   "MA20": 12.29,
   "MA60": 29.71,
   "MA120": 48.5
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 10
  },
  "RSI14": 55.7,
  "ATR14(%)": 28.85,
  "거래량(20일 평균 대비 배수)": 1.78,
  "30일 최고가": 0.05144,
  "30일 최저가": 0.01564,
  "최근 10일 종가": [
   0.03245,
   0.02959,
   0.02809,
   0.02879,
   0.02382,
   0.02336,
   0.02267,
   0.02197,
   0.021,
   0.02652
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-04",
  "등락률(%)": {
   "1일": -8.88,
   "7일": 20.04,
   "30일": 16.58,
   "90일": 32.4
  },
  "종가와 이평선 거리(%)": {
   "MA20": 15.59,
   "MA60": 8.17,
   "MA120": 16.1
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 33
  },
  "RSI14": 60.8
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
 "시가총액 순위": 811,
 "시가총액(USD)": 21632296,
 "완전희석가치 FDV(USD)": 28419776,
 "24시간 거래대금(USD)": 97624305,
 "유통량": 761170523.0,
 "총발행량": 1000000000.0,
 "최대발행량": 1000000000.0,
 "유통 비율(%)": 76.1,
 "역대 최고가(USD)": 0.317341,
 "역대 최고가 대비(%)": -91.04466,
 "가격 변화(%)": {
  "7d": -5.99225,
  "30d": 47.72643,
  "1y": -11.4462
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin and stocks post big gains, reversing overnight plunge following Blue Wave landslide",
   "요약": "The biggest losers, so far, are the AI data center stocks following victories for several candidates who campaigned expressly against the sector.",
   "시각(UTC)": "11-04 14:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "Global asset manager Schroders brings emerging market bond fund to Solana",
   "요약": "The global asset manager, which oversees $1.1 trillion in assets, is bringing an actively managed bond strategy onchain through tokenization specialist Centrifuge.",
   "시각(UTC)": "11-04 13:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "THORChain's RUNE jumps 10% as North Korean hackers resume laundering Binance loot",
   "요약": "North Korea’s TraderTraitor is routing Binance hack proceeds through THORChain, swapping ether for bitcoin after an earlier wave of conversions from Tron.",
   "시각(UTC)": "11-04 12:49"
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
  "오늘": "34 (Fear)",
  "최근 7일": [
   34,
   26,
   37,
   34,
   30,
   30,
   51
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": -0.4449,
   "Toobit Futures": -0.4449,
   "Bybit (Futures)": -0.2807,
   "Ourbit (Futures)": -0.4448,
   "Gate (Futures)": -0.3642,
   "KCEX (Futures)": -0.4448
  },
  "미결제약정 합계 USD(상위)": 23789596
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 75.0,
  "CoinGecko 인기 검색 코인": [
   "PEARL",
   "ETH",
   "NEAR",
   "DACITYCOIN",
   "BTC",
   "PENGU",
   "XMR",
   "TRUMP",
   "QTC",
   "AERO",
   "PUMP",
   "HYPE",
   "PEPE",
   "SUI",
   "ZEC"
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
  "기준일": "2026-11-03",
  "종가": 5e-06,
  "등락률(%)": {
   "1일": 1.88,
   "7일": 5.87,
   "30일": 10.43,
   "90일": 69.1
  },
  "이동평균": {
   "MA20": 5e-06,
   "MA60": 4e-06,
   "MA120": 4e-06
  },
  "종가와 이평선 거리(%)": {
   "MA20": 8.1,
   "MA60": 16.8,
   "MA120": 35.37
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 98
  },
  "RSI14": 57.8,
  "ATR14(%)": 10.59,
  "거래량(20일 평균 대비 배수)": 0.73,
  "30일 최고가": 6e-06,
  "30일 최저가": 4e-06,
  "최근 10일 종가": [
   4e-06,
   4e-06,
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
  "기준일": "2026-11-04",
  "등락률(%)": {
   "1일": 2.78,
   "7일": 7.93,
   "30일": 1.77,
   "90일": 14.13
  },
  "종가와 이평선 거리(%)": {
   "MA20": 6.47,
   "MA60": 7.57,
   "MA120": 13.61
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 88
  },
  "RSI14": 62.9
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
 "시가총액(USD)": 2158382788,
 "완전희석가치 FDV(USD)": 2158382788,
 "24시간 거래대금(USD)": 537040631,
 "유통량": 420690000000000.0,
 "총발행량": 420690000000000.0,
 "최대발행량": 420690000000000.0,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 2.803e-05,
 "역대 최고가 대비(%)": -81.67743,
 "가격 변화(%)": {
  "7d": 6.1428,
  "30d": 16.95331,
  "1y": -9.7065
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin and stocks post big gains, reversing overnight plunge following Blue Wave landslide",
   "요약": "The biggest losers, so far, are the AI data center stocks following victories for several candidates who campaigned expressly against the sector.",
   "시각(UTC)": "11-04 14:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "Global asset manager Schroders brings emerging market bond fund to Solana",
   "요약": "The global asset manager, which oversees $1.1 trillion in assets, is bringing an actively managed bond strategy onchain through tokenization specialist Centrifuge.",
   "시각(UTC)": "11-04 13:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "THORChain's RUNE jumps 10% as North Korean hackers resume laundering Binance loot",
   "요약": "North Korea’s TraderTraitor is routing Binance hack proceeds through THORChain, swapping ether for bitcoin after an earlier wave of conversions from Tron.",
   "시각(UTC)": "11-04 12:49"
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
  "오늘": "34 (Fear)",
  "최근 7일": [
   34,
   26,
   37,
   34,
   30,
   30,
   51
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "MEXC (Futures)": 0.01,
   "Gate (Futures)": 0.01,
   "OKX (Futures)": 0.01,
   "Bitget Futures": 0.01,
   "KCEX (Futures)": 0.01,
   "WhiteBIT Futures": 0.01
  },
  "미결제약정 합계 USD(상위)": 288828551
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 89.66,
  "CoinGecko 인기 검색 코인": [
   "PEARL",
   "ETH",
   "NEAR",
   "DACITYCOIN",
   "BTC",
   "PENGU",
   "XMR",
   "TRUMP",
   "QTC",
   "AERO",
   "PUMP",
   "HYPE",
   "PEPE",
   "SUI",
   "ZEC"
  ],
  "PEPE가 인기 검색에 있음": true
 }
}
```

## GOOGLB

**수집 실패**
- VIBE/선물 포지션: ValueError: GOOGLB 무기한 선물 자료 없음
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-03",
  "종가": 279.67,
  "등락률(%)": {
   "1일": -0.31,
   "7일": -13.63,
   "30일": -18.8,
   "90일": -23.41
  },
  "이동평균": {
   "MA20": 315.2195,
   "MA60": 335.033833,
   "MA120": 341.418417
  },
  "종가와 이평선 거리(%)": {
   "MA20": -11.28,
   "MA60": -16.52,
   "MA120": -18.09
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 9
  },
  "RSI14": 19.7,
  "ATR14(%)": 3.4,
  "거래량(20일 평균 대비 배수)": 1.21,
  "30일 최고가": 359.6,
  "30일 최저가": 275.25,
  "최근 10일 종가": [
   321.37,
   318.64,
   323.81,
   293.03,
   281.17,
   281.88,
   283.1,
   283.65,
   280.54,
   279.67
  ],
  "참고": "마감된 캔들만 사용 (일봉은 한국 시간 오전 9시 마감)"
 },
 "4시간봉(요약)": {
  "기준일": "2026-11-04",
  "등락률(%)": {
   "1일": 3.87,
   "7일": 5.02,
   "30일": 3.88,
   "90일": -14.14
  },
  "종가와 이평선 거리(%)": {
   "MA20": 4.15,
   "MA60": -0.55,
   "MA120": -6.82
  },
  "MA20>MA60": false,
  "최근 교차": null,
  "RSI14": 65.9
 }
}
```

### DIANA 자료 · 기본적 분석 (펀더멘털)

```json
{
 "이름": "Alphabet (bStocks Tokenized Stock)",
 "분류": [
  "Tokenized Assets",
  "BNB Chain Ecosystem",
  "Tokenized Stocks",
  "Real World Assets (RWA)",
  "bStocks Ecosystem"
 ],
 "시가총액 순위": 229,
 "시가총액(USD)": 132051686,
 "완전희석가치 FDV(USD)": 132051686,
 "24시간 거래대금(USD)": 36283010,
 "유통량": 455481.00205415004,
 "총발행량": 455481.00205415004,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 383.58,
 "역대 최고가 대비(%)": -24.41859,
 "가격 변화(%)": {
  "7d": -10.61149,
  "30d": -15.99051,
  "1y": null
 },
 "소개": ""
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "GOOGLB 관련 기사": [],
 "시장 전반 기사": [
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin and stocks post big gains, reversing overnight plunge following Blue Wave landslide",
   "요약": "The biggest losers, so far, are the AI data center stocks following victories for several candidates who campaigned expressly against the sector.",
   "시각(UTC)": "11-04 14:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "Global asset manager Schroders brings emerging market bond fund to Solana",
   "요약": "The global asset manager, which oversees $1.1 trillion in assets, is bringing an actively managed bond strategy onchain through tokenization specialist Centrifuge.",
   "시각(UTC)": "11-04 13:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "THORChain's RUNE jumps 10% as North Korean hackers resume laundering Binance loot",
   "요약": "North Korea’s TraderTraitor is routing Binance hack proceeds through THORChain, swapping ether for bitcoin after an earlier wave of conversions from Tron.",
   "시각(UTC)": "11-04 12:49"
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
  "오늘": "34 (Fear)",
  "최근 7일": [
   34,
   26,
   37,
   34,
   30,
   30,
   51
  ]
 },
 "선물 포지션": {
  "오류": "ValueError: GOOGLB 무기한 선물 자료 없음"
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": null,
  "CoinGecko 인기 검색 코인": [
   "PEARL",
   "ETH",
   "NEAR",
   "DACITYCOIN",
   "BTC",
   "PENGU",
   "XMR",
   "TRUMP",
   "QTC",
   "AERO",
   "PUMP",
   "HYPE",
   "PEPE",
   "SUI",
   "ZEC"
  ],
  "GOOGLB가 인기 검색에 있음": false
 }
}
```
