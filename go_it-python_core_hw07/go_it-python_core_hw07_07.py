def data_preparation(list_data):
    result = []
    for item in list_data:
        if len(item) > 2:
            item.remove(min(item))
            item.remove(max(item))
        result.extend(item)
        result.sort(reverse=True)
    return result


print(data_preparation([[1,2,3],[3,4], [5,6]]))