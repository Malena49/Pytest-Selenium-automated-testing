from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class StatusCodesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    Code_200 = (By.LINK_TEXT, "200")
    Code_301 = (By.LINK_TEXT, "301")
    Code_404 = (By.LINK_TEXT, "404")
    Code_500 = (By.LINK_TEXT, "500")

    def get_url(self):
        self.driver.get(TestData.BASE_URL + "/status_codes")

    def get_status_code(self):
        url = self.driver.current_url
        response = self.get_http_code(url)
        return response

    def get_200_status_code(self):
        self.get_url()
        self.do_click(self.Code_200)
        return self.get_status_code()

    def get_301_status_code(self):
        self.get_url()
        self.do_click(self.Code_301)
        return self.get_status_code()

    def get_404_status_code(self):
        self.get_url()
        self.do_click(self.Code_404)
        return self.get_status_code()

    def get_500_status_code(self):
        self.get_url()
        self.do_click(self.Code_500)
        return self.get_status_code()







