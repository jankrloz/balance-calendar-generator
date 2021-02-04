import datetime
from typing import List

from dateutil.relativedelta import relativedelta

from src.balance.application.balance_dates import compute_closing_date


def get_dates_list(
    from_date: datetime.datetime, to_date: datetime.datetime
) -> List[datetime.datetime]:
    dates = []
    while from_date < to_date:
        dates.append(from_date.replace(day=1))
        from_date = from_date + relativedelta(months=1)
    return dates


def main():
    now = datetime.datetime.now()
    base_dates = get_dates_list(
        from_date=now - relativedelta(years=1),
        to_date=now + relativedelta(years=1),
    )
    for date in base_dates:
        print(compute_closing_date(date, 1))


main()
