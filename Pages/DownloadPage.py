import os
import time
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class DownloadPage(BasePage):
    FILES = (By.CSS_SELECTOR, '.example a')

    def __init__(self, driver):
        super().__init__(driver)

    def get_url(self):
        self.driver.get(TestData.BASE_URL + '/download')

    def get_files_list(self):
        return self.get_array(self.FILES)

    def click_on_all_download_links(self):
        files = self.get_files_list()
        for file in files:
            file.click()

    def get_all_failed_download(self):
        files = self.get_files_list()
        time_counter = 0
        failed_download = []
        for file in files:
            file_name = file.get_attribute('innerHTML').strip()
            while not os.path.exists(TestData.DOWNLOAD_PATH + file_name):
                time.sleep(1)
                if time_counter > 20:
                    failed_download.append("Fail to download " + file_name)
                    break
                time_counter += 1
        return failed_download

    def delete_all_files(self):
        files = self.get_files_list()
        for file in files:
            file_name = file.get_attribute('innerHTML').strip()
            os.remove(TestData.DOWNLOAD_PATH + file_name)






