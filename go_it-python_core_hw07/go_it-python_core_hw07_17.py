def encode(data):
    if not data:
        return []
    result = []
    i = 0
    for i, n in enumerate(data):
        if n == data[0]:
            result.append(n)
        else:
            i = i
            break

    if len(data) != len(result):
        return [result[0], len(result)] + encode(data[i:])

    return [result[0], len(result)]


# print(encode(["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]))
# print(encode("XXXZZXXYYYZZ"))
# print(encode([]))
