from pyforge.all import *
from dryad.writer import str_nodes, render


section_template = """\
<div class="section">

<h{{lvl}} id="{{anchor_url}}">
    {{{title_text}}}
    <a class="section_anchor" href="#{{anchor_url}}">&para;</a>
</h{{lvl}}>

{{{child_lines}}}

</div>"""

section_level = 1

class Section:
    def write(self):
        global section_level
        
        section_level += 1
        child_lines = str_nodes(*self.child_nodes, sep='\n\n')
        section_level -= 1
        
        context = {
            'lvl':         section_level,
            'title_text':  str_nodes(*self.title_nodes),
            'anchor_url':  self.section_id,
            'child_lines': child_lines
        }
        
        return render(section_template, context)