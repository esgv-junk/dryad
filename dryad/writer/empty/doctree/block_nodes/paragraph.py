import pystache

paragraph_template = """\
"""

class Paragraph:
    def write(self):
        context = {
        }
        
        return pystache.render(paragraph_template, context)