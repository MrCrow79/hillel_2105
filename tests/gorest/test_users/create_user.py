from pytest import mark
from core.gorest.assertations.user_asserations import assert_user_was_created_response
from core.gorest.utils.user_enums import Statuses, Gender
from tests.gorest.conftest import BaseUser
from utils.faker_utils import faker


class TestCreateUser(BaseUser):

    @mark.gorest_23
    @mark.parametrize('gender', list(Gender))
    @mark.parametrize('status', list(Statuses))
    def test_create_user(self, status, gender):
        data = {"name": "Tenali Ramakrishna",
                "gender": gender.value,
                "email": faker.email(),
                "status": status.value}

        response = self.gorest_ctrl.create_users(data)

        assert_user_was_created_response(data, response.json())

        __class__._user_ids.append(response.json()['id'])  # додаю запис id в змінну класу
