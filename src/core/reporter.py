# i made the dict logger config, cause the config from .conf file cant find the file in home folder/
# the basic path to logging - the project folder , it`s not cool
# P.S if  instrested i did it from first try

import logging.config
import logging
import os
import sys

HOME_FOLDER = os.path.expanduser('~')
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
        "cuteLittlePanda":{
            "handlers": ["fileHandler"],
            "level": "INFO"
        }
    }
}


def report(message):
    logging.config.dictConfig(CONFIG_STRUCT)
    logger = logging.getLogger('cuteLittlePanda')
    logger.info(message)