import re, itertools

from . import line_utils
from .. import doctree
from .. import parsing
from .. parsing import inline_parser

parseRules = [Directive, List, Section, Paragraph]

lookahead = max(map(
    lambda r: r.lookahead,
    parseRules
))

def parseBlocks(lines):
    source = parsing.k_iter(lines, line_utils.Line(), lookahead)
    next(source, None)                  # create context iter and open it

    while True:
        while source[0].isBlank:        # skip blank lines
            next(source)

        for r in parseRules:            # iterate over all parse rules
            if r.isStartLine(source):
                for node in r.parse(source):
                    yield node
                break
