# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import sys
sys.path.append("\public")

from public import login
from public import logout

class UBOSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://backoffice-dev.everymatrix.com/login"
        self.verificationErrors = []
        self.accept_next_alert = True
        

    def test_game_search(self):
        u"""UBO游戏查找"""
        driver=self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        
        login.login(self)

        driver.find_element_by_css_selector("span.icon.icon-dropdown").click()
        driver.find_element_by_xpath("//img[@alt='CasinoEngine']").click()
        driver.find_element_by_xpath("//li[3]/a/span[2]").click()
        driver.find_element_by_css_selector("a.ProductSubMenuLink > span.text.ng-binding").click()
        driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("shawntest")
        time.sleep(2)
        driver.find_element_by_xpath("//button[3]").click()  
        time.sleep(3)
        numb=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div/div/section/div[1]/div/div[1]/ubo-casino-total-page/div").text
        print numb
        print numb[18:]
        numb2=int(numb[18:])+1
        print numb2
        logout.logout(self)

        
   
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
 
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
   
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
