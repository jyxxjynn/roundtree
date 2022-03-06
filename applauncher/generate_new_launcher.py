import os
import sys
import yaml
import shutil
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
import util.config_helper as cfgh
import util.yaml_helper as ymlh

META_LATESTFILEKEY="latestfoldername"
BASEFILS=r"C:\Users\Jason\petrus\personal\tiktok"
YAMLTEMPLATE="jax.yml"
YAMLMETADATA="hold.yml"
YAMLBASEDIR=r"C:\Users\Jason\petrus\coding\code\roundtree\applauncher\yaml_files"
YAMLFOLDERTOKEN="folders"

def run_cloner():
    print('2 running cloner')
    holdfile=os.path.join(YAMLBASEDIR, YAMLMETADATA)
    namepart=generate_new_namepart(holdfile)
    #create_new_folder(BASEFILS, namepart)
    #new_yaml_file = create_new_yaml(YAMLBASEDIR, namepart)
    #set_folders_in_yaml(new_yaml_file, namepart)
    print('2 finished with cloner')

#//TODO Generate a new folder name (test, return hardcode)
# //Create a new folder with new folder name, based on base source folder path
# //Create a new copy of a yaml file with the new folder name, as "$name.yml", in the source folder provided
# //Update the 'folders' value of the yaml to be the new name

def generate_new_namepart(yamlholdfilepath:str) -> str:
    print('3 in generate namepart')
    metadict=ymlh.get_yaml_file_to_dict(yamlholdfilepath)
    latestfoldername=metadict[META_LATESTFILEKEY]
    print(f"latest foldername is:  {latestfoldername}")
    firstletter=latestfoldername[0]
    print(f"latest letter is: {firstletter}")
    integeroffirst=ord(firstletter)
    nextletter=chr(integeroffirst+1)
    print(f"next letter is: {nextletter}")
    print('3 finished generate namepart')


def create_new_folder(sbasepath:str, namepart:str):
    # Check whether the specified path exists or not
    newdir = os.path.join(sbasepath, namepart)
    print(f'New pathname = {newdir}')
    isExist = os.path.exists(newdir)
    print(f'New folder exists?:  {isExist}')
    if(not isExist):
        os.makedirs(newdir)
    else:
        print('path already exists')

def create_new_yaml(stemplateyaml:str, namepart:str) -> str:
    print('in create_new_yaml')
    dir=os.path.dirname(stemplateyaml)
    filename=os.path.join(dir, namepart) + '.yml'
    print(f'Pathname for new yaml is: {filename}')
    isExist = os.path.exists(filename)
    print(f'New yaml file already exists?:  {isExist}')
    if(not isExist):
        shutil.copyfile(stemplateyaml, filename)
    else:
        print('Yaml file already exists')
    if(not isExist):
        isExist = os.path.exists(filename)
        print(f'Does new yaml file exist now?:   {isExist}')
    return filename

def set_folders_in_yaml(yamlfile:str, foldernames):
    listofnames = [foldernames]
    with open(yamlfile) as f:
        doc = yaml.load(f, Loader=yaml.FullLoader)
    foldersvalue = r'["' + foldernames + '"]'
    doc[YAMLFOLDERTOKEN] = listofnames
    print(f'New folder yaml value: {listofnames}')
    with open(yamlfile, 'w') as f:
        yaml.dump(doc, f, default_flow_style = True)

def main():
    print('1 main')
    run_cloner()
    print('1 completed')

if __name__ == '__main__':
    main()

