import time

from Pages.GeolocationPage import GeolocationPage
from Tests.test_base import BaseTest


class TestGeolocation(BaseTest):
    def test_allow_geolocation(self):
        self.GL = GeolocationPage(self.driver)
        self.GL.get_url()
        self.GL.trigger_location_popup()

