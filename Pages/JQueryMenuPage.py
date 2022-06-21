import os
import time
from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class JQueryMenuPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    ENABLE_LINK = (By.LINK_TEXT, "Enabled")
    DOWNLOAD_LINK = (By.LINK_TEXT, "Downloads")
    PDF_LINK = (By.LINK_TEXT, "PDF")
    CSV_LINK = (By.LINK_TEXT, "CSV")
    Excel_LINK = (By.LINK_TEXT, "Excel")

    def get_url(self):
        self.driver.get(TestData.BASE_URL + '/jqueryui/menu')

    def download_file(self, file_locator):
        enable = self.locate_visible_element(self.ENABLE_LINK)
        self.move_mouse_on_element(enable)
        download_link = self.locate_visible_element(self.DOWNLOAD_LINK)
        self.move_mouse_on_element(download_link)
        file_link = self.locate_visible_element(file_locator)
        self.move_mouse_on_element_and_click(file_link)

    def get_file_name(self, file_locator):
        href = self.get_link_href(file_locator)
        file_name = href.split("/")[-1]
        return file_name

    def file_locator_list(self):
        locator_list = [self.PDF_LINK,
                        self.CSV_LINK,
                        self.Excel_LINK]
        return locator_list

    def download_all_files(self):
        for file_locator in self.file_locator_list():
            self.download_file(file_locator)

    def are_all_files_downloaded(self):
        time_counter = 0
        failed_download = []
        for file_locator in self.file_locator_list():
            file_name = self.get_file_name(file_locator)
            while not os.path.exists(TestData.DOWNLOAD_PATH + file_name):
                time.sleep(1)
                if time_counter > 10:
                    failed_download.append("Fail to download " + file_name)
                    break
                time_counter += 1
        return failed_download


