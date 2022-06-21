from Pages.InputPage import InputPage
from Tests.test_base import BaseTest


class TestInput(BaseTest):
    def test_enter_number(self):
        self.I = InputPage(self.driver)
        self.I.get_url()
        entered_value = str(self.I.random_number(0, 100))
        self.I.send_value(entered_value)
        actuel_value = self.I.input_value()
        assert actuel_value == entered_value

    def test_enter_letter(self):
        self.I = InputPage(self.driver)
        self.I.get_url()
        entered_value = self.I.random_char(5)
        self.I.send_value(entered_value)
        actuel_value = self.I.input_value()
        assert actuel_value == ""

    def test_enter_letter_and_number(self):
        self.I = InputPage(self.driver)
        self.I.get_url()
        char = self.I.random_char(5)
        num = self.I.random_number(0, 100)
        entered_value = char + str(num)
        self.I.send_value(entered_value)
        actuel_value = self.I.input_value()
        assert actuel_value == str(num)


