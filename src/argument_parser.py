import argparse
import sys

class argumentParser():
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='The trivvy project creator',
                                              usage="trivvy start - to create the app"
        )
    
    def parseIt(self):
        if len(sys.argv) == 1:
            print('\033[33m' + 'Please add some argument or read the help by typing: trivvy --help')
            sys.exit(0)
        self.parser.add_argument('action' , help='create the settings.json file with basic config')
        args = self.parser.parse_args()
        return args
