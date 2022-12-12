def check_date(c_date: str) -> str:
    c_date = c_date.strip()
    for i in c_date:
        if not i.isnumeric():
            splitter = i
            c_date = c_date.split(splitter)
            if len(c_date) == 3:
                if len(c_date[2]) == 4:
                    c_date = c_date[::-1]
                    return '-'.join(c_date)
                elif len(c_date[0]) == 4:
                    return '-'.join(c_date)
            return ''


def split_data(data: str) -> (str, str):
    """Distribution of data by name and phone"""

    s_data = data.strip().split(' ')
    name = s_data[0].title()
    if len(s_data) == 2:
        phone = s_data[1]
        if name[0].isdigit():
            raise ValueError('Wrong name!')
        phone = phone_valid(phone)
        return name, phone
    else:
        phone = ''
        return name, phone


def phone_valid(phone: str) -> str:
    if len(phone) == 13 and phone[0] != '+' and not phone[1:].isdigit():
        raise ValueError('Wrong phone!')
    elif len(phone) == 10 and not phone.isdigit():
        raise ValueError('Wrong phone!')
    elif not 10 <= len(phone) <= 13:
        raise ValueError('Wrong phone!')
    elif len(phone) == 10:
        phone = '+38' + phone
    elif len(phone) == 11:
        phone = '+3' + phone
    elif len(phone) == 10:
        phone = '+38' + phone
    elif len(phone) == 12:
        phone = '+' + phone
    return phone
