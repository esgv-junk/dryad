import pygments, pygments.lexers, pygments.formatters

def render_code(body_text, language):
    if language == 'code':         # just plain monotype-fonted code
        pygments_lexer = pygments.lexers.TextLexer()

    elif language == 'auto':       # automatically guess language
        pygments_lexer = pygments.lexers.guess_lexer(body_text)

    else:
        pygments_lexer = (         # language has been specified
            pygments.lexers.get_lexer_by_name(language)
        )

    pygments_formatter = pygments.formatters.HtmlFormatter(
        style='trac',
        cssclass='code'
    )

    return pygments.highlight(
        body_text,
        pygments_lexer,
        pygments_formatter
    )


