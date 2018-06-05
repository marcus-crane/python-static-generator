from markdown.renderer import PostRenderer

import mistune

def test_render_code_no_lang():
    code = "print('hello world')"
    expected = f'<pre class="code"><code>{code}</code></pre>'
    renderer = PostRenderer()
    actual = renderer.block_code(code, None)
    assert expected == actual


def test_renderer_code_with_lang():
    code = "print('hello world')"
    lang = "python"
    expected = f'<pre class="code" data-lang="python"><code>{code}</code></pre>'
    renderer = PostRenderer()
    actual = renderer.block_code(code, lang)
    assert expected == actual


def test_code_render_no_lang_markdown():
    code = """```\nprint("hi")\n```"""
    expected = f'<pre class="code"><code>print("hi")</code></pre>'
    renderer = PostRenderer()
    render = mistune.Markdown(renderer=renderer)
    actual = render(code)
    assert expected == actual


def test_code_render_lang_markdown():
    code = """```javascript\nconsole.log("hello")\n```"""
    expected = f'<pre class="code" data-lang="javascript">' \
               f'<code>console.log("hello")</code></pre>'
    renderer = PostRenderer()
    render = mistune.Markdown(renderer=renderer)
    actual = render(code)
    assert expected == actual