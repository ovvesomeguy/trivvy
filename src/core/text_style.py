import shutil
import sys

class outputFormatter():
    def __init__(self, message , color='' , marker=' ' , start='' , end='' , bold = False):
        self.userColor = color
        if len(self.userColor) == 0:
            self.currentColor = '\033[37m'
        else:
            if self.userColor in self.colorsArray:
                self.currentColor = self.colorsArray[self.userColor]
            else:
                print('Key Error: This color does not found')
                sys.exit()
        self.bold = bold
        self.message = message
        self.marker = marker
        self.start = start
        self.end = end
        self.main()

    colorsArray = {
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34M',
        'white': '\033[37M',
        'cyan': '\033[36m',
        'magenta': '\033[35m',
    }

    def main(self):
        print(self.changeColor(self.center()))

    def changeColor(self , message):
        if self.bold == True:
            return '\033[1m'  + self.currentColor + message + '\033[0M'
        else:
            return  self.currentColor + message + '\033[0M'

    def center(self):
        _terminalSize = shutil.get_terminal_size()
        _allCountOfIndent = _terminalSize.columns - len(self.message) - len(self.start + self.end)
        countIndentForOneSide = int(_allCountOfIndent / 2)
        if len(self.marker) is not 0:
            currentCount = int(countIndentForOneSide / len(self.marker))
        else:
            sys.exit()
        # return message without changing color
        return str(self.start + currentCount*self.marker + self.message + currentCount*self.marker + self.end)

outputFormatter('Very very long centered message, really long', 
                color='magenta', 
                marker='-', 
                start='/',
                end='\\',
                bold=True
)