from utf9k.markdown.classes.base import Base


class Article(Base):

    def __init__(self, content):
        super(Article, self).__init__(content)
        self.template = 'article.html'
        self.template_list = 'articles.html'

    def _get_metadata(self):
        return {
            'title': self.meta.get('title', ''),
            'date': self.meta.get('date', ''),
            'excerpt': self.meta.get('excerpt', '')
        }
