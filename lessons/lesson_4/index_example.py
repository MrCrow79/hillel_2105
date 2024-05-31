string_1 = 'My name is serge. I\'m a QA. I\'m working in Hillel company|'
# e

sub_srt = string_1
curr_index = -1

for char in string_1:
    index = sub_srt.find('e')
    if index != -1:  # if -1 not found in string_1
        curr_index = curr_index + index + 1
        print(curr_index, string_1[curr_index])

        sub_srt = sub_srt[index + 1:]  # slice

x = 10
y = 23
sum_x_y = y + x  # якщо надалі використовувати
print(f'sum is {sum_x_y}')

print(f'Your answer is: \n'
      f'sum is {sum_x_y}')
