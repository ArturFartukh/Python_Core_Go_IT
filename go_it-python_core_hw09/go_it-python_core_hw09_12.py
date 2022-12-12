from functools import reduce


def amount_payment(payment):
    payment = filter(lambda x: x > 0, payment)
    return reduce(lambda x, y: x + y, payment)


# payment = [1, -3, 4]
# print(amount_payment(payment))
