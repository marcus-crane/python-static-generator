from markdown.classes.projects import Project
from test import utils


def test_parse_project_data():
    post = "---\ntitle: Neat\ndescription: A project\nyear: 1970\n" \
           "lang: ruby\ncss: thing.css\njs: stuff.js\n---\n\nA post"
    expected = {'title': 'Neat', 'description': 'A project', 'year': '1970',
                'lang': 'ruby', 'css': 'thing.css', 'js': 'stuff.js'}
    project = Project(post)
    actual = project._get_metadata()
    assert expected == actual


def test_missing_project_data():
    post = "---\ninvalid---\n\nA post"
    expected = {'title': '', 'description': '', 'year': '',
                'lang': '', 'css': '', 'js': ''}
    project = Project(post)
    actual = project._get_metadata()
    assert expected == actual


def test_project_missing_half_meta():
    post = "---\ntitle: Neat\ndescription: A project\nyear: 1970\n---\n\nHello"
    expected = {'title': 'Neat', 'description': 'A project', 'year': '1970',
                'lang': '', 'css': '', 'js': ''}
    project = Project(post)
    actual = project._get_metadata()
    assert expected == actual


def test_parse_project_from_file():
    post = utils.load_fixture(__file__, 'project.md')
    project = Project(post)
    expected = {'title': 'My cool Python project',
                'description': 'This project does this and that. Whoa!',
                'year': '1970', 'lang': 'python',
                'css': '/css/my-cool-python-project.css',
                'js': '/js/my-cool-python-project.js'}
    actual = project._get_metadata()
    assert expected == actual
