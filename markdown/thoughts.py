from markdown.base import Base


class Thought(Base):

    def __init__(self, content):
        super(Thought, self).__init__(content)

    def _get_metadata(self):
        return {
            'title': self.meta.get('title', ''),
            'date': self.meta.get('date', '')
        }
