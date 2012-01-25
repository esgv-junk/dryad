from dryad.markup.renderer import render_template

image_template = """\
<center>
    <img src="{{path}}" />
</center>"""

class ImageBlock:
    def write(self):
        context = {
            'path': self.path
        }
        
        return render_template(image_template, context)
