#############################################################################
#Topic: SCROLL , IFRAME , DATEPICKER

#Description: It will go on automationtest website and scroll to datepicker option;
             # move to datepicker ifram ; select proper date,month,year and enter date

#############################################################################
import pytest
from selenium import webdriver
from pageObject.Script1 import script1
from Utility.customlogger import logGen



class Test_script1:
    log = logGen.loggen()
    @pytest.mark.groupa
    def test_script1(self, driver):
        self.driver = driver
        self.t1 = script1(self.driver)
        self.t1.movetodob(self.driver)
        self.log.info("scroll down to dob")
        self.t1.datepicker(self.driver)
        self.log.info("date selected from datepicker")






























# class test1:
#     def setup_driver(self):
#         service = Service(executable_path='/Driver/chromedriver-win64/chromedriver.exe')
#         driver = webdriver.Chrome(service=service)
#         time.sleep(3)
#         driver.maximize_window()
#
#         return driver
#
#     def test1(self,driver):
#         config = configparser.ConfigParser()
#         config.read('C:/Users/sawal/PycharmProjects/BYWMS/Testdata/script.ini')
#         driver.get(config.get("test1","url"))
#         time.sleep(3)
#
#         # switch to iframe
#         iframe = driver.find_element(By.ID, config.get("test1","iframeid"))
#         driver.switch_to.frame(iframe)
#         time.sleep(3)
#
#         # scroll
#         dob = driver.find_element(By.XPATH, config.get("test1","dobxpath"))
#         driver.execute_script("arguments[0].scrollIntoView();", dob)
#         time.sleep(3)
#
#         # click on calendar icon
#         driver.find_element(By.XPATH, config.get("test1","calxpath")).click()
#         time.sleep(3)
#
#         # date,month,year
#         # month
#         while True:
#             mon = driver.find_element(By.XPATH, config.get("test1","monthxpath")).text
#             if mon == config.get("test1","month"):
#                 break
#             else:
#                 driver.find_element(By.XPATH, config.get("test1","forwardtrixpath")).click()
#
#         time.sleep(3)
#
#         # years
#         yrs = driver.find_elements(By.XPATH, config.get("test1","yearxpath"))
#         for i in yrs:
#             if i.text == config.get("test1","year"):
#                 i.click()
#                 break
#
#         # date
#         d = driver.find_elements(By.XPATH, config.get("test1","datexpath"))
#         for j in d:
#             if j.text == config.get("test1","date"):
#                 j.click()
#                 break
#
#         time.sleep(3)
#         driver.quit()


#call
# a = test1()
# driver = a.setup_driver()
# a.test1(driver)
