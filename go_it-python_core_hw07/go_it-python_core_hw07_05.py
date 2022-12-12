def capital_text(s):
    result = []
    s_split = s.split('.')
    for item in s_split:
        item = item.strip()
        result.append(item[0].upper() + item[1:])
    s = '. '.join(result)

    result = []
    s_split = s.split('!')
    for item in s_split:
        item = item.strip()
        result.append(item[0].upper() + item[1:])
    s = '! '.join(result)

    result = []
    s_split = s.split('?')
    for item in s_split:
        item = item.strip()
        result.append(item[0].upper() + item[1:])
    s = '? '.join(result)

    return s


# print(capital_text('alert. boss! oh'))