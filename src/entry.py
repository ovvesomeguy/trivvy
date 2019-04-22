import argument_parser
import controler
import expand
import template_engine
from tuberegister import mainTube

import time
from uuid import uuid4

def main():
    controler.prepareForStart()
    jsSettings = expand.parseSettings()
    consoleArgs = argument_parser.argumentParser().parseIt()
    engine = template_engine.templateExpander(jsSettings)

    tube = mainTube()
    if consoleArgs.action == 'start':
        engine.understandSettings()
        mainTube().addNewItem([jsSettings['name'] , time.strftime('%c') , jsSettings['template'] ,str(uuid4())])
        if jsSettings['integrate']:
            if jsSettings['integrate'] == 'true':
                tube.returnAllProjects()
    elif consoleArgs.action == 'delete':
        engine.removeAll()
    else:
        print('\033[33m' + 'The argument is not valid')
