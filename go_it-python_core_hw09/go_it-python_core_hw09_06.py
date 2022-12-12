def generator_numbers(string=""):
    result = ""
    for i in string:
        if i.isnumeric():
            result += i
            continue
        elif result:
            yield int(result)
            result = ""


def sum_profit(string):
    result = list(generator_numbers(string))
    return sum(result)


# print(sum_profit("The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."))
