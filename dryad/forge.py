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
    
    
/* Math blocks */

.theorem_outer, .definition_outer, .example_outer, .paradox_outer {
    background-color: #cccccc;
    border: 1px solid;
    border-color: #666666;
    border-radius: 5px;
    box-shadow: 1px 1px 3px rgba(0,0,0,0.25);
    padding-top: 0.25em;
}

.theorem-inner, .definition-inner, .example-inner, .paradox-inner {
    margin-top: 0.25em;
    padding: 0.25em 0.5em 0.5em 0.5em;
    background-color: white;
    border-top: 1px solid;
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 5px;
    border-color: #999999;
}

.definition-outer em {
    font-weight: bolder;
    font-style: normal;
}

.definition-title, .theorem-title, .example-title, .paradox-title {
    text-shadow: 1px 1px 1px white;
    margin-left: 0.25em;
}

.theorem-title > strong, .definition-title > strong, .paradox-title > strong {
    /*font-size: 120%;*/
}

/* ============ Plugin area ============= */

/* Code */

span.code {
    background-color: #eeeeee;
    border: 1px solid;
    border-color: #cccccc;
    border-radius: 2px;
}

em span.code {
    font-style: normal;
}

strong span.code {
    font-style: normal;
}

div.code {
    background-color: #eeeeee;
    border: 1px solid;
    border-color: #999999;
    border-radius: 5px;
    padding: 0.5em;
    box-shadow: 1px 1px 2px #dddddd;
}

h1 > .code, h2 > .code, h3 > .code, h4 > .code, h5 > .code, h6 > .code {
    background-color: white;
    border: none;
}

/* Unknown */

.unknown {
    background-color: #cc0000;
    border: 1px solid;
    border-color: #660000;
    color: white;
}

span.unknown{
    border-radius: 2px;
}

div.unknown {
    border-radius: 5px;
    box-shadow: 1px 1px 3px rgba(0,0,0,0.25);
    padding: 0.5em;
}
