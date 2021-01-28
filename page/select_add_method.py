from page.add_member import AddMember
from page.base import BasePage
from appium.webdriver.common.mobileby import By

class SelectAddMethod(BasePage):

    def addfrom_wechat(self):
        pass

    def addfrom_phone(self):
        pass

    def addfrom_manual(self):
        self.find_click((By.XPATH,'//*[@text="手动输入添加"]'))
        return AddMember(self.driver)

    def check_add(self):
        ele = self.find_get_text((By.XPATH,'//*[@class="android.widget.Toast"]'))
        return ele
