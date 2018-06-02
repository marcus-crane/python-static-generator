from utf9k.markdown.reviews import Review


def test_parse_review_data():
    post = "---\ntitle: Gitaroo Man\nmedium: videogame\nyear: 1970\n" \
           "header: /img/header/gitaroo-man.jpg\n---\n"
    expected = {'title': 'Gitaroo Man', 'medium': 'videogame', 'year': '1970',
                'header': '/img/header/gitaroo-man.jpg'}
    review = Review(post)
    actual = review._get_metadata()
    assert expected == actual


def test_missing_review_data():
    post = "---\ninvalid---\n"
    expected = {'title': '', 'medium': '', 'year': '', 'header': ''}
    review = Review(post)
    actual = review._get_metadata()
    assert expected == actual


def test_review_missing_half_meta():
    post = "---\ntitle: Gitaroo Man\nmedium: videogame\n---\n"
    expected = {'title': 'Gitaroo Man', 'medium': 'videogame',
                'year': '', 'header': ''}
    review = Review(post)
    actual = review._get_metadata()
    assert expected == actual
