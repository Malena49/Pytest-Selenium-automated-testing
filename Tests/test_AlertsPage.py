from Pages.AlertsPage import AlertsPage
from Tests.test_base import BaseTest


class TestAlerts(BaseTest):
    def test_accept_alert(self):
        self.A = AlertsPage(self.driver)
        self.A.get_url()
        self.A.accept_js_alert()
        message = self.A.get_message()
        assert message == "You successfully clicked an alert"

    def test_accept_confirm(self):
        self.A = AlertsPage(self.driver)
        self.A.get_url()
        self.A.accept_js_confirm()
        message = self.A.get_message()
        assert message == "You clicked: Ok"

    def test_dismiss_confirm(self):
        self.A = AlertsPage(self.driver)
        self.A.get_url()
        self.A.dismiss_js_confirm()
        message = self.A.get_message()
        assert message == "You clicked: Cancel"

    def test_accept_prompt(self):
        self.A = AlertsPage(self.driver)
        self.A.get_url()
        self.A.accept_js_prompt()
        message = self.A.get_message()
        assert message == "You entered:"

    def test_send_keys_and_accept_prompt(self):
        self.A = AlertsPage(self.driver)
        self.A.get_url()
        text = "abc"
        self.A.send_keys_js_prompt(text)
        message = self.A.get_message()
        assert message == "You entered: " + text

    def test_send_keys_and_cancel_prompt(self):
        self.A = AlertsPage(self.driver)
        self.A.get_url()
        text = "abc"
        self.A.send_keys_and_cancel_prompt(text)
        message = self.A.get_message()
        assert message == "You entered: null"

