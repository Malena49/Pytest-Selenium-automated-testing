from Config.config import TestData
from Tests.test_base import BaseTest
from selenium.webdriver.common.by import By


class TestImg(BaseTest):
    def test_broken_images(self):
        flag = True
        self.imgPage.get_url()
        images = self.imgPage.get_all_image()
        broken_messages = []
        for image in images:
            try:
                response = self.imgPage.get_image_res_code(image)
                if response != 200:
                    broken_messages.append(image.get_attribute('outerHTML') + " is broken.")
            except Exception as ex:
                print(ex)
        if len(broken_messages) > 0:
            flag = False
        assert flag, print(broken_messages)
