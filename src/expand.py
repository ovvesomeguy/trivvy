# This file must expand the project with some template
# The webDev class work perfectly, but need to add some featured

import sys
import os
import json

class spread():
    def __init__(self):
        self.file_path = os.getcwd() # this variable specify where the file is running
        self.settings_path = self.file_path + '/settings.json'
    
    def createSettings(self):
        if os.path.exists(self.settings_path):
            pass
        else:            
            os.mknod(self.settings_path)
            with open(self.settings_path, 'w') as file:
                file.write('{\n    "path": "."\n}')

    def parseSettings(self):
        self.jsonArgs = open(self.settings_path , 'r').read()
        if not 'path' in self.jsonArgs:
            print('\033[31m' , 'The settings file is not valid, please read the docs')
            sys.exit(0)
        self._jsData = json.loads(self.jsonArgs)
        return self._jsData

spread().parseSettings()