from core.gorest.assertations.posts_assrtation import post_was_created
from core.gorest.utils.user_enums import Gender, Statuses
from tests.test_gorest.test_user_posts.conftest import GorestUserPosts
from assertpy import soft_assertions, assert_that
from tests.test_gorest.conftest import faker


class TestGorestE2E(GorestUserPosts):
    user_data = {"name": 'E2e user name',
                 "gender": Gender.MALE.value,
                 "email": faker.email(),
                 "status": Statuses.ACTIVE.value}
    post_data = {
            "title": 'e2e create post_title',
            "body": "e2e text of user_posts"
        }

    def test_gorest_e2e(self):

        user = self.gorest_ctrl.create_users(json=self.user_data).json()
        # assert_user_was_created_response(data, response.json())
        user_id = user.get('id')

        self.gorest_ctrl.create_post(user_id=user_id, post_body=self.post_data).json()
        # post_was_created(request_data=body, response_data=resp, user_id=created_user.get('id'))

        self.gorest_ctrl.get_user_posts(user_id=user_id)
        # assert that post is returned

        self.gorest_ctrl.delete_user(user_id=user_id)
        # assrt that user was deleted
