def decode(data):
    if not data:
        return []
    return [data[0]] * data[1] + decode(data[2:])


# print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))
