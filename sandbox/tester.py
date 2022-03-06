import os
import sys
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
import util.config_helper as cfg
import util.yaml_helper as yml
import util.path_helper as pth

BASEFILS=r"C:\Users\Jason\petrus\personal\tiktok"


def main():
    #pth.print_paths(BASEFILS)
    pth.print_paths('fal.txt')


if __name__ == '__main__':
    main()


