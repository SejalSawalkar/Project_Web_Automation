################################################################
#Topic: CHECKBOX and SLIDER

#Description: It will go on snapdeal website select AERTOXX from
#             brand and then new it will move slider to get
#             preferred price

###############################################################

import pytest
from selenium import webdriver
from pageObject.Script10 import script10
from Utility.customlogger import logGen


class Test_script10:
    log = logGen.loggen()

    @pytest.mark.groupb
    def test_script10(self, driver):
        self.driver = driver
        self.t10 = script10(self.driver)
        self.t10.checkbox(self.driver)
        self.log.info("clicked on checkbox")
        self.t10.slider(self.driver)
        self.log.info("moved slider")





















##############################################################
#
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.chrome.service import Service
# import time
# from selenium.webdriver.common.by import By
# import configparser
#
# class test10:
#     def setup_driver(self):
#         service = Service(executable_path='/Driver/chromedriver-win64/chromedriver.exe')
#         driver = webdriver.Chrome(service=service)
#         time.sleep(3)
#         driver.maximize_window()
#         return driver
#
#     def test10(self,driver):
#         config = configparser.ConfigParser()
#         config.read('C:/Users/sawal/PycharmProjects/BYWMS/Testdata/script.ini')
#         driver.get(config.get("test10","url"))
#         driver.implicitly_wait(10)
#
#
#         # scroll
#         brand = driver.find_element(By.XPATH, config.get("test10","brandxpath"))
#         driver.execute_script("arguments[0].scrollIntoView();", brand)
#         time.sleep(3)
#
#         # checkbox of brand
#         checkbox = driver.find_elements(By.XPATH, config.get("test10","checkboxxpath"))
#
#         for i in checkbox:
#             name = i.get_attribute('for')
#             if name == config.get("test10","brandname"):
#                 i.click()
#         time.sleep(3)
#
#         # slider
#         s1 = driver.find_element(By.XPATH,config.get("test10","silderleftxpath"))
#         s2 = driver.find_element(By.XPATH,config.get("test10","silderrightxpath"))
#
#         act = ActionChains(driver)
#
#         # act.drag_and_drop_by_offset(s1,60,0).perform()
#         act.click_and_hold(s1).pause(1).move_by_offset(60, 0).release().perform()
#         time.sleep(3)
#         act.click_and_hold(s2).pause(1).move_by_offset(-30, 0).release().perform()
#         time.sleep(3)
#
#         driver.quit()
#
# #call
# a = test10()
# driver = a.setup_driver()
# a.test10(driver)

















