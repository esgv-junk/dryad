from dryad.doctree import walk_doctree

def default_emit(text):
    raise NotImplementedError('Writer not running')

def default_emit_raw(text):
    raise NotImplementedError('Writer not running')

def set_emitters(new_writer_name, new_emit, new_emit_raw):
    global emit, emit_raw, running_writer_name
    emit = new_emit
    emit_raw = new_emit_raw
    running_writer_name = new_writer_name

def reset_emitters():
    set_emitters(None, default_emit, default_emit_raw)
    
# set emitters to initial values
reset_emitters()

def run_writer(writer_name, root_node, emit, emit_raw):
    set_emitters(writer_name, emit, emit_raw)
    write_nodes(root_node)
    reset_emitters()
    
def write_nodes(*nodes):
    
    def on_enter_node(node):
        global running_writer_name
        
        if (hasattr(node, 'writers') and
            running_writer_name in node.writers):
            
            current_writer = node.writers[running_writer_name]
            if isinstance(current_writer, tuple):
                current_writer[0](node)
            else:
                current_writer(node)
    
    def on_exit_node(node):
        global running_writer_name
        
        if (hasattr(node, 'writers') and
            running_writer_name in node.writers):
            
            current_writer = node.writers[running_writer_name]
            if isinstance(current_writer, tuple):
                current_writer[1](node)
    
    for node in nodes:
        walk_doctree(node, on_enter_node, on_exit_node)