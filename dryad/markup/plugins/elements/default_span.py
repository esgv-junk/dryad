preferred_default_name = 'default'
default_span_name = preferred_default_name 

def set_default_span(block_name, inline_text, body_lines):
    global default_span_name
    default_span_name = inline_text.strip()
    
    # whenever default_span name is '', we'll go into infinite loop as
    # soon as we encounter default span
    if default_span_name == '':
        reset_state()             
    
    # since we're in a parse function, we have to return iterable
    return []

def parse_default_span(span_name, body_text):
    from dryad.markup.parser import parse_span
    return parse_span(default_span_name, body_text)

def reset_default_span():
    global default_span_name
    default_span_name = preferred_default_name 

before_parse_document = [reset_default_span]
block_parsers         = [('default_span', set_default_span  )]
span_parsers          = [(''            , parse_default_span)]
