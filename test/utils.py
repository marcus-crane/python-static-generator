import os


def load_fixture(file, path):
    with open(f"{os.path.dirname(file)}/{path}") as file:
        return file.read()