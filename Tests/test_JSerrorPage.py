from Pages.JSerrorPage import JSerrorPage
from Tests.test_base import BaseTest


class TestJSerror(BaseTest):
    def test_accept_alert(self):
        self.JSe = JSerrorPage(self.driver)
        self.JSe.get_url()
        log_message = self.JSe.get_browser_log()
        assert log_message == ""


