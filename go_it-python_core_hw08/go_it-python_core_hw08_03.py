from datetime import datetime


def get_str_date(date):
    date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%fZ')
    return date.strftime('%A %d %B %Y')


# print(get_str_date('2021-05-27 17:08:34.149Z'))
