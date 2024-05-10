import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from Utility.readscript import readscript4

class script4:
    url = readscript4.geturl()
    usernamexpath = readscript4.getusernamexpath()
    passwordxpath = readscript4.getpasswordxpath()
    signxpath = readscript4.getsignxpath()
    username = readscript4.getusername()
    password = readscript4.getpassword()
    infoxpath = readscript4.getinfoxpath()
    firstnamexpath = readscript4.getfirstnamexpath()
    firstname = readscript4.getfirstname()
    middlenamexpath = readscript4.getmiddlenamexpath()
    middlename = readscript4.getmiddlename()
    lastnamexpath = readscript4.getlastnamexpath()
    lastname = readscript4.getlastname()
    savexpath = readscript4.getsavexpath()

    def __init__(self,driver):
        self.driver = driver

    def login(self,driver):
        self.driver.get(self.url)
        time.sleep(2)
        driver.find_element(By.XPATH,self.usernamexpath).send_keys(self.username)
        driver.find_element(By.XPATH,self.passwordxpath).send_keys(self.password)
        driver.find_element(By.XPATH,self.signxpath).click()
        time.sleep(5)
        driver.find_element(By.XPATH,self.infoxpath).click()
        time.sleep(3)

    def updatename(self,driver):
        act = ActionChains(driver)
        # control a;backspace
        driver.find_element(By.XPATH,self.firstnamexpath).click()
        act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        act.send_keys(Keys.BACKSPACE).perform()
        act.send_keys(self.firstname).perform()
        time.sleep(3)

        driver.find_element(By.XPATH,self.middlenamexpath).click()
        act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        act.send_keys(Keys.BACKSPACE).perform()
        act.send_keys(self.middlename).perform()
        time.sleep(3)

        driver.find_element(By.XPATH,self.lastnamexpath).click()
        act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        act.send_keys(Keys.BACKSPACE).perform()
        act.send_keys(self.lastname).perform()
        time.sleep(3)

        driver.find_element(By.XPATH,self.savexpath).click()
        time.sleep(3)

        validation = driver.find_element(By.XPATH,"//div[contains(@class,'oxd-toast-container oxd-toast-container--bottom')]")
        if validation.is_displayed() == True:
            assert True
            print("Data saved successfully!!")
        else:
            assert False

        driver.quit()
