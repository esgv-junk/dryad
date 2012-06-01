class Link:
    def __init__(self, href, body_text):
        self.href = href
        self.body_text = body_text

wiki_prefix = 'w://'

def parse_link(span_name, body_text):
    if span_name == '@':
        span_name = body_text

    if span_name.startswith(wiki_prefix):
        yield Link('/wiki/' + span_name[len(wiki_prefix):], body_text)
    else:
        yield Link(span_name, body_text)
    
span_parsers = [(ur'@|[a-z]+://.*', parse_link)]
