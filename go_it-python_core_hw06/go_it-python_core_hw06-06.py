def recipe_constructor(id, name, ingredients: list):
    return {'id': id, 'name': name, 'ingredients': ingredients}


def get_recipe(path, search_id):
    for recipe_info in path.readlines():
        if recipe_info.split(',')[0] == search_id:
            recipe_info = recipe_info[:-1].split(
                ',') if recipe_info[-1:] == '\n' else recipe_info.split(',')
            return recipe_constructor(recipe_info[0], recipe_info[1], recipe_info[2:])
    return None


with open('/Users/ar4ik/Go_IT_Python/Projects/go_it-python_core_hws/go_it-python_core_hw06/test06.txt', 'r') as fh:
    print(get_recipe(fh, '60b90c3b13067a15887e1ae4'))

# Код для автоперевірки:

# def recipe_constructor(id, name, ingredients: list):
#     return {'id': id, 'name': name, 'ingredients': ingredients}


# def get_recipe(path, search_id):
#     with open(path, 'r') as fh:
#         for recipe_info in fh.readlines():
#             if recipe_info.split(',')[0] == search_id:
#                 recipe_info = recipe_info[:-1].split(
#                     ',') if recipe_info[-1:] == '\n' else recipe_info.split(',')
#                 return recipe_constructor(recipe_info[0], recipe_info[1], recipe_info[2:])
#         return None
