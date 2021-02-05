import datetime
import simplejson
from typing import List

from dateutil.relativedelta import relativedelta

from src.balance.application.balance_dates import (
    CLOSING_GROUPS,
    compute_closing_date,
    compute_payment_date,
)


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
    result = {}
    for closing_group in CLOSING_GROUPS:
        closing_dates = []
        for date in base_dates:
            closing_date = compute_closing_date(date, closing_group)
            payment_date = compute_payment_date(closing_date)
            closing_dates.append(
                (closing_date.strftime("%Y-%m-%d"), payment_date.strftime("%Y-%m-%d"))
            )
        result[closing_group] = closing_dates
    json = simplejson.dumps(result, sort_keys=True, indent=4 * " ")
    with open("closing_dates.json", "w+") as json_file:
        json_file.write(json)


main()
