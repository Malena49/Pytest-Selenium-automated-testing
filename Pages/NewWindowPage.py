from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class NewWindowPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    Btn_Window = (By.LINK_TEXT, 'Click Here')
    New_window_header = (By.TAG_NAME, "h3")

    def get_url(self):
        self.driver.get(TestData.BASE_URL + '/windows')

    def open_new_window(self):
        self.do_click(self.Btn_Window)

    def check_on_new_window(self, text):
        return self.element_contain_text(self.New_window_header, text)

