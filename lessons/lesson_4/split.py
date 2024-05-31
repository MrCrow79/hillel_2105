# spilt

string_1 = '  My name   is   Denys.   I\'m a  QA   '
string_2 = 'I\'m working with bugs. work, work, workwork, worrk'

# print(string_1.split(' '))
# print(string_1.split('  '))
# print(string_2.split('work'))

# print(string_2.split('work'))
# print(string_2)
# my_list_of_words = string_2.split('work')
# print(my_list_of_words)

print(string_1.split(' '))
print(string_1.split())


text = "one, two, three, four, five"
result = text.split(',', maxsplit=2)
print(result)