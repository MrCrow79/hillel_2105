from test_functions_new import find_primes
import memory_profiler

# def get_n_numbers_divided_by_3(n):  # yield
#     start = 1
#     list_of_numbers = []
#     while len(list_of_numbers) < n:
#         if start % 3 == 0:
#             list_of_numbers.append(start)
#         start += 1
#
#     return list_of_numbers
#
# def get_n_numbers_divided_by_3(n):  # yield
#     start = 1
#     count = 0
#     while count < n:
#         if start % 3 == 0:
#             count += 1
#             yield start
#         start += 1
#
#
# for number in get_n_numbers_divided_by_3(1000):
#
#     # long logic
#     print(number)



# def get_5_numbers():  # generator, because we have yield

    # for k in range(1, 6):
    #     print(f'return {k}')
    #     yield k
    #
    # print('return 1')
    # yield 1
    # print('return 2')
    # yield 2
    # print('return 3')
    # yield 3
    # print('return 4')
    # yield 4
    # print('return 5')
    # yield 5


# iter_ = iter(get_5_numbers())  # iter() for generator returns iterator object
#
# print(next(iter_))
# print(next(iter_))
# print(next(iter_))

# import random
#
# def create_random_row():
#     for k in 1000:
#         yield {'id': random.choice(range(50000000)), 'name': 'Test_user'}


# import time
#
# start = time.time()
# mem = memory_profiler.memory_usage()[0]
#
#
# gen_compr = (find_primes(k) for k in range(3000))
# list_compr = [find_primes(k) for k in range(3000)]
#
# for k in gen_compr:
#     print(k)
#
# print(time.time() - start)
# print(memory_profiler.memory_usage()[0] - mem)
