from Config.config import TestData
from Tests.test_base import BaseTest
import time


class TestLogin(BaseTest):

    def test_login_page_title(self):
        title = self.loginPage.get_login_page_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login_page_header(self):
        header = self.loginPage.get_login_page_header()
        assert header == TestData.LOGIN_PAGE_HEADER

    def test_login_button_visible(self):
        flag = self.loginPage.is_login_button_exist()
        assert flag

    def test_do_logout(self):
        self.loginPage.do_logout(TestData.USER_NAME, TestData.User_PASSWORD)
        logout_message = self.loginPage.is_message_exist(TestData.LOGOUT_MESSAGE)
        assert logout_message

    def test_do_login(self):
        self.loginPage.do_login(TestData.USER_NAME, TestData.User_PASSWORD)
        login_message = self.loginPage.is_message_exist(TestData.LOGIN_MESSAGE)
        assert login_message



