from tests.example_file_1 import say_hello  # візьми функцію say_hello із файла tests.example_file_1


def greeting(name):
    print(f'Greetings {name}')

if __name__ == '__main__':
    greeting('Den')
    say_hello('Ivan')