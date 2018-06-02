from markdown.projects import Project


def test_parse_project_data():
    post = "---\ntitle: Neat\ndescription: A project\nyear: 1970\n" \
           "lang: ruby\ncss: thing.css\njs: stuff.js\n---\n"
    expected = {'title': 'Neat', 'description': 'A project', 'year': '1970',
                'lang': 'ruby', 'css': 'thing.css', 'js': 'stuff.js'}
    project = Project(post)
    actual = project._get_metadata()
    assert expected == actual


def test_missing_project_data():
    post = "---\ninvalid---\n"
    expected = {'title': '', 'description': '', 'year': '',
                'lang': '', 'css': '', 'js': ''}
    project = Project(post)
    actual = project._get_metadata()
    assert expected == actual


def test_project_missing_half_meta():
    post = "---\ntitle: Neat\ndescription: A project\nyear: 1970\n---\n"
    expected = {'title': 'Neat', 'description': 'A project', 'year': '1970',
                'lang': '', 'css': '', 'js': ''}
    project = Project(post)
    actual = project._get_metadata()
    assert expected == actual
