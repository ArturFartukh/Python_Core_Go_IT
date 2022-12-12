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


def get_phone_numbers_for_countries(list_phones):
    numbers_of_Japan = []
    numbers_of_Singapore = []
    numbers_of_Taiwan = []
    numbers_of_Ukreine = []
    for number in list_phones:
        number = sanitize_phone_number(number)
        if number.startswith("81"):
            numbers_of_Japan.append(number)
        elif number.startswith("65"):
            numbers_of_Singapore.append(number)
        elif number.startswith("886"):
            numbers_of_Taiwan.append(number)
        else:
            numbers_of_Ukreine.append(number)
    return {"UA": numbers_of_Ukreine, "JP": numbers_of_Japan, "TW": numbers_of_Taiwan, "SG": numbers_of_Singapore}

# print(get_phone_numbers_for_countries(
#     ["+38067 519 57 83", "+380 67 519 57 80", "+65 67 815 773", "+886 89 258 159", "+81 325 25 124"]))
