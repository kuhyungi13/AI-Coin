# TF팀 회의 자료 (2026-11-03 15:20 KST)

GitHub Actions가 무료 공개 API로 모은 자료입니다. 회의 진행 방법은 `aicoin/tf_team/PLAYBOOK.md`.
자료에 없는 숫자는 쓰지 않습니다. 실패한 자료는 아래 '수집 실패'에 있습니다.

분석 대상: BTC, ETH

## BTC

**수집 실패**
- VIBE/커뮤니티 인기글(레딧): HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15

### TARO 자료 · 기술적 분석 (차트)

```json
{
 "일봉": {
  "기준일": "2026-11-03",
  "종가": 76528.64,
  "등락률(%)": {
   "1일": -0.37,
   "7일": -5.41,
   "30일": -11.56,
   "90일": 18.35
  },
  "이동평균": {
   "MA20": 80361.075,
   "MA60": 81325.908833,
   "MA120": 74640.846667
  },
  "종가와 이평선 거리(%)": {
   "MA20": -4.77,
   "MA60": -5.9,
   "MA120": 2.53
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 4
  },
  "RSI14": 34.0,
  "ATR14(%)": 2.46,
  "거래량(20일 평균 대비 배수)": 0.32,
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
   76528.64
  ]
 },
 "4시간봉(요약)": {
  "등락률(%)": {
   "1일": -0.53,
   "7일": -2.68,
   "30일": -4.17,
   "90일": -7.48
  },
  "종가와 이평선 거리(%)": {
   "MA20": -1.4,
   "MA60": -3.4,
   "MA120": -5.08
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 57
  },
  "RSI14": 33.3
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
 "시가총액(USD)": 1536836021174,
 "완전희석가치 FDV(USD)": 1536836021174,
 "24시간 거래대금(USD)": 26890632487,
 "유통량": 20105365.0,
 "총발행량": 20105365.0,
 "최대발행량": 21000000.0,
 "유통 비율(%)": 95.7,
 "역대 최고가(USD)": 126080,
 "역대 최고가 대비(%)": -39.37249,
 "가격 변화(%)": {
  "7d": -4.28924,
  "30d": -9.96539,
  "1y": -28.94112
 },
 "소개": "Bitcoin is the world's first decentralized cryptocurrency, created in 2009 by the pseudonymous Satoshi Nakamoto. It enables peer-to-peer electronic cash transactions without intermediaries like banks or governments, operating on a blockchain secured by Proof of Work mining and the SHA-256 cryptographic algorithm. \n\nWith a fixed supply cap of 21 million coins and programmatic halvings every four ye",
 "체인 TVL (DefiLlama)": {
  "체인": "Bitcoin",
  "TVL(USD)": 4091459448
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "BTC 관련 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Binance has spent half its SAFU bitcoin, about $580 million worth, data shows",
   "요약": "The user protection fund now sits below the $800 million level that Binance’s own rules say triggers a top-up, and the exchange hasn’t said when it will refill it.",
   "시각(UTC)": "11-03 05:36"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin drops below $77,000 as chip rout deepens ahead of U.S. midterm vote",
   "요약": "ZEC tumbled nearly 10% and BNB fell under $700 as the Nasdaq 100 slid into a correction, dragging Asian stocks lower.",
   "시각(UTC)": "11-03 04:48"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin traders eye post-election rally as exchange outflows point to supply squeeze",
   "요약": "Bulls are watching short positions, exchange withdrawals and key price levels for signs of a rebound after the midterms.",
   "시각(UTC)": "11-02 18:13"
  },
  {
   "출처": "CoinDesk",
   "제목": "Brazil’s Mercado Bitcoin halts withdrawals after $40 million drained across 10 chains",
   "요약": "The Brazilian exchange paused deposits and withdrawals after wallets on at least 10 chains were emptied, days after the $6.3 billion Binance hack.",
   "시각(UTC)": "11-02 15:53"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin's 'volatility curve' has a midterm bump",
   "요약": "Your day-ahead look for Nov. 2, 2026",
   "시각(UTC)": "11-02 12:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin eases to $77,900 as Binance customers pull $3.6 billion after withdrawals reopen",
   "요약": "Bitcoin fell 0.4% to around $77,900 since midnight UTC as Binance customers pulled a net $3.64 billion after withdrawals reopened and ETFs lost $643 million.",
   "시각(UTC)": "11-02 11:30"
  },
  {
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin bounce fades as Binance exploit, AI unwind continue to weigh",
   "요약": "The Nasdaq flipped from a 1% gain to a 1% decline on Monday even as interest rates pulled back and oil plunged on hopes for Middle East peace.",
   "시각(UTC)": "11-02 08:49"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin ETFs lost $643 million in outflows Friday, and 2026 is barely green now",
   "요약": "The first trading day after the Binance hack saw  the biggest ETF outflow since June 25.",
   "시각(UTC)": "11-02 06:46"
  },
  {
   "출처": "CoinDesk",
   "제목": "Strangers are begging the Binance hacker for bitcoin, one ‘help me bro’ at a time",
   "요약": "The 19 wallets holding 18,270 stolen BTC have taken in nothing since Thursday except payments worth under a dollar, each carrying a message, from pleas to laundering pitches to a token shill.",
   "시각(UTC)": "11-02 05:18"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Here’s what happened in crypto today",
   "요약": "Need to know what happened in crypto today? Here is the latest news on daily trends and events impacting Bitcoin price, blockchain, DeFi, Web3 and crypto regulation.",
   "시각(UTC)": "11-03 06:00"
  },
  {
   "출처": "Cointelegraph",
   "제목": "AI poses greater threat to Bitcoin than quantum computing, Swan founder says",
   "요약": "The Swan Bitcoin founder warned that hackers are using large language models to exploit security flaws with just a few prompts.",
   "시각(UTC)": "11-02 21:54"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin risks drop below $76K as 7% oil slide fails to spark BTC price rally",
   "요약": "Bitcoin fell around 1.7% on Monday as stocks pared early gains fueled by hopes of a diplomatic resolution to the US-Iran war.",
   "시각(UTC)": "11-02 19:27"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Mercado Bitcoin wallets show post-hack transfers after $46M theft",
   "요약": "Brazil’s exchange Mercado Bitcoin paused deposits and withdrawals after a security breach, saying customer funds and data were safe.",
   "시각(UTC)": "11-02 19:05"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Strategy spends triple its weekly Bitcoin outlay on STRC buybacks",
   "요약": "Strategy spent $208.2 million buying back STRC preferred shares and $65.5 million on Bitcoin, while allocating $98.5 million to its USD Cash balance.",
   "시각(UTC)": "11-02 13:48"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Binance taps half its SAFU Bitcoin holdings, releases reserve proof",
   "요약": "Binance’s SAFU Bitcoin wallet now holds about 7,500 BTC after a 7,499 BTC transfer linked to the hack, with no timeline for restoring the $1 billion fund.",
   "시각(UTC)": "11-02 13:21"
  }
 ],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Arbitrum’s council moved $30 million of Binance hack funds without the hacker’s key",
   "요약": "A 12-person committee briefly rewrote one of Arbitrum’s core contracts to spend from an address it held no key for, then put the code back. It’s the second time this year.",
   "시각(UTC)": "11-03 05:25"
  },
  {
   "출처": "CoinDesk",
   "제목": "Big crypto wants the one thing it can’t buy: your vote",
   "요약": "Our loyalty has been to the technology. This election, the trap is to let the biggest intermediaries claim it for themselves, argues Berkeley Law lecturer Hermine Wong.",
   "시각(UTC)": "11-02 21:38"
  },
  {
   "출처": "CoinDesk",
   "제목": "EU entity suspected of losing $106 million from crypto exchange accounts, ZachXBT says",
   "요약": "The unidentified attacker moved funds through ether, instant exchanges and Monero, but the victim and affected exchanges remain unknown.",
   "시각(UTC)": "11-02 17:21"
  },
  {
   "출처": "CoinDesk",
   "제목": "NYSE tokenized stock plans take shape as four more transfer agents join",
   "요약": "Broadridge, Computershare, Equiniti and Superstate join the exchange's planned blockchain market, bringing shareholder records and voting services onchain.",
   "시각(UTC)": "11-02 16:41"
  },
  {
   "출처": "CoinDesk",
   "제목": "Nvidia, Costco and Nike join pushback against OKX–ICE tokenized stock plans",
   "요약": "Nearly 70% of the companies initially picked for trading have opted out, while 19 firms including Apple, Tesla and Amazon have no disclosed objection as the 30-day response window nears its end.",
   "시각(UTC)": "11-02 15:26"
  },
  {
   "출처": "CoinDesk",
   "제목": "Anthropic swings to third quarter operating loss as compute costs surge ahead of IPO",
   "요약": "The Claude developer generated $17 billion in quarterly revenue, but higher computing costs resulted in a $567 million operating loss.",
   "시각(UTC)": "11-02 15:18"
  },
  {
   "출처": "CoinDesk",
   "제목": "Standard Chartered debuts tokenized deposits in Hong Kong for corporate clients",
   "요약": "The bank uses Hong Kong's EnsembleTX system to move deposits between participating banks around the clock, settling in central bank money.",
   "시각(UTC)": "11-02 15:05"
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto's Washington playbook is working. Don't abandon it now.",
   "요약": "Regardless of how the midterm elections unfold or which party secures the presidency in 2028, our industry must adhere to its established playbook, writes Solana Policy Institute’s Colin McLaren.",
   "시각(UTC)": "11-02 15:00"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "26 (Fear)",
  "최근 7일": [
   26,
   37,
   34,
   30,
   30,
   51,
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
  "미결제약정 합계 USD(상위)": 29628805868
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 57.97,
  "CoinGecko 인기 검색 코인": [
   "BTC",
   "HYPE",
   "MON",
   "NEAR",
   "LIT",
   "SOL",
   "PEARL",
   "ZEC",
   "KNTQ",
   "SUI",
   "PENGU",
   "QTC",
   "PUMP",
   "PEPE",
   "AXIS"
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
  "종가": 2245.75,
  "등락률(%)": {
   "1일": -0.33,
   "7일": -4.45,
   "30일": -17.65,
   "90일": 17.65
  },
  "이동평균": {
   "MA20": 2351.921,
   "MA60": 2504.654167,
   "MA120": 2269.135333
  },
  "종가와 이평선 거리(%)": {
   "MA20": -4.51,
   "MA60": -10.34,
   "MA120": -1.03
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 14
  },
  "RSI14": 32.4,
  "ATR14(%)": 3.3,
  "거래량(20일 평균 대비 배수)": 0.1,
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
   2245.75
  ]
 },
 "4시간봉(요약)": {
  "등락률(%)": {
   "1일": -0.34,
   "7일": -2.75,
   "30일": -2.8,
   "90일": -7.62
  },
  "종가와 이평선 거리(%)": {
   "MA20": -0.77,
   "MA60": -2.44,
   "MA120": -4.89
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 58
  },
  "RSI14": 40.3
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
 "시가총액(USD)": 274092845348,
 "완전희석가치 FDV(USD)": 274092845348,
 "24시간 거래대금(USD)": 9725196212,
 "유통량": 122186161.86556138,
 "총발행량": 122186161.86556138,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 4946.05,
 "역대 최고가 대비(%)": -54.64579,
 "가격 변화(%)": {
  "7d": -3.02301,
  "30d": -16.74434,
  "1y": -39.87088
 },
 "소개": "Ethereum is a global, open-source platform for decentralized applications. In other words, it is a decentralized blockchain platform that enables developers to build and deploy smart contracts and applications without central authority control. Unlike Bitcoin, which primarily functions as digital currency, Ethereum operates as a programmable global computer where developers can create any type of ",
 "체인 TVL (DefiLlama)": {
  "체인": "Ethereum",
  "TVL(USD)": 43651648411
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "ETH 관련 기사": [
  {
   "출처": "CoinDesk",
   "제목": "EU entity suspected of losing $106 million from crypto exchange accounts, ZachXBT says",
   "요약": "The unidentified attacker moved funds through ether, instant exchanges and Monero, but the victim and affected exchanges remain unknown.",
   "시각(UTC)": "11-02 17:21"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin ETFs sink into October outflows with $643M exit after Binance hack",
   "요약": "US spot Bitcoin ETFs ended October with $515 million in net withdrawals, while Ether funds posted a record $1.61 billion in monthly outflows.",
   "시각(UTC)": "11-02 07:50"
  },
  {
   "출처": "Cointelegraph",
   "제목": "THORChain halts swaps after block reorg bug, slowing Binance hackers",
   "요약": "THORChain node operators paused swaps involving assets on 10 networks, including Bitcoin, Ethereum, Solana and Tron.",
   "시각(UTC)": "11-02 01:51"
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
   "제목": "Binance has spent half its SAFU bitcoin, about $580 million worth, data shows",
   "요약": "The user protection fund now sits below the $800 million level that Binance’s own rules say triggers a top-up, and the exchange hasn’t said when it will refill it.",
   "시각(UTC)": "11-03 05:36"
  },
  {
   "출처": "CoinDesk",
   "제목": "Arbitrum’s council moved $30 million of Binance hack funds without the hacker’s key",
   "요약": "A 12-person committee briefly rewrote one of Arbitrum’s core contracts to spend from an address it held no key for, then put the code back. It’s the second time this year.",
   "시각(UTC)": "11-03 05:25"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin drops below $77,000 as chip rout deepens ahead of U.S. midterm vote",
   "요약": "ZEC tumbled nearly 10% and BNB fell under $700 as the Nasdaq 100 slid into a correction, dragging Asian stocks lower.",
   "시각(UTC)": "11-03 04:48"
  },
  {
   "출처": "CoinDesk",
   "제목": "Big crypto wants the one thing it can’t buy: your vote",
   "요약": "Our loyalty has been to the technology. This election, the trap is to let the biggest intermediaries claim it for themselves, argues Berkeley Law lecturer Hermine Wong.",
   "시각(UTC)": "11-02 21:38"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin traders eye post-election rally as exchange outflows point to supply squeeze",
   "요약": "Bulls are watching short positions, exchange withdrawals and key price levels for signs of a rebound after the midterms.",
   "시각(UTC)": "11-02 18:13"
  },
  {
   "출처": "CoinDesk",
   "제목": "NYSE tokenized stock plans take shape as four more transfer agents join",
   "요약": "Broadridge, Computershare, Equiniti and Superstate join the exchange's planned blockchain market, bringing shareholder records and voting services onchain.",
   "시각(UTC)": "11-02 16:41"
  },
  {
   "출처": "CoinDesk",
   "제목": "Brazil’s Mercado Bitcoin halts withdrawals after $40 million drained across 10 chains",
   "요약": "The Brazilian exchange paused deposits and withdrawals after wallets on at least 10 chains were emptied, days after the $6.3 billion Binance hack.",
   "시각(UTC)": "11-02 15:53"
  },
  {
   "출처": "CoinDesk",
   "제목": "Nvidia, Costco and Nike join pushback against OKX–ICE tokenized stock plans",
   "요약": "Nearly 70% of the companies initially picked for trading have opted out, while 19 firms including Apple, Tesla and Amazon have no disclosed objection as the 30-day response window nears its end.",
   "시각(UTC)": "11-02 15:26"
  }
 ]
}
```

### VIBE 자료 · 센티먼트 (개미 분위기)

```json
{
 "공포·탐욕 지수": {
  "오늘": "26 (Fear)",
  "최근 7일": [
   26,
   37,
   34,
   30,
   30,
   51,
   51
  ]
 },
 "선물 포지션": {
  "출처": "CoinGecko (거래소별 무기한 선물, 미결제약정 큰 순)",
  "거래소별 펀딩비(%)": {
   "Binance (Futures)": 0.0094,
   "WEEX (Futures)": 0.0,
   "MEXC (Futures)": 0.01,
   "CoinW (Futures)": 0.01,
   "Hyperliquid (Futures)": 0.0013
  },
  "미결제약정 합계 USD(상위)": 18012995259
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 82.61,
  "CoinGecko 인기 검색 코인": [
   "BTC",
   "HYPE",
   "MON",
   "NEAR",
   "LIT",
   "SOL",
   "PEARL",
   "ZEC",
   "KNTQ",
   "SUI",
   "PENGU",
   "QTC",
   "PUMP",
   "PEPE",
   "AXIS"
  ],
  "ETH가 인기 검색에 있음": false
 }
}
```
