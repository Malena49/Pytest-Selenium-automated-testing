from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class GeolocationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    BtnLocate = (By.CSS_SELECTOR, 'button[onclick="getLocation()"]')

    def get_url(self):
        self.driver.get(TestData.BASE_URL + '/geolocation')

    def trigger_location_popup(self):
        self.do_click(self.BtnLocate)




