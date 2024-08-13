from assertpy import assert_that, soft_assertions, soft_fail


def assert_user_was_created_response(request_data, response_data):

    with soft_assertions():
        for key in request_data:
            assert_that(request_data[key],
                        f'Data is not equal: {request_data[key]} != {response_data.get(key)}'
                    ).is_equal_to(response_data.get(key))

        assert_that(response_data.get('id')).is_instance_of(int)
        assert_that(response_data.get('id')).is_greater_than(0)

        if response_data.get('some_filed') is not None:
            soft_fail('Custom text of error')

        response_keys = list(response_data.keys())
        expected_keys = [k for k in request_data]
        expected_keys.append('id')

        assert_that(sorted(expected_keys), 'response has extra_keys').is_equal_to(sorted(response_keys))