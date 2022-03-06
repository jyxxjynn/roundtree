import os
import sys
import urllib
from urllib.request import urlopen

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))

import util.config_helper as cfg
import util.yaml_helper as yml
import util.path_helper as pth

BASEFILS=r"C:\Users\Jason\petrus\personal\tiktok"



def devtest():
    #pth.print_paths(BASEFILS)
    pth.print_paths('fal.txt')
    url = "http://olympus.realphython.org/profiles/aphrodite"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    
    print(page)







def main():
    devtest()

if __name__ == '__main__':
    main()
