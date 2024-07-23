from datetime import datetime
import time



cur_year = 2024
next_year = 2025


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


__all__ = ['cur_year']