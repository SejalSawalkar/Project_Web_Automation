import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

from Utility.readscript import readscript11


class script11:
    url = readscript11.geturl()
    sourcexpath = readscript11.getsourcexpath()
    targetxpath = readscript11.gettargetxpath()
    promptxpath = readscript11.getpromptxpath()
    prompttext = readscript11.getprompttext()
    textxpath = readscript11.gettextxpath()

    def __init__(self,driver):
        self.driver = driver

    def drag_drop(self,driver):
        driver.get(self.url)
        time.sleep(2)
        # drag and drop
        s = driver.find_element(By.XPATH,self.sourcexpath)
        t = driver.find_element(By.XPATH,self.targetxpath)
        act = ActionChains(driver)
        act.drag_and_drop(s, t).perform()
        time.sleep(3)

    def prompt(self,driver):
        # prompt
        driver.find_element(By.XPATH,self.promptxpath).click()
        alert = driver.switch_to.alert
        time.sleep(3)
        a = self.prompttext
        alert.send_keys(a)
        time.sleep(3)
        alert.accept()
        time.sleep(3)

        # customized xpath
        text = driver.find_element(By.XPATH, "//p[contains(text(),'" + a + "')]")
        if text.is_displayed():
            print(a, "- name is entered")
        else:
            print("Error")
        time.sleep(3)
        driver.quit()
