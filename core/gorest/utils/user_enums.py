from enum import Enum


class Statuses(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'


class Gender(Enum):
    MALE = 'male'
    FEMALE = 'female'


# for 3.12
#
# from enum import StrEnum
#
# class Gender(StrEnum):
#     MALE = 'male'
#     FEMALE = 'female'
#
# value = Gender.MALE  # for StrEnum
# value = Gender.MALE.value # for Enum and StrEnum