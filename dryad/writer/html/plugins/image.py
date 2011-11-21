import pystache

image_template = """\
<div class="image">
    <img src="{{path}}" />
</div>

"""

class ImageBlock:
    def write(self):
        context = {
            'path': self.path
        }
        
        return pystache.render(image_template, context)
        