import os


def load_fixture(path, filename):
    with open(f"{os.path.dirname(path)}/fixtures/{filename}") as file:
        return file.read()
