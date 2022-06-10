from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class DragDropPage(BasePage):
    COLUMN_A = (By.ID, 'column-a')
    COLUMN_B = (By.ID, 'column-b')
    COLUMN_A_text = (By.CSS_SELECTOR, '#column-a header')
    COLUMN_B_text = (By.CSS_SELECTOR, '#column-b header')

    def __init__(self, driver):
        super().__init__(driver)

    def get_url(self):
        self.driver.get(TestData.BASE_URL + '/drag_and_drop')

    def move_drag_drop(self):
        self.drag_and_drop(310, 414, 1, 300, 0, 1)

    def get_column_a_text(self):
        text_a = self.get_element_text(self.COLUMN_A_text)
        return text_a

    def get_column_b_text(self):
        text_b = self.get_element_text(self.COLUMN_B_text)
        return text_b
