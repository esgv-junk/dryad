from dryad.writer import str_nodes, render

toc_entry_list_template = """\
<ol class="toc">
{{{child_lines}}}
</ol>
""" 

toc_entry_template = """\
<li><a href="#{{section_id}}">{{{section_title_text}}}</a></li>
"""

class TableOfContents:
    def write(self):
        entries = self.entries
        if len(entries) == 1: # don't include document title into TOC
            entries = entries[0].child_entries
            
        return render_entry_list(entries)

class TOCEntry:
    def write(self):
        context = {
            'section_id': self.section.section_id,
            'section_title_text': str_nodes(*self.section.title_nodes),
        }
        
        rendered_self = render(toc_entry_template, context)
        
        if (self.child_entries):
            rendered_self += render_entry_list(self.child_entries)
            
        return rendered_self 
                
def render_entry_list(entries):
    context = {
        'child_lines': str_nodes(*entries)
    }
    
    return render(toc_entry_list_template, context)

        
