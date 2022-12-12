from sys import argv
from pathlib import Path
from os import remove
from shutil import move, Error, rmtree, unpack_archive


def main():
    if len(argv) != 2:
        run_skript()
    else:
        run_skript(Path(argv[1]))


def run_skript(home_path=Path('.')) -> None:
    '''Run skript'''
    home_path = Path(home_path)

    paths_list = direct_processing(home_path)

    move_files_to_home_directory(home_path, paths_list)

    remove_catalogs(home_path)

    paths_list = direct_processing(home_path)

    paths_dict = sort_by_extention(paths_list)

    moving_files(home_path, paths_dict)


def direct_processing(work_path: Path, stem='**/*', suffix='.*') -> list:
    '''Returns a list of paths to all files in the work_path directory.'''
    catalog = sorted(work_path.glob(f'{stem}{suffix}'))
    for path in catalog:
        if path.is_dir():
            catalog.remove(path)
    return list(map(str, catalog))


def move_files_to_home_directory(work_path: Path, paths_list: list) -> None:
    '''Moves all files specified in paths_list to directory work_path.
    If the file to be moved to work_path already exists, a copy of it will be created.'''
    for file in paths_list:
        if Path(file).parent == work_path:
            continue
        else:
            try:
                move(file, work_path)
            except Error:
                steam = Path(file).stem
                suffix = Path(file).suffix
                copy_count = list(map(str, Path(work_path).glob(f'{steam}*{suffix }')))
                new_name = f'{steam}_{len(copy_count)}{suffix }'
                move(file, Path(work_path, new_name))


def remove_catalogs(work_path: Path) -> None:
    '''Deletes all directories in work_path.'''
    catalogs_list = work_path.iterdir()
    for catalog in catalogs_list:
        if not Path(catalog).suffix:
            try:
                rmtree(Path(work_path, catalog))
            except NotADirectoryError:
                continue


def sort_by_extention(paths_list: list) -> dict:
    '''Sorts all files in paths_list by extension, and returns a dictionary.'''

    images_extentions = ('.jpeg', '.png', '.jpg', '.svg')
    video_extentions = ('.avi', '.mp4', '.mov', '.mkv')
    doc_extentions = ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx')
    audio_extentions = ('.mp3', '.ogg', '.wav', '.amr', '.m4a')
    archives_extentions = ('.zip', '.gz', '.tar', '.7z', '.rar')

    images_paths = []
    video_paths = []
    doc_paths = []
    audio_paths = []
    archives_paths = []
    unknown_paths = []

    for path in paths_list:
        path = path.lower()
        suffix = Path(path).suffix
        if suffix in images_extentions:
            images_paths.append(path)

        elif suffix in video_extentions:
            video_paths.append(path)

        elif suffix in doc_extentions:
            doc_paths.append(path)

        elif suffix in audio_extentions:
            audio_paths.append(path)

        elif suffix in archives_extentions:
            archives_paths.append(path)

        else:
            unknown_paths.append(path)

    sorted_paths = {
        'images': images_paths,
        'video': video_paths,
        'documents': doc_paths,
        'audio': audio_paths,
        'archives': archives_paths,
        'unknown': unknown_paths
    }
    return sorted_paths


def moving_files(work_path: Path, sorted_paths: dict) -> None:
    '''Creates folders and moves files into them according to their extension.
    If the file is an archive(.zip, .gz, .tar), it will be extracted to a folder with the name of the archive'''
    for folder in sorted_paths.keys():
        Path(work_path, folder).mkdir(exist_ok=True)
        for file in sorted_paths.setdefault(folder):
            name = normalize(Path(file).name)
            suffix = Path(file).suffix
            if folder != 'archives':
                move(file, Path(work_path, folder, name))
            elif suffix in ('.zip', '.gz', '.tar'):
                unpack_archive(file, Path(work_path, folder, Path(name).stem))
                remove(file)
            else:
                move(file, Path(work_path, folder, name))


def normalize(name: str) -> str:
    '''Normalizes the file name'''
    dict = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'е': 'e',
        'ё': 'yo',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'і': 'i',
        'ї': 'ji',
        'й': 'y',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'h',
        'ц': 'ts',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'shch',
        'ъ': 'y',
        'ы': 'y',
        'ь': "'",
        'э': 'e',
        'e': 'e',
        'ю': 'yu',
        'я': 'ya',

        'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Г': 'G',
        'Д': 'D',
        'Е': 'E',
        'Ё': 'Yo',
        'Ж': 'Zh',
        'З': 'Z',
        'И': 'I',
        'І': 'I',
        'Ї': 'Ji',
        'Й': 'Y',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'У': 'U',
        'Ф': 'F',
        'Х': 'H',
        'Ц': 'Ts',
        'Ч': 'Ch',
        'Ш': 'Sh',
        'Щ': 'Shch',
        'Ъ': 'Y',
        'Ы': 'Y',
        'Ь': "'",
        'Э': 'E',
        'Є': 'E',
        'Ю': 'Yu',
        'Я': 'Ya',

        ' ': '_',
        '.': '_',
        ',': '_',
        '!': '_',
        '~': '_',
        '@': '_',
        '#': '_',
        '$': '_',
        '%': '_',
        '^': '_',
        '-': '_',
        '(': '_',
        ')': '_',
        '{': '_',
        '}': '_',
        '\'': '_',
    }
    name_stem = '.'.join(name.split('.')[:-1])
    suffix = str(Path(name).suffix)
    for key in dict:
            name_stem = name_stem.replace(key, dict[key])
    return name_stem + suffix
