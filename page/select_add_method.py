from page.add_member import AddMember
from page.base import BasePage

class SelectAddMethod(BasePage):

    def addfrom_wechat(self):
        pass

    def addfrom_phone(self):
        pass

    def addfrom_manual(self):
        self.driver.find_element_by_xpath('//*[@text="手动输入添加"]').click()
        return AddMember(self.driver)

    def check_add(self):
        ele = self.driver.find_element_by_xpath('//*[@class="android.widget.Toast"]').text
        return ele
