import pystache
from dryad.markup.renderer import *

section_template = """\
<section>
    <title>
{{#title_lines}}
        {{{text}}}
{{/title_lines}}\
{{#child_lines}}
    {{{text}}}
{{/child_lines}}"""

class Section:
    def write(self):
        context = {
            'title_lines': pystache_lines(render_nodes(*self.title_nodes)),
            'child_lines': pystache_lines(render_nodes(*self.child_nodes))
        }
        
        return pystache.render(section_template, context)
