import pystache

strong_template = ''

class Strong:
    def write(self):
        context = {
        }
        
        return pystache.render(strong_template, context)