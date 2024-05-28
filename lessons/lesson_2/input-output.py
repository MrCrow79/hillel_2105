# some_variable = 'The {my_city} is the capital of {my_country}, {my_city} is big'
#
# city = input('input_city: ')  # string
# country = input('input_country: ')  # string
#
# print(some_variable.format(my_country=country, my_city=city))  #  output

my_age = input('input your age: ')  # string

print(type(my_age), my_age)

print(f'In 20 years you\'ll be {int(my_age) + 20}')