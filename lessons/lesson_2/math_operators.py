# first_number = 10
# second_number = 20
#
# print('Sum is', first_number + second_number)
#
# third_number = first_number + second_number
# third_number = third_number + 30  # == third_number += 30
# print('Sum is', third_number)
# third_number += 40
# print('plus 40 = ', third_number)
# third_number -= 25
# print('minus 25 = ', third_number)
#
# third_number *= 10  # == third_number = third_number * 10 == third_number 75 * 10
# print('mult 25 = ', third_number)

# float = 1.2
# int = 10

# print(10//3)
# print(10/3)  # int / int = float,  неявне зведення типів
#
float_number = 10.5
int_number = int(float_number) #, явне зведення типів
#
# print('float', float_number)
# print('int', int(float_number))
# print('int', int_number)
#
# # round - округлення
# print('my round', round(20/3, 1))  # round(number, символів після коми)

# str - string
# print(type(int_number))  # повертає тип змінної
# print(type(float_number))
# print(type('some_value'))

# print(str(20/3)[:5])
# my_value = f'{10 + 5}, 11, {str(round(20/3, 4))}'
# print(type(my_value), my_value)


# print(-7**2)  # pow, підведення в степінь
# import math
#
# print(math.pow(-7, 2))# pow, підведення в степінь


# print(20 % 3)  # 20/3 == 18 + 2 == 2

# bool: True False

my_age = 33
my_position = 'Manager'


is_real_age = my_age == 33  # return bool
is_real_position = my_position == 'AQA'   # return bool

# print('Type with expr', type(my_age == 33))
# print('Type with variable ', type(is_real_position))
# print('is_real_age', is_real_age)
# print('is_real_position', is_real_position)
#
# print('My age > 33', my_age > 33)
# print('My age < 33', my_age < 33)
# print('My age >= 33', my_age >= 33)
# print('My age <= 33', my_age <= 33)
#
# my_full_age = 33.5
# print('My full age >= 33', my_full_age >= 33)
# print('My full age <= 33', my_full_age <= 33)

# print(True and False)  # False
# print(False and False) # False
# print(True and True)  # True
# print(True or False) # True
# print(False or False) # False
# print(True or True) # True
#
# the_weather_is_fine = True
#
# if (my_age > 30 and my_position == 'AQA') or the_weather_is_fine == True:
#     print('Hello AQA after 30')
#
# if my_age > 30 or my_position == 'AQA':
#     print('Hello AQA or guy after 30')
#
#
# if my_age < 30 and my_position > 30:
#     print('Some value')
#
#
# True  # not False
# False  # not True
#
# if not (my_age > 30):  # if not (True) == if False
#     print('Hello AQA or guy after 30', 'asd', 132)
#
#
# value_1 = 2
# value_2 = 10
#
#
# my_review_1 = 'Blab-bla\nsome info\\t some_info_2'
# my_review_2 = 'I don\'t want to do smth'
# my_review_3 = r'''Blab-bla
# some info\t some_info_2'''  # r = raw, сира строка
#
# print(my_review_1)
# print(my_review_3)

# my_name = "Denys"
# print(my_name)
# print(my_name + ' AQA')
# print(my_name, 'AQA')
#
# my_full_position = my_name + ' AQA ' + 'in Quantum'  # конкатинація
# print(my_full_position)
#
#
# counter = 53
# SEPARATOR = '-- '*counter
# print(SEPARATOR)
