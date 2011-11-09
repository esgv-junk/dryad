import pystache

emph_template = ''

class Emph:
    def write(self):
        context = {
        }
        
        return pystache.render(emph_template, context)