import time

from selenium.webdriver.common.by import By
from selenium import webdriver

from Utility.readscript import readscript5

class script5:
    url = readscript5.geturl()
    checkbox1 = readscript5.getcheckbox1()
    checkbox2 = readscript5.getcheckbox2()

    def __init__(self,driver):
        self.driver = driver

    def box1(self,driver):
        driver.get(self.url)
        time.sleep(2)
        # is_displayed
        checkbox = driver.find_element(By.XPATH, self.checkbox1)
        print("status displayed of checkbox 1 = ", checkbox.is_displayed())
        print("status selected of checkbox 1 = ", checkbox.is_selected())
        time.sleep(3)

    def box2(self,driver):
        # is_enabled and is_selected
        checkbox2 = driver.find_element(By.XPATH,self.checkbox2)
        print("status enabled of checkbox 2 = ", checkbox2.is_enabled())
        print("status selected of checkbox 2 = ", checkbox2.is_selected())
        time.sleep(3)
        driver.quit()