from typing import Any


# def name_of_function():  # ми створюемо змінну  name_of_function і її викликате через name_of_function()

def say_hello():
    return 'Hello!'

# world = say_hello()
# print(world)


def get_square(number: int) -> int:
    return number ** 2


# print(get_square(5))

# def division(a: int | float, b= 2) -> float:
def division(a: int | float, b: int | float = 2) -> float:
    # a/b
    return a/b

#
# res = division(1, 3)
# print(res)
#
#
# res = division(1, 2)
# print(res)
#
#
# res = division(1)
# print(res)


def print_user_info(user_name, user_position, user_age=30):

    print(f'{user_name} is a(n) {user_position} and {user_name} is {user_age}')


# print_user_info('Den', 'AQA', 20)
# print_user_info(user_position='AQA', user_name='Den')
# print_user_info('Den', user_age=20, user_position='AQA')


# def multiply(num_1, num2=3):
#     print(num_1 * num2)
#     print('Print after return')
#
#     # return None
#
# result = multiply(2, 5)
# print(result)
# print(multiply(3, 5))


# name = 'Den'
# second_name = 'Merezhkin'
#
#
# def print_name_without_args():
#     second_name = 'new_second_name'
#     print(name, second_name)
#
#
# def print_name_with_args(name):
#     # вже існує змінна name
#     print(name, second_name)
#
#
# # print_name_without_args()
# # print_name_with_args('Alex')
# # print_name_without_args()
#
#
# def calc_with_2_numbers(num1, num2, operation='*'):
#     def make_math():
#
#         # action = {
#         #     '+': num1 + num2,
#         #     '-': num1 - num2,
#         #     '/': num1 / num2,
#         #     '*': num1 * num2
#         # }
#         # print(action)
#         # return action[operation]
#
#         if operation == '+':
#             return num1 + num2
#
#         elif operation == '*':
#             return num1 * num2
#
#         elif operation == '/':
#             return num1 / num2
#
#         elif operation == '-':
#             return num1 - num2
#
#     return make_math()
#
# num1, num2 = 10, 20
# operation = '-'
#
# print(calc_with_2_numbers(2, 3))
# print(calc_with_2_numbers(2, 3, '+'))
# print(make_math(2,3, '+'))