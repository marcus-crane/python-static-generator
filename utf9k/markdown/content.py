import re

from jinja2 import Environment, PackageLoader, select_autoescape, \
    TemplateNotFound
import yaml

from utf9k.settings import Constants


class Content:
    def __init__(self, content):
        self.meta = self._extract_meta(content)
        self.post = self._extract_content(content)
        self.app_name = Constants.APPLICATION_NAME
        self.template_folder = Constants.TEMPLATES_DIR
        self.template = self.meta['type'] + '.html'
        self.template_list = self.meta['type'] + '_list.html'

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

    def render(self):
        pass

    @staticmethod
    def _extract_meta(post):
        pattern = "---\\n(.+)---\\n"
        m = re.search(pattern, post, re.DOTALL)
        details = m.group(1)
        return yaml.load(details)

    @staticmethod
    def _extract_content(post):
        pattern = '---\n\n'
        results = post.split(pattern)
        return results[1]
