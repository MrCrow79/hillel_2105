import pytest

import logging


logger = logging.getLogger(__name__)

# Визначення фікстури з параметром params
@pytest.fixture(params=[1, 2, 3])
def user_data_parametrized(request):
    param_value = request.param
    logger.info('user_data_parametrized info')
    print(f"sending_request for data of user {request.param}...")
    return param_value * 2


# Приклад використання фікстури у тесті
def test_using_fixture(user_data_parametrized):
    print(f"Test with fixture value: {user_data_parametrized}")
    assert user_data_parametrized % 2 == 0


def get_user_data(user_id):
    print(f"sending_request for data of user {user_id}...")
    return user_id * 2


@pytest.mark.parametrize('user_id', [1, 2, 3])
def test_without_using_fixture(user_id):
    data = get_user_data(user_id)
    print(f"Test with fixture value: {data}")
    assert data % 2 == 0
