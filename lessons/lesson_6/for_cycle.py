# break
# continue


# iterable object

name_list = ['Den', 'Alex', 'Ivan']
second_names = ['Fedorov', 'Alexeev']
age_list = [10, 20, 30]
#
# for name in name_list:
#     print(f"name is {name}")
#
#     for age in age_list:
#         print(f'age is like {age}')

name = 'Mor'
#
# for k in name_list:
#     print(f"name is {k}")
#
#     for k in second_names:
#         print(f'Second_name {k}')
#
#     print(f'{k}')
#     print('------')
#
# print(name)
#
# for name in name_list:
#     print(f"name is {name}")



# # for _ in range(5, 10): # for k in (5,6,7,8,9)
# for _ in range(10):  # for k in (0,1,2,3,4,5,6,7,8,9)
#     print('Hello')

user_data = {'name': 'Denys', 'position': 'AQA'}

users_data = [
    ('Denys', 'AQA', 30, True), # name, Position, Age, Is_fired
    ('Alex', 'QA', 20, False),
    ('Mor', 'PM', 20, False),
]
#
# for user in users_data:
#     name, _, _, is_fired = user
#
#     print(f'Is {name}  fired? {is_fired}')


data = list(user_data.items())

new_dict = []
# for k in user_data.items():
#     key = k[0]
#     value = k[1]
#     new_dict[key] = value

# for name, pos, age, is_fired in users_data:
#     print(name)
#     print(is_fired)
#
# print('---------------')
# for user in users_data:
#     print(user[0])
#     print(user[-1])


# for index in range(len(users_data)):  # from 0 to len(users_data) -1
#
#     name = users_data[index][0]
#     age = users_data[index][2]
#
#     print(name, age)