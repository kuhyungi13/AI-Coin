"""모의 투자 실행 파일. 진짜 돈과 API 키 없이, 가상의 돈으로 분할 추세 전략을 따라 한다.

paper/config.json 의 전략마다 시작일부터 지금까지 다시 계산하고, 결과를 paper/<전략 이름>/ 폴더에 적는다.
매번 시작일부터 다시 계산하므로 몇 번 빼먹어도 다음 실행 때 자동으로 따라잡는다.
진행 중인 마지막 캔들은 지금까지의 값으로 반영한다(잔고는 현재가 기준).

사용법:
    python run_paper.py
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from aicoin.paper import load_config, simulate

PAPER = Path("paper")


def usd(v: float) -> str:
    return f"${v:,.2f}"


def main() -> None:
    cfg, strategies = load_config(PAPER / "config.json")
    if pd.Timestamp.now(tz="UTC") < pd.Timestamp(cfg["start"], tz="UTC"):
        print(f"{cfg['start']}부터 거래합니다. 아직 시작일이 오지 않았습니다.")
        return
    results = []
    for s in strategies:
        r = simulate(cfg, s)
        folder = PAPER / s.name
        folder.mkdir(exist_ok=True)
        r["balance"].to_csv(folder / "balance.csv", index=False)
        r["trades"].to_csv(folder / "trades.csv", index=False)
        results.append(r)
        last = r["balance"].iloc[-1]
        print(f"[{s.title}] 가상 잔고 {usd(last['equity_usd'])} "
              f"(그냥 보유했다면 {usd(last['hold_usd'])}), 거래 {len(r['trades'])}건")
    write_status(cfg, results)


def write_status(cfg: dict, results: list[dict]) -> None:
    now = pd.Timestamp.now(tz="UTC") + pd.Timedelta(hours=9)
    lines = ["# 모의 투자 현황", "",
             "> 진짜 돈이 아닌 가상의 돈입니다. GitHub가 자동으로 갱신하고, "
             "내 컴퓨터에서 `live_paper.py`를 켜면 실시간으로 볼 수 있습니다.", "",
             f"- 코인: {cfg['symbol']} (현물, 레버리지 없음), 시작일: {cfg['start']}, "
             f"전략마다 시작 금액 {usd(cfg['capital'])}",
             f"- {now:%Y-%m-%d %H:%M} (한국 시간) 기준", ""]
    for r in results:
        s, last, st = r["strategy"], r["balance"].iloc[-1], r["state"]
        ret = last["equity_usd"] / r["capital"] - 1
        hold = last["hold_usd"] / r["capital"] - 1
        lines += [f"## {s.title}", "", f"규칙: {s.rule()}", "",
                  "| 항목 | 값 |", "|---|---|",
                  f"| 가상 잔고 | {usd(last['equity_usd'])} ({ret:+.1%}) |",
                  f"| 그냥 보유했다면 | {usd(last['hold_usd'])} ({hold:+.1%}) |",
                  f"| 코인 보유 중 | {'예' if st['qty'] > 0 else '아니요'} |"]
        if st["qty"] > 0:
            lines.append(f"| 평균 매수가 / 손절가 | {usd(st['avg'])} / {usd(st['stop_px'])} |")
        lines += [f"| BTC 가격 | {usd(r['price'])} |",
                  f"| 거래 횟수 | {len(r['trades'])}건 |",
                  f"| 추세 | {'평균선 위 (살 수 있음)' if r['signal_up'] else '평균선 아래 (사지 않음)'} |", ""]
        if not r["trades"].empty:
            lines += ["| 시각 (UTC) | 종류 | 가격 | 금액 |", "|---|---|---|---|"]
            for t in r["trades"].tail(10).itertuples():
                lines.append(f"| {t.date} | {t.action} | {usd(t.price)} | {usd(t.amount)} |")
            lines.append("")
        lines += [f"전체 기록: [{s.name}/balance.csv]({s.name}/balance.csv), "
                  f"[{s.name}/trades.csv]({s.name}/trades.csv)", ""]
    (PAPER / "STATUS.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
