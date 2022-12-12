CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}
for i, n in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(i)] = n
    TRANS[ord(i.upper())] = n.upper()
    


def translate(name):
    return name.translate(TRANS)
    

# print(translate("Олекса Івасюк"))
