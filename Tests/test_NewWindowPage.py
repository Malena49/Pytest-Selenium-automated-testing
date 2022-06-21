from Pages.NewWindowPage import NewWindowPage
from Tests.test_base import BaseTest


class TestNewWindow(BaseTest):
    def test_send_numpad1(self):
        self.NW = NewWindowPage(self.driver)
        self.NW.get_url()
        window_before = self.driver.window_handles[0]
        self.NW.open_new_window()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        assert self.NW.check_on_new_window("New Window")
        self.driver.close()
        self.driver.switch_to.window(window_before)


