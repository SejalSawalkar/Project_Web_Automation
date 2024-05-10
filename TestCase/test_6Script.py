#############################################################################
#Topic: IMPLICIT WAIT AND EXPLICIT WAIT

#Description: It will go on google and use implicit wait to click on gmail ;
              # explicit wait to click on sign in tab

#############################################################################


import pytest
from selenium import webdriver
from pageObject.Script6 import script6
from Utility.customlogger import logGen


class Test_script6:
    log = logGen.loggen()

    @pytest.mark.groupa
    def test_script6(self, driver):
        self.driver = driver
        self.t6 = script6(self.driver)
        self.t6.implicitywait(self.driver)
        self.log.info("used implicit wait")
        self.t6.explicitwait(self.driver)
        self.log.info("used explicit wait")



















#############################################################################
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# import configparser
#
#
# class test6:
#     def setup_driver(self):
#         service = Service(executable_path='/Driver/chromedriver-win64/chromedriver.exe')
#         driver = webdriver.Chrome(service=service)
#         time.sleep(3)
#         driver.maximize_window()
#         return driver
#
#     def test6(self,driver):
#         config = configparser.ConfigParser()
#         config.read('C:/Users/sawal/PycharmProjects/BYWMS/Testdata/script.ini')
#         #implicit
#         driver.implicitly_wait(10)
#         driver.get(config.get("test6","url"))
#         driver.find_element(By.XPATH, config.get("test6","gmail")).click()
#
#         # explicit wait declaration
#         mywait = WebDriverWait(driver, 10, ignored_exceptions=[Exception])
#         signin = mywait.until(expected_conditions.presence_of_element_located((By.XPATH, config.get("test6","sign"))))
#         signin.click()
#         driver.quit()
#
#
# #call
# a = test6()
# driver = a.setup_driver()
# a.test6(driver)

