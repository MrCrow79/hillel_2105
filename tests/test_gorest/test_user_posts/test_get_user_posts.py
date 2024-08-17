from pytest import mark
from core.gorest.assertations.user_asserations import assert_user_was_created_response
from core.gorest.utils.user_enums import Statuses, Gender
from tests.test_gorest.conftest import BaseUser
from tests.test_gorest.test_user_posts.conftest import GorestUserPosts
from tests.test_gorest.test_users.conftest import GorestCreateUserBase
from utils.faker_utils import faker
from assertpy import soft_assertions, assert_that


class TestGetUserPost(GorestUserPosts):

    def test_get_user_posts(self, created_user, created_post):
        user_id = created_user.get('id')

        posts = self.gorest_ctrl.get_user_posts(user_id=user_id).json()

        assert_that(len(posts),
                    f'Expected quantity of posts is more than 1, but actual is {len(posts)}').is_greater_than(0)

        filtered_post = [k for k in posts if k.get('id') == created_post.get('id')]

        assert_that(filtered_post).is_length(1)
        filtered_post = filtered_post[0]

        with soft_assertions():
            assert_that(filtered_post['id']).is_not_none()
            assert_that(filtered_post['user_id']).is_equal_to(user_id)
            assert_that(filtered_post['title']).is_equal_to(created_post['title'])
            assert_that(filtered_post['body']).is_equal_to(created_post['body'])


            assert_that(sorted(created_post), 'response has extra_keys').is_equal_to(sorted(filtered_post))







