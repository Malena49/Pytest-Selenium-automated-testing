from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class RedirectionPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    Btn_Redirect = (By.ID, 'redirect')
    Redirection_URL = TestData.BASE_URL + '/status_codes'

    def get_url(self):
        self.driver.get(TestData.BASE_URL + '/redirector')

    def redirect_to_another_page(self):
        self.do_click(self.Btn_Redirect)
        self.wait_for_current_url_change(TestData.BASE_URL + '/redirector')

    def get_current_url(self):
        return self.driver.current_url

