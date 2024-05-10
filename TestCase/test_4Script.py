#############################################################################
#Topic: MOUSE OPERATORS

#Description: It will go on orangehrm website then login move to my info
#             then update full name using mouse operators and save successfully

#############################################################################


import pytest
from selenium import webdriver
from pageObject.Script4 import script4
from Utility.customlogger import logGen


class Test_script4:
    log = logGen.loggen()

    @pytest.mark.groupa
    def test_script4(self, driver):
        self.driver = driver
        self.t4 = script4(self.driver)
        self.t4.login(self.driver)
        self.log.info("login to the website")
        self.t4.updatename(self.driver)
        self.log.info("updated username and saved")


































########################################################################
# from selenium import webdriver
# from selenium.webdriver import ActionChains, Keys
# from selenium.webdriver.chrome.service import Service
# import time
# from selenium.webdriver.common.by import By
# import configparser
#
# class test4:
#     def setup_driver(self):
#         service = Service(executable_path='/Driver/chromedriver-win64/chromedriver.exe')
#         driver = webdriver.Chrome(service=service)
#         time.sleep(3)
#         driver.maximize_window()
#         return driver
#
#     def test4(self,driver):
#         config = configparser.ConfigParser()
#         config.read('C:/Users/sawal/PycharmProjects/BYWMS/Testdata/script.ini')
#         driver.get(config.get("test4","url"))
#         time.sleep(3)
#         driver.find_element(By.XPATH, config.get("test4","usernamexpath")).send_keys(config.get("test4","username"))
#         driver.find_element(By.XPATH, config.get("test4","passwordxpath")).send_keys(config.get("test4","password"))
#         driver.find_element(By.XPATH, config.get("test4","signxpath")).click()
#         time.sleep(5)
#         driver.find_element(By.XPATH, config.get("test4","infoxpath")).click()
#         time.sleep(3)
#
#         act = ActionChains(driver)
#         #control a;backspace
#         driver.find_element(By.XPATH, config.get("test4","firstnamexpath")).click()
#         act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
#         act.send_keys(Keys.BACKSPACE).perform()
#         act.send_keys(config.get("test4","firstname")).perform()
#         time.sleep(3)
#
#         driver.find_element(By.XPATH, config.get("test4","middlenamexpath")).click()
#         act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
#         act.send_keys(Keys.BACKSPACE).perform()
#         act.send_keys(config.get("test4","middlename")).perform()
#         time.sleep(3)
#
#         driver.find_element(By.XPATH, config.get("test4","lastnamexpath")).click()
#         act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
#         act.send_keys(Keys.BACKSPACE).perform()
#         act.send_keys(config.get("test4","lastname")).perform()
#         time.sleep(3)
#
#         driver.find_element(By.XPATH,config.get("test4","savexpath")).click()
#         time.sleep(5)
#
#         driver.quit()
#
# #call
# a = test4()
# driver = a.setup_driver()
# a.test4(driver)










