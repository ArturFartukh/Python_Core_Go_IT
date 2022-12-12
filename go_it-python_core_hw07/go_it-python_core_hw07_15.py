def flatten(data):
    if not data:
        return []
    elif isinstance(data[0], list):
        return flatten(data[0]) + flatten(data[1:])
    else:
        return [data[0]] + flatten(data[1:])


# print(flatten([1, 2, [3, 4, [5, 6]], 7]))