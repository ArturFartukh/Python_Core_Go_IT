def sanitize_phone_number(phone):
    phone = "".join(phone.strip().split(" "))

    return "".join([i for i in phone if i not in "(-)+"])
