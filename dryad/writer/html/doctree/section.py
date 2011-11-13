import urllib.parse
import pystache
from pyforge.str_utils import *
from dryad.writer import *


section_template = """\
<div class="section">

<h{{lvl}} id="{{anchor_url}}">
    {{{title_text}}}
    <a class="section_anchor" href="#{{anchor_url}}">&para;</a>
</h{{lvl}}>


{{#child_lines}}
{{{text}}}
{{/child_lines}}
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
            'lvl':         section_level,
            'title_text':  str_nodes(*self.title_nodes),
            #'anchor_url':  urllib.parse.quote(self.get_title_as_string()),
            'anchor_url':  to_id(self.get_title_as_string()),
            'child_lines': child_lines
        }
        
        return pystache.render(section_template, context)