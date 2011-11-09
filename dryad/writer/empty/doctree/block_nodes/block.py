import pystache

block_template = """\
"""

class Block:
    def write(self):
        context = {
        }
        
        return pystache.render(block_template, context)