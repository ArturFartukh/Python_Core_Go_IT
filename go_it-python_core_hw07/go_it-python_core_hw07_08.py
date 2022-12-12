def token_parser(s):
    result = []
    item = ''
    for i in s:
        if i.isnumeric():
            item += i
        elif i in ('+', '-', '*', '/', '(', ')'):
            if item:
                result.append(item)
                item = ''
            result.append(i)
    if item:
        result.append(item)
    return result


# print(token_parser("2+ 34-5 * 3"))