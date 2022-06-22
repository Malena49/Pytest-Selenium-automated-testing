"""
this  class is parent of all pages
It contains all generic methods and utilities
"""
import os
import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import pyautogui as P
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver: WebElement = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)
        P.FAILSAFE = False

    def do_click(self, by_locator):
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute('innerHTML').strip()

    def is_clickable(self, by_locator):
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        return element

    def get_title(self, title):
        self.wait.until(EC.title_is(title))
        return self.driver.title

    def element_contain_text(self, by_locator, text):
        element = self.wait.until(EC.text_to_be_present_in_element(by_locator, text))
        return bool(element)

    def get_array(self, by_locator):
        return self.wait.until(EC.visibility_of_all_elements_located(by_locator))

    def is_selected(self, by_locator):
        element = self.wait.until(EC.element_to_be_clickable(by_locator)).is_selected()
        return element

    def get_http_code(self, url):
        response = requests.get(url, stream=True).status_code
        return response

    def is_enable(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return element

    def is_disabled(self, by_locator):
        element = self.wait.until(EC.invisibility_of_element_located(by_locator))
        return element

    def right_click(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        self.action.context_click(on_element=element).perform()

    def get_alert_text(self):
        ale = Alert(self.driver)
        return ale.text

    def accept_alert(self):
        ale = Alert(self.driver)
        ale.accept()

    def dismiss_alert(self):
        ale = Alert(self.driver)
        ale.dismiss()

    def send_keys_accept_alert(self, text):
        ale = Alert(self.driver)
        ale.send_keys(text)
        ale.accept()

    def send_keys_dismiss_alert(self, text):
        ale = Alert(self.driver)
        ale.send_keys(text)
        ale.dismiss()

    def drag_and_drop(self, a, b, e, c, d, f):
        P.moveTo(a, b, e)
        P.drag(c, d, f, button='left')

    def move_mouse_offset(self, x, y):
        P.moveTo(x, y, 1)

    def focus_on_frame(self, by_locator):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(by_locator))

    def clear_input_field(self, by_locator):
        self.wait.until(EC.presence_of_element_located(by_locator)).clear()

    def move_an_objet(self, source, a, b):
        # self.action.move_to_element_with_offset(source, x, y)
        self.action.move_to_element(source)
        self.action.click_and_hold()
        self.action.move_by_offset(a, b)
        self.action.release()
        self.action.perform()

    def get_element_dimension(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).size

    def get_element_location(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).location

    def move_mouse_on_element(self, by_locator):
        self.action.move_to_element(by_locator).perform()

    def move_mouse_on_element_and_click(self, by_locator):
        self.action.move_to_element(by_locator).click().perform()

    def locate_visible_element(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    def get_invisible_array(self, by_locator):
        return self.wait.until(EC.presence_of_all_elements_located(by_locator))

    def scroll_page(self):
        screen_height = self.driver.execute_script("return window.screen.height;")
        i = 1
        while True:
            self.driver.execute_script(f"window.scrollTo(0, {screen_height}*{i});")
            i += 1
            scroll_height = self.driver.execute_script("return document.body.scrollHeight;")
            # Break the loop when the height we need to scroll to is larger than the total scroll height
            # if screen_height * i < scroll_height:
            if i > 200:
                break

    def get_input_value(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).get_attribute('value')

    def get_link_href(self, by_locator):
        return self.wait.until(EC.element_to_be_clickable(by_locator)).get_attribute('href')

    def get_browser_javascript_log(self):
        return self.driver.get_log('browser')

    def window_handler(self, num):
        return self.driver.window_handles[num]

    def switch_window(self, window):
        self.driver.switch_to.window(window)

    def wait_for_current_url_change(self, url):
        self.wait.until(EC.url_changes(url))



