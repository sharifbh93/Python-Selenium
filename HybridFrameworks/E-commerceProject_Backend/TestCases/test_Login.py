import pytest
from selenium import webdriver
from PageObjects.LoginPage import Login

class Test_001_Login:
    baseUrl = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            #self.driver.get_screenshot_as_file(".\\Screenshots\\" + "Postive.png")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"Failed.png")
            assert False

    def test_Login(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp= Login(self.driver)
        self.lp.setUserEmail(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False