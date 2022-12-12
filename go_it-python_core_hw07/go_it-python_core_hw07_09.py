def all_sub_lists(data):
    result = [[]]
    i1 = 1
    while i1 <= len(data):
        for i in range(len(data)):
            item = data[i: i + i1]
            if len(item) == i1:
                result.append(item)
        i1 += 1
    return result


# print(all_sub_lists([4, 6, 1, 3]))
