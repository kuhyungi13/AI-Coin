"""오피스 화면 가운데 모니터에 그릴 시세·총자산 자료 (paper/tf/market.json).

GitHub Actions가 매시간 회의 코인과 TRAINER 보유 코인의 최근 72시간 1시간봉 종가를 모아 둔다.
회의를 여는 Claude가 이 파일 내용을 오피스 db의 board/market 문서로 그대로 옮긴다.
(오피스 화면은 바깥 사이트에 직접 접속할 수 없어서 이렇게 전달한다.)
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from aicoin.tf_team.trainer import klines_1h

HOURS = 72
EQUITY_POINTS = 240


def _sig(x: float) -> float:
    return float(f"{x:.6g}")


def build(coins: list[str], folder: Path, now: pd.Timestamp | None = None, klines=klines_1h) -> dict:
    now = (now or pd.Timestamp.now(tz="UTC")).tz_convert("UTC").floor("h")
    start = now - pd.Timedelta(hours=HOURS)
    out: dict = {"updated_at": pd.Timestamp.now(tz="UTC").isoformat(timespec="seconds"), "hours": HOURS, "coins": {}}
    for coin in dict.fromkeys(c.upper() for c in coins):
        try:
            df = klines(coin, start, now + pd.Timedelta(hours=1))
        except Exception as e:  # 한 코인이 실패해도 나머지는 그린다
            out["coins"][coin] = {"오류": f"{type(e).__name__}: {e}"}
            continue
        if df.empty:
            out["coins"][coin] = {"오류": "시세 없음"}
            continue
        closes = [_sig(float(v)) for v in df["close"]]
        last = closes[-1]
        ref = closes[-25] if len(closes) >= 25 else closes[0]
        out["coins"][coin] = {"start": df.index[0].isoformat(), "closes": closes, "price": last,
                              "chg_24h": round((last / ref - 1) * 100, 2) if ref else None}
    ep = folder / "trainer" / "equity.csv"
    if ep.exists():
        eq = pd.read_csv(ep).tail(EQUITY_POINTS)
        out["equity"] = [[str(t), round(float(v), 2)] for t, v in zip(eq["time"], eq["equity"])]
    return out


def write(coins: list[str], folder: Path, **kw) -> dict:
    data = build(coins, folder, **kw)
    (folder / "market.json").write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    return data
