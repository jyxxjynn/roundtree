import yaml

def get_yaml_file_to_dict(yamlpath:str) -> dict:
    with open(yamlpath) as stream:
        launch_config=yaml.safe_load(stream)
    return launch_config
