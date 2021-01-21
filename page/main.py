from page.base import BasePage
from page.contact import ContactPage


class MainPage(BasePage):

    def goto_contact(self):
        self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        return ContactPage(self.driver)

    def goto_workspace(self):
        pass

    def goto_mypage(self):
        pass