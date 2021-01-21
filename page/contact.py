from page.select_add_method import SelectAddMethod
from page.base import BasePage

class ContactPage(BasePage):

    def goto_my_customer(self):
        pass

    def goto_add_member(self):
        self.driver.find_element_by_xpath('//*[@text="添加成员"]').click()
        return SelectAddMethod(self.driver)

    def goto_mypage(self):
        pass