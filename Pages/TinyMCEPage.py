from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class TinyMCEPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.action = ActionChains(self.driver)

    FRAME = (By.ID, "mce_0_ifr")
    EDITOR = (By.CSS_SELECTOR, "#tinymce")
    EDITOR_TEXT = (By.CSS_SELECTOR, "#tinymce p > *")
    Btn_Bold = (By.CSS_SELECTOR, 'button[aria-label="Bold"]')
    Btn_Italic = (By.CSS_SELECTOR, 'button[aria-label="Italic"]')

    def get_url(self):
        self.driver.get(TestData.BASE_URL + "/tinymce")

    def write_text(self, text):
        self.focus_on_frame(self.FRAME)
        self.clear_input_field(self.EDITOR)
        self.do_send_keys(self.EDITOR, text)

    def get_editor_text(self):
        return self.locate_visible_element(self.EDITOR).text

    def select_text(self):
        text_locator = self.locate_visible_element(self.EDITOR)
        self.action.double_click(
            text_locator
        ).click(
            text_locator
        ).perform()

    def make_text_bold(self):
        self.select_text()
        self.move_out_of_frame()
        self.do_click(self.Btn_Bold)

    def make_text_italic(self):
        self.select_text()
        self.move_out_of_frame()
        self.do_click(self.Btn_Italic)

    def get_text_font_weight(self):
        self.focus_on_frame(self.FRAME)
        return self.get_css_property(
            self.EDITOR_TEXT,
            "font-weight")

    def get_text_font_style(self):
        self.focus_on_frame(self.FRAME)
        return self.get_css_property(
           self.EDITOR_TEXT, "font-style")




