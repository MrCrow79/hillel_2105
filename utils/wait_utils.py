from datetime import datetime

from selenium.webdriver.common.by import By


class WaitForNElements:
    def __init__(self, by=By.XPATH, locator='//div[@class="inventory_item"]', count_of_elements=6):
        self.by = by
        self.locator = locator
        self.count = count_of_elements

    def __call__(self, driver):

        # ми перев≥р€Їмо чи Ї на екран≥ n продукт≥в
        try:
            print(f'{datetime.utcnow()}: Waiting for {self.count} elements')
            element = driver.find_elements(by=self.by, value=self.locator)  # «находимо елемент
            print(element)
            if len(element) == self.count:
                return True
            else:
                return False
        except:
            return False  # якщо елемент не знайдено або не в≥дображаЇтьс€, повертаЇмо False
