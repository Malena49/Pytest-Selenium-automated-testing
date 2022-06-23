import time

from Pages.TinyMCEPage import TinyMCEPage
from Tests.test_base import BaseTest


class TestTinyMCEPage(BaseTest):
    def test_write_text(self):
        self.TM = TinyMCEPage(self.driver)
        self.TM.get_url()
        enter_text = "Hi!"
        self.TM.write_text(enter_text)
        show_text = self.TM.get_editor_text()
        assert show_text == enter_text

    def test_bold_text(self):
        self.TM = TinyMCEPage(self.driver)
        self.TM.get_url()
        enter_text = "Hi!"
        self.TM.write_text(enter_text)
        self.TM.make_text_bold()
        text_weight = self.TM.get_text_font_weight()
        assert text_weight == "700"

    def test_italic_text(self):
        self.TM = TinyMCEPage(self.driver)
        self.TM.get_url()
        enter_text = "Hi!"
        self.TM.write_text(enter_text)
        self.TM.make_text_italic()
        text_style = self.TM.get_text_font_style()
        assert text_style == "italic"

