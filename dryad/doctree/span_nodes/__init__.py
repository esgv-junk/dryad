def pretty_format_spans(*nodes, sep=', '):
    return sep.join(map(lambda node: node.pretty_format(), 
                        nodes))            