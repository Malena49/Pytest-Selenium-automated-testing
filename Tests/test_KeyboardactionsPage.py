from selenium.webdriver import Keys
from Pages.KeyboardactionsPage import KeyboardActionsPage
from Tests.test_base import BaseTest


class TestKeyboardActions(BaseTest):
    def test_send_numpad1(self):
        self.KA = KeyboardActionsPage(self.driver)
        self.KA.get_url()
        text = Keys.NUMPAD1
        self.KA.send_key(text)
        flag = self.KA.result_contain("NUMPAD1")
        assert flag

    def test_send_subtract(self):
        self.KA = KeyboardActionsPage(self.driver)
        self.KA.get_url()
        text = Keys.SUBTRACT
        self.KA.send_key(text)
        flag = self.KA.result_contain("SUBTRACT")
        assert flag

    def test_send_SPACE(self):
        self.KA = KeyboardActionsPage(self.driver)
        self.KA.get_url()
        text = Keys.SPACE
        self.KA.send_key(text)
        flag = self.KA.result_contain("SPACE")
        assert flag


