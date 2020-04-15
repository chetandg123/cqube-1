from selenium import webdriver
import unittest
import time
from Pages.homePage import HomePage
from Pages.loginPage import LoginPage
from Pages.logoutPage import LogoutPage
from Data.data import data

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get(data.url)
        login = LoginPage(driver)
        login.enter_username(data.username)
        login.enter_password(data.password)
        login.click_login()

        homepage = HomePage(driver)
        # homepage.MouseOverOnPoints()

        # homepage.ClickOn_Blocks()
        # homepage.MouseOverOnPoints()
        #
        # homepage.ClickOn_Cluster()
        # homepage.MouseOverOnPoints()
        #
        # homepage.ClickOn_Schools()
        # homepage.MouseOverOnPoints()



        # logoutPage = LogoutPage(driver)
        # logoutPage.click_logout()

    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        print("test completed")


    if __name__ == '__main__':
        unittest.main()



