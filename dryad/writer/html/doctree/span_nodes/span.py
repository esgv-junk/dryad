import pystache

span_template = """\
<span class="unknown">\
<span class="span_name"><tt>{{span_name}}</tt></span>\
<span class="body_text"><tt>{{body_text}}</tt></span>\
</span>"""

class Span:
    def write(self):
        context = {
            'span_name': self.span_name,
            'body_text': self.body_text
        }
        
        return pystache.render(span_template, context)