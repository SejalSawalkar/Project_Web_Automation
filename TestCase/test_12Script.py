################################################################
#Topic: EXCEPTION

#Description: It will go on amazon website and search for result
              # and in search if there is no result ; it will handle
              # nosuchelement Exception

###############################################################

import pytest
from selenium import webdriver
from pageObject.Script12 import script12
from Utility.customlogger import logGen


class Test_script12:
    log = logGen.loggen()

    @pytest.mark.groupb
    def test_script12(self, driver):
        self.driver = driver
        self.t12 = script12(self.driver)
        self.t12.exception(self.driver)
        self.log.info("used nosuchexception")




















##################################################################
#
# from selenium import webdriver
# from selenium.common import NoSuchElementException
# from selenium.webdriver.chrome.service import Service
# import time
# from selenium.webdriver.common.by import By
# import configparser
#
# class test12:
#     def setup_driver(self):
#         service = Service(executable_path='/Driver/chromedriver-win64/chromedriver.exe')
#         driver = webdriver.Chrome(service=service)
#         time.sleep(3)
#         driver.maximize_window()
#         return driver
#
#     def test12(self,driver):
#         config = configparser.ConfigParser()
#         config.read('C:/Users/sawal/PycharmProjects/BYWMS/Testdata/script.ini')
#         driver.get(config.get("test12","url"))
#         time.sleep(3)
#
#         correct_search = config.get("test12","correctsearch")
#         incorrect_search = config.get("test12","incorrectsearch")
#
#         driver.find_element(By.XPATH, config.get("test12","inputboxxpath")).send_keys(incorrect_search)
#         time.sleep(2)
#         driver.find_element(By.XPATH, config.get("test12","submitxpath")).click()
#         time.sleep(2)
#         try:
#             result = driver.find_element(By.XPATH, config.get("test12","resultxpath"))
#             if result.is_displayed():
#                 print("Results are printed")
#         except NoSuchElementException:
#             print("No results are found for ", incorrect_search)
#
#         driver.quit()
#
# # call
# a = test12()
# driver = a.setup_driver()
# a.test12(driver)

