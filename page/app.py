from appium import webdriver
from page.base import BasePage
from page.main import MainPage

class App(BasePage):

    def start_app(self):
        if self.driver == None:
            desired_caps = {
                "platformName": "Android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.WwMainActivity",
                "noReset": "true"
            }
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()
        return self

    def stop_app(self):
        self.driver.quit()

    def goto_main(self)->MainPage:
        return MainPage(self.driver)