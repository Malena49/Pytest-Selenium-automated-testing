from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    BASIC_AUTH = (By.CSS_SELECTOR, 'a[href="/basic_auth"]')
    SUCCESSFUL_MESSAGE = (By.CSS_SELECTOR, 'p')

    def go_to_auth_page(self):
        self.driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

    def is_auth_succeeded(self):
        return self.element_contain_text(self.SUCCESSFUL_MESSAGE, TestData.BASIC_AUTH_MESSAGE)
