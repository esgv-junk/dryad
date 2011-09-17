filename = r'D:\Dropbox\knowledge\migration\prog\lang\c++\1_plain.txt'
inpath = r'D:\Dropbox\knowledge\migration'

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

def build():

    inputDir = 'src/'
    outputDir = 'build/html/'
    builder = 'html'

    for (path, dirs, files) in os.walk(inputDir):
        for f in files:
            path+f
            file = (outputDir+(path-inputDir)+f)
            open(file)
            k_iter(file.readlines)
            try:
                parse
            except:
                repack

# links: full path anchor list, header list
# images: local input and output folders
# customizable strongs

def outName(filepath):
    path = os.path.abspath(filepath)
    dir, name = os.path.split(path)
    name = os.path.splitext(name)[0]
    return os.path.join(dir, name + '.html')

def process(path_to_file):
    lines = iter(open(filepath, encoding = 'utf_8_sig').readlines())
    lines = map(line_utils.Line, lines)

    root = Root(block_parser.parseBlocks(lines))
    doctree.fixHierarchy(root)

    outpath = outName(filepath)
    if (not os.path.exists(outpath)) or \
       (os.path.getmtime(outpath) < os.path.getmtime(filepath)) or \
        rebuild:

        #for node in root.children:
        #    print(node.pformat())
        dryad.writer.html.writeHTML(root, outpath)

def main():
    for (path, dirs, files) in os.walk(inpath):
        for f in files:
            if os.path.splitext(f)[1] == '.txt':
                process(os.path.join(path, f))

if __name__ == "__main__":
    main()