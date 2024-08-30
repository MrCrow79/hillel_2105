from core.UI.saucedemo.login_page import LoginPage


def test_login_standard_user(url, user_password, user_name, driver):

    product_page = LoginPage(driver).open().login(user_name=user_name, user_password=user_password)

    assert product_page.is_current_page_open(), f'page {product_page.url} is not opened'
    product_page.get_one_product().wait_6_product_on_a_page()
