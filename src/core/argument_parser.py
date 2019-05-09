"""
    This file is responsible for parsing command line arguments.
    Class consoleParser will return all arguments, besides --version and --help flag
    If -v flag added, this file will print current version of trivvy
"""

import argparse
import sys
from trivvy.src.core.color_changer import colors
from trivvy.src.core.__init__ import __version__

class consoleParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(usage="Usage" , description='Decription')
    
    def print_help(self):
        print(colors.YELLOW + 'Ohh men... Just add some arguments or read help, by typing trivvy --help')
        sys.exit(0)

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
            self.print_help()
        else:
            return args
