# args, kwargs

# sum()

# print(sum([1,25,7,8,7,7,28,5885]))

# def sum_all_elements(num1, num2, *args, last_number=0) -> int:  #
#     print(f'num1 {num1}')
#     print(f'num2 {num2}')
#     print(args)
#     sum = num1 + num2
#     for k in args:
#         sum += k
#
#     print(sum)
#     sum += last_number*2
#
#     return sum
#
#
# print(sum_all_elements(5, 10, 20, 50, last_number=3))

def sum_all_elements(num1, num2, *args, last_number=0, **kwargs) -> int:  # args = (), kwargs = {}
    print(f'num1 {num1}')
    print(f'num2 {num2}')
    print(args)

    num5 = 10

    if kwargs.get('name') is not None:
        print(f'Hello {kwargs.get('name')}')
    sum = num1 + num2
    for k in args:
        sum += k

    print(sum)
    sum += last_number*2

    return sum


print(sum_all_elements(5, 10, 20, 50,  value='40', last_number=3, asd='asd'))