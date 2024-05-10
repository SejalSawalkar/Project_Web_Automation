import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

from Utility.readscript import readscript10


class script10:
    url = readscript10.geturl()
    brandxpath = readscript10.getbrandxpath()
    checkboxxpath = readscript10.getcheckboxxpath()
    brandname = readscript10.getbrandname()
    silderleftxpath = readscript10.getsilderleftxpath()
    silderrightxpath = readscript10.getsilderrightxpath()

    def __init__(self,driver):
        self.driver = driver

    def checkbox(self,driver):
        driver.get(self.url)
        time.sleep(2)
        # scroll
        brand = driver.find_element(By.XPATH,self.brandxpath)
        driver.execute_script("arguments[0].scrollIntoView();", brand)
        time.sleep(3)
        # checkbox of brand
        checkbox = driver.find_elements(By.XPATH,self.checkboxxpath)

        for i in checkbox:
            name = i.get_attribute('for')
            if name == self.brandname:
                i.click()
        time.sleep(3)

        validation = driver.find_element(By.XPATH,"//div[contains(@class,'filters-top-selected')]/descendant::div[contains(@class,'navFiltersPill') and text()='Brand: ']")
        if validation.is_displayed() == True:
            assert True
        else:
            assert False

    def slider(self,driver):
        # slider
        s1 = driver.find_element(By.XPATH,self.silderleftxpath)
        s2 = driver.find_element(By.XPATH,self.silderrightxpath)

        act = ActionChains(driver)
        # act.drag_and_drop_by_offset(s1,60,0).perform()
        act.click_and_hold(s1).pause(1).move_by_offset(60, 0).release().perform()
        time.sleep(3)
        act.click_and_hold(s2).pause(1).move_by_offset(-30, 0).release().perform()
        time.sleep(3)

        driver.quit()
