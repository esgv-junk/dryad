from dryad.writer import *
import pystache

section_template = """\
<div class="h{{lvl}}-outer">

<h{{lvl}}>{{{title_text}}}</h{{lvl}}>

<div class="h{{lvl}}-inner">

{{#child_lines}}
{{{text}}}
{{/child_lines}}
</div>

</div>

"""

section_level = 1

class Section:
    def write(self):
        global section_level
        
        section_level += 1
        child_lines = pystache_lines(str_nodes(*self.child_nodes))
        section_level -= 1
        
        context = {
            'lvl'        : section_level,
            'title_text' : str_nodes(*self.title_nodes),
            'child_lines': child_lines
        }
        
        return pystache.render(section_template, context)