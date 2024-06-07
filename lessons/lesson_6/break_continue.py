# break
# continue

# positions = ['QA', 'AQA', 'PM', 'DEV']
#
# for pos in positions:
#     if pos != 'PM':
#         print(pos)
#         # do some stuff

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

# for pos in positions:
#
#     if pos['Position'] != 'PM':
#
#         if pos['Age'] > 30:
#             print('More than 30')
#             print(pos)
#
#         elif pos['Expir'] > 5:
#             print('5 yars expirience under 30')
#             print(pos)
#
#         elif pos['Expir'] >= 3:
#             print('3 yars expirience under 30')
#             print(pos)
#
#         else:
#             print('Has less than 3 year exp')
#             print(pos)

# for pos in positions:  # всіх з (досвідом більше 5 АБО  віком більше 30) ТА (не PM)
#
#
#     if pos['Position'] == 'PM':
#         continue  # йди до цикла for і бери наступний елемент
#
#     print('--------------')
#
#     if pos['Expir'] > 5:
#         print('5 yars expirience under 30')
#         print(pos)
#         continue
#
#     if pos['Age'] > 30:
#         print('More than 30')
#         print(pos)

# for pos in positions:  # першого з (досвідом більше 5 АБО  віком більше 30) ТА (не PM)
#
#     if pos['Position'] == 'PM':
#         continue  # йди до цикла for і бери наступний елемент
#
#     print('--------------')
#
#     if pos['Expir'] > 5:
#         print('5 yars expirience under 30')
#         print(pos)
#         break
#
#     if pos['Age'] > 30:
#         print('More than 30')
#         print(pos)
#         break
#
# print('Done')