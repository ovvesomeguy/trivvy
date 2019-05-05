import sys
import os
import json
import shutil
import json
from color_changer import colors
from getpass import getuser

USER_HOME = os.path.expanduser('~') + '/'
PROJECT_HOME_FOLDER = os.getcwd() + '/'
LOCAL_TRIVVY_FOLDER = PROJECT_HOME_FOLDER + '.local_trivvy/'
GLOBAL_TRIVVY_FOLDER = USER_HOME + '.trivvy/'

SETTINGS_JSON = PROJECT_HOME_FOLDER + 'settings.json'

def removeAll():
    foldersInDir = os.listdir(os.getcwd())
    for folder in foldersInDir:
        if folder != 'settings.json':
            if os.path.isdir(folder):
                shutil.rmtree(folder)
            else:
                os.remove(folder)

# if id.txt exists and he is not empty, return id
# else return exception
def readLocalId():
    existStatus = checkStatus(LOCAL_TRIVVY_FOLDER + 'id.txt' , size=True)
    if existStatus[0] and existStatus[1] != 0:
        with open(LOCAL_TRIVVY_FOLDER + 'id.txt' , 'r') as file:
            _id = file.read()
            return _id.strip()
    elif existStatus[0] and existStatus[1] == 0:
        print('The file size is too low')


def prepareProject():
    pass
def checkStatus(file=None , size=None):
    global fileSize
    if file != None:
        # this means that need to check if project exists
        if file == 'PROJECT':
            if os.path.exists(LOCAL_TRIVVY_FOLDER + 'existing_status.txt'):
                if open(LOCAL_TRIVVY_FOLDER + 'existing_status.txt' , 'r').read() == 'yes':
                    return True
            else:
                return False
                
        if os.path.exists(file) == True:
            fileSize = os.stat(file).st_size
            if size:
                return True, fileSize
            else:
                return True
        else:
            return False
    
def parseJsonSettings():
    if checkStatus(SETTINGS_JSON):
        _openedJson = open(SETTINGS_JSON , 'r').read()
        _jsonData = json.loads(_openedJson)

        # if this options not set they will be auto replaced
        if _jsonData.get('integrate') == None:
            _jsonData['integrate'] = 'false'
        if _jsonData.get('author') == None:
            _jsonData['author'] = str(getuser())

        return _jsonData
    else:
        print(colors.RED + 'The settings file does not exists. Please create him...' + colors.RESET)


def createSettings():
    if checkStatus(SETTINGS_JSON) is False:
        jsonProjectStruct = {'path':'.' , 'name': os.path.basename(os.getcwd()) , 'template': ''}
        with open(SETTINGS_JSON, 'w') as file:
            file.write(str(json.dumps(jsonProjectStruct , indent=4)))
    else:
        pass