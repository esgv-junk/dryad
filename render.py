import os
input_path = os.getcwd() + r'\..\..\knowledge'

rebuild = False
#rebuild = True

from dryad.markup.renderer import *
from dryad.markup.renderer.batch_writer import *

def main():
    push_renderer('html')
    render_dir(input_path, rebuild)
    print('Done')
    
if __name__ == "__main__":
    main()
