from utf9k.markdown.classes.base import Base


class Snippet(Base):

    def __init__(self, content):
        super(Snippet, self).__init__(content)

    def _get_metadata(self):
        return {
            'title': self.meta.get('title', ''),
            'lang': self.meta.get('lang', ''),
            'link': self.meta.get('link', '')
        }
