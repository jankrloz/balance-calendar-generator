import datetime
from typing import Optional

from dateutil.relativedelta import relativedelta

from src.balance.domain.exceptions import ClosingGroupNotValid
from src.holidays.application.business_days import get_next_business_day

GRUPOS_LIQUIDACION = [1, 3, 10, 14, 21, 30]


def compute_closing_date(
    current_date: datetime.datetime, closing_group: int
) -> Optional[datetime.date]:
    if closing_group not in GRUPOS_LIQUIDACION:
        raise ClosingGroupNotValid

    now = current_date

    first_day_month_date = now.replace(day=1)
    if closing_group == 1:
        return get_next_business_day(
            from_date=first_day_month_date,
            until_date=first_day_month_date + relativedelta(months=1),
        )
    return None
