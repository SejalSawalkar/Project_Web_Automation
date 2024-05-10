#############################################################################
#Topic: CONDITIONAL COMMMANDS

#Description: It will go on herokuapp and check the checkbox1 and checkbox
#            is selected,enabled,displayed

#############################################################################


import pytest
from selenium import webdriver
from pageObject.Script5 import script5
from Utility.customlogger import logGen
import logging


class Test_script5:
    log = logGen.loggen()

    @pytest.mark.groupa
    def test_script5(self, driver):
        self.driver = driver
        self.t5 = script5(self.driver)
        self.t5.box1(self.driver)
        self.log.info("verified checkbox1")
        self.t5.box2(self.driver)
        self.log.info("verified checkbox1")





























#############################################################################
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
# import configparser
#
# class test5:
#     def setup_driver(self):
#         service = Service(executable_path='/Driver/chromedriver-win64/chromedriver.exe')
#         driver = webdriver.Chrome(service=service)
#         time.sleep(3)
#         driver.maximize_window()
#         return driver
#     def test5(self,driver):
#         config = configparser.ConfigParser()
#         config.read('C:/Users/sawal/PycharmProjects/BYWMS/Testdata/script.ini')
#         driver.get(config.get("test5","url"))
#         # is_displayed
#         checkbox = driver.find_element(By.XPATH, config.get("test5","checkbox1"))
#         print("status displayed of checkbox 1 = ", checkbox.is_displayed())
#         print("status selected of checkbox 1 = ",checkbox.is_selected())
#         time.sleep(3)
#         # is_enabled and is_selected
#         checkbox2 = driver.find_element(By.XPATH, config.get("test5","checkbox2"))
#         print("status enabled of checkbox 2 = ", checkbox2.is_enabled())
#         print("status selected of checkbox 2 = ", checkbox2.is_selected())
#         time.sleep(3)
#         driver.quit()
#
#
# #call
# a = test5()
# driver = a.setup_driver()
# a.test5(driver)














