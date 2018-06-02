from utf9k.markdown.technical import Technical


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
