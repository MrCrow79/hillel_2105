from pytest import fixture
from core.gorest.gorest_ctrl import GorestCtrl

import logging
from faker import Faker

from core.gorest.utils.user_enums import Statuses, Gender

faker = Faker()


@fixture(scope='session')  # by default  (scope='function', autouse=False)
def user_name():
    return faker.user_name()

@fixture(scope='session')
def created_user(user_name):
    data = {"name": user_name,
            "gender": Gender.MALE.value,
            "email": faker.email(),
            "status": Statuses.ACTIVE.value}

    user = BaseUser.gorest_ctrl.create_users(data).json()
    yield user

    BaseUser.gorest_ctrl.delete_user(user.get('id'))


@fixture(scope='session', autouse=True)
def clear_user_from_system():
    yield

    BaseUser.logger.info('Teardown was started')

    for user in BaseUser._user_ids:
        BaseUser.logger.info(f'Deleting user {user}')
        BaseUser.gorest_ctrl.delete_user(user)
    BaseUser._user_ids = []


class BaseUser:
    _user_ids = []
    gorest_ctrl = GorestCtrl()
    logger = logging.getLogger(__name__)
