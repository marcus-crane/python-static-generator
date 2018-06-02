import os


def load_fixture(file, path):
    with open(f"{os.path.dirname(file)}/fixtures/{path}") as file:
        return file.read()
