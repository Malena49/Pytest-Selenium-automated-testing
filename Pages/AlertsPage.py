from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class AlertsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    Btn_ALERT = (By.CSS_SELECTOR, 'button[onclick="jsAlert()"]')
    Btn_CONFIRM = (By.CSS_SELECTOR, 'button[onclick="jsConfirm()"]')
    Btn_PROMPT = (By.CSS_SELECTOR, 'button[onclick="jsPrompt()"]')
    MESSAGE = (By.ID, 'result')

    def get_url(self):
        self.driver.get(TestData.BASE_URL + '/javascript_alerts')

    def accept_js_alert(self):
        self.do_click(self.Btn_ALERT)
        self.accept_alert()

    def get_message(self):
        return self.get_element_text(self.MESSAGE)

    def accept_js_confirm(self):
        self.do_click(self.Btn_CONFIRM)
        self.accept_alert()

    def dismiss_js_confirm(self):
        self.do_click(self.Btn_CONFIRM)
        self.dismiss_alert()

    def accept_js_prompt(self):
        self.do_click(self.Btn_PROMPT)
        self.accept_alert()

    def send_keys_js_prompt(self, text):
        self.do_click(self.Btn_PROMPT)
        self.send_keys_accept_alert(text)

    def send_keys_and_cancel_prompt(self, text):
        self.do_click(self.Btn_PROMPT)
        self.send_keys_dismiss_alert(text)



