import pytest


class TestUserData:

    user_id = 10
    related_users = []

    @pytest.fixture(autouse=True)
    def prepare_data(self):

        # user_ids = request.....
        __class__.related_users.append(22)  # append(user_ids)
        __class__.new_user_id = 10

    def test_base_user(self):
        assert __class__.user_id == 10
        __class__.user_id = 11
        print(__class__.user_id)

    def test_related_users(self):
        assert len(__class__.related_users) > 0
