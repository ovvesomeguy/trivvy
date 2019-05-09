"""
    This is core of module.
    Class 'awesomeUnderstander' will parse settings.json file and decide what to do.
    All classes, must be inerit by mainTemplate. mainTemplate - basic class with basic functions.
    He have 2 arguments. First is folders to setup, second if files.
"""


import json
import os
import sys
from pathlib import Path

import trivvy.src.core.controller as controller
from trivvy.src.core.color_changer import colors
from trivvy.src.core.controller import checkStatus

class usersTemplate:
    def __underStandCustomTemplate(self , templateAddr):
            with open(templateAddr , 'r') as file:
                fileContent = file.read()
                jsonSerial = json.loads(fileContent)
                return jsonSerial

    def findCustomTemplates(self , name):
        for file in os.listdir(os.path.expanduser('~') + '/.trivvy/templates/'):
            if file.split('.')[0] == name:
                return os.path.expanduser('~') + '/.trivvy/templates/' + file
    
    def allUserTemplate(self):
        result = []
        for file in os.listdir(os.path.expanduser('~') + '/.trivvy/templates/'):
            result.append(file.split('.')[0])
        return result

    def createCustomTemplate(self):
        templateName = input(colors.MAGENTA + 'Give name for your template: ')
        if not templateName in self.allUserTemplate():
            pass
        else:
            print(colors.RED + 'Template with this name already exists' + colors.RESET)
            sys.exit(0)

        folders = input(colors.MAGENTA + 'All folders names: ').split()
        files = input(colors.MAGENTA + 'All files: ').split()
        customTemplateStruct = {'folders':folders , 'files':files}
        jsonExemplar = json.dumps(customTemplateStruct , indent=4)

        with open(os.path.expanduser('~') + '/.trivvy/templates/' + templateName + '.txt' , 'w') as file:
            file.write(str(jsonExemplar))

        print('Your template was created and now looking like that: ')
        print(colors.GREEN + jsonExemplar + colors.RESET)

    def expandCustomTemplate(self , template):
        with open(template , 'r') as file:
            jsonTemplate = json.loads(file.read())
            print(jsonTemplate)
            mainTemplate(jsonTemplate['folder'] , jsonTemplate['files']).createProject()


class awesomeUnderstander:
    def __init__(self, json):
        self.json = json
        self.__underStand()
    
    def __underStand(self):
        if self.json['template'] == 'python':
            pyTemplate().createProject()
        elif self.json['template'] == 'web':
            webTemplate().createProject()

        else:
            usersTemplate().expandCustomTemplate(str(usersTemplate().findCustomTemplates(self.json['template'])))

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

