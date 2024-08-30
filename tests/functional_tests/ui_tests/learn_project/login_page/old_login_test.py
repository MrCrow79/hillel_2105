from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.wait_utils import WaitForNElements

url = "https://www.saucedemo.com/"
user_name = "standard_user"
password = "secret_sauce"

driver = webdriver.Chrome()


def test_login_standard_user():
    # driver.implicitly_wait(10)  # неявне очікування 10 секунд
    driver.get(url)

    # user_name_input = driver.find_element(By.XPATH, "//*[@data-test='username']")


    # explicit wait
    user_name_input = WebDriverWait(driver, timeout=5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@data-test='username']")))

    user_passwrd_input = driver.find_element(By.XPATH, "//*[@data-test='password']")
    login_button = driver.find_element(By.ID, "login-button")

    user_name_input.send_keys(user_name)
    user_passwrd_input.send_keys(password)
    login_button.click()

    all_cookies = driver.get_cookies()  # dict fo cookies

    get_domain_cookie = driver.get_cookie('session-username') # -> dict
    driver.get_cookies()
    value_get_domain_cookie = driver.get_cookie('session-username')['value']

    set_user_cookie = driver.add_cookie({'name': "user_cookie", 'value': 'user_value'})

    current_url = driver.current_url
    driver.find_element(By.XPATH, "//*[@*='inventory_item_description']")

    assert current_url.endswith('inventory.html')

    wait = WebDriverWait(driver, 10)
    wait.until(WaitForNElements())


#
# def test_login_standard_user(login_page):
#
#     products_page = login_page.login_standart_user()
#     products_page.check_is_open()
