from selenium.webdriver.remote.webdriver import WebDriver
from appium.webdriver.common.mobileby import MobileBy


class BasePage():

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, byele):
        return self.driver.find_element(*byele)

    def find_click(self, byele):
        return self.find(byele).click()

    def find_send(self, byele, text):
        return self.find(byele).send_keys(text)

    def find_get_text(self, byele):
        return self.find(byele).text
