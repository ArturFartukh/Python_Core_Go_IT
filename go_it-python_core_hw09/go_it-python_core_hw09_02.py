DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    if "discount" in customer:
        discount = customer["discount"]
    else:
        discount = DEFAULT_DISCOUNT

    return price * (1 - discount)
