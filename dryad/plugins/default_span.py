preferred_default_name = 'default'

default_span_name = preferred_default_name 

def set_default_span(block_name, inline_text, body_lines):
    global default_span_name
    default_span_name = inline_text.strip()
    
    # whenever default_span name is '', we'll go into infinite loop as
    # soon as we encounter default span
    if default_span_name == '':             
        default_span_name = preferred_default_name 
    
    # since we're in a parse function, we have to return iterable
    return []

def parse_default_span(span_name, body_text):
    from dryad.plugins import parse_span 
    return parse_span(default_span_name, body_text)