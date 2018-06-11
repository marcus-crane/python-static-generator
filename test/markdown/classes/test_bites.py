from utf9k.markdown.classes.bites import Bite
from test import utils


def test_parse_bite_data():
    post = "---\ntitle: Thonking\ndate: 1970\n---\n\nA post"
    expected = {'title': 'Thonking', 'date': '1970'}
    bite = Bite(post)
    actual = bite._get_metadata()
    assert expected == actual


def test_missing_bite_data():
    post = "---\ninvalid---\n\nA post"
    expected = {'title': '', 'date': ''}
    bite = Bite(post)
    actual = bite._get_metadata()
    assert expected == actual


def test_bite_missing_half_meta():
    post = "---\ntitle: Thonking\n---\n\nA post"
    expected = {'title': 'Thonking', 'date': ''}
    bite = Bite(post)
    actual = bite._get_metadata()
    assert expected == actual


def test_parse_bite_from_file():
    post = utils.load_fixture(__file__, 'bite.md')
    bite = Bite(post)
    expected = {'title': 'Is X even a thing?', 'date': '1970-01-01'}
    actual = bite._get_metadata()
    assert expected == actual
