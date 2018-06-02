from utf9k.markdown.snippet import Snippet


def test_parse_snippet_data():
    post = "---\ntitle: Cool Snippet\nlang: python\nlink: " \
           "https://example.com\n---\n"
    expected = {'title': 'Cool Snippet', 'lang': 'python',
                'link': 'https://example.com'}
    snippet = Snippet(post)
    actual = snippet._get_metadata()
    assert expected == actual


def test_missing_snippet_data():
    post = "---\ninvalid---\n"
    expected = {'title': '', 'lang': '', 'link': ''}
    snippet = Snippet(post)
    actual = snippet._get_metadata()
    assert expected == actual


def test_only_missing_link():
    post = "---\ntitle: Snip Snip\nlang: go\n---\n"
    expected = {'title': 'Snip Snip', 'lang': 'go', 'link': ''}
    snippet = Snippet(post)
    actual = snippet._get_metadata()
    assert expected == actual