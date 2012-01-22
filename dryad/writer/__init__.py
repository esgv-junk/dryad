import traceback
import pystache
from pyforge.all import *

render = pystache.render

def set_writer(new_writer_name):
    global writer_name, render
    writer_name = new_writer_name
    escape_dict = \
        eval_with_import('dryad.writer.' + new_writer_name + '.escapes')
    pystache.template.escape = \
        lambda string: multiple_replace(str(string), escape_dict)
    
set_writer('debug')

def str_node(node):
    node_class_path = str(type(node))[14:-2]
        
    writer_class_path = 'dryad.writer.{writer_name}.{node_path}'.format(
        writer_name=writer_name,
        node_path=node_class_path
    )
    writer_module = '.'.join(writer_class_path.split('.')[:-1])
    
    try:
        exec('import ' + writer_module)
    except ImportError:
        traceback.print_exc()
        return ''
    
    # 3to2 fix
    return eval(writer_class_path + '.write.im_func(node)') or ''
    #return eval(writer_class_path + '.write(node)') or ''

def str_nodes(*nodes, sep='', writer=None):
    global writer_name
    if writer is not None:
        old_writer = writer_name
        set_writer(writer)
    result = sep.join(str_node(node) for node in nodes)
    if writer is not None:
        set_writer(old_writer)
    return result

def pystache_lines(lines):
    if isinstance(lines, str):
        if lines[-1:] == '\n':
            lines = lines[:-1]
        return pystache_lines(lines.split('\n'))
    else:
        return pystache_list(lines, 'text')
    
def pystache_list(list_, field_name):
    return [{field_name: element} for element in list_]
    
def pystache_files(filenames, field_name):
    return [
        {field_name: open(filename, 'r', encoding='utf_8').read()}
        for filename in filenames
    ]