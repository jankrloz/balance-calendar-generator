from dataclasses import dataclass
from datetime import date


@dataclass
class Balance:
    cycle_group: int
    year: int
    month: int
    cycle_date: date
    payment_due_date: date
    deliquency_date: date
