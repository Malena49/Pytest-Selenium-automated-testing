from Config.config import TestData
from Tests.test_base import BaseTest


class TestContextMenu(BaseTest):
    def test_alert_text(self):
        self.contextMenu.get_url()
        self.contextMenu.right_click_box()
        assert self.contextMenu.get_context_menu_alert_text() == TestData.ALERT
        self.contextMenu.accept_context_alert()


