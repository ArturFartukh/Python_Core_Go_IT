import shutil


def create_backup(path, file_name, employee_residence):
    with open(f'{path}/{file_name}', 'wb') as fh_wb:
        for resident in employee_residence:
            fh_wb.write(
                f'{resident} {employee_residence[resident]}\n'.encode())

    archive_name = shutil.make_archive(
        'backup_folder', 'zip', path)

    return archive_name


# employee_residence = {'Michael': 'Canada', 'John': 'USA', 'Liza': 'Australia'}
# print(create_backup(
#     'go_it-python_core_hw06/', 'test13.bin', employee_residence))
