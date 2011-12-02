import os, os.path, traceback
from dryad.parsing import parse_document
from dryad import writer

def is_input_file(filename):
    return (os.path.splitext(filename)[1] == '.txt')

def replace_ext(filename, new_ext):
    dir, name = os.path.split(filename)
    bare_name = os.path.splitext(name)[0]
    return os.path.join(dir, bare_name + '.' + new_ext)

def render_file(in_filename, ignore_rendered=False):
    try:
        exec('import dryad.writer.' + writer.writer_name)
    except ImportError:
        traceback.print_exc()
        return False
    
    new_ext = eval('dryad.writer.' + writer.writer_name + '.extension')
    out_filename = replace_ext(in_filename, new_ext)
    
    needs_update = (
        not os.path.exists(out_filename) or 
        os.path.getmtime(out_filename) < os.path.getmtime(in_filename) or
        ignore_rendered
    )
    
    if needs_update:        
        in_file = open(in_filename, 'r', encoding='utf_8_sig')
        root = parse_document(in_file.readlines())
        in_file.close()
        
        out_file = open(out_filename, 'w', encoding='utf_8')
        out_file.write(writer.str_nodes(root))
        out_file.close()
        
    return needs_update
        
def render_dir(in_path, ignore_rendered=False):
    for (dirpath, dirnames, filenames) in os.walk(in_path):
        for filename in filenames:
            if not is_input_file(filename):
                continue
            in_filename = os.path.join(dirpath, filename)
            has_rendered = \
                render_file(in_filename, ignore_rendered)
            if has_rendered:
                print(in_filename[len(in_path)+1:])
