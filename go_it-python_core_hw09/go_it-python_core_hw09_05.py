def format_phone_number(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        if len(result) == 10:
            return f'+38{result}'
        elif len(result) == 12:
            return f'+{result}'
        else:
            return result

    return inner


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


# number_list = ["    +38(050)123-32-34",
#                "     0503451234",
#                "(050)8889900",
#                "38050-111-22-22",
#                "38050 111 22 11   ",
#                ]
#
# for number in number_list:
#     print(sanitize_phone_number(number))
