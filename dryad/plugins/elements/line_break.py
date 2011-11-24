class LineBreakSpan:
    pass

def parse_line_break_span(span_name, inline_text):
    yield LineBreakSpan()

span_parsers = [('br', parse_line_break_span)]