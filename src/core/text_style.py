import shutil
import sys

class myException(Exception):
    def __init__(self , text):
        pass

# message - array of lines
class consolePrettier:
    """List of aviable colors
<-- green -->,
<-- red -->,
<-- white-- >,
<-- yellow -->,
<-- blue -->,
<-- cyan -->,
<-- magenta -->"""
    colorsArray = {
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
    }
 

    def __init__(self, options , box=None):
        self._boxSet = box
        self.options = options
        self.formatOutput(self.__formatOptions())

    def __formatOptions(self):
        self.__formatedOptions = []
        if self._boxSet != None:
            for box_option in self.options:
                box_option['start'] = '|'
                box_option['end'] = '|'
                box_option['marker'] = self._boxSet['marker']
                box_option['color'] = self._boxSet['color']
        for option in self.options:
            if not 'message' in option:
                option['message'] = ''
            if not 'start' in option:
                option['start'] = ''
            if not 'end' in option:
                option['end'] = ''

            if not 'bold' in option:
                option['bold'] = ''
            elif option['bold'] == True:
                option['bold'] = '\033[1m'
            
            if not 'marker' in option:
                option['marker'] = ''
            elif option['marker'] == 'center':
                option['marker'] = ' '
            if not 'color' in option:
                option['color'] = 'white'
            self.__formatedOptions.append(option)
        return self.__formatedOptions
    
    def formatOutput(self , formated_list_of_options):
        for _ in formated_list_of_options:
            terminalSize = shutil.get_terminal_size().columns
            columnsCount = terminalSize - len(list(_['message'])) - len(_['start']) - len(_['end']) - len(_['marker'])
            indents = columnsCount / 2
            _message_for_print = _['start'] + int(indents) * _['marker'] + _['message'] + int(indents) * _['marker'] + _['end']
            indentsOffset = terminalSize - len(_message_for_print)
            print(
               self.colorsArray[_['color']]+
                _['bold']+
                _['start']+
                int(indents) * _['marker']+
                _['message']+
                int(indents + indentsOffset) * _['marker']+
                _['end']+
                '\033[0m'
                )
