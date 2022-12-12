from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count
    number_list = [Decimal(number) for number in number_list]

    return sum(number_list)/Decimal(len(number_list))


# print(decimal_average([31, 55, 177, 2300, 1.57], 9))