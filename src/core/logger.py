import logging.config
import logging
import os


def logg():
    home = os.path.expanduser('~')
    print(home + '/.trivvy/logger/logger.log')
    logging.config.fileConfig(home + '/.trivvy/logger/logger.conf')
    logger = logging.getLogger(home + '/.trivvy/logger/logger.log')
    logger.info('hello i`m work')
    logger.error('not fine')
    print('fine')