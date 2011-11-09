import pystache

text_template = ''

class Text:
    def write(self):
        context = {
        }
        
        return pystache.render(text_template, context)