# file_ = open('for_reading.txt')  # відкрити файл для читання
# data = file_.read()  # return string
# print(data)
#
# file_.close()
#
#
# # ___ open() __   <=>        = file_ |  file_ = open('for_reading.txt')
# with open(r'for_reading.txt') as file_:  # відкрити файл
#     data = file_.read()
#     print(data)
#     raise AttributeError  #  файл все одно закриється
#
# print('Done')

# try:
#     file_ = open('for_reading.txt')  # відкрити файл для читання
#     data = file_.read()  # return string
#     print(data)
#
# finally:
#     file_.close()

with open(r'for_reading.txt', 'r') as file_:  # r, w, rw, a, rb, wb, ab
    data = file_.read()

# print(data)

with open(r'new_for_writing.txt', 'w') as file_:  # create file and write
    file_.write('first row')

with open(r'new_for_writing.txt') as file_:
    new_data = file_.read()
    print(new_data)

with open(r'new_for_writing.txt', 'w') as file_:  # re-create file and write
    file_.write('second row')

with open(r'new_for_writing.txt') as file_:
    print(file_.read())

with open(r'new_for_writing.txt', 'a') as file_:  # add to end of file if file exist or crete file and add text
    file_.write('\nthird row')

with open(r'new_for_writing.txt') as file_:
    print(file_.read())


print(new_data.upper())

# import os
# #
# os.remove(r'new_for_writing.txt')  # видалення файлу
# os.rmdir() # видалення диеркторії
# print(data)
