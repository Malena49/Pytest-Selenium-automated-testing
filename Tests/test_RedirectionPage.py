from Pages.RedirectionPage import RedirectionPage
from Tests.test_base import BaseTest


class TestRedirection(BaseTest):
    def test_send_numpad1(self):
        self.R = RedirectionPage(self.driver)
        self.R.get_url()
        self.R.redirect_to_another_page()
        url = self.R.get_current_url()
        assert url == self.R.Redirection_URL




