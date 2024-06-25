import unittest

from test_functions_new import factorial


# CamelCase
class FactorialPositiveTest(unittest.TestCase):  # test suite

    def test_factorial_5(self):

        expected_result = 120
        input_params = 5

        self.assertEqual(factorial(input_params), expected_result)

    def test_factorial_0(self):

        expected_result = 1
        input_params = 0

        self.assertEqual(factorial(input_params), expected_result)

    def test_factorial_1(self):

        expected_result = 1
        input_params = 1

        self.assertEqual(factorial(input_params), expected_result)



if __name__ == '__main__':  # якщо запущейний цей файл то :
    unittest.main()
