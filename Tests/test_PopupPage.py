import time

from Config.config import TestData
from Pages.PopupPage import PopupPage
from Tests.test_base import BaseTest


class TestPopup(BaseTest):
    def test_close_popup(self):
        self.PP = PopupPage(self.driver)
        self.PP.get_url()
        self.PP.close_popup()
        flag = self.PP.is_popup_closed()
        assert flag
