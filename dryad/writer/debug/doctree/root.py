from dryad.writer import *

class Root:
    def write(self):
        return str_nodes(*self.child_nodes)
        