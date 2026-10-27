"""모의 투자 계산. GitHub Actions(run_paper.py)와 내 컴퓨터 실시간 화면(live_paper.py)이 같이 쓴다."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from .data import fetch_klines
from .split_trend import SplitParams, run_split

STEP = {"15m": pd.Timedelta(minutes=15), "1h": pd.Timedelta(hours=1),
        "4h": pd.Timedelta(hours=4), "1d": pd.Timedelta(days=1)}
UNIT = {"15m": "15분", "1h": "1시간", "4h": "4시간", "1d": "하루"}


@dataclass
class Strategy:
    name: str
    title: str
    interval: str
    ma: int
    stop: float
    tp: float

    def params(self, cfg: dict) -> SplitParams:
        return SplitParams(ma=self.ma, stop=self.stop, tp=self.tp,
                           fee=cfg.get("fee", 0.001), slippage=cfg.get("slippage", 0.0005))

    def rule(self) -> str:
        return (f"{UNIT[self.interval]} 캔들 {self.ma}개 평균 위면 3번 나눠 매수, 평균가 -{self.stop:.0%} 손절, "
                f"+{self.tp:.0%}·+{self.tp * 2:.0%}에서 1/3씩 익절, 나머지는 추세가 꺾이면 매도")


def load_config(path: str | Path = "paper/config.json") -> tuple[dict, list[Strategy]]:
    cfg = json.loads(Path(path).read_text(encoding="utf-8"))
    raw = cfg.get("strategies") or [{"name": "daily", "title": "하루 단위", "interval": "1d",
                                      "ma": cfg["ma"], "stop": cfg["stop"], "tp": cfg["tp"]}]
    return cfg, [Strategy(**s) for s in raw]


def simulate(cfg: dict, s: Strategy) -> dict:
    """시작일부터 지금까지 전략을 다시 돌린다. 진행 중인 마지막 캔들도 지금까지의 값으로 반영한다."""
    start = pd.Timestamp(cfg["start"], tz="UTC")
    step = STEP[s.interval]
    capital = float(cfg["capital"])
    df = fetch_klines(cfg["symbol"], s.interval, f"{start - step * s.ma * 3:%Y-%m-%d %H:%M}")
    now = pd.Timestamp.now(tz="UTC")
    done = df[df.index + step <= now]  # 끝난 캔들

    log: list = []
    state: dict = {}
    res, _ = run_split(df, s.params(cfg), start=start, log=log, state=state)
    res = res[res.index >= start]

    fmt = "%Y-%m-%d" if s.interval == "1d" else "%Y-%m-%d %H:%M"
    balance = pd.DataFrame({
        "date": res.index.strftime(fmt),
        "btc_close": res["close"].round(2),
        "equity_usd": (res["equity"] * capital).round(2),
        "hold_usd": (capital * res["close"] / res["open"].iloc[0]).round(2) if len(res) else [],
        "in_position": res["trade"],
    })
    trades = pd.DataFrame(log, columns=["date", "action", "price", "qty", "amount"])
    if not trades.empty:
        trades["date"] = pd.to_datetime(trades["date"]).dt.strftime(fmt)
        trades["price"] = trades["price"].round(2)
        trades["qty"] = trades["qty"].round(8)
        trades["amount"] = (trades["amount"] * capital).round(2)

    ma = done["close"].rolling(s.ma).mean()
    return {"strategy": s, "balance": balance, "trades": trades, "state": state,
            "signal_up": bool(done["close"].iloc[-1] > ma.iloc[-1]),
            "last_close": float(done["close"].iloc[-1]), "last_ma": float(ma.iloc[-1]),
            "price": float(df["close"].iloc[-1]), "candles": df.assign(ma=df["close"].rolling(s.ma).mean()),
            "capital": capital}
