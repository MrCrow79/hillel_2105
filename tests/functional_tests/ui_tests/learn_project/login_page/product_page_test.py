import pytest

from core.UI.saucedemo.assrtations.product_page_assrtations import assert_prices_are_sorted


@pytest.mark.parametrize('ordering', ['asc', 'desc'])  # asc from low to high
def test_product_page_items_is_sorted_by_price(get_logged_in_product_page, ordering):
    product_page = get_logged_in_product_page

    product_page.set_sorting_by_price(ordering)

    prices = product_page.wait_all_product_on_a_page().collect_item_prices()
    assert_prices_are_sorted(prices, sort_type=ordering)


def test_product_page_add_item_to_cart(get_logged_in_product_page):
    product_page = get_logged_in_product_page

    assert product_page.get_quantity_of_products_in_bucket() == 0
    product_page.add_to_card_n_product(1)
    assert product_page.get_quantity_of_products_in_bucket() == 1
