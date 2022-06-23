from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class ShadowDOMPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    shadow_paragraphs = (By.CSS_SELECTOR, "my-paragraph")

    def get_url(self):
        self.driver.get(TestData.BASE_URL + "/shadowdom")

    def get_shadow_paragraphs(self):
        return self.get_array(self.shadow_paragraphs)

    def get_first_paragraph_text(self):
        shadow_root = self.get_shadow_paragraphs()[0].shadow_root
        text = shadow_root.find_element(By.CSS_SELECTOR, "p").text
        return text

    def get_second_paragraph_text(self):
        shadow_root = self.get_shadow_paragraphs()[1]
        text = shadow_root.find_element(By.CSS_SELECTOR, "ul li:last-child").text
        return text



