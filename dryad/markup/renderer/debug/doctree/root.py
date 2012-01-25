from dryad.markup.renderer import *

class Root:
    def write(self):
        return render_nodes(*self.child_nodes)
