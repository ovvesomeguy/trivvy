#!/usr/bin/python3.6
import sys
import trivvy.src.core.controller as controller
from trivvy.src.core.color_changer import colors
import trivvy.src.core.reporter as reporter
import trivvy.src.core.expander as expander
import trivvy.src.core.argument_parser as argument_parser
import subprocess

def main():
    consoleArgs = argument_parser.consoleParser().parseIT()
    if consoleArgs.action == 'start':
        controller.createSettings() # this function will create settings if the are not exists
        settings = controller.parseJsonSettings()
        expander.awesomeUnderstander(settings)
        sys.exit(0)
    
    elif consoleArgs.action == 'delete':
        controller.removeAll()
        print(colors.RED + 'Okey, Your project was deleted.')
    
    elif consoleArgs.action == 'create':
        expander.createCustomTemplate()
        
if __name__ == "__main__":
    main()