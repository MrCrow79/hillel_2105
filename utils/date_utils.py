from datetime import datetime
import time


class DateUtils:

    def __init__(self):
        time.sleep(5)  # wait 5 sec
        self.cur_class_name = 'DataUtils'

    @staticmethod
    def get_current_year(data_string):
        if '-' in data_string:
            data = data_string.split('-')
            for k in data:
                if len(k) == 4:
                    return k
        else:
            return 'Cant find year'

    @staticmethod
    def get_next_year():

        return datetime.now().year + 1

