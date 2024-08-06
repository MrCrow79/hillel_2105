from datetime import datetime
import time



cur_year = 2024
next_year = 2025


class DateUtils:


    date_formats = ["%Y-%m-%d %H:%M:%S.%f", "%Y-%d-%m %H:%M:%S.%f", "%m-%d-%y %p %I:%M:%S"]

    def __init__(self):
        # time.sleep(5)  # wait 5 sec
        self.cur_class_name = 'DataUtils'


    @classmethod
    def get_datetime_from_str(cls, dt: str):

        for index in range(len(cls.date_formats)):
            try:
                return datetime.strptime(dt, cls.date_formats[index - 1])
            except ValueError:
                pass
        return ValueError(f'unknown format of {dt}')

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


    @staticmethod
    def compare_two_dates(bigger_date, less_date):
        return bigger_date > less_date


    @staticmethod
    def compare_3_dates(bigger_date, medium, less_date):
        return bigger_date > medium > less_date


    @staticmethod
    def difference_in_hours(dt_1: datetime, dt_2: datetime):

        # 1 day = 24 hours
        # 1 hour = 60*60 seconds

        res = (dt_1 - dt_2)

        return res.days*24 + res.seconds/60/60


__all__ = ['cur_year']