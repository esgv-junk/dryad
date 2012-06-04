import pygments, pygments.lexers, pygments.formatters

def render_code_html(body_text, language):
    formatter = pygments.formatters.HtmlFormatter(cssclass='code')

    # just plain monotype-fonted code
    if language == 'code':
        lexer = pygments.lexers.TextLexer()

    # automatically guess language
    elif language == 'auto':
        try:
            lexer = pygments.lexers.guess_lexer(body_text)
        except TypeError:
            # Pygments has a bug: on certain input, guess_lexer can raise
            # TypeError exception
            lexer = pygments.lexers.TextLexer()

    # language has been specified
    else:
        lexer = pygments.lexers.get_lexer_by_name(language)

    return pygments.highlight(body_text, lexer, formatter)
