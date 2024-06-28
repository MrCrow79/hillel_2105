import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)
logging.getLogger('').addHandler(console_handler)


logging.debug('MSG level: DEBUG')
logging.info('MSG level: INFO')
logging.warning('MSG level: WARNING')
logging.error('MSG level: ERROR')
logging.critical('MSG level: CRITICAL')