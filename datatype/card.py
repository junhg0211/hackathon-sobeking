from dataclasses import dataclass, asdict


@dataclass
class Card:
    card_id: int
    name: str
    benefit: str

    @staticmethod
    def get(row):
        return Card(*row)

    def jsonify(self):
        return asdict(self)
