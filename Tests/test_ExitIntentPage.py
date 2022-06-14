from Pages.ExitIntentPage import ExitIntentPage
from Tests.test_base import BaseTest


class TestExitIntent(BaseTest):
    def test_popup_present(self):
        self.EI = ExitIntentPage(self.driver)
        self.EI.get_url()
        self.EI.move_out_viewport(0, 0)
        flag = self.EI.is_popup_present()
        assert flag

    def test_close_popup(self):
        self.EI = ExitIntentPage(self.driver)
        self.EI.get_url()
        self.EI.move_out_viewport(0, 0)
        self.EI.close_popup()
        flag = self.EI.is_popup_closed()
        assert flag












