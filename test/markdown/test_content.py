from utf9k.markdown import content
from test import utils


def test_parse_title():
    post = "---\ntitle: This is a title\n---\n"
    expected = {'title': 'This is a title'}
    actual = content.extract_metadata(post)
    assert expected == actual


def test_parse_date():
    post = "---\ndate: 2018-01-01\n---\n"
    expected = {'date': '2018-01-01'}
    actual = content.extract_metadata(post)
    assert expected == actual


def test_parse_safe_for_work_true():
    post = "---\nsfw: yes\n---\n"
    expected = {'sfw': True}
    actual = content.extract_metadata(post)
    assert expected == actual


def test_parse_safe_for_work_false():
    post = "---\nsfw: no\n---\n"
    expected = {'sfw': False}
    actual = content.extract_metadata(post)
    assert expected == actual


def test_parse_language():
    post = "---\nlang: go\n---\n"
    expected = {'lang': 'go'}
    actual = content.extract_metadata(post)
    assert expected == actual


def test_parse_date_and_title():
    post = "---\ntitle: This is a title\ndate: 2018-01-01\n---\n"
    expected = {'title': 'This is a title', 'date': '2018-01-01'}
    actual = content.extract_metadata(post)
    assert expected == actual


def test_parse_sfw_and_language():
    post = "---\nsfw: yes\nlang: python\n---\n"
    expected = {'sfw': True, 'lang': 'python'}
    actual = content.extract_metadata(post)
    assert expected == actual


def test_parse_file():
    post = utils.load_fixture(__file__, 'post.md')
    expected = {'title': 'This is a post', 'date': '2018-01-01',
                'sfw': False, 'lang': 'go', 'testing': True}
    actual = content.extract_metadata(post)
    assert expected == actual
