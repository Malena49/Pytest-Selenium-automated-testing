from Tests.test_base import BaseTest


class TestAddRemove(BaseTest):

    def test_add_element(self):
        self.addRemove.get_url()
        self.addRemove.add_element()
        flag = self.addRemove.is_element_added()
        assert flag

    def test_delete_element(self):
        self.addRemove.get_url()
        self.addRemove.add_element()
        self.addRemove.delete_element()
        flag = self.addRemove.is_element_deleted()
        assert flag
