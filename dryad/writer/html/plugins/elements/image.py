from dryad.writer import render

image_template = """\
<center>
    <img src="{{path}}" />
</center>"""

class ImageBlock:
    def write(self):
        context = {
            'path': self.path
        }
        
        return render(image_template, context)
        