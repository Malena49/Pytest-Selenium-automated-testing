from Pages.HoverPage import HoverPage
from Tests.test_base import BaseTest


class TestHover(BaseTest):
    def test_hover_on_images(self):
        self.H = HoverPage(self.driver)
        self.H.get_url()
        self.H.mouse_on_images()

    def test_hidden_names(self):
        self.H = HoverPage(self.driver)
        self.H.get_url()
        names = self.H.are_names_hidden()
        assert names == len(self.H.get_name_list())

    def test_hover_on_image_and_display_name(self):
        self.H = HoverPage(self.driver)
        self.H.get_url()
        names = self.H.get_name_list()
        images = self.H.get_image_list()
        # check if every user has name
        assert len(names) == len(images)
        failed_hover = self.H.hover_name_display()
        flag = True
        if len(failed_hover) > 0:
            flag = False
        # check if every hover works
        assert flag, print(failed_hover)



