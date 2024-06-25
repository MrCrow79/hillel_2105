import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

# str(pathlib.Path(__file__))  - шлях до поточного(цього) файлу

# print(str(pathlib.Path(__file__)))
# print(str(pathlib.Path(__file__).parent.parent))

# from test_fundtions import factorial


# CamelCase
class ImportExampleTest(unittest.TestCase):  # test suite

    def test_factorial_5(self):
        self.assertEqual(factorial(5), 120)


if __name__ == '__main__':  # якщо запущейний цей файл то :
    unittest.main()
