from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        url = TestData.BASE_URL.format('login')
        self.driver.get(url)

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    BtnSubmit = (By.CSS_SELECTOR, 'button[type="submit"]')
    HEADER = (By.CSS_SELECTOR, '#content h2')

    # this is used to get login page title
    def get_login_page_title(self, title):
        return self.get_title(title)

    # this is used to check page header
    def get_login_page_header(self):
        return self.get_element_text(self.HEADER)

    # this is used to check if login button exist
    def is_login_button_exist(self):
        return self.is_clickable(self.BtnSubmit)

    # this is used to login to website
    def do_login(self, username, password):
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.BtnSubmit)
