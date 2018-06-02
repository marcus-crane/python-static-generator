from utf9k.markdown.base import Base


class Review(Base):

    def __init__(self, content):
        super(Review, self).__init__(content)

    def _get_metadata(self):
        return {
            'title': self.meta.get('title', ''),
            'medium': self.meta.get('medium', ''),
            'year': self.meta.get('year', ''),
            'header': self.meta.get('header', '')
        }
