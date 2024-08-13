from pytest import fixture
from core.gorest.gorest_ctrl import GorestCtrl

import logging


class BaseUser:
    _user_ids = []
    gorest_ctrl = GorestCtrl()
    logger = logging.getLogger(__name__)

    @fixture(scope='session', autouse=True)
    def clear_user_from_system(self):
        yield

        self.logger.info('Teardown was started')

        for user in __class__._user_ids:
            self.logger.info(f'Deleting user {user}')
            self.gorest_ctrl.delete_user(user)

