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
def chrome_options():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    chrome_options.browser_version = "114"
    return chrome_options


@pytest.fixture(scope='session')
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)

    return driver


@pytest.fixture()  # scope='function' by default
def one_test_driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    return driver


@pytest.fixture(scope='session')
def get_logged_in_product_page(driver, user_name, user_password):
    return LoginPage(driver).open().login(user_name=user_name, user_password=user_password)
