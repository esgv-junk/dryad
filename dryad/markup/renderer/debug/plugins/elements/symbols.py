import pystache

symbol_span_template = """<symbol name="{{symbol_name}}" />"""

class SymbolSpan:
    def write(self):
        context = {
            'symbol_name': self.symbol_name
        }
        
        return pystache.render(symbol_span_template, context)