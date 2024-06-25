import unittest

from test_functions_new import factorial


# CamelCase
class FactorialNegativeTest(unittest.TestCase):  # test suite

    def test_factorial_input_string(self):
        input_params = 'asd'
        with self.assertRaises(TypeError) as error:
            factorial(None)
        res = error.exception.args[0]
        self.assertEqual(res, "unsupported operand type(s) for -: 'str' and 'int'")

    def test_factorial_input_list(self):

        expected_message = "unsupported operand type(s) for -: 'list' and 'int'"
        input_params = []

        with self.assertRaises(TypeError, msg='msg example') as type_error:  # with open(path) as f: f.read()
            # factorial(5)    # raise AsserationError
            factorial(input_params)

        error = type_error.exception
        error_message = error.args[0]

        self.assertEqual(error_message, expected_message)


    def test_factorial_input_None(self):

        input_params = None
        expected_message = "unsupported operand type(s) for -: 'NoneType' and 'int'"


        with self.assertRaises(TypeError) as type_error:
            factorial(input_params)

        error = type_error.exception
        error_message = error.args[0]

        self.assertEqual(error_message, expected_message)


if __name__ == '__main__':  # якщо запущейний цей файл то :
    unittest.main()
