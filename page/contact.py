from page.select_add_method import SelectAddMethod
from page.base import BasePage
from appium.webdriver.common.mobileby import By

class ContactPage(BasePage):

    def goto_my_customer(self):
        pass

    def goto_add_member(self):
        self.find_click((By.XPATH, '//*[@text="添加成员"]'))
        return SelectAddMethod(self.driver)

    def goto_mypage(self):
        pass