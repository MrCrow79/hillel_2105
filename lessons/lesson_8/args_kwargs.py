def sum_numbers(*args):

    return sum(args)


list_of_number = [1,2,5,8,7,4]

# asd, asd2, *others, asd_1 = list_of_number
# asd = list_of_number[0]
# asd2 = list_of_number[1]
# others = list_of_number[2:-1]
# asd_1 = list_of_number[-1]
#
# print(asd)
# print(asd2)
# print(others)
# print(asd_1)
#
# print(sum_numbers(1,2,5,8,7,4))
#
# print(sum_numbers(*list_of_number))
#
# print(*list_of_number)  # == print(1,2,5,8,7,4)


# def print_greetings(name, part_of_the_day):
#
#     print(f'Hello {name}, have a nice {part_of_the_day}')
#
# print_greetings('Den', 'Evening')
# print_greetings(name='Den', part_of_the_day='Evening')
# print_greetings(**{'name': 'Den', 'part_of_the_day': 'Evening'})  # print_greetings(name='Den', part_of_the_day='Evening')


def print_greetings(name, part_of_the_day='Morning'):

    print(f'Hello {name}, have a nice {part_of_the_day}')



def append_one(lst = None): # {}
    # if lst is None:
    #     lst = []

    lst = lst or []  # if bool(lst): lst = lst else lst = []
    lst.append(1)
    return lst


lst1 = [1,2,3]
print(append_one(lst1))
print(append_one(lst1))
print(append_one())
print(append_one())




