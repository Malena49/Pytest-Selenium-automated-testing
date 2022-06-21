from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class KeyboardActionsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    INPUT = (By.ID, "target")
    RESULT = (By.ID, "result")

    def get_url(self):
        self.driver.get(TestData.BASE_URL + '/key_presses')

    def send_key(self, text):
        self.do_send_keys(self.INPUT, text)

    def result_contain(self, text):
        return self.element_contain_text(self.RESULT, text)


