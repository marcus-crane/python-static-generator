from utf9k.markdown.classes.snippets import Snippet
from test import utils


def test_parse_snippet_data():
    post = "---\ntitle: Cool Snippet\nlang: python\nlink: " \
           "https://example.com\n---\n\nA post"
    expected = {'title': 'Cool Snippet', 'lang': 'python',
                'link': 'https://example.com'}
    snippet = Snippet(post)
    actual = snippet._get_metadata()
    assert expected == actual


def test_missing_snippet_data():
    post = "---\ninvalid---\n\nA post"
    expected = {'title': '', 'lang': '', 'link': ''}
    snippet = Snippet(post)
    actual = snippet._get_metadata()
    assert expected == actual


def test_snippet_missing_half_meta():
    post = "---\ntitle: Snip Snip\nlang: go\n---\n\nA post"
    expected = {'title': 'Snip Snip', 'lang': 'go', 'link': ''}
    snippet = Snippet(post)
    actual = snippet._get_metadata()
    assert expected == actual


def test_parse_snippet_from_file():
    post = utils.load_fixture(__file__, 'snippet.md')
    snippet = Snippet(post)
    expected = {'title': 'Appending to an IMAP inbox', 'lang': 'python',
                'link': 'https://github.com/example/butts'}
    actual = snippet._get_metadata()
    assert expected == actual
