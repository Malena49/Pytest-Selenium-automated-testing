from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class ExitIntentPage(BasePage):
    POPUP = (By.ID, 'ouibounce-modal')
    BtnClose = (By.CSS_SELECTOR, '.modal-footer p')

    def __init__(self, driver):
        super().__init__(driver)

    def get_url(self):
        self.driver.get(TestData.BASE_URL + '/exit_intent')

    def move_out_viewport(self, x, y):
        self.move_mouse_offset(500, 500)
        self.move_mouse_offset(x, y)

    def is_popup_present(self):
        return self.is_enable(self.POPUP)

    def close_popup(self):
        self.do_click(self.BtnClose)

    def is_popup_closed(self):
        return self.is_disabled(self.POPUP)


