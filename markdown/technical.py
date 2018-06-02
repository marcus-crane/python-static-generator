from markdown.base import Base


class Technical(Base):

    def __init__(self, content):
        super(Technical, self).__init__(content)

    def _get_metadata(self):
        return {
            'title': self.meta.get('title', ''),
            'date': self.meta.get('date', ''),
            'lang': self.meta.get('lang', '')
        }
