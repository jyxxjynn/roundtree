import os
import sys
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
import util.config_helper as cfg
import util.yaml_helper as yml

def launch_to():
    config_file=cfg.get_path_from_commandline_first_arg()
    yaml_file_dict=yml.get_yaml_file_to_dict(config_file)
    commandline=f"{yaml_file_dict['command']}"
    print("Commandline to be called" + commandline)

    for folderpath in yaml_file_dict['folders']:
        full_launch_folderpath=f"{yaml_file_dict['root']}\\{folderpath}"
        print(f"Folderpath to launch is : {full_launch_folderpath}")
        full_command_line=f'START "{folderpath}" "{commandline}" {full_launch_folderpath} {yaml_file_dict["modifiers"]}'
        fire_one((full_command_line))

def fire_one(full_command_line:str):
    print(f"Full commandline is: {full_command_line}")
    os.system(full_command_line)

def main():
    print("############### Program Start ###########")
    launch_to()
    print("############### Program End #############")

main()
