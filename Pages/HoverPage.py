from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class HoverPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    IMAGES = (By.CSS_SELECTOR, ".figure img")
    USER_NAMES = (By.CSS_SELECTOR, ".figure h5")

    def get_url(self):
        self.driver.get(TestData.BASE_URL + '/hovers')

    def get_name_list(self):
        names = self.get_invisible_array(self.USER_NAMES)
        return names

    def get_image_list(self):
        images = self.get_array(self.IMAGES)
        return images

    def mouse_on_image(self, image):
        self.move_mouse_on_element(image)

    def mouse_on_images(self):
        images = self.get_image_list()
        i = 0
        while i < len(images):
            self.mouse_on_image(images[i])
            i = i + 1

    def are_names_hidden(self):
        names = self.get_name_list()
        counter = 0
        for name in names:
            if not name.is_displayed():
                counter += 1
        return counter

    def hover_name_display(self):
        names = self.get_name_list()
        images = self.get_image_list()
        i = 0
        names_non_display = []
        while i < len(images):
            self.mouse_on_image(images[i])
            if not names[i].is_displayed():
                names_non_display.append(names[i].get_attribute('innerHTML'))
            i = i + 1
        return names_non_display




