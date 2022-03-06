import os
import sys

def print_paths(filepath:str):
    print(f'ABSPATH = ' + os.path.abspath(filepath))
    print(f'DIRECTORY + ' + os.path.dirname(filepath))

def path_exists(filepath:str) -> bool:
    return os.path.exists(filepath)

def get_path_from_commandline_first_arg() -> str:
    path = sys.argv[1]
    if os.path.exists(path):
        print("File exist")
    print( "filename : " + path.split("/")[-1])
    return path
