def save_credentials_users(path, users_info):
    with open(path, 'wb') as fh_wb:
        for key in users_info:
            fh_wb.write(f'{key}:{users_info[key]}\n'.encode())


# login_password = {
#     'andry': 'uyro18890D',
#     'steve': 'oppjM13LL9e'
# }

# save_credentials_users('/Users/ar4ik/Go_IT_Python/Projects/go_it-python_core_hws/go_it-python_core_hw06/test10.bin', login_password)
