import datetime
from typing import List

import simplejson
from dateutil.relativedelta import relativedelta

from src.balance.application.balance_dates import CLOSING_GROUPS
from src.balance.application.balance_dates import compute_cycle_date
from src.balance.application.balance_dates import compute_payment_due_date
from src.balance.application.balance_dates import compute_deliquency_date


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
    balance_dates = []
    for closing_group in CLOSING_GROUPS:
        for base_date, next_base_date in zip(base_dates, base_dates[1:]):
            deliquency_date = compute_deliquency_date(base_date, closing_group)
            cycle_date = compute_cycle_date(deliquency_date)
            payment_due_date = compute_payment_due_date(cycle_date)
            deliquency_date = compute_deliquency_date(next_base_date, closing_group)
            balance_dates.append(
                {
                    "GROUP": closing_group,
                    "YEAR": base_date.year,
                    "MONTH": base_date.month,
                    "CYCLE_DATE": cycle_date.strftime("%Y-%m-%d"),
                    "PAYMENT_DUE_DATE": payment_due_date.strftime("%Y-%m-%d"),
                    "DELIQUENCY_DATE": deliquency_date.strftime("%Y-%m-%d"),
                }
            )
    json = simplejson.dumps(balance_dates, indent=4 * " ")
    with open("balance_dates.json", "w+") as json_file:
        json_file.write(json)


if __name__ == "__main__":
    main()
