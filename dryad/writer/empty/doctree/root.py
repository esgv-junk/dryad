import pystache

root_template = """\
"""

class Root:
    def write(self):
        context = {
        }
        
        return pystache.render(root_template, context)