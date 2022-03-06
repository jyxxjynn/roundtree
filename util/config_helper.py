import os
import sys

def get_path_from_commandline_first_arg() -> str:
    path = sys.argv[1]
    if os.path.exists(path):
        print("File exist")
    print( "filename : " + path.split("/")[-1])
    return path

def get_single_arg_from_commandline() -> str:
    arg = sys.argv[1]
    return arg