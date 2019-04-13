# This file must expand the project with some template
# The webDev class work perfectly, but need to add some featured

import sys
import os
import json

class spread():
    def __init__(self):
        pass

    def findLocation(self):
        self.file_path = os.getcwd() # this variable specify where the file is running
        self.settings_path = self.file_path + '/settings.json'
        if os.path.isfile(self.settings_path):
            return True
        else:
            return False

    def parseSettings(self):
        if self.findLocation():
            self.jsonArgs = open(self.settings_path , 'r').read()
            self._jsData = json.loads(self.jsonArgs)
            return self._jsData