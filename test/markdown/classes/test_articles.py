from utf9k.markdown.classes.articles import Article
from test import utils


def test_parse_article_data():
    post = "---\ntitle: A good article\ndate: 1970-01-01\nexcerpt: This " \
           "is an article about stuff\n---\n\nA post"
    expected = {'title': 'A good article', 'date': '1970-01-01',
                'excerpt': 'This is an article about stuff'}
    article = Article(post)
    actual = article._get_metadata()
    assert expected == actual


def test_missing_article_data():
    post = "---\ninvalid---\n\nA post"
    expected = {'title': '', 'date': '', 'excerpt': ''}
    article = Article(post)
    actual = article._get_metadata()
    assert expected == actual


def test_article_missing_half_meta():
    post = "---\ntitle: A good article\ndate: 1970-01-01\n---\n\nA post"
    expected = {'title': 'A good article', 'date': '1970-01-01', 'excerpt': ''}
    article = Article(post)
    actual = article._get_metadata()
    assert expected == actual


def test_parse_article_from_file():
    post = utils.load_fixture(__file__, 'article.md')
    article = Article(post)
    expected = {'title': 'This is an article', 'date': '1970-01-01',
                'excerpt': 'I could have a short line here that gives an '
                           'idea what this is about to the reader'}
    actual = article._get_metadata()
    assert expected == actual
