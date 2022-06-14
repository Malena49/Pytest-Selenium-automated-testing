import os
import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class DownloadPage(BasePage):
    # use your own download path
    BASE_PATH = "C:/Users/shuqzeng/Downloads"
    FILES = (By.CSS_SELECTOR, '.example a')

    def __init__(self, driver):
        super().__init__(driver)

    def get_url(self):
        self.driver.get(TestData.BASE_URL + '/download')

    def get_files_list(self):
        return self.get_array(self.FILES)

    def get_files_names(self):
        files = self.get_files_list()
        files_names = []
        for file in files:
            file_name = file.get_attribute('innerHTML').strip()
            files_names.append(file_name)
        return files_names

    def get_download_liens(self):
        files = self.get_files_list()
        for file in files:
            file.click()

    def get_downloaded_file(self):
        return self.is_file_exist(self.BASE_PATH)



