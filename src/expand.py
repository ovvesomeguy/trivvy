# This file must expand the project with some template
# The webDev class work perfectly, but need to add some featured

import sys
import os
import json


SETTINGS_PATH = os.getcwd() + '/settings.json'
    
def createSettings():
    if os.path.exists(SETTINGS_PATH):
        pass
    else:            
        os.mknod(SETTINGS_PATH)
        with open(SETTINGS_PATH, 'w') as file:
            file.write('{\n    "path": "."\n}')
            print('\033[32m' + 'The configuration file was create, just edit the settings.json file')
            sys.exit(0)
    
def printWarning():
    # CODES = ['NO_AUTHOR','NO_NAME','NO_PATH_TO_FILE','NO_TEMPLATE']
    print('\033[31m' + 'The settings file is not valid')
    sys.exit(0)

def parseSettings():
    if os.path.exists(SETTINGS_PATH):
        _jsonArgs = open(SETTINGS_PATH , 'r').read()
        _jsData = json.loads(_jsonArgs)
        if not 'author' in _jsData or not 'name' in _jsData or not 'path' in _jsData or not 'template' in _jsData:
            printWarning()

        return _jsData
    else:
        createSettings()
