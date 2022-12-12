def get_cats_info(path):
    keys = ['id', 'name', 'age']
    cats = []
    for cat_info in path.readlines():
        if cat_info[-1:] == '\n':
            cat_info = cat_info[:-1]
            cats.append({key: value for (key, value)
                        in zip(keys, cat_info.split(','))})
        else:
            cats.append({key: value for (key, value)
                        in zip(keys, cat_info.split(','))})
    return cats


with open('/Users/ar4ik/Go_IT_Python/Projects/go_it-python_core_hws/go_it-python_core_hw06/test05.txt', 'r') as fh:
    print(get_cats_info(fh))

# Код для автоперевірки:

# def get_cats_info(path):
#     with open(path, 'r') as fh:
#         keys = ['id', 'name', 'age']
#         cats = []
#         for cat_info in fh.readlines():
#             if cat_info[-1:] == '\n':
#                 cat_info = cat_info[:-1]
#                 cats.append({key: value for (key, value)
#                             in zip(keys, cat_info.split(','))})
#             else:
#                 cats.append({key: value for (key, value)
#                             in zip(keys, cat_info.split(','))})
#         return cats
