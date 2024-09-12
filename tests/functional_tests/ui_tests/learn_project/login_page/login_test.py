import allure

from core.UI.saucedemo import LoginPage

# from . import LoginPage


@allure.epic('UI tests')
@allure.feature('SauseDemo')
@allure.story('SauseDemo New version Login')
def test_login_standard_user(get_logged_in_product_page):

    product_page = get_logged_in_product_page

    assert product_page.is_current_page_open(), f'page {product_page.url} is not opened'
    product_page.get_one_product().wait_6_product_on_a_page()

    product_page.set_sorting_by_price_asc()
    prices = product_page.collect_item_prices()


