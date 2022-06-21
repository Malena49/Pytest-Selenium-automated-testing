from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage
import string
import random
from random import randint


class InputPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    INPUT_CHAMPS = (By.CSS_SELECTOR, 'input[type="number"]')

    def get_url(self):
        self.driver.get(TestData.BASE_URL + '/inputs')

    def send_value(self, text):
        self.do_send_keys(self.INPUT_CHAMPS, text)

    def input_value(self):
        return self.get_input_value(self.INPUT_CHAMPS)

    def random_char(self, y):
        return ''.join(random.choice(string.ascii_letters) for x in range(y))

    def random_number(self, min_v, max_v):
        return randint(min_v, max_v)

