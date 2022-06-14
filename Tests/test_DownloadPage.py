import time

from Pages.DownloadPage import DownloadPage
from Tests.test_base import BaseTest


class TestDownload(BaseTest):
    def test_file_path(self):
        self.DP = DownloadPage(self.driver)
        self.DP.get_url()
        self.DP.get_download_liens()

