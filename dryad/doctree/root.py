from dryad.doctree.section import Section

class Root:
    def __init__(self, child_nodes):
        self.child_nodes = list(child_nodes)
        
    def get_first_section_title(self):
        for node in self.child_nodes:
            if isinstance(node, Section):
                return node.get_title_as_string()
        return None
    