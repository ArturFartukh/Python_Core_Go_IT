def game(terra, power):
    for list in terra:
        for i in list:
            if i <= power:
                power += i
            else:
                break
    return power
