# import datetime
#
# print(datetime.timezone)
# print(datetime.UTC)
# print(datetime.datetime)
# print(datetime.datetime.now())

from datetime import datetime

from utils.date_utils import DateUtils

# print(datetime.now())
# print(datetime.now().date())
# print(datetime.now().hour)
# print(datetime.now().minute)


# print(datetime.now().tzinfo)
# print(datetime.now().tzinfo)
# print(datetime.UTC)  # AttributeError: type object 'datetime.datetime' has no attribute 'UTC'


dt_in_str = '2024-08-06 19:06:35.459687'

from_iso_obj = datetime.fromisoformat('2024-06-08 19:06:35.459687')
from_iso_obj = datetime.fromisoformat('2024-06-08 19:06:35.459687')

# print(from_iso_obj)
# print(from_iso_obj.month)

# %Y - Рік у форматі з чотирма цифрами (наприклад, 2023).
# %y - Рік у форматі з двома цифрами (наприклад, 23).
# %m - Місяць у числовому форматі (01-12).
# %B - Повна назва місяця (наприклад, січня).
# %b або %h - Скорочена назва місяця (наприклад, січ.).
# %d - День місяця у числовому форматі (01-31).
# %A - Повна назва дня тижня (наприклад, понеділок).
# %a - Скорочена назва дня тижня (наприклад, пн).
# %H - Година у 24-годинному форматі (00-23).
# %I - Година у 12-годинному форматі (01-12).
# %p - AM або PM.
# %M - Хвилини (00-59).
# %S - Секунди (00-59).
# %f - Мікросекунди (000000-999999).
# %z - Зона часу UTC з або без знака + або -.
# %Z - Назва часового поясу або абревіатура (наприклад, UTC, EST).
# %j - День року у числовому форматі (001-366).
# %U - Номер тижня у році, де неділя - перший день тижня (00-53).
# %W - Номер тижня у році, де понеділок - перший день тижня (00-53).
# %c - Дата та час у локальному форматі.
# %x - Дата у локальному форматі.
# %X - Час у локальному форматі.

date = '8-13-24 PM 5:06:35'

print(DateUtils.get_datetime_from_str(date))

from_non_iso_obj = datetime.strptime('2024-06-08 19:06:35.459687', "%Y-%d-%m %H:%M:%S.%f")
#
#
# print(from_non_iso_obj)
# print(from_non_iso_obj.month)
#
# from_iso_obj = datetime.fromisoformat('2024-06-08 19:06:35.459687')
#
# print(from_iso_obj)
# print(from_iso_obj.month)



#
# class A:
#
#     def __init__(self):
#         self.a_prop = 10
#
# class B:
#
#     def __init__(self):
#         self.b_prop = 20
#         self.a_instance = A()
#
#
# b = B()
# print(b.a_instance.a_prop)