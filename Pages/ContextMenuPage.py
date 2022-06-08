from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class ContextMenuPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    BOX = (By.ID, "hot-spot")

    def get_url(self):
        self.driver.get(TestData.BASE_URL + '/context_menu')

    def right_click_box(self):
        self.right_click(self.BOX)

    def get_context_menu_alert_text(self):
        return self.get_alert_text()

    def accept_context_alert(self):
        self.accept_alert()

