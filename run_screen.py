"""오늘의 코인 순위표. 바이낸스에서 지금 거래 중인 USDT 코인 전부를 훑어 순위를 매긴다.

규칙은 aicoin/rotation.py 와 같다(어제 종가까지의 정보만 쓴다).
1. 최근 30일 거래대금 상위 10개(상장 90일 넘은 코인만, 상장 폐지 코인은 뺀다)
2. 그중 종가가 50일 이동평균 위인 코인
3. 최근 14일 상승률 높은 순서로 5개
4. 비트코인이 50일 이동평균 아래면 아무것도 고르지 않는다

결과는 paper/PICKS.md 에 적는다. 과거 시험에서 비트코인 그냥 보유보다 못했으므로 참고용이다.

사용법:
    python run_screen.py
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import pandas as pd

from aicoin.data import fetch_klines
from aicoin.rotation import Panels, RotationParams, pick, scores
from aicoin.universe import usdt_symbols

OUT = Path("paper/PICKS.md")


def pct(v: float) -> str:
    return f"{v * 100:+.1f}%"


def main() -> None:
    p = RotationParams()
    now = pd.Timestamp.now(tz="UTC")
    since = f"{now - pd.Timedelta(days=max(p.min_age, p.ma, p.lookback) + 60):%Y-%m-%d}"
    symbols = usdt_symbols(include_delisted=False)
    print(f"지금 거래 중인 코인 {len(symbols)}개 확인 중...")

    def one(sym):
        try:
            return sym, fetch_klines(sym, "1d", since, quote_volume=True)
        except RuntimeError:
            return sym, None

    with ThreadPoolExecutor(6) as ex:
        frames = {s: df for s, df in ex.map(one, symbols) if df is not None and len(df)}
    px = Panels.from_frames(frames)
    sc = scores(px, p)
    day = px.close.index[-1]   # 오늘(진행 중) 캔들. 점수는 어제 종가까지로 계산돼 있다.
    picks = pick(sc, day, p)

    rank = sc["rank"].loc[day]
    top = rank[rank <= p.top_n].sort_values().index
    ma = px.close.rolling(p.ma).mean().shift(1).loc[day]
    rows = []
    for sym in top:
        rows.append(f"| {int(rank[sym])} | {sym.removesuffix('USDT')} | "
                    f"{px.close[sym].shift(1).loc[day]:,.6g} | {pct(sc['mom'].loc[day, sym])} | "
                    f"{'위 ✅' if sc['up'].loc[day, sym] else '아래'} | "
                    f"{'**선정 ' + str(picks.index(sym) + 1) + '위**' if sym in picks else ''} |")

    btc_up = bool(sc["btc_up"].loc[day])
    btc_close = px.close["BTCUSDT"].shift(1).loc[day]
    lines = [
        "# 오늘의 코인 순위표 (참고용)",
        "",
        f"기준: {day - pd.Timedelta(days=1):%Y-%m-%d} 종가 (한국 시간 {day:%Y-%m-%d} 오전 9시까지) · "
        f"갱신 {now.tz_convert('Asia/Seoul'):%Y-%m-%d %H:%M} KST",
        "",
        f"- 시장 날씨: 비트코인 {btc_close:,.0f} USDT, 50일 평균 "
        f"{px.close['BTCUSDT'].rolling(p.ma).mean().shift(1).loc[day]:,.0f} → "
        + ("**맑음** (평균 위, 살 수 있음)" if btc_up else "**흐림** (평균 아래, 전부 현금)"),
        "- 고른 코인: " + (", ".join(s.removesuffix("USDT") for s in picks) if picks else "없음"),
        "",
        f"## 거래대금 상위 {p.top_n}개 (지금 거래 중인 코인 {len(frames)}개 중)",
        "",
        f"| 거래대금 순위 | 코인 | 어제 종가 | 최근 {p.lookback}일 | {p.ma}일 평균 | 선정 |",
        "|---|---|---|---|---|---|",
        *rows,
        "",
        "## 고르는 규칙",
        "",
        f"1. 상장 {p.min_age}일 넘은 코인 중 최근 30일 거래대금 상위 {p.top_n}개 (상장 폐지·스테이블코인 제외)",
        f"2. 그중 어제 종가가 {p.ma}일 평균 위인 코인",
        f"3. 최근 {p.lookback}일 상승률이 높은 순서로 {p.picks}개",
        f"4. 비트코인이 {p.ma}일 평균 아래면 아무것도 고르지 않음",
        "",
        "## 주의: 아직 이걸로 사면 안 됩니다",
        "",
        "2019~2022년 데이터로 설정을 고르고 처음 보는 2023년~지금 데이터로 시험했더니(수수료 포함),",
        "이 설정은 +108% (최대 손실폭 -54%), 같은 기간 **비트코인 그냥 보유는 +383%** 였습니다.",
        "시험한 44개 설정 중 비트코인 보유를 이긴 설정은 0개, 돈을 번 설정도 13개뿐이었습니다.",
        "2023년 이후엔 알트코인이 비트코인보다 계속 약했기 때문입니다. 자세한 건 `python run_rotation.py`.",
    ]
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:8]))
    print(f"\n저장: {OUT}")


if __name__ == "__main__":
    main()
