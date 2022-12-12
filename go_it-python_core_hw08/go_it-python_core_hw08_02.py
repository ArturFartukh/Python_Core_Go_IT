from datetime import date


def get_days_in_month(month, year):
    day = 31
    while day > 27:
        try:
            date1 = date(year, month, day)
            return date1.day
        except:
            day -= 1
            continue


# print(get_days_in_month(month=2, year=2024))
