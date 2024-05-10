#############################################################################
#Topic: SCROLL & READ DATA FROM STATIC TABLE

#Description: It will go on automationtest website then scroll to table;
#             read all the data from static table

#############################################################################

import pytest
from selenium import webdriver
from pageObject.Script3 import script3
from Utility.customlogger import logGen


class Test_script3:
    log = logGen.loggen()

    @pytest.mark.groupa
    def test_script3(self, driver):
        self.driver = driver
        self.t3 = script3(self.driver)
        self.t3.scroll(self.driver)
        self.log.info("scroll down to table")
        self.t3.readtable(self.driver)
        self.log.info("read data from static table")






























###############################################################################
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time
# from selenium.webdriver.common.by import By
# import configparser
#
# class test3:
#     def setup_driver(self):
#         service = Service(executable_path='/Driver/chromedriver-win64/chromedriver.exe')
#         driver = webdriver.Chrome(service=service)
#         time.sleep(3)
#         driver.maximize_window()
#         return driver
#
#     def test3(self,driver):
#         config = configparser.ConfigParser()
#         config.read('C:/Users/sawal/PycharmProjects/BYWMS/Testdata/script.ini')
#         driver.get(config.get("test3","url"))
#         time.sleep(3)
#         # scroll
#         table = driver.find_element(By.XPATH, config.get("test3","tablexpath"))
#         driver.execute_script("arguments[0].scrollIntoView();", table)
#         # to read data of full table
#         time.sleep(3)
#         row = len(driver.find_elements(By.XPATH, config.get("test3","rowxpath")))
#         col = len(driver.find_elements(By.XPATH, config.get("test3","colxpath")))
#         print("number of rows ", row)
#         print("number of col ", col)
#         value = driver.find_element(By.XPATH, config.get("test3","valuexpath")).text
#         print("value of ", value)
#         for r in range(2, row + 1):
#             for c in range(1, col + 1):
#                 data = driver.find_element(By.XPATH,config.get("test3","datexpath")).text
#                 print(data, end=" ")
#             print()
#
#         driver.quit()


#call
# a = test3()
# driver = a.setup_driver()
# a.test3(driver)











