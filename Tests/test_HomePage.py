import time

from Config.config import TestData
from Tests.test_base import BaseTest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestHome(BaseTest):

    def test_list_elements(self):
        self.homePage.get_url()
        element = self.homePage.count_list_elements()
        assert element == 44

    def test_checkbox(self):
        self.homePage.get_url()
        self.homePage.go_to_checkbox()
        header = self.homePage.get_checkbox_header()
        assert header == TestData.CHECKBOX_HEADER

    def test_default_checkbox(self):
        self.homePage.get_url()
        self.homePage.go_to_checkbox()
        check = self.homePage.is_default_checkbox_selected()
        assert check

    def test_change_selected_checkbox(self):
        self.homePage.get_url()
        self.homePage.go_to_checkbox()
        self.homePage.change_selected_checkbox()
        defaultcheck = self.homePage.is_default_checkbox_selected()
        othercheck = self.homePage.is_other_checkbox_selected()
        assert othercheck and defaultcheck == False
