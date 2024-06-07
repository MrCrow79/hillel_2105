
# while умова

# while True:  нескінченний цикл


is_found_10 = False

# print('start')
# while not is_found_10:  # while True by default
#     print('new try')
#     for k in range(20):  # from 0 to 19
#         if k == 10:
#             is_found_10 = True
#             print(f'{k} found, While Done')
#             break
#         print(f'{k} not found')
#     print('finish try')
# print('Finish')


counter = 0
while True:
    # get data from kafka
    # if response from kafka is bad an error
    # break

    counter += 1

    if counter > 10:
        break


# for k in range(0, 10, 2): # start, end - 1, step
#     print(k)