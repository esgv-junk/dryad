import pystache

span_template = '<span class="{{span_name}}">{{body_text}}</span>'

class Span:
    def write(self):
        context = {
            'span_name': self.span_name,
            'body_text': self.body_text
        }
        
        return pystache.render(span_template, context)