#!/usr/bin/python3.6
import sys
import controller
from color_changer import colors
import reporter
import expander
import argument_parser

def main():
    consoleArgs = argument_parser.consoleParser().parseIT()
    
    if consoleArgs.action == 'start':
        controller.createSettings() # this function will create settings if the are not exists
        settings = controller.parseJsonSettings()
        expander.awesomeUnderstander(settings)
        sys.exit(0)
    
    if consoleArgs.action == 'delete':
        controller.removeAll()
        print(colors.RED + 'Okey, Your project was deleted.')
    
    else:
        print(colors.YELLOW + 'Not like this. Please read the docs...' + colors.RESET)

if __name__ == "__main__":
    main()