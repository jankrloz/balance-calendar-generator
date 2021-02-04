import datetime

from dateutil.relativedelta import relativedelta


def get_dates_list(from_date: datetime.datetime, to_date: datetime.datetime):
    dates = []
    while from_date < to_date:
        first_day = from_date.replace(day=1)
        dates.append(first_day)
        from_date = from_date + relativedelta(months=1)
    return dates


def main():
    print(
        get_dates_list(from_date=datetime.datetime.now()),
        to_date=datetime.datetime.now() + relativedelta(years=1),
    )


main()
