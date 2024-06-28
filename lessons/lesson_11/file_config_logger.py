import logging.config

logging.config.fileConfig(r'..\..\logger_config.ini')


logger = logging.getLogger('sampleLogger')

logger.error('log message level: ERROR')
logger.debug('log message level: DEBUG')
logger.info('log message level: INFO')
logger.critical('log message level: CRITICAL')