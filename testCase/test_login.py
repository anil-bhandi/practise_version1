import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("*************** verifying homepage title *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        
        if act_title == "Your store. Login":
            self.logger.info("*************** Homepage title test passed *****************")
            assert True
            self.driver.close()


        else:
            self.driver.save_screenshot(".\\Screenshots\\"+ "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*************** Homepage title test failed *****************")
            assert False
            
            
    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("*************** Verifiying login test *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("*************** login test passed *****************")
            assert True

            
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+ "test_login.png")
            self.driver.close()
            self.logger.error("*************** login test failed *****************")
            assert False
