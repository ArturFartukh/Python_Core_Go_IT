def cost_delivery(quantity, *_, discount=0):
    return (5 + 2 * (quantity - 1)) - (5 + 2 * (quantity - 1)) * discount
