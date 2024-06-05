unsorted_list = [1,2,3,6,5,4]
# print(unsorted_list)
# unsorted_list.sort()
# print(unsorted_list)
# unsorted_list.sort(reverse=True)
# print(unsorted_list)

# new_list = sorted(unsorted_list)
# new_list_reverse = sorted({3,2,1,5,76}, reverse=True)
# print(unsorted_list)
# print(new_list_reverse)

lst_of_strs = ['asd', 'dd', 'GSD', 'aaaaaa', 'cc', 'Asad']

print(sorted(lst_of_strs))
print(sorted(lst_of_strs, reverse=True))

def get_len(sent):  # function, if lambda ==> lambda sent: len(sent)
    return len(sent)
#
# for s in lst_of_strs:
#     print(f'{s} has len', get_len(s))

# lambda function анонімні функції

print(sorted(lst_of_strs, key = lambda sent: len(sent), reverse=True))  # sorting of list of numbers

names = ['Vlad', 'Den', 'V', None, '']
names = [k for k in names if k]  # list comprehantion
print(names)





