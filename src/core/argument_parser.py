import argparse
import sys
from color_changer import colors

def print_help():
    print(colors.YELLOW + 'Ohh men... Just add some arguments or read help, by typing trivvy --help')

class consoleParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(usage="Usage" , description='Decription')
    def parseIT(self):
        self.parser.add_argument('action' , nargs='?')

        args = self.parser.parse_args()
        if len(sys.argv) == 1:
            print_help()
        else:
            return args
