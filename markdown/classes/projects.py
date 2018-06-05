from markdown.classes.base import Base


class Project(Base):

    def __init__(self, content):
        super(Project, self).__init__(content)

    def _get_metadata(self):
        return {
            'title': self.meta.get('title', ''),
            'description': self.meta.get('description', ''),
            'year': self.meta.get('year', ''),
            'lang': self.meta.get('lang', ''),
            'css': self.meta.get('css', ''),
            'js': self.meta.get('js', '')
        }
