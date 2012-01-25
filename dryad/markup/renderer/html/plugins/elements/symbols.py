symbols = {
    'br': '<br>'
}

class SymbolSpan:
    def write(self):
        return symbols.get(self.symbol_name, '')
