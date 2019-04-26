import argument_parser
import controler
import extend
import template_engine
from tuberegister import mainTube

import time
from uuid import uuid4

def main():

    controler.prepareForStart()
    consoleArgs = argument_parser.argumentParser().parseIt()
    projecId = uuid4()

    if consoleArgs.action == 'start':
        jsSettings = extend.parseSettings()
        engine = template_engine.templateExpander(jsSettings)
        engine.understandSettings()
        if controler.check_status() == False:
            mainTube().addNewItem([jsSettings['name'] , time.strftime('%c') , jsSettings['template'] ,str(projecId)])
            controler.logInLocalFolder(str(projecId))
            print('\033[32m' + 'Creating was succssesful complete')
        else:
            print('Project just exists')
    
    elif consoleArgs.action == 'delete':
        if controler.check_status() == True:
            mainTube().removeItem(controler.return_local_id())
            template_engine.removeAll()
        else:
            print('The project does not exists. Nothing to delete')
    
    else:
        print('\033[33m' + 'The argument is not valid')

if __name__ == "__main__":
    main()