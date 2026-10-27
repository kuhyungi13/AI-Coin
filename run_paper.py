"""모의 투자 실행 파일. 진짜 돈과 API 키 없이, 가상의 돈으로 분할 추세 전략을 따라 한다.

하루 한 번(한국 시간 오전 9시 이후) 실행하면 바이낸스 공개 시세를 받아
paper/config.json 의 시작일부터 어제까지 전략을 그대로 다시 돌리고, 결과를 paper/ 폴더에 적는다.
매번 시작일부터 다시 계산하므로 하루 빼먹어도 다음 실행 때 자동으로 따라잡는다.

사용법:
    python run_paper.py
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from aicoin.data import fetch_klines
from aicoin.split_trend import SplitParams, run_split

PAPER = Path("paper")


def usd(v: float) -> str:
    return f"${v:,.2f}"


def main() -> None:
    cfg = json.loads((PAPER / "config.json").read_text(encoding="utf-8"))
    start = pd.Timestamp(cfg["start"], tz="UTC")
    p = SplitParams(ma=cfg["ma"], stop=cfg["stop"], tp=cfg["tp"],
                    fee=cfg["fee"], slippage=cfg["slippage"])
    capital = float(cfg["capital"])

    # 이동평균 계산용으로 시작일보다 넉넉히 앞부터 받는다.
    warmup = start - pd.Timedelta(days=p.ma * 3)
    df = fetch_klines(cfg["symbol"], "1d", f"{warmup:%Y-%m-%d}")
    today = pd.Timestamp.now(tz="UTC").normalize()
    df = df[df.index < today]  # 오늘 캔들은 아직 안 끝났으므로 뺀다

    days = df[df.index >= start]
    if days.empty:
        print(f"아직 끝난 거래일이 없습니다. {start:%Y-%m-%d} 하루가 끝난 뒤(한국 시간 다음 날 오전 9시) 다시 실행하세요.")
        write_status(cfg, None, pd.DataFrame(), None)
        return

    log: list = []
    res, _ = run_split(df, p, start=start, log=log)
    res = res[res.index >= start]

    balance = pd.DataFrame({
        "date": res.index.strftime("%Y-%m-%d"),
        "btc_close": res["close"].round(2),
        "equity_usd": (res["equity"] * capital).round(2),
        "hold_usd": (capital * res["close"] / res["open"].iloc[0]).round(2),
        "in_position": res["trade"],
    })
    balance.to_csv(PAPER / "balance.csv", index=False)

    trades = pd.DataFrame(log, columns=["date", "action", "price", "qty", "amount"])
    if not trades.empty:
        trades["date"] = pd.to_datetime(trades["date"]).dt.strftime("%Y-%m-%d")
        trades["price"] = trades["price"].round(2)
        trades["qty"] = trades["qty"].round(8)
        trades["amount"] = (trades["amount"] * capital).round(2)
    trades.to_csv(PAPER / "trades.csv", index=False)

    ma = df["close"].rolling(p.ma).mean()
    signal_up = bool(df["close"].iloc[-1] > ma.iloc[-1])
    write_status(cfg, balance, trades, signal_up)

    last = balance.iloc[-1]
    print(f"{last['date']} 기준 가상 잔고 {usd(last['equity_usd'])} "
          f"(그냥 보유했다면 {usd(last['hold_usd'])}), 거래 {len(trades)}건")


def write_status(cfg: dict, balance: pd.DataFrame | None, trades: pd.DataFrame,
                 signal_up: bool | None) -> None:
    lines = ["# 모의 투자 현황", "",
             "> 진짜 돈이 아닌 가상의 돈입니다. 매일 한국 시간 오전 9시쯤 자동으로 갱신됩니다.", "",
             f"- 코인: {cfg['symbol']} (현물, 레버리지 없음)",
             f"- 시작일: {cfg['start']}, 시작 금액: {usd(cfg['capital'])}",
             f"- 규칙: {cfg['ma']}일 이동평균 위면 3번 나눠 매수, 평균가 -{cfg['stop']:.0%} 손절, "
             f"+{cfg['tp']:.0%}·+{cfg['tp'] * 2:.0%}에서 1/3씩 익절, 나머지는 추세가 꺾이면 매도", ""]
    if balance is None:
        lines += ["아직 끝난 거래일이 없습니다. 첫 결과는 시작일 다음 날 나옵니다."]
    else:
        last = balance.iloc[-1]
        ret = last["equity_usd"] / cfg["capital"] - 1
        hold = last["hold_usd"] / cfg["capital"] - 1
        lines += [f"## {last['date']} 기준", "",
                  "| 항목 | 값 |", "|---|---|",
                  f"| 가상 잔고 | {usd(last['equity_usd'])} ({ret:+.1%}) |",
                  f"| 그냥 보유했다면 | {usd(last['hold_usd'])} ({hold:+.1%}) |",
                  f"| 코인 보유 중 | {'예' if last['in_position'] else '아니요'} |",
                  f"| BTC 종가 | {usd(last['btc_close'])} |",
                  f"| 거래 횟수 | {len(trades)}건 |",
                  f"| 오늘 추세 | {'이동평균 위 (살 수 있음)' if signal_up else '이동평균 아래 (사지 않음, 들고 있으면 판다)'} |",
                  ""]
        if not trades.empty:
            lines += ["## 최근 거래", "", "| 날짜 | 종류 | 가격 | 금액 |", "|---|---|---|---|"]
            for t in trades.tail(10).itertuples():
                lines.append(f"| {t.date} | {t.action} | {usd(t.price)} | {usd(t.amount)} |")
            lines.append("")
        lines += ["전체 기록: [balance.csv](balance.csv) (날짜별 잔고), [trades.csv](trades.csv) (거래)"]
    (PAPER / "STATUS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
