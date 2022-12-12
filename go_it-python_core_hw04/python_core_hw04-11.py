def is_valid_password(password):
    if len(password) == 8:
        lenght = True
    else:
        return False
    up_char = False
    low_char = False
    is_digit = False
    for i in password:
        if i.isalpha():
            if i.isupper():
                up_char = True
            elif i.islower():
                low_char = True
        elif i.isdigit():
            is_digit = True
    return all([up_char, low_char, is_digit])
