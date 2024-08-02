import time
import random

def greetings():
    print('Hello from greetings')
    return 'Hello'

def get_5_numbers():
    nums = list(range(5))
    time.sleep(random.choice(int(range(1,11)/10)))
    print(nums)
    return nums


grettings_2 = greetings
# grettings_2()

# print(greetings)
# print(grettings_2)


def decorator(fn_variable):
    print('decorator print')
    return fn_variable()

# greetings()

# decorator(greetings)
# decorator(get_5_numbers)


# start_time = time.time()
# time.sleep(3)
# end_time = time.time()
# print(end_time - start_time)



def time_decorator(fn):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
        return result

    return wrapper

@time_decorator  # get_5_numbers = time_decorator(get_5_numbers)
def get_5_numbers():
    nums = list(range(5))
    time.sleep(random.choice(range(1, 11))/10)
    # print(nums)
    return nums


def do_twice(fn):
    def wrapper(*args, **kwargs):

        result = fn(*args, **kwargs)
        print(f'first_res: {result}')
        result = fn(*args, **kwargs)
        print(f'second_res: {result}')
        return result

    return wrapper


@do_twice  # calculate_sum_2_numbers = do_twice(time_decorator(calculate_sum_2_numbers(a, b)))
@time_decorator  # calculate_sum_2_numbers = time_decorator(calculate_sum_2_numbers(a, b))
def calculate_sum_2_numbers(a, b):
    time.sleep(random.choice(range(1, 11))/10)
    return a + b




# get_5_numbers = time_decorator(get_5_numbers)
# print(get_5_numbers())
calculate_sum_2_numbers(5, 12)


