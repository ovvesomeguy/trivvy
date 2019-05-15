import shutil
import sys

class myException(Exception):
    def __init__(self , text):
        pass

class consolePrettier:
    """List of aviable colors red , green , white , yellow   blue , cyan , magenta"""
    colorsArray = {
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
    }

    def __init__(self , options=None):
        self.terminalWidth = shutil.get_terminal_size().columns
        self.__magicCheck(options)
    
    def __magicCheck(self , user_settings):
        if 'lay' in user_settings[0]:
            self.layout = user_settings[0]['lay']
            self.layout_color = user_settings[0]['box-color']
            self.box_header = user_settings[0]['header']
            self.header_color = user_settings[0]['header-color']
            self.inBox(user_settings[1:] , header=self.box_header , box_color=self.layout_color , header_color=self.header_color)

    def countIndents(self , startLen=0 , endLen=0 , messageLen=0):
        aviableIndents = self.terminalWidth - startLen - endLen - messageLen
        leftIndents = int(aviableIndents / 2)
        indentsOffset = aviableIndents - leftIndents*2
        return {'left': leftIndents , 'right': leftIndents + indentsOffset}        

    def inBox(self , messages , header='' , box_color='white' , header_color = 'white'):
        currentIndents = self.countIndents(1 , 1 , len(list(header)))
        print(self.colorsArray[box_color]+ 
            '|' 
            + currentIndents['left']*'-' + 
            self.colorsArray[header_color] + header + self.colorsArray[box_color] + 
            '-'*currentIndents['right'] + 
            '|'+
            '\033[0m')
        for _ in messages:
            margin = self.countIndents(messageLen=len(_['message']))
            print(self.colorsArray[box_color] + '|' + '\033[0m'+ (margin['left']-1)*' ' + _['message'] + (margin['right']-1)*' ' + self.colorsArray[box_color] + '|' + '\033[0m')
        print(self.colorsArray[box_color] + '|' + '-'*(self.terminalWidth-2) + '|' + '\033[0m')
    

consolePrettier(options=[
    {'lay': 'box', 
     'box-color': 'yellow', 
     'header': 'Header here',
     'header-color': 'green'
    },
    {'message': 'first world'},
    {'message': 'second mesage'},
    {'message': 'third message'},
    {'message': 'Some really long message'}
])
