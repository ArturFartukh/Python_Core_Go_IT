import base64


def encode_data_to_base64(data: list):
    result = []
    for access_base64 in data:
        access_base64 = base64.b64encode(access_base64.encode())
        result.append(access_base64.decode())
    return result


# def get_credentials_base64(path):
#     with open(path, 'rb') as fh_rb:
#         return encode_data_to_base64([access.decode()[: -1] if access.decode()[-1] == '\n' else access.decode() for access in fh_rb.readlines()])


# print(get_credentials_base64(
#     '/Users/ar4ik/Go_IT_Python/Projects/go_it-python_core_hws/go_it-python_core_hw06/test10.bin'))
