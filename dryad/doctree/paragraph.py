class Paragraph:
    def __init__(self, child_nodes):
        self.child_nodes = list(child_nodes)        

def parse_paragraph(block_name, inline_text, body_lines):
    pass

block_parsers = [('paragraph', parse_paragraph)]