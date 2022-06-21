from Pages.InfiniteScrollPage import InfiniteScrollPage
from Tests.test_base import BaseTest


class TestInfiniteScroll(BaseTest):
    def test_scroll_one_page(self):
        self.IS = InfiniteScrollPage(self.driver)
        self.IS.get_url()
        self.IS.scroll_infinite_page()
