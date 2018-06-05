from markdown.classes.base import Base
from test import utils


def test_parse_title():
    post = "---\ntitle: This is a title\n---\n"
    expected = {'title': 'This is a title'}
    actual = Base.extract_metadata(post)
    assert expected == actual


def test_parse_date():
    post = "---\ndate: 2018-01-01\n---\n"
    expected = {'date': '2018-01-01'}
    actual = Base.extract_metadata(post)
    assert expected == actual


def test_parse_safe_for_work_true():
    post = "---\nsfw: yes\n---\n"
    expected = {'sfw': 'yes'}
    actual = Base.extract_metadata(post)
    assert expected == actual


def test_parse_safe_for_work_false():
    post = "---\nsfw: no\n---\n"
    expected = {'sfw': 'no'}
    actual = Base.extract_metadata(post)
    assert expected == actual


def test_parse_language():
    post = "---\nlang: go\n---\n"
    expected = {'lang': 'go'}
    actual = Base.extract_metadata(post)
    assert expected == actual


def test_parse_date_and_title():
    post = "---\ntitle: This is a title\ndate: 2018-01-01\n---\n"
    expected = {'title': 'This is a title', 'date': '2018-01-01'}
    actual = Base.extract_metadata(post)
    assert expected == actual


def test_parse_sfw_and_language():
    post = "---\nsfw: yes\nlang: python\n---\n"
    expected = {'sfw': 'yes', 'lang': 'python'}
    actual = Base.extract_metadata(post)
    assert expected == actual


def test_parse_file():
    post = utils.load_fixture(__file__, 'post.md')
    expected = {'title': 'This is a post', 'date': '2018-01-01',
                'sfw': 'no', 'lang': 'go', 'testing': 'yes'}
    actual = Base.extract_metadata(post)
    assert expected == actual
