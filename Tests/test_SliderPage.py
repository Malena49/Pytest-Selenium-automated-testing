from Pages.SliderPage import SliderPage
from Tests.test_base import BaseTest


class TestSlider(BaseTest):
    def test_slider_left_to_right(self):
        self.S = SliderPage(self.driver)
        self.S.get_url()
        step = self.S.get_slider_step()
        max_value = self.S.get_slider_max()
        i = 0
        while i < max_value:
            i += step
            self.S.move_slider(i)
            assert self.S.get_selected_number() == i

    def test_slider_right_to_left(self):
        self.S = SliderPage(self.driver)
        self.S.get_url()
        step = self.S.get_slider_step()
        max_value = self.S.get_slider_max()
        i = max_value
        while i > 0:
            i -= step
            self.S.move_slider(i)
            assert self.S.get_selected_number() == i





