# i made the dict logger config, cause the config from .conf file cant find the file in home folder/
# the basic path to logging - the project folder , it`s not cool
# P.S if  instrested i did it from first try

import logging.config
import logging
import os
import sys

HOME_FOLDER = os.path.expanduser('~')
CONFIG = HOME_FOLDER + '/.trivvy/logger/logger.conf'
LOGGER = HOME_FOLDER + '/.trivvy/logger/logger.log'

CONFIG_STRUCT = {
    "version": 1,
    "handlers":{
        "fileHandler":{
            "class": "logging.FileHandler",
            "formatter": "myFormatter",
            "filename": LOGGER
        }
    },
    "formatters":{
        "myFormatter":{
            "format":"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },
    "loggers": {
        "trivvyLogger":{
            "handlers": ["fileHandler"],
            "level": "INFO"
        }
    }
}

# degree 1 - info
# degree 2 - debug
# degree 3 - error
# degree CRITICAL - it`s cool way to broke your pc

def report(message):
    logging.config.dictConfig(CONFIG_STRUCT)
    logger = logging.getLogger('trivvyLogger')
    logger.info(message)