import pystache

image_template = """\
<center>
    <img src="{{path}}" />
</center>"""

class ImageBlock:
    def write(self):
        context = {
            'path': self.path
        }
        
        return pystache.render(image_template, context)
        