from Config.config import TestData
from Tests.test_base import BaseTest


class TestLogin(BaseTest):

    def test_login_page_title(self):
        title = self.loginPage.get_login_page_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login_button_visible(self):
        flag = self.loginPage.is_login_button_exist()
        assert flag

    def test_open_url(self):
        self.loginPage.do_login(TestData.USER_NAME, TestData.User_PASSWORD)


"""
    def test_login_button_visible(self):
        self.driver.get(TestData.BASE_URL)
        self.loginpage = LoginPage(self.driver)
        flag = self.loginPage.is_login_button_exist()
        assert flag"""
