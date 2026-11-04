"""TRAINER 로스컷 감시 (무료, API 키 불필요, 실제 주문 없음). GitHub Actions가 짧은 간격으로 돌린다.

보유 코인의 1분봉 저가가 로스컷 가격에 닿았으면 회의·시간봉을 기다리지 않고 바로 청산한다.
보유 코인이 없으면 아무것도 하지 않는다.
"""

from pathlib import Path

from aicoin.tf_team import trainer

FOLDER = Path("paper/tf")

if __name__ == "__main__":
    sm = trainer.watch(FOLDER)
    print("로스컷 청산 있음 → 모의 계좌 갱신" if sm else "로스컷 없음")
