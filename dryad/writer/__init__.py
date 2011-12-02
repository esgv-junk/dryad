import traceback
from dryad.writer.template import make_renderer

def set_writer(new_writer_name):
    global writer_name, render
    writer_name = new_writer_name
    render = make_renderer()
    
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
    
    return eval(writer_class_path + '.write(node)') or ''

def str_nodes(*nodes, sep=''):
    return sep.join(str_node(node) for node in nodes)

def pystache_lines(lines):
    if isinstance(lines, str):
        if lines[-1:] == '\n':
            lines = lines[:-1]
        return pystache_lines(lines.split('\n'))
    else:
        return pystache_list(lines, 'text')
    
def pystache_list(list_, field_name):
    return [{field_name: element} for element in list_]