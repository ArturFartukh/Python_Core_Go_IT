from ntpath import join


def format_ingredients(items):
    if len(items) == 1:
        return items[0]
    elif items == []:
        return ""
    else:
        return ", ".join(items[:-1]) + " and " + items[-1]
