# 1. open the file at local home folder with '.' prefix
# 2. create the database if she not exists
# 3. add some new project then 'trivvy start' pressed
# 4. log at the same folder

# all this library are going with std python lib

import os
import sys
import sqlite3


class mainTube():
    def __init__(self):
        self.home = os.path.expanduser('~')
    
    # if folder exists just return True
    # if act was given than create a folder and return True
    # else just return False
    def _initializeDb(self):
        self.dbFile = self.home + '/.trivvy/' + 'projects.db'
        self.conn = sqlite3.connect(self.dbFile)
        self.cursor = self.conn.cursor()
        
        if os.stat(self.dbFile).st_size == 0:
            self.cursor.execute("""CREATE TABLE projects
                                (name text , init_date text, temlate text , id text)
            """)

    def returnAllProjects(self): # perfectly work but if one of parameters not exists?
        self._initializeDb()
        
        self.result = [] 
        self.output = self.cursor.execute("""SELECT * FROM projects""").fetchall()
        
        for i in self.output:
            self._jsSerial = {'project_name':i[0], 'init_date':i[1] , 'template':i[2]}
            self.result.append(self._jsSerial)
        
        return self.result

    def addNewItem(self , args):
        self._initializeDb()
        self.query = """
            INSERT INTO projects VALUES (? , ? , ? ,?)
        """
        self.cursor.execute(self.query , args)
        self.conn.commit()

    def removeItem(self):
        pass
