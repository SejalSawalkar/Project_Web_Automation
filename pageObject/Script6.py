import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from Utility.readscript import readscript6

class script6:
    url = readscript6.geturl()
    gmail = readscript6.getgmail()
    sign = readscript6.getsign()

    def __init__(self,driver):
        self.driver = driver

    def implicitywait(self,driver):
         # implicit
         driver.implicitly_wait(10)
         driver.get(self.url)
         time.sleep(2)
         driver.find_element(By.XPATH,self.gmail).click()
         act_title = driver.title
         if act_title == "Gmail: Private and secure email at no cost | Google Workspace":
             assert True
         else:
             assert False

    def explicitwait(self,driver):
         # explicit wait declaration
         mywait = WebDriverWait(driver, 10, ignored_exceptions=[Exception])
         signin = mywait.until(expected_conditions.presence_of_element_located((By.XPATH,self.sign)))
         signin.click()
         driver.quit()
