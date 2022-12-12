def make_request(keys, values):
    result = {}
    if len(keys) == len(values):
        for i in range(len(keys)):
            result[keys[i]] = values[i]
    return result


# my_keys = ['IP1', 'IP2', 'IP3']
# my_values = ['85.157.172.253', '85.157.172.210', '85.157.172.175']
# print(make_request(my_keys, my_values))
