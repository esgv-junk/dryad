import os
input_path = os.getcwd() + r'\..\..\knowledge'

rebuild = False
#rebuild = True

from dryad import *

def main():
    set_writer('wiki_html')
    render_dir(input_path, rebuild)
    print('Done')
    
if __name__ == "__main__":
    main()
