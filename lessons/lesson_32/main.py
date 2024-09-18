#
# from pytest import fixture, mark
#
# @fixture(scope='session')
# def some_fx():
#     return 'some_text'
#
#
# @fixture()
# def some_fx2(some_fx):
#     text = some_fx
#
#     return text * 2
#
#
# @mark.parametrize('first_number', [1,2,3], ids=['one', 'two', 'three'])
# @mark.parametrize('second_number', [4,5,6])
# def test_fixture(first_number, second_number):
#     print(first_number * second_number)


# Напишіть тест який перевіряє, що запит на  get users повертаеться мінімум 5 юзерів ?

# def  test_get_5_or_more_users():
#
#     response = request.get(url)
#     assert response.status_code == 200
#     assert len(response.json()) >= 5

# напишіть функцію яка перевіряє чи є число простим
def is_simple(num):

    if num in (0, 1):
        return True

    if num < 1:
        return None

    for k in range( num):
        if num / k == int(num/k):  # 5.2 == 5, 2.0 == 2
            return False

    return True


# напишіть функцію яка приймає словник, а повертає список унікальних значень для ключів цього словника.
# Для простоти словним в якості значення може мати тільки int та str

dict_ = {'name': 'Denys', 'age': 32, 'teeth': 32}  # -> ['Denys', 32]

def return_unique_values(dct):
    values_set = set()

    for k in dct.values():
        values_set.add(k)

    return list(values_set)

# print(return_unique_values(dict_))


# відсортуейте список від найбільшого до найменшого( список містить тільки числа)
# відсортуйте список від найбільшо до найменгого числа, всі None винесіть вперед(списк містить числа та None)

lst = [1,2,4,None, 2,6, None]

lst_without_nones = [k for k in lst if k is not None]
lst_nones = [k for k in lst if k is None]


print(lst_nones + sorted(lst_without_nones, reverse=True))



