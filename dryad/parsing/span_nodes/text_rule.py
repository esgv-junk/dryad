text_escapes = { 
    '\\\\': '\\',
    r'\`' : '`',
    r'\*' : '*'
}

class TextRule:
    rule_regex = '.*'
    
    @staticmethod
    def parse(text):
        text = descaped(typographed(text), text_escapes)
        yield Text(text)