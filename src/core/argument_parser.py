import argparse
import sys
from color_changer import colors
from __init__ import __version__

def print_help():
    print(colors.YELLOW + 'Ohh men... Just add some arguments or read help, by typing trivvy --help')
    sys.exit(0)
class consoleParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(usage="Usage" , description='Decription')
    def parseIT(self):
        self.parser.add_argument(
                                'action',
                                nargs='?',
                                help='start , delete')
        self.parser.add_argument(
                                '-v',
                                '--version',
                                action='store_true',
                                help='Dislay the current version of product')

        args = self.parser.parse_args()
        if args.version == True:
            print(__version__)
        if len(sys.argv) == 1:
            print_help()
        else:
            return args
