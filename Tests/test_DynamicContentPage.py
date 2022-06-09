
from Config.config import TestData
from Pages.DynamicContentPage import DynamicContentPage
from Tests.test_base import BaseTest


class TestDynamicContent(BaseTest):
    def test_refresh_content(self):
        self.DC = DynamicContentPage(self.driver)
        self.DC.get_url()
        images_before = self.DC.get_all_images()
        texts_before = self.DC.get_all_texts()
        self.driver.refresh()
        images_after = self.DC.get_all_images()
        texts_after = self.DC.get_all_texts()
        assert images_before != images_after and texts_before != texts_after



