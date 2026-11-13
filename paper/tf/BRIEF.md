# TF팀 회의 자료 (2026-11-13 13:37 KST)

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
   "1일": -3.49,
   "7일": -6.82,
   "30일": -9.16,
   "90일": -13.64
  },
  "종가와 이평선 거리(%)": {
   "MA20": -6.05,
   "MA60": -8.81,
   "MA120": -10.97
  },
  "MA20>MA60": false,
  "최근 교차": null,
  "RSI14": 17.6
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
 "시가총액(USD)": 1386434154819,
 "완전희석가치 FDV(USD)": 1386439118377,
 "24시간 거래대금(USD)": 35824237763,
 "유통량": 20111231.0,
 "총발행량": 20111303.0,
 "최대발행량": 21000000.0,
 "유통 비율(%)": 95.8,
 "역대 최고가(USD)": 126080,
 "역대 최고가 대비(%)": -45.32456,
 "가격 변화(%)": {
  "7d": -9.06975,
  "30d": -17.58176,
  "1y": -32.4464
 },
 "소개": "Bitcoin is the world's first decentralized cryptocurrency, created in 2009 by the pseudonymous Satoshi Nakamoto. It enables peer-to-peer electronic cash transactions without intermediaries like banks or governments, operating on a blockchain secured by Proof of Work mining and the SHA-256 cryptographic algorithm. \n\nWith a fixed supply cap of 21 million coins and programmatic halvings every four ye",
 "체인 TVL (DefiLlama)": {
  "체인": "Bitcoin",
  "TVL(USD)": 3655736026
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "BTC 관련 기사": [
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
   "출처": "CoinDesk",
   "제목": "Live updates: Bitcoin slumps below $72,000 as Nvidia's Huang resigns, interest rates surge",
   "요약": "The Fed continued amping up its hawkishness on Thursday; meanwhile, existing home sales fell to their weakest level in 16 years.",
   "시각(UTC)": "11-12 09:15"
  },
  {
   "출처": "CoinDesk",
   "제목": "Canaan may sell more bitcoin for stock buybacks as mining-rig revenue falls 96%",
   "요약": "The Avalon maker has launched a $20 million repurchase program, while most of its bitcoin holdings were pledged or placed in a fixed-term product at September’s end.",
   "시각(UTC)": "11-12 07:41"
  },
  {
   "출처": "CoinDesk",
   "제목": "MSCI is dropping Strategy from its index, and the exclusion could hit its bitcoin-buying machine",
   "요약": "MSCI’s decision to exclude Strategy from its equity indexes could hamper the company’s ability to buy more bitcoin, according to some analysts.",
   "시각(UTC)": "11-12 07:00"
  },
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin Core reveals bug that made thousands of nodes trust any stranger on Tor",
   "요약": "The flaw was fixed in October 2025 and kept quiet until Tuesday. It came out alongside a high-severity bug that could stop a miner from producing blocks until someone restarted it.",
   "시각(UTC)": "11-12 05:22"
  },
  {
   "출처": "CoinDesk",
   "제목": "Nvidia perps crash 7% as CEO Jensen Huang reportedly faces the axe",
   "요약": "Nvidia perps are down 7% on Hyperliquid as traders react to reports that CEO Jensen Huang may be removed. Bitcoin continues to trade in a familiar price range.",
   "시각(UTC)": "11-12 04:03"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Here’s what happened in crypto today",
   "요약": "Need to know what happened in crypto today? Here is the latest news on daily trends and events impacting Bitcoin price, blockchain, DeFi, Web3 and crypto regulation.",
   "시각(UTC)": "11-12 22:11"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Strategy stock sheds 5% amid MSCI index removal, Bitcoin sell-off",
   "요약": "Strategy shares declined Thursday following MSCI’s decision to remove the company from its indexes, as Bitcoin also fell amid a broader crypto market decline.",
   "시각(UTC)": "11-12 21:52"
  },
  {
   "출처": "Cointelegraph",
   "제목": "Bitcoin slides toward $71K as Nvidia stock tumbles after Huang steps down",
   "요약": "Bitcoin fell to its lowest leve since Aug. 20 as tech stocks slid following the resignation of Nvidia CEO Jensen Huang.",
   "시각(UTC)": "11-12 15:46"
  },
  {
   "출처": "Cointelegraph",
   "제목": "BlackRock Bitcoin ETF outflows hit $2B over nine sessions",
   "요약": "US spot Bitcoin ETF outflows rose to nearly $300 million on Wednesday, up from $95 million a day earlier, as five-session withdrawals reached $1.44 billion.",
   "시각(UTC)": "11-12 08:06"
  },
  {
   "출처": "Cointelegraph",
   "제목": "US data center restrictions could give Bitcoin miners an edge in AI, though challenges remain",
   "요약": "As US voters push back against new data centers, Bitcoin miners already expanding into AI could benefit from their existing facilities.",
   "시각(UTC)": "11-11 20:43"
  },
  {
   "출처": "Decrypt",
   "제목": "Strategy Made $19.5 Billion in Profit. So Why Is MSCI Removing It From Stock Indexes?",
   "요약": "Michael Saylor’s Bitcoin giant is being excluded from major investment benchmarks, raising questions about what qualifies as a business—and whether the decision could slow its Bitcoin buying.",
   "시각(UTC)": "11-12 21:26"
  },
  {
   "출처": "Decrypt",
   "제목": "Why the Path to Quantum Resistance Runs Uphill for Bitcoin Wallet Makers",
   "요약": "Trezor CTO Tomáš Sušánka explains the trade-offs of Bitcoin’s leading post-quantum signature scheme.",
   "시각(UTC)": "11-12 20:36"
  }
 ],
 "시장 전반 기사": [
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto for Advisors: The blockchain built to run financial markets",
   "요약": "",
   "시각(UTC)": "11-12 15:34"
  },
  {
   "출처": "CoinDesk",
   "제목": "Jupiter adds Anchorage-backed USDGO to its $1 billion Solana lending platform",
   "요약": "OSL offers a yield on USDGO only to professional investors, but Jupiter said its market lets other holders earn onchain at rates set by borrower demand.",
   "시각(UTC)": "11-12 14:45"
  },
  {
   "출처": "CoinDesk",
   "제목": "The next Congress will write rules for AI and emerging tech. They should use the stuff first.",
   "요약": "The best thing industry leaders can do is to invest the time to ensure this country’s policymakers can experience the technology they’re regulating up close, writes Allie Page, executive director of American Innovation Project.",
   "시각(UTC)": "11-12 14:24"
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
   "Binance (Futures)": 0.0046,
   "OKX (Futures)": 0.0045,
   "Bybit (Futures)": 0.0038,
   "Gate (Futures)": 0.0012,
   "MEXC (Futures)": 0.0047,
   "XT.COM (Derivatives)": 0.0047
  },
  "미결제약정 합계 USD(상위)": 18294534805
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 58.58,
  "CoinGecko 인기 검색 코인": [
   "MIHAO",
   "BTC",
   "SANC",
   "ZEC",
   "PENGU",
   "ETH",
   "SOL",
   "XRP",
   "NEAR",
   "TAO",
   "PUMP",
   "PEARL",
   "HYPE",
   "LIT",
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
   "1일": -4.22,
   "7일": -5.92,
   "30일": -13.57,
   "90일": -16.22
  },
  "종가와 이평선 거리(%)": {
   "MA20": -5.84,
   "MA60": -11.69,
   "MA120": -13.92
  },
  "MA20>MA60": false,
  "최근 교차": {
   "종류": "데드크로스",
   "며칠 전": 30
  },
  "RSI14": 22.2
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
 "시가총액(USD)": 236268495420,
 "완전희석가치 FDV(USD)": 236268495420,
 "24시간 거래대금(USD)": 12852648299,
 "유통량": 122215668.80579185,
 "총발행량": 122215668.80579185,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 4946.05,
 "역대 최고가 대비(%)": -60.91404,
 "가격 변화(%)": {
  "7d": -13.41486,
  "30d": -23.03774,
  "1y": -43.94138
 },
 "소개": "Ethereum is a global, open-source platform for decentralized applications. In other words, it is a decentralized blockchain platform that enables developers to build and deploy smart contracts and applications without central authority control. Unlike Bitcoin, which primarily functions as digital currency, Ethereum operates as a programmable global computer where developers can create any type of ",
 "체인 TVL (DefiLlama)": {
  "체인": "Ethereum",
  "TVL(USD)": 39768619278
 }
}
```

### NOVA 자료 · 뉴스 분석

```json
{
 "ETH 관련 기사": [
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
   "출처": "Cointelegraph",
   "제목": "Ethlabs drops Hegotá slot proposal in push for 2027 quantum readiness",
   "요약": "Ethlabs’ roadmap aims to help Ethereum withstand quantum attacks and give users a way to protect their accounts by 2027.",
   "시각(UTC)": "11-12 10:30"
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto for Advisors: The blockchain built to run financial markets",
   "요약": "",
   "시각(UTC)": "11-12 15:34"
  },
  {
   "출처": "CoinDesk",
   "제목": "Jupiter adds Anchorage-backed USDGO to its $1 billion Solana lending platform",
   "요약": "OSL offers a yield on USDGO only to professional investors, but Jupiter said its market lets other holders earn onchain at rates set by borrower demand.",
   "시각(UTC)": "11-12 14:45"
  },
  {
   "출처": "CoinDesk",
   "제목": "The next Congress will write rules for AI and emerging tech. They should use the stuff first.",
   "요약": "The best thing industry leaders can do is to invest the time to ensure this country’s policymakers can experience the technology they’re regulating up close, writes Allie Page, executive director of American Innovation Project.",
   "시각(UTC)": "11-12 14:24"
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
   "Binance (Futures)": 0.0035,
   "WEEX (Futures)": 0.0,
   "OKX (Futures)": 0.0001,
   "CoinW (Futures)": 0.0037,
   "MEXC (Futures)": 0.0037
  },
  "미결제약정 합계 USD(상위)": 11816413375
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 73.21,
  "CoinGecko 인기 검색 코인": [
   "MIHAO",
   "BTC",
   "SANC",
   "ZEC",
   "PENGU",
   "ETH",
   "SOL",
   "XRP",
   "NEAR",
   "TAO",
   "PUMP",
   "PEARL",
   "HYPE",
   "LIT",
   "AERO"
  ],
  "ETH가 인기 검색에 있음": true
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
   "1일": 0.5,
   "7일": -8.23,
   "30일": 7.93,
   "90일": 6.78
  },
  "종가와 이평선 거리(%)": {
   "MA20": -2.6,
   "MA60": 7.89,
   "MA120": 7.34
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 35
  },
  "RSI14": 48.2
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
 "시가총액 순위": 955,
 "시가총액(USD)": 14328592,
 "완전희석가치 FDV(USD)": 81994807,
 "24시간 거래대금(USD)": 37666530,
 "유통량": 174750000.0,
 "총발행량": 1000000000.0,
 "최대발행량": 1000000000.0,
 "유통 비율(%)": 17.5,
 "역대 최고가(USD)": 1.88,
 "역대 최고가 대비(%)": -95.6364,
 "가격 변화(%)": {
  "7d": 11.53019,
  "30d": 28.15032,
  "1y": -65.79323
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
   "제목": "Bitcoin dips below $70,000 as Dollar Index hits 19-month high",
   "요약": "The crypto market selloff gathered pace early Friday. Bitcoin dropped below $70,000 and ether traded below $2,000, triggering large liquidations in futures market.",
   "시각(UTC)": "11-13 03:37"
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto for Advisors: The blockchain built to run financial markets",
   "요약": "",
   "시각(UTC)": "11-12 15:34"
  },
  {
   "출처": "CoinDesk",
   "제목": "Jupiter adds Anchorage-backed USDGO to its $1 billion Solana lending platform",
   "요약": "OSL offers a yield on USDGO only to professional investors, but Jupiter said its market lets other holders earn onchain at rates set by borrower demand.",
   "시각(UTC)": "11-12 14:45"
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
   "OrangeX Futures": -0.1143,
   "Binance (Futures)": -0.1426,
   "XT.COM (Derivatives)": -0.0321,
   "Toobit Futures": -0.1426,
   "Bybit (Futures)": -0.2128,
   "KCEX (Futures)": -0.1416
  },
  "미결제약정 합계 USD(상위)": 50553752
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 0.0,
  "CoinGecko 인기 검색 코인": [
   "MIHAO",
   "BTC",
   "SANC",
   "ZEC",
   "PENGU",
   "ETH",
   "SOL",
   "XRP",
   "NEAR",
   "TAO",
   "PUMP",
   "PEARL",
   "HYPE",
   "LIT",
   "AERO"
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
   "1일": -0.47,
   "7일": 2.9,
   "30일": 11.11,
   "90일": -0.36
  },
  "종가와 이평선 거리(%)": {
   "MA20": 3.04,
   "MA60": 6.33,
   "MA120": 3.52
  },
  "MA20>MA60": true,
  "최근 교차": {
   "종류": "골든크로스",
   "며칠 전": 7
  },
  "RSI14": 67.9
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
 "시가총액 순위": 840,
 "시가총액(USD)": 18321141,
 "완전희석가치 FDV(USD)": 18321141,
 "24시간 거래대금(USD)": 10317430,
 "유통량": 46021.18905985,
 "총발행량": 46021.18905985,
 "최대발행량": null,
 "유통 비율(%)": 100.0,
 "역대 최고가(USD)": 435.42,
 "역대 최고가 대비(%)": -8.58201,
 "가격 변화(%)": {
  "7d": 14.66367,
  "30d": 5.67576,
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
   "제목": "Bitcoin dips below $70,000 as Dollar Index hits 19-month high",
   "요약": "The crypto market selloff gathered pace early Friday. Bitcoin dropped below $70,000 and ether traded below $2,000, triggering large liquidations in futures market.",
   "시각(UTC)": "11-13 03:37"
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
  },
  {
   "출처": "CoinDesk",
   "제목": "Crypto for Advisors: The blockchain built to run financial markets",
   "요약": "",
   "시각(UTC)": "11-12 15:34"
  },
  {
   "출처": "CoinDesk",
   "제목": "Jupiter adds Anchorage-backed USDGO to its $1 billion Solana lending platform",
   "요약": "OSL offers a yield on USDGO only to professional investors, but Jupiter said its market lets other holders earn onchain at rates set by borrower demand.",
   "시각(UTC)": "11-12 14:45"
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
  "CoinGecko 이용자 투표 상승(%)": 0.0,
  "CoinGecko 인기 검색 코인": [
   "MIHAO",
   "BTC",
   "SANC",
   "ZEC",
   "PENGU",
   "ETH",
   "SOL",
   "XRP",
   "NEAR",
   "TAO",
   "PUMP",
   "PEARL",
   "HYPE",
   "LIT",
   "AERO"
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
   "1일": -3.98,
   "7일": -5.78,
   "30일": -12.15,
   "90일": -21.29
  },
  "종가와 이평선 거리(%)": {
   "MA20": -5.91,
   "MA60": -11.23,
   "MA120": -16.06
  },
  "MA20>MA60": false,
  "최근 교차": null,
  "RSI14": 21.9
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
 "시가총액(USD)": 46405517153,
 "완전희석가치 FDV(USD)": 50012978212,
 "24시간 거래대금(USD)": 2753344326,
 "유통량": 591511156.4310429,
 "총발행량": 637493910.0592042,
 "최대발행량": null,
 "유통 비율(%)": 92.8,
 "역대 최고가(USD)": 293.31,
 "역대 최고가 대비(%)": -73.25473,
 "가격 변화(%)": {
  "7d": -12.48142,
  "30d": -27.20411,
  "1y": -49.18565
 },
 "소개": "Solana is a high-performance Layer 1 blockchain designed for mass adoption by providing a fast, secure, and low-cost environment for decentralized applications. It distinguishes itself by scaling globally without the use of complex sharding or multiple layers, instead maintaining a single, unified ledger to avoid liquidity fragmentation. This architecture allows it to process thousands of transact",
 "체인 TVL (DefiLlama)": {
  "체인": "Solana",
  "TVL(USD)": 4985936670
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
  },
  {
   "출처": "Decrypt",
   "제목": "Decrypt Becomes First News Publisher to Offer Perps Trading, Powered by Solana's Phoenix",
   "요약": "The integration brings perpetual futures trading into Decrypt, so readers can trade crypto, stocks and commodities without leaving the news.",
   "시각(UTC)": "11-11 14:02"
  }
 ],
 "시장 전반 기사": [
  {
   "출처": "CoinDesk",
   "제목": "Bitcoin dips below $70,000 as Dollar Index hits 19-month high",
   "요약": "The crypto market selloff gathered pace early Friday. Bitcoin dropped below $70,000 and ether traded below $2,000, triggering large liquidations in futures market.",
   "시각(UTC)": "11-13 03:37"
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
   "제목": "Crypto for Advisors: The blockchain built to run financial markets",
   "요약": "",
   "시각(UTC)": "11-12 15:34"
  },
  {
   "출처": "CoinDesk",
   "제목": "The next Congress will write rules for AI and emerging tech. They should use the stuff first.",
   "요약": "The best thing industry leaders can do is to invest the time to ensure this country’s policymakers can experience the technology they’re regulating up close, writes Allie Page, executive director of American Innovation Project.",
   "시각(UTC)": "11-12 14:24"
  },
  {
   "출처": "CoinDesk",
   "제목": "Nvidia CEO Huang quits company he co-founded, led for 3 decades. Shares slump",
   "요약": "CFO Colette Kress takes over as interim CEO after Huang steps down immediately as president, chief executive and board member, as shares tumble.",
   "시각(UTC)": "11-12 13:57"
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
   "Binance (Futures)": 0.01,
   "Gate (Futures)": 0.002,
   "OKX (Futures)": 0.0084,
   "Bybit (Futures)": -0.0007,
   "CoinUp.io (Futures)": 0.0071,
   "WhiteBIT Futures": 0.01
  },
  "미결제약정 합계 USD(상위)": 2059656969
 },
 "커뮤니티 인기글(레딧)": {
  "오류": "HTTPError: 403 Client Error: Blocked for url: https://www.reddit.com/r/CryptoCurrency/hot.json?limit=15"
 },
 "군중 심리(CoinGecko)": {
  "CoinGecko 이용자 투표 상승(%)": 69.44,
  "CoinGecko 인기 검색 코인": [
   "MIHAO",
   "BTC",
   "SANC",
   "ZEC",
   "PENGU",
   "ETH",
   "SOL",
   "XRP",
   "NEAR",
   "TAO",
   "PUMP",
   "PEARL",
   "HYPE",
   "LIT",
   "AERO"
  ],
  "SOL가 인기 검색에 있음": true
 }
}
```
