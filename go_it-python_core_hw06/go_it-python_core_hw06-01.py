import re


def total_salary(path):
    fh = open(path, 'r')
    lines = fh.readlines()
    fh.close()
    salary = []
    for line in lines:
        salary.append(float(re.search('\d+', line).group()))
    return sum(salary)


# fh = open('/Users/ar4ik/Go_IT_Python/Projects/go_it-python_core_hws/go_it-python_core_hw06/test01.txt', 'w')
# fh.write('Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000')
# fh.close()
# print(total_salary(
#     '/Users/ar4ik/Go_IT_Python/Projects/go_it-python_core_hws/go_it-python_core_hw06/test01.txt'))
