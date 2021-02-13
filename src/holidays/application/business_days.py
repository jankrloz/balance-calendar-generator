import datetime
from typing import Optional

from dateutil import rrule

from src.holidays.infrastructure.holidays_json_repository import HolidaysJsonRepository


def get_next_business_day(
    from_date: datetime.datetime,
    until_date: datetime.datetime,
    time_limit: Optional[datetime.time] = None,
    reverse: bool = False,
) -> datetime.date:
    rs = rrule.rruleset()
    weekdays = [rrule.MO, rrule.TU, rrule.WE, rrule.TH, rrule.FR]
    weekenddays = (rrule.SA, rrule.SU)
    rs.rrule(
        rrule.rrule(
            rrule.DAILY, dtstart=from_date, until=until_date, byweekday=weekdays
        )
    )
    rs.exrule(
        rrule.rrule(
            rrule.WEEKLY, dtstart=from_date, until=until_date, byweekday=weekenddays
        )
    )
    rs = [rule.date() for rule in rs]  # type: ignore
    holidays_repository = HolidaysJsonRepository()
    holidays = holidays_repository.get_holidays(from_date.date(), until_date.date())
    rs = list(filter(lambda date: date not in holidays, rs))  # type: ignore
    next_business_day = rs[0] if not reverse else rs[-1]
    if from_date.date() in rs and time_limit and from_date.time() >= time_limit:
        next_business_day = rs[1] if not reverse else rs[-2]
    return next_business_day
