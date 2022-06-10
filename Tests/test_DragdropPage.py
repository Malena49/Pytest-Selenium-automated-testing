from Pages.DragDropPage import DragDropPage
from Tests.test_base import BaseTest


class TestDragDrop(BaseTest):
    def test_drag_drop(self):
        self.DD = DragDropPage(self.driver)
        self.DD.get_url()
        self.DD.move_drag_drop()
        text_a = self.DD.get_column_a_text()
        text_b = self.DD.get_column_b_text()
        assert text_a == 'B' and text_b == 'A'



