import pygments, pygments.lexers, pygments.formatters

def render_code(body_text, language):
    if language == 'code':         # just plain monotype-fonted code
        lexer = pygments.lexers.TextLexer()
    elif language == 'auto':       # automatically guess language
        try:
            lexer = pygments.lexers.guess_lexer(body_text)
        except TypeError:
            # Pygments has a bug: on certain input, guess_lexer can raise
            # TypeError exception
            lexer = pygments.lexers.TextLexer()
    else:
        # language has been specified
        lexer = pygments.lexers.get_lexer_by_name(language)

    formatter = pygments.formatters.HtmlFormatter(cssclass='code')
    return pygments.highlight(body_text, lexer, formatter)
