def write_employees_to_file(employee_list, path):
    fh = open(path, 'w')
    for item in employee_list:
        for employee in item:
            fh.write(f'{employee}\n')
    fh.close()


# write_employees_to_file([['Robert Stivenson,28', 'Alex Denver,30'], [
#                         'Drake Mikelsson,19']], '/Users/ar4ik/Go_IT_Python/Projects/go_it-python_core_hws/go_it-python_core_hw06/test02.txt')
