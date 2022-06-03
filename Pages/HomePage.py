from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    LIST = (By.CSS_SELECTOR, 'ul li')
    CHECKBOX = (By.CSS_SELECTOR, 'a[href="/checkboxes"]')
    CHECKBOX_HEADER = (By.CSS_SELECTOR, '#content h3')
    DEFAULT_SELECTED_CHECKBOX = (By.CSS_SELECTOR, '#checkboxes input:last-child')
    OTHER_CHECKBOX = (By.CSS_SELECTOR, '#checkboxes input:first-child')
    All_CHECKBOX = (By.CSS_SELECTOR, '#checkboxes input')

    def get_url(self):
        self.driver.get(TestData.BASE_URL)

    # this is used to get all list elements
    def count_list_elements(self):
        return len(self.get_array(self.LIST))

    # this is used to go to checkbox page
    def go_to_checkbox(self):
        self.do_click(self.CHECKBOX)

    # this is used to get header of checkbox page
    def get_checkbox_header(self):
        return self.get_element_text(self.CHECKBOX_HEADER)

    # this is used to get the status of the default selected checkbox
    def is_default_checkbox_selected(self):
        return self.is_selected(self.DEFAULT_SELECTED_CHECKBOX)

    # this is used to get the status of the other checkbox
    def is_other_checkbox_selected(self):
        return self.is_selected(self.OTHER_CHECKBOX)

    # this is used to change the status of all checkbox
    def change_selected_checkbox(self):
        checkboxes = self.get_array(self.All_CHECKBOX)
        for checkbox in checkboxes:
            self.do_click(checkbox)




