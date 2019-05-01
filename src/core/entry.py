import trivvy.src.core.argument_parser as argument_parser
import trivvy.src.core.controler as controler
import trivvy.src.core.extend as extend
import trivvy.src.core.template_engine as template_engine
import trivvy.src.core.reporter as reporter
from trivvy.src.integrate.tuberegister import mainTube

import time
from uuid import uuid4

def main():
    print('hey')
    controler.prepareForStart()
    consoleArgs = argument_parser.argumentParser().parseIt()
    projecId = uuid4()
    if consoleArgs.action == 'start':
        controler.createSettings()
        reporter.report('| I`m started |')
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