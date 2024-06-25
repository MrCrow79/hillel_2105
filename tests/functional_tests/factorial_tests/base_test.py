import unittest


def add(a, b):
    return a + b


# CamelCase
class GetCompaniesTest(unittest.TestCase):  # test suite

    def test_get_companies_first_page(self):   # test case
        result = add(1, 2)
        self.assertEqual(result, 3)  # assert result == 3, return None or AssertationError
        self.assertAlmostEqual(1, 4, delta=3)

    def test_get_companies_default_values(self):  # snake_case
        result = add(3, 4)
        self.assertEqual(result, 3, msg=f'Expected resutl = 3, but actual = {result}')

        # assert result == 3,

    def test_comparing_list_of_dicts(self):  # snake_case

        expected = [{
            'id': 10,
            'name': 'Yuri',
            'age': 25
        },{
            'id': 10,
            'name': 'Yuri',
            'age': 25
        },{
            'id': 10,
            'name': 'Yuri',
            'age': 25
        }]

        actual = [{
            'id': 10,
            'name': 'Yuri',
            'age': 25
        }, {
            'id': 11,
            'name': 'Yuri',
            'age': 25
        }, {
            'id': 10,
            'name': 'Yuria',
            'age': 25
        }]
        # result = add(3, 4)
        self.assertEqual(expected, actual, msg=f'Lists are not equal')

        # assert result == 3,


if __name__ == '__main__':  # якщо запущейний цей файл то :
    unittest.main()
