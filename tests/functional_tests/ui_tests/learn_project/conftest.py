import os

import pytest
from selenium import webdriver

from core.UI.saucedemo import LoginPage


@pytest.fixture(scope='session')
def user_name():
    return "standard_user"


@pytest.fixture(scope='session')
def user_password():
    return "secret_sauce"


@pytest.fixture(scope='session')
def driver():
    return webdriver.Chrome()


@pytest.fixture()  # scope='function' by default
def one_test_driver():
    return webdriver.Chrome()


@pytest.fixture(scope='session')
def get_logged_in_product_page(driver,user_name, user_password):
    return LoginPage(driver).open().login(user_name=user_name, user_password=user_password)
