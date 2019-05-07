from color_changer import colors
import trivvy.src.core.controller as controller
from trivvy.src.core.controller import checkStatus
import os
import json
import sys
def __underStandCustomTemplate(fileAddres):
        with open(fileAddres , 'r') as file:
            fileContent = file.read()
            jsonSerial = json.loads(fileContent)
            return jsonSerial

def findAllCustomTemplates():
    allTemplates = []
    for file in os.listdir(os.path.expanduser('~') + '/.trivvy/templates/'):
        file = file.split('.')[0]
        allTemplates.append(file)
    return allTemplates

def createCustomTemplate():
    templateName = input(colors.MAGENTA + 'Give name for your template: ')
    if not templateName in findAllCustomTemplates():
        pass
    else:
        print(colors.RED + 'Template with this name already exists' + colors.RESET)
        sys.exit(0)

    folders = input(colors.MAGENTA + 'All folders names with backslash: ').split()
    files = input(colors.MAGENTA + 'All files: ').split()
    customTemplateStruct = {'folder':folders , 'files':files}
    jsonExemplar = json.dumps(customTemplateStruct , indent=4)

    with open(os.path.expanduser('~') + '/.trivvy/templates/' + templateName + '.txt' , 'w') as file:
        file.write(str(jsonExemplar))

    print('Your template was created and now looking like that: ')
    print(colors.GREEN + jsonExemplar + colors.RESET)

class awesomeUnderstander:
    def __init__(self, json):
        self.json = json
        self.__underStand()
    
    def __underStand(self):
        if self.json['template'] == 'python':
            pyTemplate().createProject()
        elif self.json['template'] == 'web':
            webTemplate().createProject()

        # TODO some database of all templates
        else:
            pass
class mainTemplate():
    def __init__(self , folders , files):
        self.__filesToCreate = files
        self.__foldersToCreate = folders
        self.__homePrefix = os.getcwd() + '/'

    def createProject(self):
        for folder in self.__foldersToCreate:
            if checkStatus(self.__homePrefix + folder) is False:
                os.mkdir(self.__homePrefix + folder)


        for file in self.__filesToCreate:
            if checkStatus(self.__homePrefix + file) is False:
                os.mknod(self.__homePrefix + file)
        
        self.logSelfStatus()
        print(colors.MAGENTA + 'The project was succssesful build' + colors.RESET)

    def logSelfStatus(self):
        if checkStatus(os.getcwd() + '/.local_trivvy/existing_status.txt'):
            with open(os.getcwd() + '/.local_trivvy/existings_status.txt' , 'w') as file:
                file.write('yes')
            print('fine')
        else:
            print(colors.YELLOW + 'I cant log it, but i crete your project' +  colors.RESET)
        
class pyTemplate(mainTemplate):
    def __init__(self):
        self.__filesToCreate = ['src/__init__.py' , 'src/__main__.py' , 'README.md']
        self.__foldersToCreate = ['src/']
        super().__init__(self.__foldersToCreate , self.__filesToCreate)

class webTemplate(mainTemplate):
    def __init__(self):
        self.__filesToCreate = ['src/index.html' , 'src/style.css' , 'src/script.js' ,'README.md']
        self.__foldersToCreate = ['src/' , 'images/']
        super().__init__(self.__foldersToCreate , self.__filesToCreate)

findAllCustomTemplates()