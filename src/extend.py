# this file is responsible for the json file and is settings:
# 1. create this file if he is not exists
# 2. parse his settings


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
    

def printWarning(attr):
    # CODES = ['NO_AUTHOR','NO_NAME','NO_PATH_TO_FILE','NO_TEMPLATE']
    if attr == 'name':
        print('WARNING: the name is not definded')
    if attr == 'template':
        print('WARNING: the template is not definded')
    if attr == 'path':
        print('WARNING: the path is not definded')

    sys.exit(0)



def parseSettings():
    # TODO append not necesary arguments: integrate , author
    if os.path.exists(SETTINGS_PATH):
        _jsonArgs = open(SETTINGS_PATH , 'r').read()
        _jsData = json.loads(_jsonArgs)

        # if this options not set they will be auto replaced
        if _jsData.get('integrate') == None:
            _jsData['integrate'] = 'false'
        if _jsData.get('author') == None:
            _jsData['author'] = 'None'

        # these options are required
        if not 'name' in _jsData:
            printWarning('name')
        if not 'path' in _jsData:
            printWarning('path')
        if not 'template' in _jsData:
            printWarning('template')

        print('this is fine')
        return _jsData
    
    else:
        createSettings()
