from dryad.writer import *
import pystache

paragraph_template = """\
<paragraph>
{{#child_lines}}
    {{{text}}}
{{/child_lines}}"""

class Paragraph:
    def write(self):
        context = {
            'child_lines': pystache_lines(
                str_nodes(*self.child_nodes)
            )
        }
        
        return pystache.render(paragraph_template, context)