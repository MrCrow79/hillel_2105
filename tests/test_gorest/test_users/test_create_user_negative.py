from pytest import mark

from core.gorest.utils.user_enums import Statuses
from tests.test_gorest.test_users.conftest import GorestCreateUserBase
from utils.faker_utils import faker


class TestCreateUserNegative(GorestCreateUserBase):

    @mark.gorest_23
    @mark.parametrize('gender', [None, '1', -1, 3.14])
    # @mark.usefixtures(f"for_exmple_of_{os.environ['WORKING_ENV']}_usefixture")
    def test_create_user_negative(self, gender, user_name, for_exmple_of_usefixture):
        data = {"name": user_name,
                "gender": gender,
                "email": faker.email(),
                "status": Statuses.ACTIVE.value}

        self.gorest_ctrl.create_users(data, status_code=422)
