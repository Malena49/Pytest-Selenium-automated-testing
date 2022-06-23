from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class ShiftingContentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    MENU = (By.CSS_SELECTOR, "ul li")
    IMAGE = (By.CSS_SELECTOR, 'img[class="shift"]')
    LIST = (By.CSS_SELECTOR, "#content .row div")

    def get_url_menu(self):
        self.driver.get(TestData.BASE_URL + "/shifting_content/menu")

    def get_menu_list(self):
        return self.get_array(self.MENU)

    def get_menu_list_link_locations(self):
        link_locations = []
        for link in self.get_menu_list():
            link_locator = link.find_element(By.TAG_NAME, "a")
            link_location = link_locator.location
            link_locations.append(link_location)
        return link_locations

    def get_url_image(self):
        self.driver.get(TestData.BASE_URL + "/shifting_content/image")

    def get_image_location(self):
        return self.get_element_location(self.IMAGE)

    def get_url_list(self):
        self.driver.get(TestData.BASE_URL + "/shifting_content/list")

    def get_list_content(self):
        return self.get_element_text(self.LIST)




