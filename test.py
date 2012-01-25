from dryad.markup.parser import parse_document
from dryad.markup.renderer import *
from dryad.markup import plugins

input_file = 'tests/test.txt'
output_file = 'tests/test.html'

def main():
    test_lines = iter(open(input_file).readlines())
    root = parse_document(test_lines)
    
    set_renderer('html')
    print(render_nodes(*root.child_nodes))
    
    set_renderer('html')
    print(render_nodes(root), file=open(output_file, 'w', encoding="utf-8"))
    
    print('Done')    
    
if __name__ == '__main__':
    #main()
    
    from pyforge.all import *
    import re
    
    math_replaces = [
        (r'\\left\s*([(\[])' , r'\1'),
        (r'\\right\s*([)\]])', r'\1'),
        (r'(\(?)(.*?)\)'     , r'\\left(?(1)\(|.) \2 \\right\)'),
    ]
    
    math_src = 'x_i + x_j)'
    
    print(multiple_replace_re(math_src, math_replaces))
    
    


