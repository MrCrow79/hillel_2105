from core.gorest.assertations.posts_assrtation import post_was_created
from tests.test_gorest.test_user_posts.conftest import GorestUserPosts
from assertpy import soft_assertions, assert_that


class TestCreateUserPost(GorestUserPosts):

    def test_create_post(self, created_user):
        body = {
            "title": 'create post_title',
            "body": "text of user_posts"
        }
        resp = self.gorest_ctrl.create_post(user_id=created_user.get('id'), post_body=body).json()

        post_was_created(request_data=body, response_data=resp, user_id=created_user.get('id'))
