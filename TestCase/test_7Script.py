#############################################################################
#Topic: NAVIGATION COMMMAND & COOKIES

#Description: It will go on nopcommerce website and navigate to computer window &
              # again move back to main window; count total cookies present ,
              # add cookies , print all the cookies , delete new added cookkies

#############################################################################


import pytest
from selenium import webdriver
from pageObject.Script7 import script7
from Utility.customlogger import logGen


class Test_script7:
    log = logGen.loggen()
    @pytest.mark.groupb
    def test_script7(self, driver):
        self.driver = driver
        self.t7 = script7(self.driver)
        self.t7.navigation(self.driver)
        self.log.info("navigated back and forward on website")
        self.t7.cookies(self.driver)
        self.log.info("added and deleted new cookies")




















############################################################################
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time
# from selenium.webdriver.common.by import By
# import configparser
#
# class test7:
#     def setup_driver(self):
#         service = Service(executable_path='/Driver/chromedriver-win64/chromedriver.exe')
#         driver = webdriver.Chrome(service=service)
#         time.sleep(3)
#         driver.maximize_window()
#         return driver
#
#     def test7(self,driver):
#         config = configparser.ConfigParser()
#         config.read('C:/Users/sawal/PycharmProjects/BYWMS/Testdata/script.ini')
#         driver.get(config.get("test7","url"))
#         # computers
#         driver.find_element(By.XPATH, config.get("test7","compxpath")).click()
#         time.sleep(3)
#
#         # navigation
#         driver.back() # reach to home page
#         time.sleep(2)
#         # driver.forward()#reach to computer page
#         # time.sleep(2)
#         driver.refresh() # refresh the page
#         time.sleep(2)
#
#         # cookies
#         c1 = driver.get_cookies()
#         print("total cookies: ", len(c1))  # count of cookies
#         # print(c1)
#
#         # add cookies
#         driver.add_cookie({"name": config.get("test7","cookiname"), "value": config.get("test7","cookivalue")})
#         c2 = driver.get_cookies()
#         print("total after adding new cookies", len(c2))
#         for c in c2:
#             print(c.get('name'), ":", c.get('value'))
#
#         # delete cookies
#         driver.delete_cookie("abc")
#         time.sleep(2)
#
#         driver.quit()
#
# #call
# a = test7()
# driver = a.setup_driver()
# a.test7(driver)








