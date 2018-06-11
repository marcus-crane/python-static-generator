from utf9k.markdown.classes.base import Base


class Bite(Base):

    def __init__(self, content):
        super(Bite, self).__init__(content)
        self.template = 'bite.html'
        self.template_list = 'bites.html'

    def _get_metadata(self):
        return {
            'title': self.meta.get('title', ''),
            'date': self.meta.get('date', '')
        }
