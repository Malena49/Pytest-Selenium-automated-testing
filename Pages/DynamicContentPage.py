from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class DynamicContentPage(BasePage):
    CONTENT_List = (By.CSS_SELECTOR, '#content .row .row')

    def __init__(self, driver):
        super().__init__(driver)

    def get_url(self):
        self.driver.get(TestData.BASE_URL + '/dynamic_content')

    def get_content_list(self):
        return self.get_array(self.CONTENT_List)

    def get_all_images(self):
        img_array = []
        contents = self.get_content_list()
        for content in contents:
            img = content.find_element(
                By.TAG_NAME, 'img'
            ).get_attribute(
                'outerHTML')
            img_array.append(img)
        return img_array

    def get_all_texts(self):
        text_array = []
        contents = self.get_content_list()
        for content in contents:
            text = content.find_element(
                By.CSS_SELECTOR, 'div:last-child'
            ).get_attribute("innerHTML")
            text_array.append(text)
        return text_array



