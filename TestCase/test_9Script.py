#############################################################################
#Topic: ALERT

#Description: It will go on rediff mail website and directly click on sign in
#             alert will popup ; handle that popup and then enter username
#             & password and sign in successfully!

##########################################################################


import pytest
from selenium import webdriver
from pageObject.Script9 import script9
from Utility.customlogger import logGen


class Test_script9:
    log = logGen.loggen()

    @pytest.mark.groupb
    def test_script9(self, driver):
        self.driver = driver
        self.t9 = script9(self.driver)
        self.t9.alert(self.driver)
        self.log.info("accepted alert box")
        self.t9.signin(self.driver)
        self.log.info("entered correct data and signin")


















##############################################################################
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time
# from selenium.webdriver.common.by import By
# import configparser
#
# class test9:
#     def setup_driver(self):
#         service = Service(executable_path='/Driver/chromedriver-win64/chromedriver.exe')
#         driver = webdriver.Chrome(service=service)
#         time.sleep(3)
#         driver.maximize_window()
#         return driver
#
#     def test9(self,driver):
#         config = configparser.ConfigParser()
#         config.read('C:/Users/sawal/PycharmProjects/BYWMS/Testdata/script.ini')
#         driver.get(config.get("test9","url"))
#         driver.implicitly_wait(10)
#
#         # sign in
#         driver.find_element(By.XPATH, config.get("test9","signxpath")).click()
#         time.sleep(3)
#
#         # alert
#         alert = driver.switch_to.alert
#         time.sleep(3)
#         alert.accept()
#         time.sleep(3)
#
#         # username, password, sign in
#         driver.find_element(By.XPATH, config.get("test9","usernamexpath")).send_keys(config.get("test9","username"))
#         driver.find_element(By.XPATH, config.get("test9","passwordxpath")).send_keys(config.get("test9","password"))
#         driver.find_element(By.XPATH,config.get("test9","signxpath")).click()
#         time.sleep(3)
#
#         driver.quit()
#
# #call
# a = test9()
# driver = a.setup_driver()
# a.test9(driver)
