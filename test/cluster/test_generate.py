import os
import tempfile

import pytest

from utf9k.cluster import generate


def test_generate_create_directory_success():
    folder = 'utf9k_test'
    tempdir = tempfile.TemporaryDirectory()
    directory = f"{tempdir.name}/{folder}"
    actual = generate.make_directory(directory)
    expected = os.path.exists(directory)
    assert expected == actual


def test_generate_create_directory_failure():
    folder = 'utf9k_fail'
    tempdir = tempfile.TemporaryDirectory()
    directory = f"{tempdir.name}/{folder}"
    os.mkdir(directory)
    with pytest.raises(FileExistsError):
        generate.make_directory(directory)


def test_generate_create_directories_success():
    folders = ['test', 'hi']
    tempdir = tempfile.TemporaryDirectory()
    actual = generate.make_directories(tempdir.name, folders)
    assert actual is True
    for folder in folders:
        assert os.path.exists(f"{tempdir.name}/{folder}") is True


def test_generate_create_directories_failure():
    folders = ['test', 'hi']
    directory = 'place_that_does_not_exist'
    with pytest.raises(FileNotFoundError):
        generate.make_directories(directory, folders)


def test_init_build_directory_first_time():
    tempdir = tempfile.TemporaryDirectory()
    build_dir = 'output'
    path = f"{tempdir.name}/{build_dir}"
    folders = ['crap', 'hotdogs']
    generate.init_build_directory(path, folders)
    for folder in folders:
        assert os.path.exists(f"{path}/{folder}")


def test_init_build_directory_overwrite():
    tempdir = tempfile.TemporaryDirectory()
    build_dir = 'build'
    path = f"{tempdir.name}/{build_dir}"
    os.mkdir(path)
    assert os.path.exists(path) is True
    folders = ['poop', 'hah']
    generate.init_build_directory(path, folders)
    for folder in folders:
        assert os.path.exists(f"{path}/{folder}")
