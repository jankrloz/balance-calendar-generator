import datetime
from typing import List

from dateutil.relativedelta import relativedelta


def get_base_dates(
    from_date: datetime.datetime, to_date: datetime.datetime
) -> List[datetime.datetime]:
    dates = []
    while from_date <= to_date:
        dates.append(from_date.replace(day=1))
        from_date = from_date + relativedelta(months=1)
    return dates
