import os

from test import utils
from utf9k.cluster import boot
from utf9k.markdown.classes.articles import Article
from utf9k.markdown.classes.projects import Project
from utf9k.markdown.classes.reviews import Review
from utf9k.markdown.classes.snippets import Snippet
from utf9k.markdown.classes.bites import Bite


def test_fill_class_article():
    content = utils.load_fixture(__file__, 'article.md')
    content_type = "article"
    actual = boot.fill_class(content_type, content)
    assert isinstance(actual, Article)


def test_fill_class_project():
    content = utils.load_fixture(__file__, 'project.md')
    content_type = "project"
    actual = boot.fill_class(content_type, content)
    assert isinstance(actual, Project)


def test_fill_class_review():
    content = utils.load_fixture(__file__, 'review.md')
    content_type = "review"
    actual = boot.fill_class(content_type, content)
    assert isinstance(actual, Review)


def test_fill_class_snippet():
    content = utils.load_fixture(__file__, 'snippet.md')
    content_type = "snippet"
    actual = boot.fill_class(content_type, content)
    assert isinstance(actual, Snippet)


def test_fill_class_bite():
    content = utils.load_fixture(__file__, 'bite.md')
    content_type = "bite"
    actual = boot.fill_class(content_type, content)
    assert isinstance(actual, Bite)


def test_load_content_article():
    content_path = os.path.dirname(__file__) + '/fixtures/article.md'
    content_type = "article"
    content = "This is my article. Here are some words."
    title = "This is an article"
    actual = boot.load_content(content_path, content_type)
    assert isinstance(actual, Article)
    assert title == actual.meta['title']
    assert content == actual.content


def test_load_content_project():
    content_path = os.path.dirname(__file__) + '/fixtures/project.md'
    content_type = "project"
    content = "Here is my neato project. I've written some stuff about it."
    description = "This project does this and that. Whoa!"
    actual = boot.load_content(content_path, content_type)
    assert isinstance(actual, Project)
    assert description == actual.meta['description']
    assert content == actual.content


def test_load_content_review():
    content_path = os.path.dirname(__file__) + '/fixtures/review.md'
    content_type = "review"
    content = "Here is a review. Here's what I think!"
    header = "/img/header/gitaroo-man.jpg"
    actual = boot.load_content(content_path, content_type)
    assert isinstance(actual, Review)
    assert header == actual.meta['header']
    assert content == actual.content


def test_load_content_snippet():
    content_path = os.path.dirname(__file__) + '/fixtures/snippet.md'
    content_type = "snippet"
    content = "Here is a thing."
    title = "Appending to an IMAP inbox"
    actual = boot.load_content(content_path, content_type)
    assert isinstance(actual, Snippet)
    assert title == actual.meta['title']
    assert content == actual.content


def test_load_content_bite():
    content_path = os.path.dirname(__file__) + '/fixtures/bite.md'
    content_type = "bite"
    content = "I dunno, good question"
    title = "Is X even a thing?"
    actual = boot.load_content(content_path, content_type)
    assert isinstance(actual, Bite)
    assert title == actual.meta['title']
    assert content == actual.content
