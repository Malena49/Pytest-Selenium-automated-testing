"""
this  class is parent of all pages
It contains all generic methods and utilities
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def do_click(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_clickable(self, by_locator):
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        return bool(element)

    def get_title(self, title):
        self.wait.until(EC.title_is(title))
        return self.driver.title
