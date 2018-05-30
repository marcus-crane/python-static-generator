import os


def make_directory(path):
    try:
        os.mkdir(path)
        return True
    except FileExistsError as FileException:
        raise FileException


def make_directories(path, directories):
    try:
        for directory in directories:
            make_directory(f"{path}/{directory}")
        return True
    except FileExistsError as FileException:
        return FileException

