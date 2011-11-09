import pystache

list_template = """\
"""

class List:
    def write(self):
        context = {
        }
        
        return pystache.render(list_template, context)
    
item_template = """\
"""

class ListItem:
    def write(self):
        context = {
        }
        
        return pystache.render(item_template, context)