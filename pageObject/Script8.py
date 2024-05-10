import time

from selenium.webdriver.common.by import By
from selenium import webdriver

from Utility.readscript import readscript8


class script8:
    url = readscript8.geturl()
    contatusxpath = readscript8.getcontatusxpath()
    firstnamexpath = readscript8.getfirstnamexpath()
    firstname = readscript8.getfirstname()
    cancelxpath = readscript8.getcancelxpath()

    def __init__(self,driver):
        self.driver = driver

    def mul_window(self,driver):
        driver.get(self.url)
        # contact us
        driver.find_element(By.XPATH,self.contatusxpath).click()
        time.sleep(2)
        # Handling window
        w = driver.window_handles
        original_window = w[0]
        new_window = w[1]
        driver.switch_to.window(new_window)
        time.sleep(2)

        # new window opened and entering data

        firstname = driver.find_element(By.XPATH, self.firstnamexpath)
        if firstname.is_enabled() == True:
            assert True
            print("Driver moved to new window!!")
            firstname.send_keys(self.firstname)
            time.sleep(3)
        else:
            assert False

        # switch to main window
        driver.switch_to.window(original_window)
        time.sleep(3)

        driver.quit()