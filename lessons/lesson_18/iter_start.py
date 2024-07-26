# iter()
# next()
#

range(1000000000)
my_list = ['a', 'b', 'c', 'd']
iter_obj = iter(my_list)





#
#
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
#


def print_by_iterable_obj(obj):
    i = iter(obj)
    while True:
        try:
            print(next(i))
        except StopIteration:
            break

# my_list[5]
print_by_iterable_obj(my_list)
print('-'*10)

for k in my_list:
    print(k)

