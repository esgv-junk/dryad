class Emph:
    def __init__(self, child_nodes):
        self.child_nodes = list(child_nodes)
        
def parse_emph(span_name, body_text):
    pass
        
span_parsers = [('emph', parse_emph)]