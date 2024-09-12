import os

import allure

from core.UI.saucedemo.base_page import BaseSauceDemoPage
from core.UI.saucedemo.elements.login_page_elements import LoginPageElements
from core.UI.saucedemo.pages.products_page import ProductsPage


class LoginPage(BaseSauceDemoPage):

    def __init__(self, driver):
        super().__init__(driver=driver, page_part_of_url='')  # page url = base_url
        self.elements = LoginPageElements

    @allure.step(f'Open Login page')
    def open(self):
        return super().open()


    @allure.step('Filling user name {user_name}')
    def fill_user_name(self, user_name):
        self.send_keys_to_input(locator=self.elements.USER_NAME_INPUT, data=user_name, timeout=5)
        return self

    @allure.step('filling user password')
    def fill_user_password(self, user_password):
        self.send_keys_to_input(locator=self.elements.USER_PASSWORD_INPUT, data=user_password, timeout=4)
        return self

    @allure.step('click login button')
    def click_login_button(self):
        self.click_on_element(self.elements.LOGIN_BUTTON)
        return ProductsPage(self.driver)

    def login(self, user_name, user_password):
        return self.fill_user_name(user_name).fill_user_password(user_password).click_login_button()

