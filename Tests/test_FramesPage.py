
from Pages.FramesPage import FramesPage
from Tests.test_base import BaseTest


class TestFrames(BaseTest):
    def test_frame_bottom_text(self):
        self.F = FramesPage(self.driver)
        self.F.get_url()
        flag = self.F.bottom_frame_text()
        assert flag

    def test_frame_left_text(self):
        self.F = FramesPage(self.driver)
        self.F.get_url()
        flag = self.F.left_frame_text()
        assert flag

    def test_iframe_default_text(self):
        self.F = FramesPage(self.driver)
        self.F.get_url()
        flag = self.F.iframe_default_text()
        assert flag

    def test_iframe_write_text(self):
        self.F = FramesPage(self.driver)
        self.F.get_url()
        flag = self.F.iframe_write_text("Hello")
        assert flag

