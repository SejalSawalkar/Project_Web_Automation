import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from Utility.readscript import readscript1

class script1:
    url = readscript1.geturl()
    iframid = readscript1.getiframeid()
    dobxpath = readscript1.getdobxpath()
    calxpath = readscript1.getcalxpath()
    date = readscript1.getdate()
    month = readscript1.getmonth()
    year = readscript1.getyear()
    monthxpath = readscript1.getmonthxpath()
    forwardtrixpath = readscript1.getforwardtrixpath()
    yearxpath=readscript1.getyearxpath()
    datexpath=readscript1.getdatexpath()

    def __init__(self,driver):
        self.driver = driver

    def movetodob(self,driver):
        driver.get(self.url)
        time.sleep(2)
        iframe = driver.find_element(By.ID,self.iframid)
        driver.switch_to.frame(iframe)
        time.sleep(2)
        dob = driver.find_element(By.XPATH,self.dobxpath)
        driver.execute_script("arguments[0].scrollIntoView();", dob)
        if dob.is_displayed() == True:
            assert True
        else:
            assert False
        time.sleep(2)
        driver.find_element(By.XPATH,self.calxpath).click()
        time.sleep(2)

    def datepicker(self,driver):
        while True:
            mon = driver.find_element(By.XPATH, self.monthxpath).text
            if mon == self.month:
                break
            else:
                driver.find_element(By.XPATH, self.forwardtrixpath).click()

        time.sleep(3)
        # years
        yrs = driver.find_elements(By.XPATH,self.yearxpath)
        for i in yrs:
            if i.text == self.year:
                i.click()
                break
        # date
        d = driver.find_elements(By.XPATH,self.datexpath)
        for j in d:
            if j.text == self.date:
                j.click()
                break


        time.sleep(3)
        driver.quit()


