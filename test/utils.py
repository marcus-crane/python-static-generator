import os


def load_fixture(file, filename):
    with open(f"{os.path.dirname(file)}/fixtures/{filename}") as file:
        return file.read()