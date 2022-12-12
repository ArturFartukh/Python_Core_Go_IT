import shutil


def unpack(archive_path, path_to_unpack):
    shutil.unpack_archive(archive_path, path_to_unpack)


# unpack('backup_folder.zip',
#        'go_it-python_core_hw06/test14/')
