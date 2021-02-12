import datetime
from typing import List

import simplejson
from dateutil.relativedelta import relativedelta

from src.balance.application.balance_dates import CLOSING_GROUPS
from src.balance.application.balance_dates import compute_closing_date
from src.balance.application.balance_dates import compute_payment_date
from src.balance.application.balance_dates import compute_unpaid_date


def get_base_dates(
    from_date: datetime.datetime, to_date: datetime.datetime
) -> List[datetime.datetime]:
    dates = []
    while from_date <= to_date:
        dates.append(from_date.replace(day=1))
        from_date = from_date + relativedelta(months=1)
    return dates


def main():
    now = datetime.datetime.now()
    base_dates = get_base_dates(
        from_date=datetime.datetime(2021, 1, 1),
        to_date=datetime.datetime(2022, 1, 1),
    )
    result = {}
    for closing_group in CLOSING_GROUPS:
        balance_dates = []
        for base_date, next_base_date in zip(base_dates, base_dates[1:]):
            unpaid_date = compute_unpaid_date(base_date, closing_group)
            closing_date = compute_closing_date(unpaid_date)
            payment_date = compute_payment_date(closing_date)
            unpaid_date = compute_unpaid_date(next_base_date, closing_group)
            balance_dates.append(
                {
                    "month": base_date.month,
                    "closing_date": closing_date.strftime("%Y-%m-%d"),
                    "payment_date": payment_date.strftime("%Y-%m-%d"),
                    "unpaid_date": unpaid_date.strftime("%Y-%m-%d"),
                }
            )
        result[closing_group] = balance_dates
    json = simplejson.dumps(result, sort_keys=True, indent=4 * " ")
    with open("balance_dates.json", "w+") as json_file:
        json_file.write(json)


if __name__ == "__main__":
    main()
