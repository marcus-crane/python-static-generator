from markdown.classes.base import Base
from test import utils


def test_parse_title():
    post = "---\ntitle: This is a title\n---\n"
    expected = {'title': 'This is a title'}
    actual = Base._extract_metadata(post)
    assert expected == actual


def test_parse_date():
    post = "---\ndate: 2018-01-01\n---\n"
    expected = {'date': '2018-01-01'}
    actual = Base._extract_metadata(post)
    assert expected == actual


def test_parse_safe_for_work_true():
    post = "---\nsfw: yes\n---\n"
    expected = {'sfw': 'yes'}
    actual = Base._extract_metadata(post)
    assert expected == actual


def test_parse_safe_for_work_false():
    post = "---\nsfw: no\n---\n"
    expected = {'sfw': 'no'}
    actual = Base._extract_metadata(post)
    assert expected == actual


def test_parse_language():
    post = "---\nlang: go\n---\n"
    expected = {'lang': 'go'}
    actual = Base._extract_metadata(post)
    assert expected == actual


def test_parse_date_and_title():
    post = "---\ntitle: This is a title\ndate: 2018-01-01\n---\n"
    expected = {'title': 'This is a title', 'date': '2018-01-01'}
    actual = Base._extract_metadata(post)
    assert expected == actual


def test_parse_sfw_and_language():
    post = "---\nsfw: yes\nlang: python\n---\n"
    expected = {'sfw': 'yes', 'lang': 'python'}
    actual = Base._extract_metadata(post)
    assert expected == actual


def test_strip_whitespace():
    post = "---\nsfw   :    yes     \n---\n"
    expected = {'sfw': 'yes'}
    actual = Base._extract_metadata(post)
    assert expected == actual


def test_condensed_keys():
    post = "---\ntitle:thereisnospace\n---\n"
    expected = {'title': 'thereisnospace'}
    actual = Base._extract_metadata(post)
    assert expected == actual


def test_parse_post():
    post = "---\ntitle: bleh\n---\n\nThis is a post"
    expected = "This is a post"
    actual = Base._extract_content(post)
    assert expected == actual


def test_parse_file_meta():
    post = utils.load_fixture(__file__, 'post.md')
    expected = {'title': 'This is a post', 'date': '2018-01-01',
                'sfw': 'no', 'lang': 'go', 'testing': 'yes'}
    actual = Base._extract_metadata(post)
    assert expected == actual


def test_parse_file_content():
    post = utils.load_fixture(__file__, 'post.md')
    expected = "This part of the post contains all the good stuff!"
    actual = Base._extract_content(post)
    assert expected == actual
