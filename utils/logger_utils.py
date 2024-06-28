import logging

st_handler = logging.StreamHandler()
fl_handler = logging.FileHandler('errors.log')

st_handler.setLevel(logging.DEBUG)
fl_handler.setLevel(logging.ERROR)

st_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
fl_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(message)s'))


logging.basicConfig(level=logging.DEBUG,
                    handlers=[
                        st_handler,
                        fl_handler
                    ])


logger = logging.getLogger(__name__)