from color_changer import colors
import controller 
from controller import checkStatus
import os


class awesomeUnderstander:
    def __init__(self , json):
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
        print(colors.GREEN + 'The project was succssesful build' + colors.RESET)

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
