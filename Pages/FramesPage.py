from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Config.config import TestData
from Pages.BasePage import BasePage


class FramesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    Nested_frame_link = (By.LINK_TEXT, 'Nested Frames')
    Iframe_link = (By.LINK_TEXT, 'iFrame')
    Nested_frame_section = (By.XPATH, '//body')
    frame_bottom = (By.NAME, "frame-bottom")
    frame_top = (By.NAME, "frame-top")
    frame_left = (By.NAME, "frame-left")
    iframe = (By.ID, "mce_0_ifr")
    iframe_editor = (By.ID, "tinymce")

    def get_url(self):
        self.driver.get(TestData.BASE_URL + '/frames')

    def nested_frame_page(self):
        self.do_click(self.Nested_frame_link)

    def iframe_page(self):
        self.do_click(self.Iframe_link)

    def bottom_frame_text(self):
        self.nested_frame_page()
        self.focus_on_frame(self.frame_bottom)
        return self.element_contain_text(self.Nested_frame_section, 'BOTTOM')

    def left_frame_text(self):
        self.nested_frame_page()
        self.focus_on_frame(self.frame_top)
        self.focus_on_frame(self.frame_left)
        return self.element_contain_text(self.Nested_frame_section, 'LEFT')

    def iframe_default_text(self):
        self.iframe_page()
        self.focus_on_frame(self.iframe)
        return self.element_contain_text(self.Nested_frame_section, 'Your content goes here.')

    def iframe_write_text(self, new_text):
        self.iframe_page()
        self.focus_on_frame(self.iframe)
        self.do_click(self.iframe_editor)
        self.clear_input_field(self.iframe_editor)
        self.do_send_keys(self.iframe_editor, new_text)
        return self.element_contain_text(self.iframe_editor, new_text)







