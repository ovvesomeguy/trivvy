""" 
    This file included the finder and creater of templates
    The templates will be divided on 2 classes:
        1) The primordial templates 
        2) The other templates

    And nedd to create some secuirity hierarchy
"""
import os
import shutil
from colorama import Fore , init



class webTemplate():
    def __init__(self , args):
        self.folder = args['path']
        init(autoreset=True)

    def createElements(self):
        # create folders
        if os.path.exists(self.folder + '/image') == False:
            os.mkdir(self.folder+'/image') 
        if os.path.exists(self.folder + '/src') == False:
            os.mkdir(self.folder + '/src') 

        # create files
        if os.path.isfile(self.folder + '/src/index.html') == False: 
            os.mknod(self.folder + '/src/index.html')
        if os.path.isfile(self.folder + '/src/style.css') == False: 
            os.mknod(self.folder + '/src/style.css')
        if os.path.isfile(self.folder + '/src/script.js') == False: 
            os.mknod(self.folder + '/src/script.js')
        if True:
            print(Fore.GREEN + 'Your app was sucsesfull create')
    def removeAll(self):
        if os.path.exists(self.folder + '/src'):
            shutil.rmtree(self.folder + '/src')
        if os.path.exists(self.folder + '/image'):
            shutil.rmtree(self.folder + '/image')
        if True:
            print(Fore.YELLOW + 'The project was sucsesfull deleted')


class pythonTemplate():
    def __init__(self , args):
        self.args = args
        self.folder = self.args['path']

    def createElements(self):
        # create folders
        if os.path.exists(self.folder + '/src') == False:
            os.mkdir(self.folder + '/src') 
        # create files
        if os.path.isfile(self.folder + '/src/__init__.py') == False: 
            os.mknod(self.folder + '/src/__init__.py')
        if os.path.isfile(self.folder + '/src/__main__.py') == False: 
            os.mknod(self.folder + '/src/__main__.py')
        if os.path.isfile(self.folder + 'REAMDE.md') == False: 
            os.mknod(self.folder + 'README.md')
    def removeAll(self):
        if os.path.exists(self.folder + '/src'):
            shutil.rmtree(self.folder + '/src')