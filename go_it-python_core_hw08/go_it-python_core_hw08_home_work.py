from datetime import date, timedelta


users = [{'name': 'Artur', 'birthday': date(year=1989, month=3, day=14)},
         {'name': 'Katerina', 'birthday': date(year=1998, month=11, day=10)},
         {'name': 'Vasil', 'birthday': date(year=1995, month=11, day=7)},
         {'name': 'Kira', 'birthday': date(year=1998, month=11, day=6)},
         {'name': 'Valera', 'birthday': date(year=1991, month=11, day=12)},
         {'name': 'Vitalia', 'birthday': date(year=1988, month=11, day=5)},
         {'name': 'Vitia', 'birthday': date(year=1991, month=11, day=10)},
         {'name': 'Dima', 'birthday': date(year=1997, month=11, day=9)},
         {'name': 'Anna', 'birthday': date(year=2001, month=11, day=11)}
         ]


def get_birthdays_per_week(users_list: list) -> None:

    result = {}
    count = start_index()

    for _ in range(7):
        interval = timedelta(days=count)
        week_day = date.today() + interval
        day = week_day.strftime('%A')
        for user in users_list:
            name = user['name']
            birthday = user['birthday'].replace(year=date.today().year)
            if birthday == week_day:
                if day not in ('Saturday', 'Sunday'):
                    result.setdefault(day, [])
                    result[day].append(name)
                else:
                    result.setdefault('Monday', [])
                    result['Monday'].append(name)
        count += 1

    print_birthday(result)


def start_index() -> int:
    week_day = date.today()
    day = week_day.strftime('%A')

    if day == 'Sunday':
        count = -1
    elif day == 'Monday':
        count = -2
    else:
        count = 0

    return count


def print_birthday(birth_dict: dict) -> None:

    for day_of_week in birth_dict.keys():
        print_result = f'{day_of_week}: '
        for name in birth_dict[day_of_week]:
            print_result += f'{name}, '
        print(f'{print_result}\b\b')



get_birthdays_per_week(users)