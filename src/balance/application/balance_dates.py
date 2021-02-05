import datetime
from typing import Optional

from dateutil.relativedelta import relativedelta

from src.balance.domain.exceptions import ClosingGroupNotValid
from src.holidays.application.business_days import get_next_business_day

CLOSING_GROUPS = [1, 3, 10, 14, 21, 30]


def compute_closing_date(
    current_date: datetime.datetime, closing_group: int
) -> Optional[datetime.date]:
    if closing_group not in CLOSING_GROUPS:
        raise ClosingGroupNotValid

    now = current_date

    first_day_month_date = now.replace(day=1)
    first_day_next_month_date = first_day_month_date + relativedelta(months=1)
    last_day_month_date = first_day_next_month_date - relativedelta(days=1)
    if closing_group == 1:
        return get_next_business_day(
            from_date=first_day_month_date,
            until_date=first_day_month_date + relativedelta(months=1),
        )
    if closing_group == 30:
        return get_next_business_day(
            from_date=first_day_month_date, until_date=last_day_month_date, reverse=True
        )
    base_date = first_day_month_date.replace(day=closing_group)
    return get_next_business_day(
        from_date=base_date,
        until_date=base_date + relativedelta(months=1),
        reverse=True,
    )


def compute_payment_date(closing_date: datetime.date) -> datetime.date:
    return closing_date + relativedelta(days=20)