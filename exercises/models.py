from dataclasses import dataclass
from datetime import date


@dataclass
class Expense:
    amount: int
    category: str
    spent_on: date

    def is_in_month(self, year: int, month: int) -> bool:
        return year == self.spent_on.year and month == self.spent_on.month