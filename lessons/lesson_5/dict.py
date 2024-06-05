# my_dict = {
#     'key': 'value',
#     'key_2': 'value 2',
#     'key_2': 'value 3',  # перезапишу попереднє значення
#     True: 'value',
#     5: 'value',
#     None: 'value',
#     'key_3': {'key_3': [1,2,3]},
#     'key_4': {'new_key_4': [1,2,3]},
#     # [1, 2, 3]: 'value' не може бути ключем
# }

# print(my_dict)
# print(my_dict['key_2'])
# print(my_dict['key_3'])
# value_of_key_4 = my_dict['key_4'] # my_dict['key_4'] returns {'new_key_4': [1,2,3]}
# value_of_new_key_4 = value_of_key_4['new_key_4']
# print(value_of_new_key_4) # == print(my_dict['key_4']['new_key_4'])
# print(my_dict['key_4']['new_key_4']) # my_dict['key_4'] returns {'new_key_4': [1,2,3]}


phones = {
    'iPhone': ['10s', '13'],
    'samsung': ['A20', 'S23']
}

# get values
print(phones['iPhone'])
# print(phones['iPhone1'])
print(phones.get('iPhone'))
print(phones.get('iPhone1'))  # None by default
print(phones.get('iPhone1', 'There is no iPhones1'))  # returns string 'There is iPhones1'

# create
my_dict_2 = dict()  # create empty dict
my_dict_3 = dict([(1, 2), (3, 4)])

# print(my_dict_2)
# print(my_dict_3)
#
# # add value
#
# my_dict_2['new_key'] = 'new_value'
# print(my_dict_2)
#
# my_dict_2.update({'update_key': 'update_value', 'update_key_2': 'update_value'})
# print(my_dict_2)

snt = 'The weather is fine'

counter = {}
counter1 = {}

for char in snt:
    current_value = counter1.get(char, 0)  # current value or 0 if key doesn't exist in dict
    new_value = current_value + 1
    counter1[char] = new_value

    # counter1[char] = counter1.get(char, 0) + 1

for char in snt:

    if char not in counter:
        counter[char] = 0

    if char in counter:
        counter[char] += 1

# print(counter)
# print(counter1)


for key in counter:  # iterate by keys
    print(f'Char {key} is {counter[key]} in sentence')

for value in counter.values():
    print(f'some char was in sentence {value} times')

for key in counter.keys():
    print(f'{key} was in sentence n times')

for first, second in counter.items():  # ==> for key, value
    print(f'{first} was in sentence {second} times')


item = counter.pop('e')  # by key, not index
print(item)
print(counter)

# get user
user = [
    {'Name': 'Ivan', 'age': 20},
    {'Name': 'Vlad', 'age': 30}
]
