"""
 Rework  the architecture, maybe it`s cool way
"""

import os
import shutil

class templateExpander():
    def __init__(self , args):
        self.args = args
        self.path = self.args['path']
        self.template = self.args['template']
        if 'github' in self.args:
            self.gitConnetcion = self.args['github']
        self.foldersInDir = os.listdir(os.getcwd())

    def understandSettings(self):
        # the folder of project
        if self.path == '.':
            self.folder = os.getcwd()
        else:
            self.folder = self.path

        if self.template == 'web':
            self.mainClass = webTemplate(self.path)
            self.mainClass.createElements()
    
    def removeAll(self):
        for folder in self.foldersInDir:
            if os.path.isdir(folder):
                shutil.rmtree(folder)
        print('Deleting complete')


class webTemplate():
    def __init__(self , path):
        self.path = path
        self.homeFolder = os.getcwd()
        self.folders = [self.homeFolder + '/src' , self.homeFolder + '/image']
    def createElements(self):
        # the folders
        if os.path.exists(self.homeFolder + '/image') == False:
            os.mkdir(self.homeFolder + '/image')
        if os.path.exists(self.homeFolder + 'src') == False:
            os.mkdir(self.homeFolder + '/src')

        # the files create
        if os.path.isfile(self.homeFolder + '/src/index.html') == False:
            os.mknod(self.homeFolder + '/src/index.html')
        if os.path.isfile(self.homeFolder + '/src/style.css') == False:
            os.mknod(self.homeFolder + '/src/style.css')
        if os.path.isfile(self.homeFolder + '/src/script.js') == False:
            os.mknod(self.homeFolder + '/src/script.js')
