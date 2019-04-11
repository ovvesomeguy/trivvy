# This file must expand the project with some template
# The webDev class work perfectly, but need to add some featured

import sys
import os
import json
from template_engine import webTemplate
import time

def findLocation():
    file_path = os.getcwd() # this variable specify where the file is running
    settings_path = file_path + '/settings.json'
    if os.path.isfile(settings_path) == False:
        print('Please create settings file')
        sys.exit(0)
    else:
        patt = webTemplate(file_path)
        patt.create_elements()
        print('created')
        time.sleep(5)
        patt.remove_all()



findLocation()