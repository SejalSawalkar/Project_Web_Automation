################################################################
#Topic: MULTIPLE WINDOWS

#Description: It will go on salesforce website and click on start free trial
#               new window will open ; move to second window enter text
#               and again move back to main window

###############################################################


import pytest
from selenium import webdriver
from pageObject.Script8 import script8
from Utility.customlogger import logGen


class Test_script8:
    log = logGen.loggen()

    @pytest.mark.groupb
    def test_script8(self, driver):
        self.driver = driver
        self.t8 = script8(self.driver)
        self.t8.mul_window(self.driver)
        self.log.info("moved to multiple window")

























##################################################################
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time
# from selenium.webdriver.common.by import By
# import configparser
#
# class test8:
#     def setup_driver(self):
#         service = Service(executable_path='/Driver/chromedriver-win64/chromedriver.exe')
#         driver = webdriver.Chrome(service=service)
#         time.sleep(3)
#         driver.maximize_window()
#         return driver
#
#     def test8(self,driver):
#         config = configparser.ConfigParser()
#         config.read('C:/Users/sawal/PycharmProjects/BYWMS/Testdata/script.ini')
#         driver.implicitly_wait(10)
#         driver.get(config.get("test8","url"))
#
#         # contact us
#         driver.find_element(By.XPATH,config.get("test8","contatusxpath")).click()
#         time.sleep(2)
#
#         # Handling window
#         w = driver.window_handles
#         original_window = w[0]
#         new_window = w[1]
#         driver.switch_to.window(new_window)
#         time.sleep(2)
#
#         # new window opened and entering data
#         driver.find_element(By.XPATH,config.get("test8","firstnamexpath")).send_keys(config.get("test8","firstname"))
#         time.sleep(3)
#
#         # switch to main window
#         driver.switch_to.window(original_window)
#         time.sleep(3)
#
#         driver.quit()
#
# #call
# a = test8()
# driver = a.setup_driver()
# a.test8(driver)