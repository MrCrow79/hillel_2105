import os

from tests.test_gorest.conftest import BaseUser
from pytest import fixture

from faker import Faker


class GorestUserPosts(BaseUser):

    @fixture
    def created_post(self, created_user):
        body = {
            "title": 'fixture create post_title',
            "body": "fixture text of user_post"
        }
        return self.gorest_ctrl.create_post(user_id=created_user.get('id'), post_body=body).json()