from markdown.thoughts import Thought
from test import utils


def test_parse_thought_data():
    post = "---\ntitle: Thonking\ndate: 1970\n---\n"
    expected = {'title': 'Thonking', 'date': '1970'}
    thought = Thought(post)
    actual = thought._get_metadata()
    assert expected == actual


def test_missing_thought_data():
    post = "---\ninvalid---\n"
    expected = {'title': '', 'date': ''}
    thought = Thought(post)
    actual = thought._get_metadata()
    assert expected == actual


def test_thought_missing_half_meta():
    post = "---\ntitle: Thonking\n---\n"
    expected = {'title': 'Thonking', 'date': ''}
    thought = Thought(post)
    actual = thought._get_metadata()
    assert expected == actual


def test_parse_thought_from_file():
    post = utils.load_fixture(__file__, 'thought.md')
    thought = Thought(post)
    expected = {'title': 'Is X even a thing?', 'date': '1970-01-01'}
    actual = thought._get_metadata()
    assert expected == actual