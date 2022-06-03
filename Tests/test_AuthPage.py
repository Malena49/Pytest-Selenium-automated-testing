from Config.config import TestData
from Tests.test_base import BaseTest


class TestAuth(BaseTest):
    def test_goto_auth(self):
        self.authPage.go_to_auth_page()
        assert self.authPage.is_auth_succeeded()

