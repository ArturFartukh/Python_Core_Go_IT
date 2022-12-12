articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    result = []
    for lib in articles_dict:
        for i in lib.values():
            if letter_case:
                if str(i).find(key) > -1:
                    result.append(lib)
            else:
                if str(i).lower().find(key.lower()) > -1:
                    result.append(lib)

    return result
