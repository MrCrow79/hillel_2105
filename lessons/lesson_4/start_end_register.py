string_1 = 'My name is Denys. I\'m a QA'
string_2 = 'My name is serge. I\'m a QA. I\'m working in some company'

# print('starts with My', string_1.startswith('My'))
# print('starts with Your', string_1.startswith('Your'))
# print('ends with QA', string_1.endswith('QA'))
# print('ends with PM', string_1.endswith('PM'))

# for word in string_2.split():  # spit by spaces -> list of words, ['My', 'name', 'is serge', ...]
#     if word.startswith('s'):
#         print(word)
# print('Done')

# for word in string_2:  # for each char
#     print(word)


string_3 = 'My name is serge. I\'m a QA. I\'m working in some company'
string_4 = string_3.lower()

#
# print(string_4)
# print(string_3.islower())

# print(string_3.upper())
# print(string_3.isupper())

# print(string_3)
# print(string_3.capitalize())

# print(string_3.split().istitle())  # => ['asd', 'asd', ..].istitle() => error
print(string_3.title())
print(string_3.istitle())
