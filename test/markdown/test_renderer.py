from markdown.renderer import PostRenderer


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