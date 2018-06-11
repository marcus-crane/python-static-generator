from utf9k.markdown.classes.reviews import Review
from test import utils


def test_parse_review_data():
    post = "---\ntitle: Gitaroo Man\nmedium: videogame\nyear: 1970\n" \
           "header: /img/header/gitaroo-man.jpg\n---\n\nA post"
    expected = {'title': 'Gitaroo Man', 'medium': 'videogame', 'year': '1970',
                'header': '/img/header/gitaroo-man.jpg'}
    review = Review(post)
    actual = review._get_metadata()
    assert expected == actual


def test_missing_review_data():
    post = "---\ninvalid---\n\nA post"
    expected = {'title': '', 'medium': '', 'year': '', 'header': ''}
    review = Review(post)
    actual = review._get_metadata()
    assert expected == actual


def test_review_missing_half_meta():
    post = "---\ntitle: Gitaroo Man\nmedium: videogame\n---\n\nA post"
    expected = {'title': 'Gitaroo Man', 'medium': 'videogame',
                'year': '', 'header': ''}
    review = Review(post)
    actual = review._get_metadata()
    assert expected == actual


def test_parse_project_from_file():
    post = utils.load_fixture(__file__, 'review.md')
    review = Review(post)
    expected = {'title': 'Gitaroo Man', 'medium': 'videogame',
                'year': '1970', 'header': '/img/header/gitaroo-man.jpg'}
    actual = review._get_metadata()
    assert expected == actual
