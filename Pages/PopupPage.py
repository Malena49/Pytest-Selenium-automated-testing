
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class PopupPage(BasePage):
    BtnClose = (By.CSS_SELECTOR, '.modal-footer p')
    Popup = (By.ID, 'modal')

    def __init__(self, driver):
        super().__init__(driver)

    def get_url(self):
        self.driver.get(TestData.BASE_URL + '/entry_ad')

    def close_popup(self):
        try:
            self.do_click(self.BtnClose)
        except:
            print("no popup")

    def is_popup_closed(self):
        return self.is_disabled(self.Popup)


