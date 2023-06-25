import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XlUtilis
import time

class Test_002_Login:
    baseURL = ReadConfig.getApplicationUrl()
    path = ".//TestData/loginData.xlsx"
    logger = LogGen.loggen()
    

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("*************** Test_002_Login *****************")
        self.logger.info("*************** Verifiying login DDt test *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XlUtilis.getRowCount(self.path, 'Sheet1')
        print("Numbers of rows in an excel:", self.rows)

        lst_status = []

        for r in range(2, self.rows):
            self.username = XlUtilis.readData(self.path, 'Sheet1', r, 1)
            self.password = XlUtilis.readData(self.path, 'Sheet1', r, 2)
            self.exp = XlUtilis.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)    

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*************** passed *****************")
                    self.lp.clickLogout()
                    time.sleep(5)
                    lst_status.append("Pass")
                    
                elif self.exp == "Fail":
                    self.logger.info("*************** failed *****************")
                    
            
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*************** failed *****************")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    lst_status.append("Pass")

            if "Fail" not in lst_status:
                self.logger.info("*************** Login DDT test passed *****************")   
                assert True
            else:
                self.logger.info("*************** Login DDT test failed *****************")   
                assert False
        self.driver.close()
        self.logger.info("*************** End of Login ddt test *****************")
        self.logger.info("*************** Completed Test_002_Login  *****************")
