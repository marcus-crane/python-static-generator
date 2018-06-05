from markdown.classes.technical import Technical
from test import utils


def test_parse_technical_data():
    post = "---\ntitle: A techy post\ndate: 1970\nlang: swift\n---\n"
    expected = {'title': 'A techy post', 'date': '1970', 'lang': 'swift'}
    technical = Technical(post)
    actual = technical._get_metadata()
    assert expected == actual


def test_missing_technical_data():
    post = "---\ninvalid---\n"
    expected = {'title': '', 'date': '', 'lang': ''}
    technical = Technical(post)
    actual = technical._get_metadata()
    assert expected == actual


def test_technical_missing_half_meta():
    post = "---\ntitle: A techy post\nlang: swift\n---\n"
    expected = {'title': 'A techy post', 'date': '', 'lang': 'swift'}
    technical = Technical(post)
    actual = technical._get_metadata()
    assert expected == actual


def test_parse_technical_from_file():
    post = utils.load_fixture(__file__, 'technical.md')
    technical = Technical(post)
    expected = {'title': 'Setting up a technical thing',
                'date': '1970-01-01', 'lang': 'python'}
    actual = technical._get_metadata()
    assert expected == actual
