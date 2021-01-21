import pytest
from page.app import App



class TestAddMember():

    def setup(self):
        self.app = App()
        self.main = self.app.start_app().goto_main()

    def teardown(self):
        self.app.stop_app()

    def test_wework_add_mem(self):
        result = self.main.goto_contact().goto_add_member().addfrom_manual().\
            fillin_character("hehe", "1234567899510").check_add()
        assert result == "添加成功"