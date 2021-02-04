from dataclasses import dataclass
from datetime import date


@dataclass
class Holiday:
    holiday_id: int
    country_code: str
    date: date
    description: str
