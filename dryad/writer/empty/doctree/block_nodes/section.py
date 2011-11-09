import pystache

section_template = """\
"""

class Section:
    def write(self):
        context = {
        }
        
        return pystache.render(section_template, context)