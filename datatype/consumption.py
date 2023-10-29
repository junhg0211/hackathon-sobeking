from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Consumption:
    consumption_id: int
    user_id: int
    card_id: int
    consume_at: datetime
    content: str
    amount: int

    @staticmethod
    def get(row):
        return Consumption(*row)

    def jsonify(self):
        return asdict(self)
