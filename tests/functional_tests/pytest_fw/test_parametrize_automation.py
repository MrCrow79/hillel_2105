import pytest

from test_functions_new import convert_to_24_hour

input_ = ('1:00 AM', '12:00 AM', '12:59 AM', '11:59 AM')# , '1:01 AM')
expected = ('01:00', '00:00', '00:59', '11:59')# , '01:00')

io_params = list(zip(input_, expected))
# [('1:00 AM', '1:00'), ('12:00 AM', '12:00'), ('12:59 AM', '12:59'), ('11:59 AM', '11:59'), ('1:01 AM', '1:01')]


@pytest.mark.convert_time
@pytest.mark.parametrize('input_,expected', [
    ('1:00 AM', '01:00'), ('12:00 AM', '00:00'),
    ('12:59 AM', '00:59'), ('11:59 AM', '11:59'),
    ('01:01 AM', '1:00')],
                         ids=['asd1', 'asd2', 'asd1', 'asd2', 'last'])
def tc_convert_to_24_hour_am_positive_all(input_, expected):

    if input_ == '01:01 AM':
        pytest.skip('known issue with 1 minute')

    assert expected == convert_to_24_hour(input_), f'Incorrect converting {input_}'


@pytest.mark.convert_time
@pytest.mark.parametrize('input_,expected', io_params, ids=['asd1', 'asd2', 'asd1', 'asd2'])
def tc_convert_to_24_hour_am_positive(input_, expected):

    # input_ = ('1:00 AM', '12:00 AM', '12:59 AM', '11:59 AM', '1:01 AM')
    # expected = ('1:00', '12:00', '12:59', '11:59', '1:01')

    assert expected == convert_to_24_hour(input_), f'Incorrect converting {input_}'


@pytest.mark.convert_time
@pytest.mark.xfail()
def tc_convert_to_24_hour_am_positive_1_01_am():
    assert '1:01' == convert_to_24_hour('1:01 AM'), f'Incorrect converting {'1:01 AM'}'


# def tc_convert_to_24_hour_pm_positive():
#     pass
#
#
# def tc_convert_to_24_hour_incoorect_type_negative():
#     pass
#
#
# def tc_convert_to_24_hour_incoorect_value_negative():
#     pass