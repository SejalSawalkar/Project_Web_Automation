import time

from selenium.webdriver.common.by import By
from selenium import webdriver

from Utility.readscript import readscript3

class script3:
    url = readscript3.geturl()
    tablexpath = readscript3.gettablexpath()
    rowxpath = readscript3.getrowxpath()
    colxpath = readscript3.getcolxpath()
    valuexpath = readscript3.getvaluexpath()
    datexpath = readscript3.getdatexpath()

    def __init__(self,driver):
        self.driver = driver

    def scroll(self,driver):
        driver.get(self.url)
        time.sleep(2)
        # scroll
        table = driver.find_element(By.XPATH, self.tablexpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", table)
        time.sleep(3)

    def readtable(self,driver):
        # to read data of table
        row = len(driver.find_elements(By.XPATH, self.rowxpath))
        col = len(driver.find_elements(By.XPATH, self.colxpath))
        # print("number of rows ", row)
        # print("number of col ", col)

        if row == 7 and col == 4:
            assert True
            print("No. of rows = 7; No. of col = 4")
        else:
            assert False

        value = driver.find_element(By.XPATH, self.valuexpath).text
        for r in range(2, row+1):
            author = driver.find_element(By.XPATH, "//table[contains(@name,'BookTable')]//tr["+str(r)+"]/td[2]").text
            if author == "Mukesh":
                book = driver.find_element(By.XPATH, "//table[contains(@name,'BookTable')]//tr["+str(r)+"]/td[1]").text
                price = driver.find_element(By.XPATH, "//table[contains(@name,'BookTable')]//tr[" + str(r) + "]/td[4]").text
                print("bookname-> ",book,"; price-> ",price)

        driver.quit()


