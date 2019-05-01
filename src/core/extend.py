# this file is responsible for the json file and is settings:
# 1. create this file if he is not exists
# 2. parse his settings


import sys
import os
import json
    
SETINGS_ADDR = os.getcwd() + '/settings.json'

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
    if os.path.exists(SETINGS_ADDR):        
        _jsonArgs = open(SETINGS_ADDR , 'r').read()
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
        return _jsData
    else:
        print('The settings file does not exists')
        sys.exit(0)