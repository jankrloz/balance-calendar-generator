import datetime
import os
from typing import List

from src.holidays.domain.repositories.holidays_repository import HolidaysRepository
from src.holidays.domain.schemas.holiday import HolidaySchema
from src.kernel.infrastructure.json import read_json_file


class HolidaysJsonRepository(HolidaysRepository):
    def get_holidays(
        self, from_date: datetime.date, until_date: datetime.date
    ) -> List[datetime.date]:
        holidays = HolidaySchema(many=True).load(
            read_json_file(os.path.abspath("./holidays.json"))
        )
        return [h.date for h in holidays]
