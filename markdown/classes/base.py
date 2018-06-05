import re


class Base:
    def __init__(self, post):
        self.meta = self._extract_metadata(post)
        self.content = self._extract_content(post)

    @staticmethod
    def _extract_metadata(post):
        pattern = "---\\n(.+)---\\n"
        m = re.search(pattern, post, re.DOTALL)
        metadata = dict()
        data = m.group(1)
        items = data.split('\n')[:-1]
        for item in items:
            key, value = item.split(':')
            metadata[key.strip()] = value.replace('\n', '').strip()
        return metadata

    @staticmethod
    def _extract_content(post):
        pattern = '---\n\n'
        results = post.split(pattern)
        return results[1]
