import os
from shutil import copyfile
from tuberegister import mainTube


# Thiis script prepare the project to start with making the local and global trivvy folder
# and if the project database does not exists than make it

LOCAL_TRIVVY_FOLDER = os.getcwd() + '/.local_trivvy/'
SETINGS_ADDR = os.getcwd() + '/settings.json'
GLOBAL_TRIVVY_FOLDER = os.path.expanduser('~') + '/.trivvy/'
PROJECTS_DATABASE_ADDR = GLOBAL_TRIVVY_FOLDER + 'projects.db'

def prepareForStart():
    if os.path.exists(LOCAL_TRIVVY_FOLDER) == False:
        os.mkdir(LOCAL_TRIVVY_FOLDER)

    if os.path.exists(GLOBAL_TRIVVY_FOLDER) == False:
        os.mkdir(GLOBAL_TRIVVY_FOLDER)
    
    if os.path.exists(PROJECTS_DATABASE_ADDR) == False:
        os.mknod(PROJECTS_DATABASE_ADDR)
 
    mainTube()._initializeDb()

def logInLocalFolder(project_id):
    # copy settings.json file in special place
    copyfile(SETINGS_ADDR , LOCAL_TRIVVY_FOLDER + 'copied.txt')
    with open(LOCAL_TRIVVY_FOLDER + 'id.txt' , 'w') as file:
        file.write(project_id)

    
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