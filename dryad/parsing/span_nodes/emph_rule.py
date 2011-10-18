import re

emph_escapes = {
    '\\\\': '\\',
   r'\*'   : '*' 
}

escaped_text_re = r'(?:[^\\]|\\.)+?'

emph_re_capturing = r'\*({body_re})\*'.format(
    body_re=escaped_text_re) 
    
class EmphRule:
    rule_regexp = capture_groups_removed(emph_re_capturing)
    
    @staticmethod
    def parse(text):
        body_text = descaped(
            re.match(emph_re_capturing, text).group(1),
            emph_escapes)
        yield Emph(parse_spans(body_text))
        