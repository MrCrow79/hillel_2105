from assertpy import assert_that, soft_assertions, soft_fail


def assert_prices_are_sorted(prices, sort_type: str):

    if sort_type not in ('asc', 'desc'):
        raise AttributeError('assert_prices_are_sorted:sort_type must be in asc, desc')

    assert_that(prices, 'We expect prices for 6 products').is_length(6)

    float_prices = []

    with soft_assertions():

        for price in prices:
            if price.startswith('$'):  # price starts with $
                float_prices.append(float(price[1:]))  # add price as a number to special list
            else:
                soft_fail(f'We have price: {price}. It not started with $')

        assert_prices_are_more_than_1_usd(float_prices)

        reverse = False if sort_type == 'asc' else True

        assert_that(float_prices, 'Expected prices are sorted').is_sorted(reverse=reverse)


def assert_prices_are_more_than_1_usd(prices):
    with soft_assertions():
        for price in prices:
            assert_that(price).is_greater_than_or_equal_to(1)
