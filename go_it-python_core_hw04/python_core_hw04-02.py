def prepare_data(data):
    data.remove(min(data))
    data.remove(max(data))
    return sorted(data)
