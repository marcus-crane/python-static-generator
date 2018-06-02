import os
import shutil

from bundler.settings import Constants


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
    except FileNotFoundError as FileException:
        raise FileException


def init_build_directory(build_dir=Constants.BUILD_DIR,
                         folders=Constants.DIRECTORIES):
    try:
        make_directory(build_dir)
    except FileExistsError:
        shutil.rmtree(build_dir)
        make_directory(build_dir)
    make_directories(build_dir, folders)