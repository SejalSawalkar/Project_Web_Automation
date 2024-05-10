import time

from selenium.webdriver.common.by import By
from selenium import webdriver

from Utility.readscript import readscript7


class script7:
    url = readscript7.geturl()
    compxpath = readscript7.getcompxpath()
    cookiname = readscript7.getcookiname()
    cookivalue = readscript7.getcookivalue()

    def __init__(self,driver):
        self.driver = driver

    def navigation(self,driver):
        driver.get(self.url)
        time.sleep(2)
        # computers
        driver.find_element(By.XPATH, self.compxpath).click()
        time.sleep(3)
        #validation
        act_title = driver.title
        if act_title == "nopCommerce demo store. Computers":
            assert True
            print("Navigated to Computers screen!!")
        else:
            assert False

        # navigation
        driver.back()  # reach to home page
        time.sleep(2)
        driver.refresh()  # refresh the page


    def cookies(self,driver):
        # cookies
        c1 = driver.get_cookies()
        print("total cookies: ", len(c1))  # count of cookies
        # add cookies
        driver.add_cookie({"name": self.cookiname, "value": self.cookivalue})
        c2 = driver.get_cookies()
        print("total after adding new cookies", len(c2))
        for c in c2:
            print(c.get('name'), ":", c.get('value'))
        # delete cookies
        driver.delete_cookie("abc")
        time.sleep(2)



