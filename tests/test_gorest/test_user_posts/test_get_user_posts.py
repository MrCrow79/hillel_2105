from core.gorest.assertations.posts_assrtation import get_posts_assertations
from tests.test_gorest.test_user_posts.conftest import GorestUserPosts


class TestGetUserPost(GorestUserPosts):

    def test_get_user_posts(self, created_user, created_post):
        user_id = created_user.get('id')

        posts = self.gorest_ctrl.get_user_posts(user_id=user_id)

        get_posts_assertations(post_data=created_post, response_data=posts.json(), user_id=user_id)







