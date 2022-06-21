from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class InfiniteScrollPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_url(self):
        self.driver.get(TestData.BASE_URL + '/infinite_scroll')

    def scroll_infinite_page(self):
        self.scroll_page()

