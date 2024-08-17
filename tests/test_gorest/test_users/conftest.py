import os

from tests.test_gorest.conftest import BaseUser
from pytest import fixture

from faker import Faker


class GorestCreateUserBase(BaseUser):

    faker = Faker()


    @fixture
    def for_exmple_of_usefixture(self):
        if os.environ['WORKING_ENV'] == 'dev':
            print('for_exmple_of_dev_usefixture is running')
        if os.environ['WORKING_ENV'] == 'stage':
            print('for_exmple_of_stage_usefixture is running')

    @fixture
    def for_exmple_of_dev_usefixture(self):
        print('for_exmple_of_dev_usefixture is running')


    @fixture
    def for_exmple_of_stage_usefixture(self):
        print('for_exmple_of_stage_usefixture is running')

    # @fixture(scope='session')  # by default  (scope='function', autouse=False)
    # def user_name(self):
    #     return self.faker.user_name()
