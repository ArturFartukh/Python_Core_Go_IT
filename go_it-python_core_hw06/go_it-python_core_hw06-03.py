def read_employees_from_file(path):
    fh = open(path, 'r')
    employee_list = []
    for employee in fh.readlines():
        if employee[-1:] == '\n':
            employee_list.append(employee[0: -1])
        else:
            employee_list.append(employee)
    fh.close()
    return employee_list


# print(read_employees_from_file(
#     '/Users/ar4ik/Go_IT_Python/Projects/go_it-python_core_hws/go_it-python_core_hw06/test02.txt'))
