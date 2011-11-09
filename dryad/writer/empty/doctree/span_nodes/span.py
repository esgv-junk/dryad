import pystache

span_template = ''

class Span:
    def write(self):
        context = {
        }
        
        return pystache.render(span_template, context)