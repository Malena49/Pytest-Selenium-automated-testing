from Pages.SecureDownloaderPage import SecureDownloaderPage
from Tests.test_base import BaseTest


class TestRedirection(BaseTest):
    def test_all_links_clickable_after_login(self):
        self.SD = SecureDownloaderPage(self.driver)
        self.SD.login_to_access_files()
        self.SD.download_all_files()

    def test_are_files_download_after_login(self):
        flag = True
        self.SD = SecureDownloaderPage(self.driver)
        self.SD.login_to_access_files()
        files_failed = self.SD.are_all_files_downloaded()
        if len(files_failed) > 0:
            flag = False
        assert flag, print(files_failed)

    def test_all_links_not_clickable_before_login(self):
        flag = True
        self.SD = SecureDownloaderPage(self.driver)
        self.SD.access_without_login()
        try:
            if self.SD.download_all_files():
                flag = False
        except Exception as e:
            print(e)
        assert flag





