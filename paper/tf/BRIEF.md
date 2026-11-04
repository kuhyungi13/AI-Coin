# TF팀 회의 자료 (2026-11-05 00:29 KST)

GitHub Actions가 무료 공개 API로 모은 자료입니다. 회의 진행 방법은 `aicoin/tf_team/PLAYBOOK.md`.
자료에 없는 숫자는 쓰지 않습니다. 실패한 자료는 아래 '수집 실패'에 있습니다.

분석 대상: BTC, ETH, BMT, PEPE, GOOGLB

**지금까지 승률** ACE 85.7% (6/7), 채점 대기 15개 · 자세히는 `paper/tf/SCOREBOARD.md`, 교훈은 `aicoin/tf_team/LESSONS.md`

**TRAINER 모의 계좌** 총자산 10,022.15 USDT (+0.22%), 보유 PEPE · 자세히는 `paper/tf/trainer/TRAINER.md`

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
   "1일": 0.43,
   "7일": 2.14,
   "30일": 1.42,
   "90일": -3.71
  },
  "종가와 이평선 거리(%)": {
   "MA20": 1.07,
   "MA60": -0.51,
   "MA120": -2.38
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 64
  },
  "RSI14": 55.7
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
 "시가총액(USD)": 1616697627529,
 "완전희석가치 FDV(USD)": 1616697627529,
 "24시간 거래대금(USD)": 34778811754,
 "유통량": 20105365.0,
 "총발행량": 20105365.0,
 "최대발행량": 21000000.0,
 "유통 비율(%)": 95.7,
 "역대 최고가(USD)": 126080,
 "역대 최고가 대비(%)": -36.21227,
 "가격 변화(%)": {
  "7d": -0.1021,
  "30d": -6.08314,
  "1y": -23.05229
 },
 "소개": "Bitcoin is the world's first decentralized cryptocurrency, created in 2009 by the pseudonymous Satoshi Nakamoto. It enables peer-to-peer electronic cash transactions without intermediaries like banks or governments, operating on a blockchain secured by Proof of Work mining and the SHA-256 cryptographic algorithm. \n\nWith a fixed supply cap of 21 million coins and programmatic halvings every four ye",
 "체인 TVL (DefiLlama)": {
  "체인": "Bitcoin",
  "TVL(USD)": 4165234855
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "BTC 관련 기사": [
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
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin price defends $76K lows as analysts see stocks pricing in ‘political gridlock’",
   "요약": "Bitcoin made modest gains at the start of Wall Street trading on Tuesday as markets awaited cues from the US midterm elections.",
   "시각(UTC)": "11-03 15:44"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Moscow Exchange to launch Bitcoin, Ether and USDT trading in December",
   "요약": "Moscow Exchange plans to launch crypto trading on Dec. 1 under Russia’s new law, with annual purchase limits for non-qualified investors.",
   "시각(UTC)": "11-03 13:15"
  }
 ],
 "시장 전반 기사": [
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Morgan Stanley says it is among the first banks to tokenize real world assets",
   "요약": "The bank's announcement follows the launch of the Depository Trust & Clearing Corporation’s Tokenization Service, or DTS, on Oct. 28.",
   "시각(UTC)": "11-04 09:22"
  },
  {
   "출처": "CoinDesk",
   "제목": "Zcash grants committee drops plan to redirect 98,000 ZEC to future mining rewards",
   "요약": "The committee withdrew its proposal after community backlash, leaving competing plans to cut off its funding or preserve the existing grants system.",
   "시각(UTC)": "11-04 08:04"
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
   "Gate (Futures)": 0.0076,
   "MEXC (Futures)": 0.01,
   "Tapbit (Futures)": 0.01,
   "WEEX (Futures)": 0.0001
  },
  "미결제약정 합계 USD(상위)": 30286818693
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 70.51,
  "CoinGecko 인기 검색 코인": [
   "PEARL",
   "DACITYCOIN",
   "NEAR",
   "ETH",
   "BTC",
   "SOL",
   "LIT",
   "XMR",
   "PENGU",
   "TRUMP",
   "MON",
   "ZEC",
   "HYPE",
   "PUMP",
   "UNI"
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
   "1일": 1.06,
   "7일": 3.07,
   "30일": 4.08,
   "90일": -2.38
  },
  "종가와 이평선 거리(%)": {
   "MA20": 2.27,
   "MA60": 1.43,
   "MA120": -1.1
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 65
  },
  "RSI14": 61.1
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
 "시가총액(USD)": 297546505847,
 "완전희석가치 FDV(USD)": 297546505847,
 "24시간 거래대금(USD)": 14341837107,
 "유통량": 122189135.08807562,
 "총발행량": 122189135.08807562,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 4946.05,
 "역대 최고가 대비(%)": -50.78658,
 "가격 변화(%)": {
  "7d": 4.45695,
  "30d": -9.98171,
  "1y": -31.6241
 },
 "소개": "Ethereum is a global, open-source platform for decentralized applications. In other words, it is a decentralized blockchain platform that enables developers to build and deploy smart contracts and applications without central authority control. Unlike Bitcoin, which primarily functions as digital currency, Ethereum operates as a programmable global computer where developers can create any type of ",
 "체인 TVL (DefiLlama)": {
  "체인": "Ethereum",
  "TVL(USD)": 44473822008
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin rebounds from midterm dip as DeFi leads gains",
   "요약": "Bitcoin recovered from a dip to around $75,600 as Democrats won Congress, while DeFi tokens led gains and Trump-linked coins fell.",
   "시각(UTC)": "11-04 10:38"
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
   "WEEX (Futures)": 0.0001,
   "Hyperliquid (Futures)": 0.0013,
   "MEXC (Futures)": 0.01,
   "Toobit Futures": 0.01
  },
  "미결제약정 합계 USD(상위)": 19157063645
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 87.88,
  "CoinGecko 인기 검색 코인": [
   "PEARL",
   "DACITYCOIN",
   "NEAR",
   "ETH",
   "BTC",
   "SOL",
   "LIT",
   "XMR",
   "PENGU",
   "TRUMP",
   "MON",
   "ZEC",
   "HYPE",
   "PUMP",
   "UNI"
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
   "1일": 0.76,
   "7일": 26.1,
   "30일": 29.19,
   "90일": 65.57
  },
  "종가와 이평선 거리(%)": {
   "MA20": 28.23,
   "MA60": 18.54,
   "MA120": 27.86
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 32
  },
  "RSI14": 76.0
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
 "시가총액 순위": 822,
 "시가총액(USD)": 21219560,
 "완전희석가치 FDV(USD)": 27877538,
 "24시간 거래대금(USD)": 96290371,
 "유통량": 761170523.0,
 "총발행량": 1000000000.0,
 "최대발행량": 1000000000.0,
 "유통 비율(%)": 76.1,
 "역대 최고가(USD)": 0.317341,
 "역대 최고가 대비(%)": -91.21526,
 "가격 변화(%)": {
  "7d": -11.05566,
  "30d": 44.69869,
  "1y": -14.26027
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Here's how analysts are reacting to the new blue Congress",
   "요약": "Your day-ahead look for Nov. 4, 2026",
   "시각(UTC)": "11-04 12:14"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin rebounds from midterm dip as DeFi leads gains",
   "요약": "Bitcoin recovered from a dip to around $75,600 as Democrats won Congress, while DeFi tokens led gains and Trump-linked coins fell.",
   "시각(UTC)": "11-04 10:38"
  },
  {
   "출처": "CoinDesk",
   "제목": "ZachXBT names French bank Crédit Mutuel Arkéa as suspected victim of $133 million crypto theft",
   "요약": "Blockchain sleuth ZachXBT says the French bank may have lost more than $133 million from crypto exchange accounts. Crypto.com confirms it has blocked funds linked to the theft.",
   "시각(UTC)": "11-04 10:18"
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
   "Binance (Futures)": -0.7208,
   "Toobit Futures": -0.7208,
   "Bybit (Futures)": -0.639,
   "Ourbit (Futures)": -0.7292,
   "Gate (Futures)": -0.714,
   "KCEX (Futures)": -0.7292
  },
  "미결제약정 합계 USD(상위)": 23093713
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 75.0,
  "CoinGecko 인기 검색 코인": [
   "PEARL",
   "DACITYCOIN",
   "NEAR",
   "ETH",
   "BTC",
   "SOL",
   "LIT",
   "XMR",
   "PENGU",
   "TRUMP",
   "MON",
   "ZEC",
   "HYPE",
   "PUMP",
   "UNI"
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
   "1일": 0.6,
   "7일": 7.25,
   "30일": -4.91,
   "90일": 19.76
  },
  "종가와 이평선 거리(%)": {
   "MA20": 3.75,
   "MA60": 4.94,
   "MA120": 10.74
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 87
  },
  "RSI14": 57.8
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
 "시가총액(USD)": 2206708610,
 "완전희석가치 FDV(USD)": 2206708610,
 "24시간 거래대금(USD)": 510204476,
 "유통량": 420690000000000.0,
 "총발행량": 420690000000000.0,
 "최대발행량": 420690000000000.0,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 2.803e-05,
 "역대 최고가 대비(%)": -81.28508,
 "가격 변화(%)": {
  "7d": 8.37047,
  "30d": 18.52024,
  "1y": -9.36027
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Here's how analysts are reacting to the new blue Congress",
   "요약": "Your day-ahead look for Nov. 4, 2026",
   "시각(UTC)": "11-04 12:14"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin rebounds from midterm dip as DeFi leads gains",
   "요약": "Bitcoin recovered from a dip to around $75,600 as Democrats won Congress, while DeFi tokens led gains and Trump-linked coins fell.",
   "시각(UTC)": "11-04 10:38"
  },
  {
   "출처": "CoinDesk",
   "제목": "ZachXBT names French bank Crédit Mutuel Arkéa as suspected victim of $133 million crypto theft",
   "요약": "Blockchain sleuth ZachXBT says the French bank may have lost more than $133 million from crypto exchange accounts. Crypto.com confirms it has blocked funds linked to the theft.",
   "시각(UTC)": "11-04 10:18"
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
  "미결제약정 합계 USD(상위)": 289689281
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 88.46,
  "CoinGecko 인기 검색 코인": [
   "PEARL",
   "DACITYCOIN",
   "NEAR",
   "ETH",
   "BTC",
   "SOL",
   "LIT",
   "XMR",
   "PENGU",
   "TRUMP",
   "MON",
   "ZEC",
   "HYPE",
   "PUMP",
   "UNI"
  ],
  "PEPE가 인기 검색에 있음": false
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
   "1일": 1.48,
   "7일": 1.04,
   "30일": 0.58,
   "90일": -17.58
  },
  "종가와 이평선 거리(%)": {
   "MA20": 0.46,
   "MA60": -4.4,
   "MA120": -10.43
  },
  "MA20>MA60": false,
  "최근 교차": null,
  "RSI14": 48.6
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
 "시가총액 순위": 228,
 "시가총액(USD)": 134176716,
 "완전희석가치 FDV(USD)": 134176716,
 "24시간 거래대금(USD)": 33925358,
 "유통량": 455159.91563274997,
 "총발행량": 455159.91563274997,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 383.58,
 "역대 최고가 대비(%)": -23.15992,
 "가격 변화(%)": {
  "7d": -8.84293,
  "30d": -14.36287,
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Here's how analysts are reacting to the new blue Congress",
   "요약": "Your day-ahead look for Nov. 4, 2026",
   "시각(UTC)": "11-04 12:14"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin rebounds from midterm dip as DeFi leads gains",
   "요약": "Bitcoin recovered from a dip to around $75,600 as Democrats won Congress, while DeFi tokens led gains and Trump-linked coins fell.",
   "시각(UTC)": "11-04 10:38"
  },
  {
   "출처": "CoinDesk",
   "제목": "ZachXBT names French bank Crédit Mutuel Arkéa as suspected victim of $133 million crypto theft",
   "요약": "Blockchain sleuth ZachXBT says the French bank may have lost more than $133 million from crypto exchange accounts. Crypto.com confirms it has blocked funds linked to the theft.",
   "시각(UTC)": "11-04 10:18"
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
   "DACITYCOIN",
   "NEAR",
   "ETH",
   "BTC",
   "SOL",
   "LIT",
   "XMR",
   "PENGU",
   "TRUMP",
   "MON",
   "ZEC",
   "HYPE",
   "PUMP",
   "UNI"
  ],
  "GOOGLB가 인기 검색에 있음": false
 }
}
```
