class Section:
    def __init__(self, title_nodes, child_nodes):
        self.title_nodes = list(title_nodes)
        self.child_nodes = list(child_nodes)
        
    def get_title_as_string(self):
        def get_span_text(span_node):
            if hasattr(span_node, 'text'):
                return span_node.text
            if hasattr(span_node, 'body_text'):
                return span_node.body_text
            return ''

        title = ''
        for title_node in self.title_nodes:
            title += get_span_text(title_node) 
        return title
    
def parse_section(block_name, inline_text, body_lines):
    pass
    
span_parsers = [('section', parse_section)]
        