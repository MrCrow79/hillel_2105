import os

from core.UI.base_page import BasePage
from utils.setting_utils import settings


class BaseSauceDemoPage(BasePage):

    def __init__(self, driver, page_part_of_url):
        super().__init__(driver=driver,
                         base_url=settings[os.environ['WORKING_ENV']]['SAUCE_DEMO_HOME_PAGE'],
                         page_part_of_url=page_part_of_url)
