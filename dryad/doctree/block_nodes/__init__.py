def pretty_format_blocks(*nodes, indent_level=0):
    return '\n'.join(map(lambda node: node.pretty_format(indent_level), 
                         nodes))