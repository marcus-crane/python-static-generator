from datetime import date

from jinja2 import Template, TemplateNotFound
import pytest

from utf9k.markdown.content import Content
from test import utils


def test_parse_title():
    post = "---\ntitle: This is a title\n---\n"
    expected = {'title': 'This is a title'}
    actual = Content._extract_meta(post)
    assert expected == actual


def test_parse_date():
    post = "---\ndate: 2018-01-01\n---\n"
    expected = {'date': date(2018, 1, 1)}
    actual = Content._extract_meta(post)
    assert expected == actual


def test_parse_safe_for_work_true():
    post = "---\nsfw: yes\n---\n"
    expected = {'sfw': True}
    actual = Content._extract_meta(post)
    assert expected == actual


def test_parse_safe_for_work_false():
    post = "---\nsfw: no\n---\n"
    expected = {'sfw': False}
    actual = Content._extract_meta(post)
    assert expected == actual


def test_parse_language():
    post = "---\nlang: go\n---\n"
    expected = {'lang': 'go'}
    actual = Content._extract_meta(post)
    assert expected == actual


def test_parse_date_and_title():
    post = "---\ntitle: This is a title\ndate: 2018-01-01\n---\n"
    expected = {'title': 'This is a title', 'date': date(2018, 1, 1)}
    actual = Content._extract_meta(post)
    assert expected == actual


def test_parse_sfw_and_language():
    post = "---\nsfw: yes\nlang: python\n---\n"
    expected = {'sfw': True, 'lang': 'python'}
    actual = Content._extract_meta(post)
    assert expected == actual


def test_strip_whitespace():
    post = "---\nsfw   :    yes     \n---\n"
    expected = {'sfw': True}
    actual = Content._extract_meta(post)
    assert expected == actual


def test_parse_post():
    post = "---\ntitle: bleh\n---\n\nThis is a post"
    expected = "This is a post"
    actual = Content._extract_content(post)
    assert expected == actual


def test_parse_file_meta():
    post = utils.load_fixture(__file__, 'post.md')
    expected = {'type': 'base', 'title': 'This is a post',
                'date': date(2018, 1, 1),
                'sfw': False, 'lang': 'go', 'testing': True}
    actual = Content._extract_meta(post)
    assert expected == actual


def test_parse_file_content():
    post = utils.load_fixture(__file__, 'post.md')
    expected = "This part of the post contains all the good stuff!"
    actual = Content._extract_content(post)
    assert expected == actual


def test_get_template():
    post = utils.load_fixture(__file__, 'post.md')
    base = Content(post)
    base.app_name = "test"
    base.template_folder = "markdown/fixtures"
    base.template = "post.html"
    actual = base._get_template()
    assert isinstance(actual, Template)
    assert "post.html" == actual.name


def test_get_invalid_template():
    post = utils.load_fixture(__file__, 'post.md')
    base = Content(post)
    base.app_name = "test"
    base.template_folder = "markdown/fixtures"
    base.template = "nothing.html"
    with pytest.raises(TemplateNotFound):
        base._get_template()


def test_render_template():
    post = utils.load_fixture(__file__, 'post.md')
    base = Content(post)
    base.app_name = "test"
    base.template_folder = "markdown/fixtures"
    base.template = "post.html"
    expected = utils.load_fixture(__file__, 'post_render.html')
    actual = base._render_template(title=base.meta['title'],
                                   date=base.meta['date'],
                                   content=base.post)
    assert expected == actual


def test_render_template_kwargs():
    post = utils.load_fixture(__file__, 'post.md')
    base = Content(post)
    base.app_name = "test"
    base.template_folder = "markdown/fixtures"
    base.template = "post.html"
    expected = utils.load_fixture(__file__, 'post_render.html')
    data = {'title': base.meta['title'],
            'date': base.meta['date'],
            'content': base.post}
    actual = base._render_template(**data)
    assert expected == actual