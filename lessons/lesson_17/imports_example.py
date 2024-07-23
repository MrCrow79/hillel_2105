import utils.date_utils
#
#
# utils.date_utils.DateUtils.get_next_year()
#
from utils.date_utils import DateUtils

import pytest
import os
import requests

# print(cur_year)
#
# DateUtils.get_next_year()


# from utils.date_utils import *  #  import all
# from utils.date_utils import DateUtils
# cur_year
# DateUtils.get_next_year()
# print(cur_year)

import pytest


from pytest import mark

from utils.assert_companies import AssertCompanies
from utils.company_schema import CompanySchema
from lessons.lesson_16.abstract import Animal, Cat


print(dir([]))
print([k for k in dir([]) if not k.startswith('__')])
print(dir(Cat))
print([k for k in dir(Animal) if not k.startswith('__')])
print([k for k in dir(Cat) if not k.startswith('__')])

print(Cat.mro())
