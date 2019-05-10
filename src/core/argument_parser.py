"""
    This file is responsible for parsing command line arguments.
    Class consoleParser will return all arguments, besides --version and --help flag
    If -v flag added, this file will print current version of trivvy
"""

import argparse
import sys
from trivvy.src.core.color_changer import colors
from trivvy.src.core.__init__ import __version__
from trivvy.src.core.expander import usersTemplate
import shutil

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
        self.parser.add_argument(
                                '-t',
                                '--templates',
                                action='store_true',
                                help='Show all your templates',
        )
        args = self.parser.parse_args()
        if args.version == True:
            print(__version__)
        if args.templates:
            phraseLength = len('All your templates man')
            countOfFallbackToCenter = int((shutil.get_terminal_size().columns - phraseLength)/2) - 1
            print(colors.GREEN + '|' + '-'*countOfFallbackToCenter + 'All tour templates man' + '-'*countOfFallbackToCenter + '|' + colors.RESET)
            for template in usersTemplate().allUserTemplate():
                print(colors.YELLOW + '|' + ' '*countOfFallbackToCenter + template + ' '*countOfFallbackToCenter + colors.RESET)
            print(colors.GREEN + '-'* shutil.get_terminal_size().columns + colors.RESET)
        if len(sys.argv) == 1:
            self.print_help()
        else:
            return args
