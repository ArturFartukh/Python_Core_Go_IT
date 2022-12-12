def sanitize_file(source, output):
    with open(source, 'r') as fh_r:
        with open(output, 'w') as fh_w:
            sanitize_line = ''
            for line in fh_r.readlines():
                for char in line:
                    if char.isdigit():
                        continue
                    else:
                        sanitize_line += char
            fh_w.write(f'{sanitize_line}')


# sanitize_file('/Users/ar4ik/Go_IT_Python/Projects/go_it-python_core_hws/go_it-python_core_hw06/test06.txt', '/Users/ar4ik/Go_IT_Python/Projects/go_it-python_core_hws/go_it-python_core_hw06/test07.txt')
