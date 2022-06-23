from Pages.ShiftingContentPage import ShiftingContentPage
from Tests.test_base import BaseTest


class TestShiftingContent(BaseTest):
    def test_shifted_menu(self):
        self.SC = ShiftingContentPage(self.driver)
        self.SC.get_url_menu()
        locations_1 = self.SC.get_menu_list_link_locations()
        self.driver.refresh()
        locations_2 = self.SC.get_menu_list_link_locations()
        assert locations_1 == locations_2, print("menu has shifted")

    def test_shifted_image(self):
        self.SC = ShiftingContentPage(self.driver)
        self.SC.get_url_image()
        locations_1 = self.SC.get_image_location()
        self.driver.refresh()
        locations_2 = self.SC.get_image_location()
        assert locations_1 == locations_2, print("image has shifted")

    def test_shifted_list(self):
        self.SC = ShiftingContentPage(self.driver)
        self.SC.get_url_list()
        list_1 = self.SC.get_list_content()
        self.driver.refresh()
        list_2 = self.SC.get_list_content()
        assert list_1 == list_2, print("list content has shifted")


