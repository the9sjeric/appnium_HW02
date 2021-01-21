from page.base import BasePage


class AddMember(BasePage):

    def fillin_character(self, name, phonenum):
        from page.select_add_method import SelectAddMethod

        self.driver.find_element_by_xpath('//*[contains(@resource-id,"b78") and @index="2"]').send_keys(name)
        self.driver.find_element_by_xpath(
            '//*[contains(@resource-id,"b8_") and @class="android.widget.RelativeLayout"]').click()
        self.driver.find_element_by_xpath('//*[contains(@resource-id,"elq") and @text="男"]').click()
        self.driver.find_element_by_xpath('//*[@text="手机号"]').send_keys(phonenum)
        self.driver.find_element_by_xpath('//*[@text="保存"]').click()

        return SelectAddMethod(self.driver)

