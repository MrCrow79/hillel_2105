from assertpy import assert_that, soft_assertions, soft_fail


def post_was_created(request_data, response_data, user_id):

    with soft_assertions():
        assert_that(response_data['id']).is_not_none()
        assert_that(response_data['user_id']).is_equal_to(user_id)
        assert_that(response_data['title']).is_equal_to(request_data['title'])
        assert_that(response_data['body']).is_equal_to(request_data['body'])

        response_list_of_keys = [k for k in response_data if k not in ('id', 'user_id')]

        assert_that(sorted(request_data), 'response has extra_keys').is_equal_to(sorted(response_list_of_keys))