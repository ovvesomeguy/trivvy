""" 
    This file included the finder and creater of templates
    The templates will be divided on 2 classes:
        1) The primordial templates 
        2) The other templates

    And nedd to create some secuirity hierarchy
"""
import os
import shutil

class webTemplate():
    def __init__(self , folder):
        self.folder = folder

    def create_elements(self):
        if os.path.exists(self.folder + '/image') == False:
            os.mkdir(self.folder+'/image') # make the folder to download th image
        if os.path.exists(self.folder + '/src') == False:
            os.mkdir(self.folder + '/src') # make the source folder

        if os.path.isfile(self.folder + '/src/index.html') == False: 
            os.mknod(self.folder + '/src/index.html')
        if os.path.isfile(self.folder + '/src/style.css') == False: 
            os.mknod(self.folder + '/src/style.css')
        if os.path.isfile(self.folder + '/src/script.js') == False: 
            os.mknod(self.folder + '/src/script.js')
    
    def remove_all(self):
        if os.path.exists(self.folder + '/src'):
            shutil.rmtree(self.folder + '/src')
        if os.path.exists(self.folder + '/src'):
            shutil.rmtree(self.folder + '/src')
            

# TODO
class pythonTemplate(): 
    pass