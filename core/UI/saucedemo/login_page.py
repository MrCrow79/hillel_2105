import os
from selenium.webdriver.common.by import By

from tests.functional_tests.ui_tests.base_page import BasePage
from core.UI.saucedemo.products_page import ProductsPage



# class HeaderElement:
#
#     def __init__(self):
#         self.base_element = By.XPATH, '//div[@class="primary_header"]'
#         self.backet = ''


class LoginPage(BasePage):
    USER_NAME_INPUT = (By.XPATH, "//*[@data-test='username']")

    USER_PASSWORD_INPUT = (By.XPATH, "//*[@data-test='password']")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver=driver, url=os.environ['HOME_PAGE'])

    def fill_user_name(self, user_name):
        self.send_keys_to_input(locator=self.USER_NAME_INPUT, data=user_name, timeout=5)
        return self

    def fill_user_password(self, user_password):
        self.send_keys_to_input(locator=self.USER_PASSWORD_INPUT, data=user_password, timeout=4)
        return self

    def click_login_button(self):
        self.click_on_element(self.LOGIN_BUTTON)
        return ProductsPage(self.driver)

    def login(self, user_name, user_password):
        return self.fill_user_name(user_name).fill_user_password(user_password).click_login_button()

