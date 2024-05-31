fruits = 'apple, banana, apple, pineapple, apple'

# print(fruits.replace('apple', ''))

fruits_without_apples = []  # ['banana', 'pineapple']
list_of_all_fluits = fruits.split(',')

for fruit in list_of_all_fluits:  # or ', ' or fruit.strip()
    fruit = fruit.strip()  # delete whitespaces
    if fruit != 'apple':
        fruits_without_apples.append(fruit.strip())  # add to list

fruits_without_apples_string = ', '.join(fruits_without_apples)
print(f'We have next fruits: {fruits_without_apples_string}')
print(f'We have next fruits: {'|'.join(['1', '2', '3', '4'])}')
print(f'Print chars: {'|'.join('asdasdasdasdas')}')

# ', '.join(['banana', 'pineapple']) = >
# ', '.join(fruits_without_apples_string) = >
# fruits_without_apples_string[0] + ', ' + fruits_without_apples_string[1]
