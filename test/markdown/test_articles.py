from utf9k.markdown.articles import Article


def test_parse_article_data():
    post = "---\ntitle: A good article\ndate: 1970-01-01\nexcerpt: This " \
           "is an article about stuff\n---\n"
    expected = {'title': 'A good article', 'date': '1970-01-01',
                'excerpt': 'This is an article about stuff'}
    article = Article(post)
    actual = article._get_metadata()
    assert expected == actual


def test_missing_article_data():
    post = "---\ninvalid---\n"
    expected = {'title': '', 'date': '', 'excerpt': ''}
    article = Article(post)
    actual = article._get_metadata()
    assert expected == actual


def test_article_missing_half_meta():
    post = "---\ntitle: A good article\ndate: 1970-01-01\n---\n"
    expected = {'title': 'A good article', 'date': '1970-01-01', 'excerpt': ''}
    article = Article(post)
    actual = article._get_metadata()
    assert expected == actual
