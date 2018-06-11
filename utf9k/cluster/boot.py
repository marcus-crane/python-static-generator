from utf9k.markdown.classes.articles import Article
from utf9k.markdown.classes.projects import Project
from utf9k.markdown.classes.reviews import Review
from utf9k.markdown.classes.snippets import Snippet
from utf9k.markdown.classes.bites import Bite


def fill_class(content_type, content):

    if content_type == 'article':
        return Article(content)
    if content_type == 'project':
        return Project(content)
    if content_type == 'review':
        return Review(content)
    if content_type == 'snippet':
        return Snippet(content)
    if content_type == 'bite':
        return Bite(content)


def load_content(content_path, content_type):
    with open(content_path, 'r') as file:
        content = file.read()
    return fill_class(content_type, content)
