import mistune


class PostRenderer(mistune.Renderer):

    def block_code(self, code, lang):
        if not lang:
            code = mistune.escape(code)
            return f'<pre class="code"><code>{code}</code></pre>'
        return f'<pre class="code" data-lang="{lang}"><code>{code}</code></pre>'
