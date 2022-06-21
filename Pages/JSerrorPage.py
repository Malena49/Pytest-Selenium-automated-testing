from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class JSerrorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_url(self):
        self.driver.get(TestData.BASE_URL + '/javascript_error')

    def get_browser_log(self):
        return self.get_browser_javascript_log()

