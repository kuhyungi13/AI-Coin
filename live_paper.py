"""내 컴퓨터에서 모의 투자를 실시간으로 보는 화면. 진짜 돈과 API 키는 쓰지 않는다.

    streamlit run live_paper.py      (윈도우에서는 start_live.bat 을 더블클릭)

몇 초마다 바이낸스 공개 시세를 받아 paper/config.json 의 전략들을 시작일부터 다시 계산하고 보여 준다.
GitHub Actions가 계산하는 것과 같은 코드(aicoin/paper.py)를 쓴다.
"""

from __future__ import annotations

import altair as alt
import pandas as pd
import streamlit as st

from aicoin.paper import load_config, simulate

REFRESH_SECONDS = 15

st.set_page_config(page_title="BTC 실시간 모의 투자", layout="wide")
st.title("BTC 실시간 모의 투자")
st.caption(f"가상의 돈입니다. {REFRESH_SECONDS}초마다 바이낸스 시세로 새로 계산해요. 이 창을 닫으면 멈춰요.")


def usd(v: float) -> str:
    return f"${v:,.2f}"


def md_usd(v: float) -> str:  # 마크다운에서 $가 수식 기호로 읽히지 않게
    return usd(v).replace("$", "\\$")


def lines(df: pd.DataFrame, x: str, height: int) -> alt.Chart:
    """여러 줄 그래프. 세로축을 0부터 시작하지 않아서 움직임이 잘 보인다."""
    long = df.reset_index().melt(x, var_name="항목", value_name="값").dropna()
    base = alt.Chart(long).encode(
        x=alt.X(f"{x}:T", title=None),
        y=alt.Y("값:Q", title=None, scale=alt.Scale(zero=False), axis=alt.Axis(format="$,.0f")),
        color=alt.Color("항목:N", legend=alt.Legend(orient="bottom", title=None)),
        tooltip=[alt.Tooltip(f"{x}:T", format="%Y-%m-%d %H:%M"), "항목:N", alt.Tooltip("값:Q", format="$,.2f")])
    chart = base.mark_line(strokeWidth=2)
    if len(df) < 40:
        chart = chart + base.mark_point(filled=True, size=40)
    return chart.properties(height=height)


@st.fragment(run_every=REFRESH_SECONDS)
def board() -> None:
    cfg, strategies = load_config()
    try:
        results = [simulate(cfg, s) for s in strategies]
    except Exception as e:  # 인터넷이 잠깐 끊겨도 화면은 유지하고 다음에 다시 시도한다
        st.warning(f"시세를 받지 못했어요. 잠시 뒤 다시 시도해요. ({e})")
        return

    now = pd.Timestamp.now(tz="Asia/Seoul")
    st.subheader(f"BTC {usd(results[0]['price'])}")
    st.caption(f"{now:%Y-%m-%d %H:%M:%S} (한국 시간) 기준 · 시작일 {cfg['start']} · 전략마다 시작 금액 {usd(cfg['capital'])}")

    for col, r in zip(st.columns(len(results)), results):
        s, st_, bal = r["strategy"], r["state"], r["balance"]
        with col:
            st.markdown(f"### {s.title}")
            st.caption(s.rule())
            if bal.empty:
                st.info("아직 시작 전이에요.")
                continue
            last = bal.iloc[-1]
            a, b = st.columns(2)
            a.metric("가상 잔고", usd(last["equity_usd"]), f"{last['equity_usd'] / r['capital'] - 1:+.2%}")
            b.metric("그냥 BTC를 샀다면", usd(last["hold_usd"]), f"{last['hold_usd'] / r['capital'] - 1:+.2%}")

            if st_["qty"] > 0:
                price = r["price"]
                st.success(f"BTC 보유 중 · 평균 매수가 {md_usd(st_['avg'])} · {st_['bought']}/3번 매수")
                c, d = st.columns(2)
                c.metric("손절가", usd(st_["stop_px"]), f"지금보다 {st_['stop_px'] / price - 1:+.2%}",
                         delta_color="off")
                if st_["tp_px"]:
                    d.metric(f"다음 익절가 ({st_['tp_done'] + 1}번째)", usd(st_["tp_px"]),
                             f"지금보다 {st_['tp_px'] / price - 1:+.2%}", delta_color="off")
            elif r["signal_up"]:
                st.info("현금 대기 · 추세가 평균선 위라서 다음 캔들 시작에 1/3을 사요"
                        + (" (손절 뒤라 추세가 한 번 꺾였다가 다시 올라와야 사요)" if st_["locked"] else ""))
            else:
                st.warning(f"현금 대기 · 평균선 아래라서 쉬는 중 "
                           f"(마지막 종가 {md_usd(r['last_close'])}, 평균 {md_usd(r['last_ma'])}, "
                           f"{r['last_close'] / r['last_ma'] - 1:+.2%})")

            candles = r["candles"].tail(120)[["close", "ma"]].rename(columns={"close": "BTC", "ma": "평균선"})
            candles.index = candles.index.tz_convert("Asia/Seoul").tz_localize(None).rename("시각")
            st.markdown("**BTC 가격과 평균선** (최근 120개 캔들, 한국 시간)")
            st.altair_chart(lines(candles, "시각", 220), use_container_width=True)

            eq = bal.assign(시각=pd.to_datetime(bal["date"])).set_index("시각")[["equity_usd", "hold_usd"]].rename(
                columns={"equity_usd": "가상 잔고", "hold_usd": "그냥 보유"})
            st.markdown("**가상 잔고 vs 그냥 보유**")
            st.altair_chart(lines(eq, "시각", 180), use_container_width=True)

            st.markdown(f"**거래 기록** ({len(r['trades'])}건, 시각은 UTC)")
            if r["trades"].empty:
                st.caption("아직 거래가 없어요.")
            else:
                t = r["trades"].iloc[::-1].rename(columns={"date": "시각", "action": "종류", "price": "가격",
                                                          "qty": "수량(BTC)", "amount": "금액($)"})
                st.dataframe(t, hide_index=True, use_container_width=True)


board()
