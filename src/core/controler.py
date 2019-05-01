# This script prepare the project to start with making the local and global trivvy folder
# and if the project database does not exists than make it

import os
from shutil import copyfile
from trivvy.src.integrate.tuberegister import mainTube
import sys
import json

logger_struct = """[loggers]
keys=root,exampleApp
 
[handlers]
keys=fileHandler, consoleHandler
 
[formatters]
keys=myFormatter
 
[logger_root]
level=CRITICAL
handlers=consoleHandler
 
[logger_exampleApp]
level=INFO
handlers=fileHandler
qualname=exampleApp
 
[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=myFormatter
args=(sys.stdout,)
 
[handler_fileHandler]
class=FileHandler
formatter=myFormatter
args=("config.log",)
 
[formatter_myFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt="""

LOCAL_TRIVVY_FOLDER = os.getcwd() + '/.local_trivvy/'
GLOBAL_TRIVVY_FOLDER = os.path.expanduser('~') + '/.trivvy/'
LOGGER_FOLDER = GLOBAL_TRIVVY_FOLDER + 'logger/'


LOGGER_CONFIG = LOGGER_FOLDER + 'logger.conf'
SETINGS_ADDR = os.getcwd() + '/settings.json'
PROJECTS_DATABASE_ADDR = GLOBAL_TRIVVY_FOLDER + 'projects.db'

folder_array = [LOCAL_TRIVVY_FOLDER , GLOBAL_TRIVVY_FOLDER , LOGGER_FOLDER]
files_array = [LOGGER_CONFIG , PROJECTS_DATABASE_ADDR]

def prepareForStart():
    # create the basic folders and files
    for folder in folder_array:
        if os.path.exists(folder) == False:
            os.mkdir(folder)

    for file in files_array:
        if os.path.exists(file) == False:
            os.mknod(file)

    mainTube()._initializeDb()
    prepareLoggerConfig()

def prepareLoggerConfig():
    with open(LOGGER_CONFIG , 'w') as file:
        file.write(logger_struct)

def logInLocalFolder(project_id):
    # copy settings.json file in special place
    copyfile(SETINGS_ADDR , LOCAL_TRIVVY_FOLDER + 'copied.txt')
    with open(LOCAL_TRIVVY_FOLDER + 'id.txt' , 'w') as file:
        file.write(project_id)

def createSettings():
        if os.path.exists(SETINGS_ADDR) == False:
                settings_struct = {'path': '.' , 'name':os.path.basename(os.getcwd()) , 'template': ''}
                os.mknod(SETINGS_ADDR)
                with open(SETINGS_ADDR, 'w') as file:
                        file.write(json.dumps(settings_struct , indent=4))
                        print('\033[32m' + 'The configuration file was create, just edit the settings.json file')
                        sys.exit(0)

    
def check_status():
    project_exist = False
    if os.path.exists(LOCAL_TRIVVY_FOLDER + 'id.txt') and os.stat(LOCAL_TRIVVY_FOLDER + 'id.txt').st_size != 0:
        project_exist = True
    else:
        project_exist = False
    
    return project_exist

def return_local_id():
    with open(LOCAL_TRIVVY_FOLDER + 'id.txt' , 'r') as file:
        project_id = file.read()
        return project_id