import logging

st_handler = logging.StreamHandler()
fl_handler = logging.FileHandler('example_code_config.log')

st_handler.setLevel(logging.DEBUG)
fl_handler.setLevel(logging.ERROR)

st_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
fl_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(message)s'))


logging.basicConfig(level=logging.DEBUG,
                    handlers=[
                        st_handler,  # send logs to the cmd/terminal
                        fl_handler  # write logs to the file
                    ])


logger = logging.getLogger(__name__)
#
# logger.debug('Asd DEBUG')
# logger.info('Asd INFO')
# logger.error('Asd Error')

# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)