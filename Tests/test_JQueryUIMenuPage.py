from Pages.JQueryMenuPage import JQueryMenuPage
from Tests.test_base import BaseTest


class TestInput(BaseTest):
    def test_enter_number(self):
        self.JM = JQueryMenuPage(self.driver)
        self.JM.get_url()
        self.JM.download_all_files()
        flag = True
        failed_download = self.JM.are_all_files_downloaded()
        if len(failed_download) > 0:
            flag = False
        assert flag, print(failed_download)

