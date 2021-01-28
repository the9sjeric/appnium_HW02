from page.base import BasePage
from page.contact import ContactPage
from appium.webdriver.common.mobileby import By


class MainPage(BasePage):

    def goto_contact(self):
        self.find_click((By.XPATH, '//*[@text="通讯录"]'))
        return ContactPage(self.driver)

    def goto_workspace(self):
        pass

    def goto_mypage(self):
        pass