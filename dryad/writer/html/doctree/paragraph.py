import pystache
from dryad.writer import *

paragraph_template = '<p>{{{child_text}}}</p>'

class Paragraph:
    def write(self):
        context = {
            'child_text': str_nodes(*self.child_nodes, sep='')
        }
        
        return pystache.render(paragraph_template, context)