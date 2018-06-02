import os
import shutil
import tempfile

import pytest

from bundler import detect


@pytest.fixture()
def generate_files():
    folders = ['text', 'words', 'poop']
    files = ['butts.md', 'heck.js', 'wow.txt']
    base = tempfile.TemporaryDirectory().name
    os.mkdir(base)
    paths = []
    for folder in folders:
        os.mkdir(f"{base}/{folder}")
    for index, file in enumerate(files):
        item = f"{base}/{folders[index]}/{file}"
        with open(item, 'w') as test_file:
            test_file.write('this is a test file')
        paths.append(item)
    return {'base': base, 'paths': paths}


def test_content_scan_no_settings():
    sandbox = generate_files()
    base = sandbox['base']
    expected = []
    content = []
    extensions = []
    actual = detect.content_scan(base, content, extensions)
    assert expected == actual
    shutil.rmtree(base)


def test_content_scan_all():
    sandbox = generate_files()
    base = sandbox['base']
    expected = [f'{base}/text/butts.md', f'{base}/words/heck.js',
                f'{base}/poop/wow.txt']
    content = ['text', 'words', 'poop']
    extensions = ['.md', '.js', '.txt']
    actual = detect.content_scan(base, content, extensions)
    assert expected == actual
    shutil.rmtree(base)


def test_content_no_content_all_ext():
    sandbox = generate_files()
    base = sandbox['base']
    expected = []
    content = []
    extensions = ['.md', '.js', '.txt']
    actual = detect.content_scan(base, content, extensions)
    assert expected == actual
    shutil.rmtree(base)


def test_content_all_content_no_ext():
    sandbox = generate_files()
    base = sandbox['base']
    expected = []
    content = ['text', 'words', 'wow']
    extensions = []
    actual = detect.content_scan(base, content, extensions)
    assert expected == actual
    shutil.rmtree(base)


def test_content_one_folder_one_ext():
    sandbox = generate_files()
    base = sandbox['base']
    expected = [f'{base}/words/heck.js']
    content = ['words']
    extensions = ['.js']
    actual = detect.content_scan(base, content, extensions)
    assert expected == actual
    shutil.rmtree(base)


def test_content_two_folder_three_ext():
    sandbox = generate_files()
    base = sandbox['base']
    expected = [f'{base}/text/butts.md']
    content = ['text', 'poop']
    extensions = ['.md', '.js']
    actual = detect.content_scan(base, content, extensions)
    assert expected == actual
    shutil.rmtree(base)


def test_content_three_folder_two_ext():
    sandbox = generate_files()
    base = sandbox['base']
    expected = [f'{base}/text/butts.md', f'{base}/poop/wow.txt']
    content = ['text', 'words', 'poop']
    extensions = ['.md', '.txt']
    actual = detect.content_scan(base, content, extensions)
    assert expected == actual
    shutil.rmtree(base)