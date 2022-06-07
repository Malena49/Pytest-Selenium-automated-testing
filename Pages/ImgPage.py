from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class ImgPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_url(self):
        self.driver.get(TestData.BASE_URL + '/broken_images')

    def get_all_image(self):
        return self.driver.find_elements(By.TAG_NAME, "img")

    def get_image_res_code(self, image):
        return self.get_http_code(image.get_attribute('src'))

