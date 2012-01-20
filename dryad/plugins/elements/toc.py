from dryad.doctree.section import Section

class TableOfContents:
    def __init__(self, entries):
        self.entries = list(entries)

class TOCEntry:
    def __init__(self, section, child_entries):
        self.section = section
        self.child_entries = list(child_entries)
      
def gather_toc_entry_list(node):
    return [
        TOCEntry(child_node, gather_toc_entry_list(child_node))
        for child_node in node.child_nodes
        if isinstance(child_node, Section)
    ]
    
def make_table_of_contents(root_node):
    return TableOfContents(gather_toc_entry_list(root_node))
    
