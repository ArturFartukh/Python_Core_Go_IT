def split_list(grade):
    smaller = []
    bigger = []
    for i in grade:
        if i <= sum(grade) / len(grade):
            smaller.append(i)
        else:
            bigger.append(i)
    return (smaller, bigger)
