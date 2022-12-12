import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    if isinstance(cats[0], Cat):
        return [cat._asdict() for cat in cats]
    elif isinstance(cats[0], dict):
        return [Cat._make(cat.values()) for cat in cats]


# print(convert_list([Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]))
# print(convert_list([{'nickname': 'Mick', 'age': 5, 'owner': 'Sara'}, {'nickname': 'Barsik', 'age': 7, 'owner': 'Olga'}, {'nickname': 'Simon', 'age': 3, 'owner': 'Yura'}]))
