from .. forge import *
from .. import doctree

blockMarkers = ['!', '@', '#', '$', '%', '^', '&',  '`']
strongMarkers = ['*']

knownEscapes = list(
    frozenset(filter(isChar, blockMarkers)) |
    frozenset(filter(isChar, strongMarkers))
) + ['\\']

idRe = r'[a-zA-Z-_]+'
knownEscapesRe = mergeStrRe(knownEscapes)
bodyRe = r'(?:[^\\]|\\.)+?'

def inlineRe(extract):
    g, st, end = ('', '^', '$') if extract else ('?:', '', '')

    return r'{st}({g}{0}|\[{1}\])?`({g}{2})`{end}'.format(
        mergeStrRe(blockMarkers), idRe, bodyRe,
        g = g, st = st, end = end)

def strongRe(extract):
    if extract:
        return r'^\*({0})\*$'.format(bodyRe)
    else:
        return r'\*(?:{0})\*'.format(bodyRe)

def descaped(text):
    for e in knownEscapes:
        text = text.replace('\\'+e, e)
    return text

def descapedBackslash(text):
    return text.replace('\\\\', '\\')


typoEscapes = {
    '->': '\u2192',
    '<-': '\u2190',
    '<->': '\u2194',
    '--': '\u2014', #em dash
    ' - ': '\u2013' #en dash
}

def typograph(text):
    return escape(text, typoEscapes)

def parseInline(text):
    from .. import directives
    
    parts = re.split(
        '((?:{0})|(?:{1}))'.format(inlineRe(False), strongRe(False)),
        text)

    for p in parts:
        if p:
            # try directive
            inline = re.match(inlineRe(True), p)
            if inline:
                nodeType = directives.inlineParsers[inline.group(1)]
                yield nodeType(descapedBackslash(inline.group(2)))
                continue

            # try strong
            strong = re.match(strongRe(True), p)
            if strong:
                yield doctree.Strong(parseInline(descaped(strong.group(1))))
                continue

            # make text node
            p = descaped(p)
            yield doctree.Text(typograph(p))
