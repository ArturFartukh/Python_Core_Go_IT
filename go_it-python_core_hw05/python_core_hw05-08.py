grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    result = list()
    count = 1
    for key, value in students.items():
        result.append('{numerate:>4}|{name:<10}|{ball:^5}|{grade:^5}'.format(numerate=count, name=key, ball=value, grade=grades.get(value)))
        count += 1
    return result

# print(formatted_grades({"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}))
