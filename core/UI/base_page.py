from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure

from utils.logger_utils import logger

class BasePage:

    def __init__(self, driver, page_part_of_url, base_url):  # was: (driver, url), is : (driver, page_part_of_url, base_url)

        self.driver = driver
        self.base_url = base_url  # ���� ������� � ���������� �� env(dev, stage, prod)
        self.page_part_of_url = page_part_of_url  # �� ���� �������
        self.url = self.base_url + self.page_part_of_url

    def open(self):
        logger.info(f"Opening {self.url}")
        self.driver.get(self.url)
        return self

    def is_current_page_open(self):
        return self.driver.current_url == self.url

    def _element_is_present(self, locator, timeout):
        return WebDriverWait(self.driver, timeout=timeout).until(
            EC.presence_of_element_located(locator)
        )

    def _elements_are_presents(self, locator, timeout):
        return WebDriverWait(self.driver, timeout=timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def _element_is_clickable(self, locator, timeout):
        return WebDriverWait(self.driver, timeout=timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def send_keys_to_input(self, locator: tuple, data: str, timeout=3):

        element = self._element_is_present(locator=locator, timeout=timeout)
        element.send_keys(data)

    def click_on_element(self, locator: tuple, element_number=1, timeout=3):
        elements = self._elements_are_presents(locator, timeout=timeout)

        if not 1 <= element_number <= len(elements):
            raise AttributeError(f'Can\t find {element_number} element in elements. count = len({len(elements)})')

        element = self._element_is_clickable(elements[element_number-1], timeout=3)
        element.click()

    def collect_visible_elements(self, locator: tuple, timeout=3):

        return self._elements_are_presents(locator=locator, timeout=timeout)