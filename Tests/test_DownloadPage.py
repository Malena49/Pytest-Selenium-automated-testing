from Pages.DownloadPage import DownloadPage
from Tests.test_base import BaseTest


class TestDownload(BaseTest):
    def test_download_all_files(self):
        self.DP = DownloadPage(self.driver)
        self.DP.get_url()
        self.DP.click_on_all_download_links()
        flag = True
        failed_download = self.DP.get_all_failed_download()
        # check if there is any failed download
        if len(failed_download) > 0:
            flag = False
        assert flag, print(failed_download)
        # after download test, delete all the downloaded files
        self.DP.delete_all_files()




