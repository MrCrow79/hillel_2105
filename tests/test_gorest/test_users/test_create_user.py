from pytest import mark
from core.gorest.assertations.user_asserations import assert_user_was_created_response
from core.gorest.utils.user_enums import Statuses, Gender
from tests.test_gorest.conftest import BaseUser
from tests.test_gorest.test_users.conftest import GorestCreateUserBase
from utils.faker_utils import faker


class TestCreateUserGender(GorestCreateUserBase):

    @mark.gorest_23
    @mark.parametrize('gender', list(Gender))
    def test_create_user(self, gender, user_name):
        data = {"name": user_name,
                "gender": gender.value,
                "email": faker.email(),
                "status": Statuses.ACTIVE.value}

        response = self.gorest_ctrl.create_users(data)

        assert_user_was_created_response(data, response.json())

        __class__._user_ids.append(response.json()['id'])  # додаю запис id в змінну класу


class TestCreateUserStatus(GorestCreateUserBase):

    @mark.gorest_23
    @mark.parametrize('status', list(Statuses))
    def test_create_user(self, status, user_name):
        data = {"name": user_name,
                "gender": Gender.MALE.value,
                "email": faker.email(),
                "status": status.value}

        response = self.gorest_ctrl.create_users(data)

        assert_user_was_created_response(data, response.json())

        __class__._user_ids.append(response.json()['id'])  # додаю запис id в змінну класу
