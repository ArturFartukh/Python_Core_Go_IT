from random import randrange


def get_numbers_ticket(min, max, quantity):
    if min > 0 and max <= 1000 and min < quantity < max:
        numbers = set()
        while len(numbers) < quantity:
            numbers.add(randrange(min, max + 1))
        return sorted(numbers)
    else:
        return []


# print(get_numbers_ticket(1, 36, 8))