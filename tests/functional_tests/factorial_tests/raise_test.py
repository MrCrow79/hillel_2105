import unittest


def div(a, b):
    # int('asd')
    return a / b


# CamelCase
class RaisesTest(unittest.TestCase):  # test suite

    def test_division_with_raise(self):

        # is_catch = False
        # try:
        #     div(1, 1)
        # except ZeroDivisionError as err:
        #     is_catch = True
        #
        # assert is_catch, 'ZeroDivisionError was not raised '
        with self.assertRaises(ZeroDivisionError):
            res = div(1, 0)


if __name__ == '__main__':  # якщо запущейний цей файл то :
    unittest.main()
