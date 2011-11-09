from dryad.writer import *
import pystache

block_template = """\
{{#has_lines}}
<div class="unknown">

<span>
    <span class="block_name"><tt>{{block_name}}</tt></span>
    <span class="inline_text"><tt>{{inline_text}}</tt></span>
</span>

<pre>
{{#body_lines}}
{{text}}
{{/body_lines}}
</pre>

</div>

{{/has_lines}}
{{^has_lines}}
<p><span class="unknown">
    <span class="span_name"><tt>{{block_name}}</tt></span>
    <span class="body_text"><tt>{{inline_text}}</tt></span>
</span></p>

{{/has_lines}}
"""

class Block:
    def write(self):
        context = {
            'block_name' : self.block_name,
            'inline_text': self.inline_text,
            'has_lines'  : bool(self.body_lines),    
            'body_lines' : pystache_lines(self.body_lines)
        }
        
        return pystache.render(block_template, context)