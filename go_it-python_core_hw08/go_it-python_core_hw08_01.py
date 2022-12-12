from datetime import datetime


def get_days_from_today(date):
    date = date.split('-')
    date = datetime(year=int(date[0]), month=int(date[1]), day=int(date[2])).date()
    result = datetime.now().date() - date
    return result.days


# print(get_days_from_today("2023-04-09"))
