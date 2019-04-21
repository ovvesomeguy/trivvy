#!/usr/bin/python3.6
import expand
from argument_parser import argumentParser
from template_engine import templateExpander
from tuberegister import mainTube
import os
import time

# the entry point
def main():
        expand.createSettings()
        args = argumentParser().parseIt() # args of command line
        settings = expand.parseSettings() # the settings from json file
        mainClass = templateExpander(settings) # this must be main class entry
        
        tube = mainTube()
        if args.action == 'start':
                mainClass.understandSettings()
                tube.addNewItem([settings['name'] , str(time.strftime('%c')) ,settings['author']])
                print('\033[32m' + 'The project added to trivvy database')

        elif args.action == 'delete':
                mainClass.removeAll()
        else:
                print('\033[33m' + 'The argument is not valid')
if __name__ == "__main__":
    main()