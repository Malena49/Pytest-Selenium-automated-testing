from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class FramesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    Nested_frame_link = (By.LINK_TEXT, 'Nested Frames')
    Iframe_link = (By.LINK_TEXT, 'iFrame')
    Nested_frame_section = (By.XPATH, '//body')

    def get_url(self):
        self.driver.get(TestData.BASE_URL + '/frames')

    def nested_frame_page(self):
        self.do_click(self.Nested_frame_link)

    def iframe_page(self):
        self.do_click(self.Iframe_link)

    def bottom_frame_text(self):
        self.nested_frame_page()
        self.driver.switch_to.frame("frame-bottom")
        return self.element_contain_text(self.Nested_frame_section, 'BOTTOM')

    def left_frame_text(self):
        self.nested_frame_page()
        self.driver.switch_to.frame("frame-top")
        self.driver.switch_to.frame("frame-left")
        return self.element_contain_text(self.Nested_frame_section, 'LEFT')






