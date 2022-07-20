import configparser
from pathlib import Path


SETTINGS = configparser.ConfigParser()


def init_settings(ini_file: Path):
    global SETTINGS
    if not SETTINGS.sections():
        SETTINGS.read(ini_file)


def new_task_folder(wf, task):
    main_dir = Path(SETTINGS['FOLDERS']['MAIN'])
    task_dir = main_dir.joinpath(wf, task)
    task_dir.mkdir(parents=True)
    return task_dir
