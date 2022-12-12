def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        return " " * ((length - len(string)) // 2) + string
