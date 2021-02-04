from abc import ABC
from abc import abstractmethod
from datetime import date
from typing import List


class HolidaysRepository(ABC):
    @abstractmethod
    def get_holidays(self, from_date: date, until_date: date) -> List[date]:
        pass
