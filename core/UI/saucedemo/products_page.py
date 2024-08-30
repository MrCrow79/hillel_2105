import os

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from tests.functional_tests.ui_tests.base_page import BasePage
from utils.wait_utils import WaitForNElements


class ProductsPage(BasePage):
    PRODUCT_DESCRIPTION = (By.XPATH, "//*[@*='inventory_item_description']")

    def __init__(self, driver: webdriver):
        super().__init__(driver=driver, url=f"{os.environ['HOME_PAGE']}inventory.html")

    def get_one_product(self):
        self._element_is_present(locator=self.PRODUCT_DESCRIPTION, timeout=3)
        return self

    def wait_6_product_on_a_page(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(WaitForNElements(count_of_elements=6))
