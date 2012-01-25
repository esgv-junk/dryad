from dryad.markup.renderer import *
import pystache

image_template = """\
<image>
    <path> {{path}}
"""

class ImageBlock:
    def write(self):
        context = {
            'path' : self.path,
        }
        
        return pystache.render(image_template, context)
