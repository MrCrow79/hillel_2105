my_name = 'Denys'

first_char = my_name[0]  # D, string

# print(my_name[2])  # доступ до елемента
# print(['a', 'b', 'c'][2])
#
#
# print(my_name[0] + my_name[1] + my_name[2])
# print(my_name[0:3])  # з 0 по 3й невключно 3, [0, 3)

# string[first:second:step]
some_string = 'The London is  capital'
# print(some_string[4:10])
# print(some_string[0:10])
# print(some_string[:10])
# print(some_string[0:10:5])
# print(some_string[10:0:-1])
# print(some_string[10:-1:-1])
# print(some_string[10:])
# print(some_string[:10])
# print(some_string[::-1])
# print(some_string[10::-1])

# print(some_string[-1])  # останній

# print(len(some_string))  # return int
#
# print(len(some_string) > 0)  # bool(some_string), if some_string: == if len(some_string) > 0
# print(len('') > 0)
# print(bool(some_string))
# print(bool(''))


# print(some_string)
# print(some_string[:10])
# print(some_string[5])  # символ з ідексом 5
# print(type(some_string.split(' ')), some_string.split(' '))   # split = розрізати
# print(some_string.split(' ')[-1])
# print(type(some_string))
#
#
# for k in some_string:
#     print(k)

some_variable = None
some_variable_2 = ''
some_variable_3 = []

my_town = None

if my_name == 'Alex':
    my_town = 'Odesa'
    my_name = my_name + ' Guy'

# print('My town ' + my_town)
print('bool(None) ', bool(None))

if some_variable:  # bool(some_variable) is False, bool(some_variable) == False
    ...  # do nothing

# if some_variable is None # id(some_variable) == id(None)

some_list = [1,2]

if some_list == [1, 2]:
    print('Done')

if some_list is [1, 2]:
    print('WellDone')

print(id(some_list))
print(id([1, 2]))