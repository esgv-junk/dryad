import itertools
import re

def isChar(s):
    return len(s) == 1

def mergeStrRe(strList):
    charClass = ''.join(map(re.escape, filter(isChar, strList)))
    if charClass:
        charClass = '['+charClass+']'

    strRe = '|'.join(map(re.escape, itertools.filterfalse(isChar, strList)))

    return charClass + ('|' if (charClass and strRe) else '') + strRe

def escape(text, escapeDict):
    return re.sub(
        mergeStrRe(escapeDict.keys()),
        lambda m: escapeDict[m.group(0)],
        text)

mathEscapes = {
    '<': '&lt;',
    '>': '&gt;',
    '&': '&amp;',
    '"': '&quot;',
    "'": '&apos;',
}

htmlEscapes = {
    '$': '\$'
}
htmlEscapes.update(mathEscapes)

escapeHTML = lambda text: escape(text, htmlEscapes)
escapeMath = lambda text: escape(text, mathEscapes)