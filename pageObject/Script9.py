import time

from selenium.webdriver.common.by import By
from selenium import webdriver

from Utility.readscript import readscript9


class script9:
    url = readscript9.geturl()
    signxpath = readscript9.getsignxpath()
    usernamexpath = readscript9.getusernamexpath()
    username = readscript9.getusername()
    passwordxpath = readscript9.getpasswordxpath()
    password = readscript9.getpassword()

    def __init__(self,driver):
        self.driver = driver

    def alert(self,driver):
        driver.get(self.url)
        time.sleep(2)
        # sign in
        driver.find_element(By.XPATH, self.signxpath).click()
        time.sleep(3)
        # alert
        alert = driver.switch_to.alert
        time.sleep(3)
        alert.accept()
        time.sleep(3)

    def signin(self,driver):
        # username, password, sign in
        driver.find_element(By.XPATH,self.usernamexpath).send_keys(self.username)
        driver.find_element(By.XPATH,self.passwordxpath).send_keys(self.password)
        driver.find_element(By.XPATH,self.signxpath).click()
        time.sleep(3)
        signin_page = driver.find_element(By.XPATH,"//a[text()='« Back to login page']")
        if signin_page.is_displayed() == True:
            assert True
        else:
            assert False

        driver.quit()
