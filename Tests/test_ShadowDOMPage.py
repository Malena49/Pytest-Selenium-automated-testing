from Pages.ShadowDOMPage import ShadowDOMPage
from Tests.test_base import BaseTest


class TestShadowDom(BaseTest):
    def test_first_shadow_paragraph_text(self):
        self.SD = ShadowDOMPage(self.driver)
        self.SD.get_url()
        first_text = self.SD.get_first_paragraph_text()
        assert first_text == "Let's have some different text!"

    def test_default_text(self):
        self.SD = ShadowDOMPage(self.driver)
        self.SD.get_url()
        default_text = self.SD.get_second_paragraph_text()
        assert default_text == "In a list!"

