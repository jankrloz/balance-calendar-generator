import datetime
from abc import ABC
from abc import abstractmethod
from typing import List


class HolidaysRepository(ABC):
    @abstractmethod
    def get_holidays(
        self, from_date: datetime.date, until_date: datetime.date
    ) -> List[datetime.date]:
        pass
