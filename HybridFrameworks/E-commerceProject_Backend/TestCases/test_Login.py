import pytest
from selenium import webdriver
from PageObjects.LoginPage import Login
from Utilities.readProperties import ReadConfig
from Utilities.CustomLogger import LogGen

class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

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
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseUrl)
        self.lp= Login(self.driver)
        self.lp.setUserEmail(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("**** Home page title test passed ****")
            assert True
        else:
            self.logger.error("**** Home page title test failed****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            assert False
            self.driver.close()

        self.lp.clickLogout()
        self.driver.close