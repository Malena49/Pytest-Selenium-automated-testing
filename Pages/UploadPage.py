from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class UploadPage(BasePage):
    BtnChoose = (By.ID, "file-upload")
    File_PATH = "C:/test/testUpload.txt"
    BtnSubmit = (By.ID, "file-submit")
    FILE_Name = "testUpload.txt"
    MESSAGE = (By.ID, "uploaded-files")

    def __init__(self, driver):
        super().__init__(driver)

    def get_url(self):
        self.driver.get(TestData.BASE_URL + '/upload')

    def choose_file(self):
        self.do_send_keys(self.BtnChoose, self.File_PATH)
        self.do_click(self.BtnSubmit)

    def is_file_uploaded(self):
        return self.element_contain_text(self.MESSAGE, self.FILE_Name)

