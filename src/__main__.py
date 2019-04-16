#!/usr/bin/python3.6
from expand import spread
from argument_parser import argumentParser
from template_engine import templateExpander
import os

# the entry point
def main():
        args = argumentParser().parseIt() # args of command line
        settings = spread().parseSettings() # the settings from json file
        mainClass = templateExpander(settings) # this must be main class entry
        
        if args.action == 'start':
                mainClass.understandSettings()
        
        elif args.action == 'delete':
                mainClass.removeAll()
        else:
                print('\033[33m' , 'The argument is not valid')
if __name__ == "__main__":
    main()