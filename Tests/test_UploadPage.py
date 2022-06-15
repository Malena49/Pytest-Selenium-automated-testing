import time

from Pages.UploadPage import UploadPage
from Tests.test_base import BaseTest


class TestDownload(BaseTest):
    def test_download_all_files(self):
        self.U = UploadPage(self.driver)
        self.U.get_url()
        self.U.choose_file()
        flag = self.U.is_file_uploaded()
        assert flag

