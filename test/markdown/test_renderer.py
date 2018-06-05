from markdown.renderer import PostRenderer

import mistune


def test_render_code_no_lang():
    code = "print('hello world')"
    expected = f'<pre class="code"><code>{code}</code></pre>'
    renderer = PostRenderer()
    actual = renderer.block_code(code, None)
    assert expected == actual


def test_render_code_lang():
    code = "print('hello world')"
    lang = "python"
    expected = f'<pre class="code" data-lang="python">' \
               f'<code>{code}</code></pre>'
    renderer = PostRenderer()
    actual = renderer.block_code(code, lang)
    assert expected == actual


def test_render_code_no_lang_markdown():
    code = """```\nprint("hi")\n```"""
    expected = f'<pre class="code"><code>print("hi")</code></pre>'
    renderer = PostRenderer()
    render = mistune.Markdown(renderer=renderer)
    actual = render(code)
    assert expected == actual


def test_render_code_lang_markdown():
    code = """```javascript\nconsole.log("hello")\n```"""
    expected = f'<pre class="code" data-lang="javascript">' \
               f'<code>console.log("hello")</code></pre>'
    renderer = PostRenderer()
    render = mistune.Markdown(renderer=renderer)
    actual = render(code)
    assert expected == actual


def test_render_blockquote_no_citation():
    quote = "This was a thing someone once said."
    expected = f"<blockquote>{quote}</blockquote>"
    renderer = PostRenderer()
    actual = renderer.block_quote(quote)
    assert expected == actual


def test_render_single_blockquote_markdown():
    quote = "> This is a one line quote from someone."
    expected = f"<blockquote><p>This is a one line quote from someone." \
               f"</p>\n</blockquote>"
    renderer = PostRenderer()
    render = mistune.Markdown(renderer=renderer)
    actual = render(quote)
    assert expected == actual
