import re


def find_word(text, word):

    result = bool(re.search(word, text))

    if result:
        first_index = re.search(word, text).span()[0]
        last_index = re.search(word, text).span()[1]
    else:
        first_index = None
        last_index = None

    return {'result': result, 'first_index': first_index, 'last_index': last_index, 'search_string': word, 'string': text}

# print(find_word(
#     "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
#     "Python"))
