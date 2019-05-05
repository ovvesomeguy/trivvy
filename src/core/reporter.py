import logging.config
import logging
import os

LOGGER_ADDR = os.getcwd() + '/.trivvy/logger/logger.log'
LOGGER_STRUCT = {
    "version": 1,
    "handlers":{
        "fileHandler":{
            "class": "logging.FileHandler",
            "formatter": "myFormatter",
            "filename": LOGGER_ADDR
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
    logging.config.dictConfig(LOGGER_STRUCT)
    logger = logging.getLogger('cuteLittlePanda')
    logger.info(message)