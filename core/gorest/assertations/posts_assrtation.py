from assertpy import assert_that, soft_assertions


def post_was_created(request_data, response_data, user_id):

    with soft_assertions():
        assert_that(response_data['id']).is_not_none()
        assert_that(response_data['user_id']).is_equal_to(user_id)
        assert_that(response_data['title']).is_equal_to(request_data['title'])
        assert_that(response_data['body']).is_equal_to(request_data['body'])

        response_list_of_keys = [k for k in response_data if k not in ('id', 'user_id')]

        assert_that(sorted(request_data), 'response has extra_keys').is_equal_to(sorted(response_list_of_keys))


def get_posts_assertations(post_data, response_data, user_id):

    assert_that(len(response_data),
                f'Expected quantity of posts is more than 1, but actual is {len(response_data)}').is_greater_than(0)

    filtered_post = [k for k in response_data if k.get('id') == post_data.get('id')]

    assert_that(filtered_post).is_length(1)
    filtered_post = filtered_post[0]

    with soft_assertions():
        assert_that(filtered_post['id']).is_not_none()
        assert_that(filtered_post['user_id']).is_equal_to(user_id)
        assert_that(filtered_post['title']).is_equal_to(post_data['title'])
        assert_that(filtered_post['body']).is_equal_to(post_data['body'])

        assert_that(sorted(post_data), 'response has extra_keys').is_equal_to(sorted(filtered_post))