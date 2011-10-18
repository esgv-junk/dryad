input_path = r'D:\Dropbox\knowledge\migration'

rebuild = True
rebuild = False

class Root:
    def __init__(self, children):
        self.children = list(children)

import dryad.directives
import dryad.writer
import dryad.writer.html.block_nodes
import dryad.writer.html.inline_nodes

from dryad.parsing import block_parser, line_utils
import dryad.writer.html
import os.path
import os
from dryad import doctree

def replace_ext(filename, ext):
    dir, name = os.path.split(filename)
    name_bare = os.path.splitext(name)[0]
    return os.path.join(dir, name_bare + ext)

def render(in_stream, out_stream):
    lines = iter(cin.readlines())
    root = Root(block_parser.parseBlocks(lines))
    doctree.fixHierarchy(root)
    
    #for node in root.children:
    #    print(node.pformat())
    
    dryad.writer.html.writeHTML(root, outpath)

def render_file(filename):
    out_filename = replace_ext(filename, 'html')
    if (not os.path.exists(out_filename) or 
            os.path.getmtime(out_filename) < os.path.getmtime(filename) or
            rebuild):
        in_stream = open(filename)
        out_stream = open(out_filename)
        render(in_stream, out_stream)
        
def render_dir(path):
    for (dirpath, dirnames, filenames) in os.walk(path):
        for f in filenames:
            if os.path.splitext(f)[1] == '.txt':
                render_file(os.path.join(path, f))

def main():
    render_dir(input_path)
  
if __name__ == "__main__":
    main()
