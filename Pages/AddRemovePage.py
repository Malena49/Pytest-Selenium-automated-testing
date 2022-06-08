from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class AddRemovePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    BtnAdd = (By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    BtnDelete = (By.CLASS_NAME, 'added-manually')

    def get_url(self):
        self.driver.get(TestData.BASE_URL + '/add_remove_elements/')

    def add_element(self):
        self.do_click(self.BtnAdd)

    def is_element_added(self):
        return self.is_enable(self.BtnDelete)

    def delete_element(self):
        self.do_click(self.BtnDelete)

    def is_element_deleted(self):
        deleted = self.is_disabled(self.BtnDelete)
        return deleted
