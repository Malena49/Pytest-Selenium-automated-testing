from Tests.test_base import BaseTest


class TestDropdown(BaseTest):
    def test_select_option_1(self):
        self.Dropdown.get_url()
        self.Dropdown.select_option_1()
        flag = self.Dropdown.is_option_1_selected()
        assert flag

    def test_select_option_2(self):
        self.Dropdown.get_url()
        self.Dropdown.select_option_2()
        flag = self.Dropdown.is_option_2_selected()
        assert flag

    def test_default_option(self):
        self.Dropdown.get_url()
        default_text = self.Dropdown.get_default_option()
        assert default_text == "Please select an option"



