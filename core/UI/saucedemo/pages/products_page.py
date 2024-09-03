from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

from core.UI.saucedemo.base_page import BaseSauceDemoPage
from utils.wait_utils import WaitForNElements


class ProductsPage(BaseSauceDemoPage):
    PRODUCT_DESCRIPTION = (By.XPATH, "//*[@*='inventory_item_description']")
    SORTING_SELECTOR = (By.XPATH, "//select[@class='product_sort_container']")
    SORTING_SELECTOR_LOW_HIGH_VALUE = (By.XPATH, "//option[@value='lohi']")
    SORTING_SELECTOR_HIGH_LOW_VALUE = (By.XPATH, "//option[@value='hilo']")
    ITEM_PRICE = (By.XPATH, "//*[@data-test='inventory-item-price']")
    ADD_TO_CARD_BUTTON = (By.CLASS_NAME, "btn_small")
    BUCKET_ITEMS_COUNTER = (By.XPATH, "//*[@data-test='shopping-cart-badge']")

    def __init__(self, driver: webdriver):   # page url = base_url + inventory.html
        super().__init__(driver=driver, page_part_of_url='inventory.html')
        print('ProductsPage has address ', self.url)

    def get_one_product(self):
        self._element_is_present(locator=self.PRODUCT_DESCRIPTION, timeout=3)
        return self

    def wait_all_product_on_a_page(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(WaitForNElements(count_of_elements=6))
        return self

    def set_sorting_by_price(self, sort_type: str):

        if sort_type not in ('asc', 'desc'):
            raise AttributeError('set_sorting_by_price:sort_type should be asc or desc')

        sort_locator = self.SORTING_SELECTOR_LOW_HIGH_VALUE
        if sort_type == 'desc':
            sort_locator = self.SORTING_SELECTOR_HIGH_LOW_VALUE

        self.click_on_element(self.SORTING_SELECTOR)
        self.click_on_element(sort_locator)
        return self

    def collect_item_prices(self):
        els = self.collect_visible_elements(self.ITEM_PRICE)

        return [k.text for k in els]

    def add_to_card_n_product(self, n=1):
        self.click_on_element(self.ADD_TO_CARD_BUTTON, element_number=n)

        return self

    def get_quantity_of_products_in_bucket(self):
        try:
            return int(self.collect_visible_elements(self.BUCKET_ITEMS_COUNTER)[0].text)
        except TimeoutException:
            return 0
