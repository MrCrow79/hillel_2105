# with open(path_to_file, mode):

some_row = 'some new row'
pi_ = 3.14
file_name = 'file_4_writing.txt'

def return_greetings(name):
    return f'Hello mr./ms. {name}'


#
# with open(file_name, mode='w') as f:  # the same as with open(file_name, 'w') as f
#     f.write('first_row\t')
#     f.write("""second line
#     last line""")
#     f.write("\n\" 'second line'  \"\n"
#             "last line\n\n")
#     f.write(some_row)
#     f.write('\n\n')
#     f.write(str(pi_))
#     f.write('\n\n')
#     f.write(return_greetings('Alex'))
#
#     f.writelines(['\nwritelines 1', '\nwritelines 2', '\nwritelines 3'])

# with open('new' + file_name, 'r') as read_file:
#     text = read_file.readlines()
#
# print(text)
# print('-'*80)
#
# with open('new' + file_name, 'a') as append_to_file:
#     append_to_file.write('\nappend_mode')
#
# with open('new' + file_name, 'r') as read_file:
#     text = read_file.readlines()
#
# print(text)



#text[3].find('a') # index
# a_in_3_index = text[2].find('e')
# text_from_3_to_5 = ''.join(text[2:5])
# print(text_from_3_to_5)
# text_a_in_3_with_index = text_from_3_to_5[max(a_in_3_index, 0):]
#
# b_in_6_index = text[5].find('o')
# text_6_row = text[5][:b_in_6_index]
# result = text_a_in_3_with_index + text_6_row
# result = result.replace('\n', ' ')
# print('-'*80)
# print(result)


# with open('file_4_reading.txt', 'r', encoding='UTF-8') as f:
#     x = f.read()

