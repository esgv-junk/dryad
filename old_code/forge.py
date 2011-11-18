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
#    #                )
#    #            for i in range(blanks):
#    #                yield Line()
#    #        except:
#    #            pass
# 
#    # strip blank lines in the end
#===============================================================================

def setup_doctree_fields(root_node):
    if not hasattr(root_node, 'parent_node'):
        root_node.parent = None
    
    if hasattr(root_node, 'child_nodes'):
        for child_index in range(len(root_node.child_nodes)):
            # create some fields:
            # parent_node, child_index, next_sibling, prev_sibling
            child_node = root_node.child_nodes[child_index]
            child_node.parent_node = root_node
            child_node.child_index = child_index
            
            if child_index > 0:
                child_node.prev_sibling = root_node.child_nodes[child_index - 1]
            if child_index < (len(root_node.child_nodes) - 1):
                child_node.next_sibling = root_node.child_nodes[child_index + 1]

            # proceed
            setup_doctree_fields(child_node)

def walk_doctree(start_node, on_enter, on_exit):
    on_enter(start_node)
    if hasattr(start_node, 'child_nodes'):
        for child_node in start_node.child_nodes:
            walk_doctree(child_node, on_enter, on_exit)
    on_exit(start_node)
    
"""
<!-- MathJax -->
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    tex2jax: {
        inlineMath: [['$','$']],
        processEscapes: true,
        skipTags: ["script", "noscript", "style"]
    },
    "HTML-CSS": {
        scale: 120,
        showMathMenu: false,
    },
    NativeMML: {
        scale: 120
    }
});
</script>

<script type="text/javascript"
    src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
"""

"""
/* div > div > ul > li.even, div > div > ol > li.even {
    background-color: hsl(260, 50%, 97%);
}

div > div > ul > li.odd, div > div > ol > li.odd {
    background-color: inherit;
} */
"""