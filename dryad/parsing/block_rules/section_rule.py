class SectionRule:
    @staticmethod
    def applies_to(source):
        pass
    
    @staticmethod
    def parse():
        pass

class Section:
    lookahead = 2

    @staticmethod
    def outlineRe(title):
        return r'^[=\-~]{{{title_len},}}$'.format(len(title.text))

    @staticmethod
    def case2(source):
        indMatch = source[0].indent == source[1].indent == 0
        title = source[0]
        return not source[0].isBlank and indMatch and re.match(Section.outlineRe(title), source[1].text)

    @staticmethod
    def case3(source):
        indMatch = source[0].indent == source[1].indent == \
                   source[2].indent == 0
        title = source[1]
        outlineRe = Section.outlineRe(title)
        return not source[0].isBlank and indMatch and re.match(outlineRe, source[0].text) and \
               re.match(outlineRe, source[2].text)
               
    @staticmethod
    def isStartLine(source):
        # match '======'-type pattern in the second line
        return Section.case2(source) or Section.case3(source)

    @staticmethod
    def parse(source):
        if Section.case2(source):
            title = source[0]
            headingChar = source[1].text[0]
            headingCase = 2
            parsing.eat(source, 2)
        else:
            title = source[1]
            headingChar = source[0].text[0]
            headingCase = 3
            parsing.eat(source, 3)

        titleNodes = inline_parser.parseInline(title.text)

        def take(s):
            nonlocal headingChar, headingCase
            if headingCase == 2:
                return not(Section.case2(s) and 
                    (s[1].text[0] == headingChar))
            else:
                return not(Section.case3(s) and
                    (s[0].text[0] == headingChar))

        lines = source.takewhile(take)

        # resulting node
        result = doctree.Section(titleNodes, list(parseBlocks(lines)))

        # yield
        yield result
