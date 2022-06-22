import os
import time

from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class SecureDownloaderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    ALL_FILE_LINKS = (By.CSS_SELECTOR, '.example a')

    def login_to_access_files(self):
        self.driver.get(f"https://admin:admin@the-internet.herokuapp.com/download_secure")

    def access_without_login(self):
        self.driver.get(TestData.BASE_URL + "/download_secure")

    def can_file_be_downloaded(self, link_locator):
        return self.is_clickable(link_locator)

    def get_all_files_links(self):
        return self.get_array(self.ALL_FILE_LINKS)

    def download_all_files(self):
        files = self.get_all_files_links()
        for file in files:
            file.click()

    def are_all_files_downloaded(self):
        self.download_all_files()
        files = self.get_all_files_links()
        time_counter = 0
        failed_download = []
        for file in files:
            file_name = file.get_attribute('innerHTML').strip()
            while not os.path.exists(TestData.DOWNLOAD_PATH + file_name):
                time.sleep(1)
                if time_counter > 10:
                    failed_download.append("Fail to download " + file_name)
                    break
                time_counter += 1
        return failed_download




