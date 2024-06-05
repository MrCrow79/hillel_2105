string_1 = 'Hillel is school'

if ('Hillel' in string_1) is True:  # return bool ==> (True) is True
    print('1 Hillel in string')

if ('Hillel' in string_1) is False:  # return bool ==> False is True ==> False
    print('2 Hillel in string')

if 'Hillel' in string_1:  # return bool, ==> True
    print('3 Hillel in string')

if 'Hillel' in string_1 is True:  # the same is  1 + 2*8, string_1 is True returns True
    print('4 Hillel in string')
#
# if 'Hillel' in (string_1 == True):  # ==> 'Hillel' in True
#     print('4 Hillel in string')
