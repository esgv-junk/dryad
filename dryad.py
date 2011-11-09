input_path = r'D:\Dropbox\knowledge\migration'

rebuild = True
#rebuild = False

testing = True
testing = False

import os.path
import os
from dryad.parsing import parse_document
from dryad.writer import *
import dryad.writer


def replace_ext(filename, ext):
    dir, name = os.path.split(filename)
    name_bare = os.path.splitext(name)[0]
    return os.path.join(dir, name_bare + '.' + ext)

def render(in_stream, out_stream):
    test_lines = iter(in_stream.readlines())
    root = parse_document(test_lines)
    
    set_writer('html')    
    print(str_nodes(root), file=out_stream)

def render_file(filename):
    out_filename = replace_ext(filename, 'html')
    if (not os.path.exists(out_filename) or 
            os.path.getmtime(out_filename) < os.path.getmtime(filename) or
            rebuild):
        
        print(filename[len(input_path)+1:])
        
        in_stream = open(filename, 'r', encoding='utf_8_sig')
        out_stream = open(out_filename, 'w', encoding='utf_8')
        
        render(in_stream, out_stream)
        
        in_stream.close()
        out_stream.close()
        
def render_dir(path):
    for (dirpath, dirnames, filenames) in os.walk(path):
        for f in filenames:
            if os.path.splitext(f)[1] == '.txt':
                render_file(os.path.join(dirpath, f))

input_file = 'test.txt'

def main():
    if not testing:
        render_dir(input_path)
        print('Done')
    else:
        test_lines = iter(open(input_file).readlines())
        root = parse_document(test_lines)
        
        set_writer('debug')    
        print(str_nodes(root))
        print(str_nodes(root), file=open('test.html', 'w', encoding="utf-8"))
    
if __name__ == "__main__":
    main()
