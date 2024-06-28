from test_functions_new import find_primes
import pytest
from utils.logger_utils import logging


@pytest.mark.parametrize('number,expected_result', [
    (1, []),
    (5, [2, 3, 5]),
    (24, [2, 3, 5, 7, 11, 13, 17, 19, 22])
], ids=[1, 5, 24])
def tc_find_primes_positive(number, expected_result):
    logging.info(f'start test tc_find_primes_positive with {number} '
                f'param and {expected_result} expected result')
    result = find_primes(number)

    if result != expected_result:
        logging.critical(f'test failed expected {expected_result} != actual {result}')
    assert result == expected_result
