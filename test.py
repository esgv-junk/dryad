from dryad.parsing import parse_document
from dryad.writer import *
from dryad import plugins

input_file = 'tests/test.txt'
output_file = 'tests/test.html'

def main():
    test_lines = iter(open(input_file).readlines())
    root = parse_document(test_lines)
    
    set_writer('debug')   
    print(str_nodes(root))
    
    set_writer('html')
    print(str_nodes(root), file=open(output_file, 'w', encoding="utf-8"))
    
    print('Done')
        
if __name__ == '__main__':
    main()
