from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class SliderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    SLIDER = (By.CSS_SELECTOR, 'input[type="range"]')
    NUMBER = (By.ID, 'range')

    def get_url(self):
        self.driver.get(TestData.BASE_URL + '/horizontal_slider')

    def get_slider_width(self):
        width = self.get_element_dimension(self.SLIDER)["width"]
        return width

    def calculate_x_offset(self, num):
        width = self.get_slider_width()
        maxi = self.get_slider_max()
        return width*(num*2-maxi)/(2*maxi)

    def move_slider(self, num):
        source = self.driver.find_element(By.CSS_SELECTOR, 'input[type="range"]')
        move_distance = self.calculate_x_offset(num)
        self.move_an_objet(source, move_distance, 0)

    def get_selected_number(self):
        element = self.get_element_text(self.NUMBER)
        return float(element)

    def get_slider_step(self):
        step = float(self.driver.find_element(
            By.CSS_SELECTOR,
            'input[type="range"]'
        ).get_attribute("max"))
        return step

    def get_slider_max(self):
        max_value = float(self.driver.find_element(
            By.CSS_SELECTOR,
            'input[type="range"]'
        ).get_attribute("max"))
        return max_value




