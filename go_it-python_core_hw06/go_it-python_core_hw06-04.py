def add_employee_to_file(record, path):
    fh = open(path, 'a')
    fh.write(f'{record}\n')
    fh.close()


# add_employee_to_file('Drake Mikelsson,19',
#                      '/Users/ar4ik/Go_IT_Python/Projects/go_it-python_core_hws/go_it-python_core_hw06/test02.txt')
