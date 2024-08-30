import os

import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def user_name():
    return "standard_user"


@pytest.fixture(scope='session')
def user_password():
    return "secret_sauce"


@pytest.fixture(scope='session')
def url():
    return os.environ['HOME_PAGE']


@pytest.fixture(scope='session')
def driver():
    return webdriver.Chrome()


@pytest.fixture()  # scope='function' by default
def one_test_driver():
    return webdriver.Chrome()
