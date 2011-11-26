input_path = r'D:\Dropbox\knowledge'

rebuild = False
rebuild = True

from dryad import *

def main():
    set_writer('html')
    render_dir(input_path, rebuild)
    print('Done')
    
if __name__ == "__main__":
    main()
