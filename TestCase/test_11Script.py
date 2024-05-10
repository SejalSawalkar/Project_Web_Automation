################################################################
#Topic: DRAG & DROP , PROMPT , CUSTOMIZED XPATH

#Description: It will go on automationtest website first it will do drag and drop then
#             it will click on Prompt ; it will enter text in prompt
#             and then check whether it is inserted properly or not
#             to check it used customized xpath
###############################################################


import pytest
from selenium import webdriver
from pageObject.Script11 import script11
from Utility.customlogger import logGen


class Test_script11:
    log = logGen.loggen()

    @pytest.mark.groupb
    def test_script11(self, driver):
        self.driver = driver
        self.t11 = script11(self.driver)
        self.t11.drag_drop(self.driver)
        self.log.info("did drag and drop")
        self.t11.prompt(self.driver)
        self.log.info("entered text in prompt and verified it")












##############################################################
#
# from selenium import webdriver
# from selenium.webdriver import ActionChains, Keys
# from selenium.webdriver.chrome.service import Service
# import time
# from selenium.webdriver.common.by import By
# import configparser
#
# class test11:
#     def setup_driver(self):
#         service = Service(executable_path='/Driver/chromedriver-win64/chromedriver.exe')
#         driver = webdriver.Chrome(service=service)
#         time.sleep(3)
#         driver.maximize_window()
#         return driver
#
#     def test11(self,driver):
#         config = configparser.ConfigParser()
#         config.read('C:/Users/sawal/PycharmProjects/BYWMS/Testdata/script.ini')
#         driver.implicitly_wait(10)
#         driver.get(config.get("test11","url"))
#         time.sleep(5)
#
#         # drag and drop
#         s = driver.find_element(By.XPATH, config.get("test11","sourcexpath"))
#         t = driver.find_element(By.XPATH, config.get("test11","targetxpath"))
#         act = ActionChains(driver)
#         act.drag_and_drop(s, t).perform()
#         time.sleep(3)
#
#         # prompt
#         driver.find_element(By.XPATH, config.get("test11","promptxpath")).click()
#         alert = driver.switch_to.alert
#         time.sleep(3)
#         a = config.get("test11","prompttext")
#         alert.send_keys(a)
#         time.sleep(3)
#         alert.accept()
#         time.sleep(3)
#
#         # customized xpath
#         text = driver.find_element(By.XPATH, "//p[contains(text(),'" + a + "')]")
#         if text.is_displayed():
#             print(a, "- name is entered")
#         else:
#             print("Error")
#         time.sleep(3)
#         driver.quit()
#
# #call
# a = test11()
# driver = a.setup_driver()
# a.test11(driver)
#
