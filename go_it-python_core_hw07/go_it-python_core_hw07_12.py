def file_operations(path, additional_info, start_pos, count_chars):
    with open(path, 'a') as file:
        file.write(additional_info)
    with open(path, 'r') as file:
        file.seek(start_pos)
        result = file.read(count_chars)
    return result
