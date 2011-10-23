#===============================================================================
# def build():
# 
#    inputDir = 'src/'
#    outputDir = 'build/html/'
#    builder = 'html'
# 
#    for (path, dirs, files) in os.walk(inputDir):
#        for f in files:
#            path+f
#            file = (outputDir+(path-inputDir)+f)
#            open(file)
#            k_iter(file.readlines)
#            try:
#                parse
#            except:
#                repack
# 
# links: full path anchor list, header list
# images: local input and output folders
# customizable strongs
#===============================================================================

#===============================================================================
# math_HTML_escapes = {
#    '<': '&lt;',
#    '>': '&gt;',
#    '&': '&amp;',
#    '"': '&quot;',
#    "'": '&apos;',
# }
# 
# HTML_escapes = {
#    '$': '\$'
# }
# HTML_escapes.update(math_HTML_escapes)
# 
# escape_HTML = lambda text: escape(text, HTML_escapes)
# escape_HTML_math = lambda text: escape(text, math_HTML_escapes)
#===============================================================================


#===============================================================================
#    Kinda lazy version of strip_blank_lines
#
#    #source = parsing.k_iter(lines, k = 0)
# 
#    #for l in source:
#    #    if not l.isBlank:
#    #        yield l
#    #    else:
#    #        blanks = 0
#    #        try:
#    #            while source[0].isBlank:
#    #                blanks += 1
#    #                next(source)
#    #            for i in range(blanks):
#    #                yield Line()
#    #        except:
#    #            pass
# 
#    # strip blank lines in the end
#===============================================================================

# From doctree.Block
#def allLines(self):
#        if self.inline_text:
#            return itertools.chain(
#                [line_utils.Line(self.inline_text)], 
#                self.body_lines)
#        else:
#            return self.body_lines
