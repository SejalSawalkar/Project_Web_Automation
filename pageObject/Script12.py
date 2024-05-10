import time

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

from Utility.readscript import readscript12


class script12:
    url = readscript12.geturl()
    correctsearch = readscript12.getcorrectsearch()
    incorrectsearch = readscript12.getincorrectsearch()
    inputboxxpath = readscript12.getinputboxxpath()
    submitxpath = readscript12.getsubmitxpath()
    resultxpath = readscript12.getresultxpath()

    def __init__(self,driver):
        self.driver = driver

    def exception(self,driver):
        driver.get(self.url)
        time.sleep(3)
        driver.find_element(By.XPATH,self.inputboxxpath).send_keys(self.incorrectsearch)
        time.sleep(2)
        driver.find_element(By.XPATH,self.submitxpath).click()
        time.sleep(2)
        try:
            result = driver.find_element(By.XPATH, self.resultxpath)
            if result.is_displayed():
                print("Results are printed")
        except NoSuchElementException:
            print("No results are found for ", self.incorrectsearch)

        driver.quit()
