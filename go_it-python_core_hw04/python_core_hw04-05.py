def lookup_key(data, value):
    return [key for key, values in data.items() if values == value]
