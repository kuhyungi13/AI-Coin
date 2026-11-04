# TF팀 회의 자료 (2026-11-04 13:32 KST)

GitHub Actions가 무료 공개 API로 모은 자료입니다. 회의 진행 방법은 `aicoin/tf_team/PLAYBOOK.md`.
자료에 없는 숫자는 쓰지 않습니다. 실패한 자료는 아래 '수집 실패'에 있습니다.

분석 대상: BTC, ETH, BMT, PEPE, GOOGLB

**지금까지 승률** ACE 자료 없음% (0/0), 채점 대기 17개 · 자세히는 `paper/tf/SCOREBOARD.md`, 교훈은 `aicoin/tf_team/LESSONS.md`

**TRAINER 모의 계좌** 총자산 10,002.11 USDT (+0.02%), 보유 PEPE · 자세히는 `paper/tf/trainer/TRAINER.md`

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
   "1일": -1.24,
   "7일": -0.42,
   "30일": -2.22,
   "90일": -6.87
  },
  "종가와 이평선 거리(%)": {
   "MA20": -1.4,
   "MA60": -3.12,
   "MA120": -4.9
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 62
  },
  "RSI14": 35.9
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
 "시가총액(USD)": 1541127253001,
 "완전희석가치 FDV(USD)": 1541127253001,
 "24시간 거래대금(USD)": 27457720999,
 "유통량": 20105365.0,
 "총발행량": 20105365.0,
 "최대발행량": 21000000.0,
 "유통 비율(%)": 95.7,
 "역대 최고가(USD)": 126080,
 "역대 최고가 대비(%)": -39.2032,
 "가격 변화(%)": {
  "7d": -5.40208,
  "30d": -10.9594,
  "1y": -28.47604
 },
 "소개": "Bitcoin is the world's first decentralized cryptocurrency, created in 2009 by the pseudonymous Satoshi Nakamoto. It enables peer-to-peer electronic cash transactions without intermediaries like banks or governments, operating on a blockchain secured by Proof of Work mining and the SHA-256 cryptographic algorithm. \n\nWith a fixed supply cap of 21 million coins and programmatic halvings every four ye",
 "체인 TVL (DefiLlama)": {
  "체인": "Bitcoin",
  "TVL(USD)": 4075713045
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "BTC 관련 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin is breaking a midterm election pattern going back to 2014",
   "요약": "Your day-ahead look for Nov. 3, 2026",
   "시각(UTC)": "11-03 12:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin steadies after dip to $76,300 as ETF outflows and midterm elections weigh on crypto",
   "요약": "Bitcoin edged up 0.2% to around $76,900 since midnight UTC as spot ETFs lost $399 million for a second day and Binance customers pulled a net $4.72 billion.",
   "시각(UTC)": "11-03 11:28"
  },
  {
   "출처": "CoinDesk",
   "제목": "Liquid’s bitcoin IOUs are fully backed again after a $320 million exploit",
   "요약": "A final 250 BTC transfer closed the hole left by September’s bug, but the federation behind the network still hasn’t said who paid to fill it.",
   "시각(UTC)": "11-03 11:12"
  },
  {
   "출처": "CoinDesk",
   "제목": "Tether holds 150,000 bitcoin worth $11.5 billion, CEO Paolo Ardoino says",
   "요약": "Ardoino didn’t say where the extra coins sit. Holdings outside USDT reserves, such as Tether’s investments, wouldn’t appear in the report.",
   "시각(UTC)": "11-03 10:15"
  },
  {
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin and tech stocks edge higher as U.S. voters head to the polls",
   "요약": "Bitcoin is currently on pace for a fifth straight weekly decline, which would tie for its third-longest losing streak ever.",
   "시각(UTC)": "11-03 09:50"
  },
  {
   "출처": "CoinDesk",
   "제목": "Mercado Bitcoin pledges to cover all user losses after near $40 million hack",
   "요약": "Partners like Tether, Circle, and Chainalysis helped freeze $11M of the stolen assets.",
   "시각(UTC)": "11-03 08:56"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin’s latest chart signal looks a lot like the ones before its big crashes",
   "요약": "The Guppy Multiple Moving Average bands signal a bearish momentum, even as seasonality and post-midterm history lean bullish.",
   "시각(UTC)": "11-03 08:50"
  },
  {
   "출처": "CoinDesk",
   "제목": "Binance has spent half its SAFU bitcoin, about $580 million worth, data shows",
   "요약": "The user protection fund now sits below the $800 million level that Binance’s own rules say triggers a top-up, and the exchange hasn’t said when it will refill it.",
   "시각(UTC)": "11-03 05:36"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin miner Cipher posts $31 million profit as AI pivot begins",
   "요약": "The company's revenue dropped 63% in the third quarter, while a $127 million accounting gain helped turn an operating loss into a reported profit.",
   "시각(UTC)": "11-03 05:29"
  },
  {
   "출처": "Cointelegraph",
   "제목": "RUNE rallies 15% as THORChain restarts most swaps after halt",
   "요약": "THORChain has restored trading on Bitcoin, Ethereum and several other networks following a refund bug, while three chains remain paused.",
   "시각(UTC)": "11-03 23:56"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Here’s what happened in crypto today",
   "요약": "Need to know what happened in crypto today? Here is the latest news on daily trends and events impacting Bitcoin price, blockchain, DeFi, Web3 and crypto regulation.",
   "시각(UTC)": "11-03 22:39"
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
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin price threatens $77.7K support loss with recent buyers underwater",
   "요약": "Bitcoin fell below the realized price of the one-to-three-month-old buyer cohort in a move that risked flipping it to new resistance.",
   "시각(UTC)": "11-03 10:04"
  }
 ],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Live updates: Crypto's big election gamble faces voters as Democrats gain ground",
   "요약": "Voters are choosing who will represent them in the House, Senate and state-wide seats.",
   "시각(UTC)": "11-04 00:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "What voters said about their views on crypto",
   "요약": "A CoinDesk-commissioned poll from April sheds light on how voters — who aren't necessarily part of the crypto sector — view this industry.",
   "시각(UTC)": "11-03 23:19"
  },
  {
   "출처": "CoinDesk",
   "제목": "What happens if North Korea steals Wall Street's tokenized assets next",
   "요약": "The $6.3 billion Binance hack showed how quickly cryptocurrencies can disappear on blockchain rails. Tokenized securities may offer better recourse than crypto after a theft, but the markets around them can still break down when stress hits",
   "시각(UTC)": "11-03 23:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "CFTC gets into legal clash over stock perps after having cleared path for crypto version",
   "요약": "A group backed by Citadel Securities and other firms sued the U.S. derivatives regulator for opening a path for perps that it argued belong in the SEC's hands.",
   "시각(UTC)": "11-03 22:14"
  },
  {
   "출처": "CoinDesk",
   "제목": "Justin Sun seeks sanctions against Trump-linked World Liberty Financial over UAE ties",
   "요약": "The Tron founder says World Liberty failed to disclose its UAE ties until months into his lawsuit over $45 million in WLFI tokens.",
   "시각(UTC)": "11-03 16:55"
  },
  {
   "출처": "CoinDesk",
   "제목": "South Korea's president says country needs a ‘cybersecurity czar’ following $6.3 billion Binance hack",
   "요약": "Lee Jae Myung said he wants a government-wide agency to tackle cyberattacks as AI raises security concerns across financial institutions and critical infrastructure.",
   "시각(UTC)": "11-03 16:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Amazon, Tesla and SpaceX join OKX–ICE tokenized stock objections as deadline looms",
   "요약": "Objections have reached 56 companies, with nearly 80% of the venture’s initial stock selection opting out.",
   "시각(UTC)": "11-03 16:17"
  },
  {
   "출처": "CoinDesk",
   "제목": "Stablecoin governance group behind OUSD sets out management fee, offers equity earning pool",
   "요약": "Governance group Open Standard will charge a 0.1 basis point management fee on payment volume, capped at at $0.01 per payment.",
   "시각(UTC)": "11-03 16:12"
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
   "Bybit (Futures)": 0.0072,
   "Gate (Futures)": 0.01,
   "MEXC (Futures)": 0.01,
   "Tapbit (Futures)": 0.01,
   "WEEX (Futures)": 0.0001
  },
  "미결제약정 합계 USD(상위)": 29557970771
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 62.5,
  "CoinGecko 인기 검색 코인": [
   "DACITYCOIN",
   "HYPE",
   "BTC",
   "ZEC",
   "XMR",
   "AKE",
   "PENGU",
   "RUNE",
   "NEAR",
   "QTC",
   "SHIB",
   "PEPE",
   "CRV",
   "AZTEC",
   "XEC"
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
   "1일": -1.12,
   "7일": -0.18,
   "30일": 0.51,
   "90일": -6.86
  },
  "종가와 이평선 거리(%)": {
   "MA20": -0.95,
   "MA60": -2.04,
   "MA120": -4.48
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 63
  },
  "RSI14": 42.7
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
 "시가총액(USD)": 275977401271,
 "완전희석가치 FDV(USD)": 275977401271,
 "24시간 거래대금(USD)": 9242941119,
 "유통량": 122189135.08807562,
 "총발행량": 122189135.08807562,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 4946.05,
 "역대 최고가 대비(%)": -54.33507,
 "가격 변화(%)": {
  "7d": -4.20092,
  "30d": -16.8451,
  "1y": -37.99567
 },
 "소개": "Ethereum is a global, open-source platform for decentralized applications. In other words, it is a decentralized blockchain platform that enables developers to build and deploy smart contracts and applications without central authority control. Unlike Bitcoin, which primarily functions as digital currency, Ethereum operates as a programmable global computer where developers can create any type of ",
 "체인 TVL (DefiLlama)": {
  "체인": "Ethereum",
  "TVL(USD)": 43446816808
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "ETH 관련 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Binance's $6.3 billion hack began with a fake job interview, and a campaign 'built over many months'",
   "요약": "North Korea-linked attackers spent months compromising Binance employees and internal systems before exploiting its hot-wallet signing infrastructure through Ethereum's EIP-7702 mechanism.",
   "시각(UTC)": "11-03 14:53"
  },
  {
   "출처": "CoinDesk",
   "제목": "ETHGas wants to bring Wall Street to public Ethereum with institutional controls",
   "요약": "The proposed service would offer sanctions screening and qualified validators, but current compensation for failed commitments is set at zero.",
   "시각(UTC)": "11-03 12:01"
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
   "제목": "Live updates: Crypto's big election gamble faces voters as Democrats gain ground",
   "요약": "Voters are choosing who will represent them in the House, Senate and state-wide seats.",
   "시각(UTC)": "11-04 00:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "What voters said about their views on crypto",
   "요약": "A CoinDesk-commissioned poll from April sheds light on how voters — who aren't necessarily part of the crypto sector — view this industry.",
   "시각(UTC)": "11-03 23:19"
  },
  {
   "출처": "CoinDesk",
   "제목": "What happens if North Korea steals Wall Street's tokenized assets next",
   "요약": "The $6.3 billion Binance hack showed how quickly cryptocurrencies can disappear on blockchain rails. Tokenized securities may offer better recourse than crypto after a theft, but the markets around them can still break down when stress hits",
   "시각(UTC)": "11-03 23:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "CFTC gets into legal clash over stock perps after having cleared path for crypto version",
   "요약": "A group backed by Citadel Securities and other firms sued the U.S. derivatives regulator for opening a path for perps that it argued belong in the SEC's hands.",
   "시각(UTC)": "11-03 22:14"
  },
  {
   "출처": "CoinDesk",
   "제목": "Justin Sun seeks sanctions against Trump-linked World Liberty Financial over UAE ties",
   "요약": "The Tron founder says World Liberty failed to disclose its UAE ties until months into his lawsuit over $45 million in WLFI tokens.",
   "시각(UTC)": "11-03 16:55"
  },
  {
   "출처": "CoinDesk",
   "제목": "South Korea's president says country needs a ‘cybersecurity czar’ following $6.3 billion Binance hack",
   "요약": "Lee Jae Myung said he wants a government-wide agency to tackle cyberattacks as AI raises security concerns across financial institutions and critical infrastructure.",
   "시각(UTC)": "11-03 16:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Amazon, Tesla and SpaceX join OKX–ICE tokenized stock objections as deadline looms",
   "요약": "Objections have reached 56 companies, with nearly 80% of the venture’s initial stock selection opting out.",
   "시각(UTC)": "11-03 16:17"
  },
  {
   "출처": "CoinDesk",
   "제목": "Stablecoin governance group behind OUSD sets out management fee, offers equity earning pool",
   "요약": "Governance group Open Standard will charge a 0.1 basis point management fee on payment volume, capped at at $0.01 per payment.",
   "시각(UTC)": "11-03 16:12"
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
   "Binance (Futures)": 0.0077,
   "WEEX (Futures)": 0.0001,
   "MEXC (Futures)": 0.0028,
   "Hyperliquid (Futures)": 0.0013,
   "CoinW (Futures)": 0.0027
  },
  "미결제약정 합계 USD(상위)": 18302191695
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 92.31,
  "CoinGecko 인기 검색 코인": [
   "DACITYCOIN",
   "HYPE",
   "BTC",
   "ZEC",
   "XMR",
   "AKE",
   "PENGU",
   "RUNE",
   "NEAR",
   "QTC",
   "SHIB",
   "PEPE",
   "CRV",
   "AZTEC",
   "XEC"
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
   "1일": 12.63,
   "7일": 42.24,
   "30일": 24.04,
   "90일": 71.77
  },
  "종가와 이평선 거리(%)": {
   "MA20": 29.12,
   "MA60": 15.53,
   "MA120": 25.86
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 30
  },
  "RSI14": 74.4
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
 "시가총액 순위": 776,
 "시가총액(USD)": 22318565,
 "완전희석가치 FDV(USD)": 29346189,
 "24시간 거래대금(USD)": 118479487,
 "유통량": 760526861.0,
 "총발행량": 1000000000.0,
 "최대발행량": 1000000000.0,
 "유통 비율(%)": 76.1,
 "역대 최고가(USD)": 0.317341,
 "역대 최고가 대비(%)": -90.75246,
 "가격 변화(%)": {
  "7d": 5.54722,
  "30d": 51.1342,
  "1y": -11.48971
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
   "제목": "Live updates: Crypto's big election gamble faces voters as Democrats gain ground",
   "요약": "Voters are choosing who will represent them in the House, Senate and state-wide seats.",
   "시각(UTC)": "11-04 00:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "What voters said about their views on crypto",
   "요약": "A CoinDesk-commissioned poll from April sheds light on how voters — who aren't necessarily part of the crypto sector — view this industry.",
   "시각(UTC)": "11-03 23:19"
  },
  {
   "출처": "CoinDesk",
   "제목": "What happens if North Korea steals Wall Street's tokenized assets next",
   "요약": "The $6.3 billion Binance hack showed how quickly cryptocurrencies can disappear on blockchain rails. Tokenized securities may offer better recourse than crypto after a theft, but the markets around them can still break down when stress hits",
   "시각(UTC)": "11-03 23:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "CFTC gets into legal clash over stock perps after having cleared path for crypto version",
   "요약": "A group backed by Citadel Securities and other firms sued the U.S. derivatives regulator for opening a path for perps that it argued belong in the SEC's hands.",
   "시각(UTC)": "11-03 22:14"
  },
  {
   "출처": "CoinDesk",
   "제목": "Justin Sun seeks sanctions against Trump-linked World Liberty Financial over UAE ties",
   "요약": "The Tron founder says World Liberty failed to disclose its UAE ties until months into his lawsuit over $45 million in WLFI tokens.",
   "시각(UTC)": "11-03 16:55"
  },
  {
   "출처": "CoinDesk",
   "제목": "South Korea's president says country needs a ‘cybersecurity czar’ following $6.3 billion Binance hack",
   "요약": "Lee Jae Myung said he wants a government-wide agency to tackle cyberattacks as AI raises security concerns across financial institutions and critical infrastructure.",
   "시각(UTC)": "11-03 16:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Amazon, Tesla and SpaceX join OKX–ICE tokenized stock objections as deadline looms",
   "요약": "Objections have reached 56 companies, with nearly 80% of the venture’s initial stock selection opting out.",
   "시각(UTC)": "11-03 16:17"
  },
  {
   "출처": "CoinDesk",
   "제목": "Stablecoin governance group behind OUSD sets out management fee, offers equity earning pool",
   "요약": "Governance group Open Standard will charge a 0.1 basis point management fee on payment volume, capped at at $0.01 per payment.",
   "시각(UTC)": "11-03 16:12"
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
   "Binance (Futures)": -1.2335,
   "Toobit Futures": -1.2335,
   "Ourbit (Futures)": -1.2372,
   "Bybit (Futures)": -1.2004,
   "Gate (Futures)": -1.1551,
   "Variational Omni": -1.436
  },
  "미결제약정 합계 USD(상위)": 25657920
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 60.0,
  "CoinGecko 인기 검색 코인": [
   "DACITYCOIN",
   "HYPE",
   "BTC",
   "ZEC",
   "XMR",
   "AKE",
   "PENGU",
   "RUNE",
   "NEAR",
   "QTC",
   "SHIB",
   "PEPE",
   "CRV",
   "AZTEC",
   "XEC"
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
   "1일": -1.03,
   "7일": 0.84,
   "30일": -2.03,
   "90일": 14.22
  },
  "종가와 이평선 거리(%)": {
   "MA20": -0.6,
   "MA60": 0.97,
   "MA120": 6.54
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 85
  },
  "RSI14": 48.6
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
 "시가총액(USD)": 2040604228,
 "완전희석가치 FDV(USD)": 2040604228,
 "24시간 거래대금(USD)": 387222978,
 "유통량": 420690000000000.0,
 "총발행량": 420690000000000.0,
 "최대발행량": 420690000000000.0,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 2.803e-05,
 "역대 최고가 대비(%)": -82.6938,
 "가격 변화(%)": {
  "7d": -1.31819,
  "30d": 9.58592,
  "1y": -16.85484
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
   "제목": "Live updates: Crypto's big election gamble faces voters as Democrats gain ground",
   "요약": "Voters are choosing who will represent them in the House, Senate and state-wide seats.",
   "시각(UTC)": "11-04 00:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "What voters said about their views on crypto",
   "요약": "A CoinDesk-commissioned poll from April sheds light on how voters — who aren't necessarily part of the crypto sector — view this industry.",
   "시각(UTC)": "11-03 23:19"
  },
  {
   "출처": "CoinDesk",
   "제목": "What happens if North Korea steals Wall Street's tokenized assets next",
   "요약": "The $6.3 billion Binance hack showed how quickly cryptocurrencies can disappear on blockchain rails. Tokenized securities may offer better recourse than crypto after a theft, but the markets around them can still break down when stress hits",
   "시각(UTC)": "11-03 23:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "CFTC gets into legal clash over stock perps after having cleared path for crypto version",
   "요약": "A group backed by Citadel Securities and other firms sued the U.S. derivatives regulator for opening a path for perps that it argued belong in the SEC's hands.",
   "시각(UTC)": "11-03 22:14"
  },
  {
   "출처": "CoinDesk",
   "제목": "Justin Sun seeks sanctions against Trump-linked World Liberty Financial over UAE ties",
   "요약": "The Tron founder says World Liberty failed to disclose its UAE ties until months into his lawsuit over $45 million in WLFI tokens.",
   "시각(UTC)": "11-03 16:55"
  },
  {
   "출처": "CoinDesk",
   "제목": "South Korea's president says country needs a ‘cybersecurity czar’ following $6.3 billion Binance hack",
   "요약": "Lee Jae Myung said he wants a government-wide agency to tackle cyberattacks as AI raises security concerns across financial institutions and critical infrastructure.",
   "시각(UTC)": "11-03 16:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Amazon, Tesla and SpaceX join OKX–ICE tokenized stock objections as deadline looms",
   "요약": "Objections have reached 56 companies, with nearly 80% of the venture’s initial stock selection opting out.",
   "시각(UTC)": "11-03 16:17"
  },
  {
   "출처": "CoinDesk",
   "제목": "Stablecoin governance group behind OUSD sets out management fee, offers equity earning pool",
   "요약": "Governance group Open Standard will charge a 0.1 basis point management fee on payment volume, capped at at $0.01 per payment.",
   "시각(UTC)": "11-03 16:12"
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
   "WhiteBIT Futures": 0.01,
   "KCEX (Futures)": 0.01
  },
  "미결제약정 합계 USD(상위)": 262119496
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 86.96,
  "CoinGecko 인기 검색 코인": [
   "DACITYCOIN",
   "HYPE",
   "BTC",
   "ZEC",
   "XMR",
   "AKE",
   "PENGU",
   "RUNE",
   "NEAR",
   "QTC",
   "SHIB",
   "PEPE",
   "CRV",
   "AZTEC",
   "XEC"
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
   "1일": -1.74,
   "7일": -2.04,
   "30일": -2.65,
   "90일": -20.41
  },
  "종가와 이평선 거리(%)": {
   "MA20": -2.49,
   "MA60": -7.54,
   "MA120": -13.26
  },
  "MA20>MA60": false,
  "최근 교차": null,
  "RSI14": 23.1
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
 "시가총액 순위": 232,
 "시가총액(USD)": 121198826,
 "완전희석가치 FDV(USD)": 121198826,
 "24시간 거래대금(USD)": 20283338,
 "유통량": 442039.40876172,
 "총발행량": 442039.40876172,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 383.58,
 "역대 최고가 대비(%)": -28.52096,
 "가격 변화(%)": {
  "7d": -15.8218,
  "30d": -20.26556,
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
   "제목": "Live updates: Crypto's big election gamble faces voters as Democrats gain ground",
   "요약": "Voters are choosing who will represent them in the House, Senate and state-wide seats.",
   "시각(UTC)": "11-04 00:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "What voters said about their views on crypto",
   "요약": "A CoinDesk-commissioned poll from April sheds light on how voters — who aren't necessarily part of the crypto sector — view this industry.",
   "시각(UTC)": "11-03 23:19"
  },
  {
   "출처": "CoinDesk",
   "제목": "What happens if North Korea steals Wall Street's tokenized assets next",
   "요약": "The $6.3 billion Binance hack showed how quickly cryptocurrencies can disappear on blockchain rails. Tokenized securities may offer better recourse than crypto after a theft, but the markets around them can still break down when stress hits",
   "시각(UTC)": "11-03 23:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "CFTC gets into legal clash over stock perps after having cleared path for crypto version",
   "요약": "A group backed by Citadel Securities and other firms sued the U.S. derivatives regulator for opening a path for perps that it argued belong in the SEC's hands.",
   "시각(UTC)": "11-03 22:14"
  },
  {
   "출처": "CoinDesk",
   "제목": "Justin Sun seeks sanctions against Trump-linked World Liberty Financial over UAE ties",
   "요약": "The Tron founder says World Liberty failed to disclose its UAE ties until months into his lawsuit over $45 million in WLFI tokens.",
   "시각(UTC)": "11-03 16:55"
  },
  {
   "출처": "CoinDesk",
   "제목": "South Korea's president says country needs a ‘cybersecurity czar’ following $6.3 billion Binance hack",
   "요약": "Lee Jae Myung said he wants a government-wide agency to tackle cyberattacks as AI raises security concerns across financial institutions and critical infrastructure.",
   "시각(UTC)": "11-03 16:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Amazon, Tesla and SpaceX join OKX–ICE tokenized stock objections as deadline looms",
   "요약": "Objections have reached 56 companies, with nearly 80% of the venture’s initial stock selection opting out.",
   "시각(UTC)": "11-03 16:17"
  },
  {
   "출처": "CoinDesk",
   "제목": "Stablecoin governance group behind OUSD sets out management fee, offers equity earning pool",
   "요약": "Governance group Open Standard will charge a 0.1 basis point management fee on payment volume, capped at at $0.01 per payment.",
   "시각(UTC)": "11-03 16:12"
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
   "DACITYCOIN",
   "HYPE",
   "BTC",
   "ZEC",
   "XMR",
   "AKE",
   "PENGU",
   "RUNE",
   "NEAR",
   "QTC",
   "SHIB",
   "PEPE",
   "CRV",
   "AZTEC",
   "XEC"
  ],
  "GOOGLB가 인기 검색에 있음": false
 }
}
```
