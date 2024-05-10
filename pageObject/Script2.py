import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

from Utility.readscript import readscript2

class script2:
    url = readscript2.geturl()
    productsxpath = readscript2.getproductsxpath()
    selectproductopt = readscript2.getselectproductopt()
    alloptionxpath = readscript2.getalloptionxpath()
    animalxpath = readscript2.getanimalxpath()
    selectanimalopt = readscript2.getselectanimalopt()

    def __init__(self,driver):
        self.driver = driver

    def products(self,driver):
        driver.get(self.url)
        time.sleep(2)
        products = Select(driver.find_element(By.XPATH, self.productsxpath))
        time.sleep(3)
        # using select command
        products.select_by_visible_text(self.selectproductopt)
        print("Google selected")
        time.sleep(3)
        # capture length all the options
        a = products.options
        if len(a) == 4:
            assert True
            print("length of Product dropdown = ", len(a))
        else:
            assert False

        # capture text of all the options
        p = driver.find_elements(By.XPATH, self.alloptionxpath)
        for i in a:
            print(i.text)

    def animals(self,driver):
        # selecting dropdown options without using inbuilt functions
        animals = Select(driver.find_element(By.XPATH, self.animalxpath))
        b = animals.options
        for i in b:
            if i.text == self.selectanimalopt:
                i.click()
                break
        time.sleep(3)
        print("Avatar selected")


        driver.quit()
