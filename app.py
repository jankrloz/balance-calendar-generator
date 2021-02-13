import datetime

import simplejson

from src.balance.application.balance_dates import CYCLE_GROUPS
from src.balance.application.balance_dates import compute_cycle_date
from src.balance.application.balance_dates import compute_deliquency_date
from src.balance.application.balance_dates import compute_payment_due_date
from src.balance.domain.balance import Balance
from src.balance.domain.schemas.balance_schema import BalanceSchema
from src.kernel.application.base_dates import get_base_dates
from src.kernel.infrastructure.file import write_file


def main():
    base_dates = get_base_dates(
        from_date=datetime.datetime(2021, 1, 1),
        to_date=datetime.datetime(2022, 1, 1),
    )
    balance_dates = []
    for cycle_group in CYCLE_GROUPS:
        for base_date, next_base_date in zip(base_dates, base_dates[1:]):
            deliquency_date = compute_deliquency_date(base_date, cycle_group)
            cycle_date = compute_cycle_date(deliquency_date)
            payment_due_date = compute_payment_due_date(cycle_date)
            deliquency_date = compute_deliquency_date(next_base_date, cycle_group)
            balance_dates.append(
                Balance(
                    cycle_group=cycle_group,
                    year=base_date.year,
                    month=base_date.month,
                    cycle_date=cycle_date,
                    payment_due_date=payment_due_date,
                    deliquency_date=deliquency_date,
                )
            )
    write_file(
        "balance_dates.json",
        simplejson.dumps(BalanceSchema(many=True).dump(balance_dates), indent=4 * " "),
    )


if __name__ == "__main__":
    main()
