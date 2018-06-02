import re


class Base:
    def __init__(self, content):
        self.meta = self.extract_metadata(content)

    @staticmethod
    def extract_metadata(post):
        pattern = "---\\n(.+)---\\n"
        m = re.search(pattern, post, re.DOTALL)
        metadata = dict()
        data = m.group(1)
        items = data.split('\n')[:-1]
        for item in items:
            meta = item.split(': ')
            key = meta[0].strip()
            value = meta[1].replace('\n', '')
            metadata[key] = value
        return metadata
