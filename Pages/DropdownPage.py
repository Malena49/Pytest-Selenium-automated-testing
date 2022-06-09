import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class DropdownPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    SELECT = (By.ID, 'dropdown')
    OPTION_DEFAULT = (By.CSS_SELECTOR, 'option[disabled="disabled"]')
    OPTION_1 = (By.CSS_SELECTOR, 'option[value="1"]')
    OPTION_2 = (By.CSS_SELECTOR, 'option[value="2"]')

    def get_url(self):
        self.driver.get(TestData.BASE_URL + '/dropdown')

    def select_option_1(self):
        self.do_click(self.SELECT)
        self.do_click(self.OPTION_1)

    def is_option_1_selected(self):
        return self.is_selected(self.OPTION_1)

    def select_option_2(self):
        self.do_click(self.SELECT)
        self.do_click(self.OPTION_2)

    def is_option_2_selected(self):
        return self.is_selected(self.OPTION_2)

    def get_default_option(self):
        return self.get_element_text(self.OPTION_DEFAULT)
