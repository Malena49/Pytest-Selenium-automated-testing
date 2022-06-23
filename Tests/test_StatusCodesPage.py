from Pages.StatusCodesPage import StatusCodesPage
from Tests.test_base import BaseTest


class TestStatusCodes(BaseTest):
    def test_code_200(self):
        self.SC = StatusCodesPage(self.driver)
        code_200 = self.SC.get_200_status_code()
        assert code_200 == 200

    def test_code_301(self):
        self.SC = StatusCodesPage(self.driver)
        code_301 = self.SC.get_301_status_code()
        assert code_301 == 301

    def test_code_404(self):
        self.SC = StatusCodesPage(self.driver)
        code_404 = self.SC.get_404_status_code()
        assert code_404 == 404

    def test_code_500(self):
        self.SC = StatusCodesPage(self.driver)
        code_500 = self.SC.get_500_status_code()
        assert code_500 == 500




