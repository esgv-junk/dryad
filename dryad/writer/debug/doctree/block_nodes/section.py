from dryad.writer import *
import pystache

section_template = """\
<section>
    <title>
{{#title_lines}}
        {{{text}}}
{{/title_lines}}\
{{#child_lines}}
    {{{text}}}
{{/child_lines}}

"""

class Section:
    def write(self):
        context = {
            'title_lines': pystache_lines(
                str_nodes(*self.title_nodes)
            ),
            'child_lines': pystache_lines(
                str_nodes(*self.child_nodes)
            )
        }
        
        return pystache.render(section_template, context)