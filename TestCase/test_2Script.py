#############################################################################
#Topic: DROPDOWN

#Description: It will go on chercher website then from PRODUCTS dropdown
#             select Google(using select command),length of dropdown,
#             print all the options from dropdown ; then move to ANIMALS dropdown
#             select AVATAR (using loop)

#############################################################################

import pytest
from selenium import webdriver
from pageObject.Script2 import script2
from Utility.customlogger import logGen


class Test_script2:
    log = logGen.loggen()

    @pytest.mark.groupa
    def test_script1(self, driver):
        self.driver = driver
        self.t2 = script2(self.driver)
        self.t2.products(self.driver)
        self.log.info("data selected from produts dropdown")
        self.t2.animals(self.driver)
        self.log.info("data selected from animals dropdown")





























################################################################

#from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support.select import Select
# import select
# import configparser
#
# class test2:
#     def setup_driver(self):
#         service = Service(executable_path='/Driver/chromedriver-win64/chromedriver.exe')
#         driver = webdriver.Chrome(service=service)
#         time.sleep(3)
#         driver.maximize_window()
#         return driver
#     def test2(self,driver):
#         config = configparser.ConfigParser()
#         config.read('C:/Users/sawal/PycharmProjects/BYWMS/Testdata/script.ini')
#         driver.get(config.get("test2","url"))
#         products = Select(driver.find_element(By.XPATH, config.get("test2","productsxpath")))
#         time.sleep(3)
#
#         # using select command
#         products.select_by_visible_text(config.get("test2","selectproductopt"))
#         # products.select_by_index("1")
#         print("Google selected")
#         time.sleep(3)
#
#         # capture length all the options
#         a = products.options
#         print("length of Product dropdown = ", len(a))
#
#         #capture text of all the options
#         p = driver.find_elements(By.XPATH,config.get("test2","alloptionxpath"))
#         for i in a:
#             print(i.text)
#
#         # selecting dropdown options without using inbuilt functions
#         animals = Select(driver.find_element(By.XPATH, config.get("test2","animalxpath")))
#         b = animals.options
#         for i in b:
#             if i.text == config.get("test2","selectanimalopt"):
#                 i.click()
#                 break
#         time.sleep(3)
#         print("Avatar selected")
#
#         driver.quit()
#
# #call
# a = test2()
# driver = a.setup_driver()
# a.test2(driver)
#


