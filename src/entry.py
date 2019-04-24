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

    tube = mainTube()
    if consoleArgs.action == 'start':
        jsSettings = extend.parseSettings()
        engine = template_engine.templateExpander(jsSettings)
        engine.understandSettings()
        # mainTube().addNewItem([jsSettings['name'] , time.strftime('%c') , jsSettings['template'] ,str(uuid4())])
    elif consoleArgs.action == 'delete':
        template_engine.removeAll()
    else:
        print('\033[33m' + 'The argument is not valid')

if __name__ == "__main__":
    main()