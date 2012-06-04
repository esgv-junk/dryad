class Paragraph:
    def __init__(self, child_nodes):
        self.child_nodes = list(child_nodes)

    doctree = ['child_nodes']

def parse_paragraph(block_name, inline_text, body_lines):
    text = ' '.join(line.strip() for line in body_lines)

    from dryad.markup.parser import parse_spans
    return Paragraph(parse_spans(text))

block_parsers = [(ur'paragraph', parse_paragraph)]
