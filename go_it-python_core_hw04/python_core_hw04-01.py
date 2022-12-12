def amount_payment(payment):
    return sum(i for i in payment if i > 0)
