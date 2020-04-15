from Locators.locators import Locators
class LogoutPage():
    def __init__(self,driver):
        self.driver=driver
        self.Logout = Locators.logout
    def click_logout(self):
        self.driver.find_element_by_xpath(self.Logout).click()