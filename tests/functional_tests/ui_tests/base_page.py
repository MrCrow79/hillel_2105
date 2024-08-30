from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage:

    def __init__(self, driver, url):

        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)
        return self

    def is_current_page_open(self):
        return self.driver.current_url == self.url

    def _element_is_present(self, locator, timeout):
        return WebDriverWait(self.driver, timeout=timeout).until(
            EC.presence_of_element_located(locator)
        )

    def _element_is_clickable(self, locator, timeout):
        return WebDriverWait(self.driver, timeout=timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def send_keys_to_input(self, locator: tuple, data: str, timeout=3):

        element = self._element_is_present(locator=locator, timeout=timeout)
        element.send_keys(data)

    def click_on_element(self, locator: tuple, timeout=3):

        element = self._element_is_clickable(locator=locator, timeout=timeout)
        element.click()