def formatted_numbers():

    table = ["|{:^10}|{:^10}|{:^10}|".format('decimal', 'hex', 'binary')]

    for i in range(16):
        table.append("|{:<10}|{:^10}|{:>10}|".format(i, format(i, 'x'), format(i, 'b')))

    return table


# print(formatted_numbers())
