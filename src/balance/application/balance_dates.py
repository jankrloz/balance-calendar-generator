import datetime
from typing import Optional

from dateutil.relativedelta import relativedelta

from src.balance.domain.exceptions import ClosingGroupNotValid
from src.holidays.application.business_days import get_next_business_day

CYCLE_GROUPS = [1, 3, 10, 17, 24, 30]


def compute_deliquency_date(
    current_date: datetime.datetime, cycle_group: int
) -> Optional[datetime.date]:
    if cycle_group not in CYCLE_GROUPS:
        raise ClosingGroupNotValid

    now = current_date

    first_day_month_date = now.replace(day=1)
    first_day_next_month_date = first_day_month_date + relativedelta(months=1)
    if cycle_group in (1, 3, 30):
        return get_next_business_day(
            from_date=first_day_month_date,
            until_date=first_day_month_date + relativedelta(months=1),
        )
    base_date = first_day_month_date.replace(day=cycle_group - 1)
    return get_next_business_day(
        from_date=base_date, until_date=base_date + relativedelta(months=1)
    )


def compute_cycle_date(deliquency_date: datetime.date):
    deliquency_date = datetime.datetime.combine(
        deliquency_date, datetime.datetime.min.time()
    )
    return get_next_business_day(
        from_date=deliquency_date + relativedelta(days=1),
        until_date=deliquency_date + relativedelta(months=1),
    )


def compute_payment_due_date(cycle_date: datetime.date) -> datetime.date:
    cycle_date = datetime.datetime.combine(cycle_date, datetime.datetime.min.time())
    return get_next_business_day(
        from_date=cycle_date, until_date=cycle_date + relativedelta(days=20)
    )
