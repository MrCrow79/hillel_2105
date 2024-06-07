# age = input('Set your age')  # age is string

# print(age)

# list_of_names = ['Den', 'Yuri', '', None, 24, 'Al']
#
# real_names = []
# for name in list_of_names:
#     if isinstance(name,  str): # return True is type(name) is string else False, or if type(name) is str
#         if len(name) > 0:
#             real_names.append(name)
# print(real_names)
#
# real_names = []
# for name in list_of_names:
#     if name and type(name) is str: # if name return False if name in ['', None, False, 0, [], {}]
#         real_names.append(name)
# print(real_names)
#
# real_names = [n*2 for n in list_of_names if n and type(n) is str]  # [що_додавати for змінна in список]
# div_3_numbers = [n for n in range(500) if n%3 == 0]  # числа, що діляться на 3
#
# print(div_3_numbers)


positions = [
    {
        'Position': 'QA',
        'Age': 30,
        'Expir': 6
    },
    {
        'Position': 'QA',
        'Age': 29,
        'Expir': 6
    },
    {
        'Position': 'QA',
        'Age': 40,
        'Expir': 14
    },
    {
        'Position': 'PM',
        'Age': 30,
        'Expir': 1
    },
    {
        'Position': 'AQA',
        'Age': 25,
        'Expir': 3
    },
    {
        'Position': 'AQA',
        'Age': 25,
        'Expir': 1
    },
]

# positions = [p for p in positions if p['Age'] >= 30]
# print(positions)

dict_comprehension = {p['Position']: (p['Age'], p['Expir']) for p in positions}  # {key: value for elem in iterable}

dict_second = {}
for p in positions: # p is dict
    position = p.get('Position')  # value of p['Position']
    age = p.get('Age')
    exp = p.get('Expir')
    dict_second[position] = (age, exp)


print(dict_comprehension)
set_comprehension = {}  # {n*2 for n in list_of_names if n and type(n) is str} as list comprehension but set
tuple_comprehension = ()  # (n*2 for n in list_of_names if n and type(n) is str) as list comprehension but tuple

new_position =     \
    {
        'Position': 'QA',
        'Age': 30,
        'Expir': 6
    }

new_position_dict_2 = {k: v for k, v in new_position.items()}
# new_position == new_position_dict_2
