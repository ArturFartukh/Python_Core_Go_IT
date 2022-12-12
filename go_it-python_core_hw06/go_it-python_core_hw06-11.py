def get_credentials_users(path):
    with open(path, 'rb') as fh_rb:
        return [access.decode()[: -1] if access.decode()[-1] == '\n' else access.decode() for access in fh_rb.readlines()]


# print(get_credentials_users('/Users/ar4ik/Go_IT_Python/Projects/go_it-python_core_hws/go_it-python_core_hw06/test10.bin'))
