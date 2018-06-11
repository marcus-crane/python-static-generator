import re

from jinja2 import Environment, PackageLoader, select_autoescape, \
    TemplateNotFound

from utf9k.settings import Constants


class Base:
    def __init__(self, post):
        self.meta = self._extract_metadata(post)
        self.content = self._extract_content(post)
        self.app_name = Constants.APPLICATION_NAME
        self.template_folder = Constants.TEMPLATES_DIR

    def _get_template(self):
        try:
            env = Environment(
                loader=PackageLoader(self.app_name, self.template_folder),
                autoescape=select_autoescape(['html'])
            )
            return env.get_template(self.template)
        except TemplateNotFound as error:
            raise error

    def _render_template(self, **kwargs):
        template = self._get_template()
        return template.render(**kwargs)

    @staticmethod
    def _extract_metadata(post):
        pattern = "---\\n(.+)---\\n"
        m = re.search(pattern, post, re.DOTALL)
        metadata = dict()
        data = m.group(1)
        items = data.split('\n')[:-1]
        for item in items:
            key, value = item.split(':', 1)
            metadata[key.strip()] = value.replace('\n', '').strip()
        return metadata

    @staticmethod
    def _extract_content(post):
        pattern = '---\n\n'
        results = post.split(pattern)
        return results[1]
