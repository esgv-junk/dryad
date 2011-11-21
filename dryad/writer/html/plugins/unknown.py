import pystache

block_template = """\
{{#has_lines}}
<div class="unknown">

{{#span_remap}}
{{>span_template}}
{{/span_remap}}

<pre>
{{{body_lines}}}
</pre>

</div>
{{/has_lines}}
{{^has_lines}}
<p>{{#span_remap}}
{{>span_template}}
{{/span_remap}}</p>
{{/has_lines}}

"""

span_template = """\
<span class="unknown">\
<tt class="span_name">{{span_name}}</tt>\
{{#has_body_text}}\
<tt class="body_text">{{body_text}}</tt>\
{{/has_body_text}}\
{{^has_body_text}}\
<span style="margin-right: 1pt;"></span>\
{{/has_body_text}}\
</span>\
"""

class UnknownBlock:
    def write(self):
        context = {
            'has_lines':     bool(self.body_lines),    
            'body_lines':    '\n'.join(self.body_lines),
            
            'span_template': span_template,
            'span_remap': {
                'span_name':     self.block_name,
                'has_body_text': bool(self.inline_text),
                'body_text':     self.inline_text
            }
        }
        
        return pystache.render(block_template, context)

class UnknownSpan:
    def write(self):
        context = {
            'span_name': self.span_name,
            'has_body_text': bool(self.body_text),
            'body_text': self.body_text
        }
        
        return pystache.render(span_template, context)
    