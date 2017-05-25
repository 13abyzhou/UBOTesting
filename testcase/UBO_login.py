#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

import sys
sys.path.append("\public")
#导入登录登出模块
from public import login
from public import logout

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url="https://backoffice-dev.everymatrix.com/login"
        self.verificationErrors=[]
        self.accept_next_alert=True
        
    def test_login(self):
        
        u"""UBO用户登录"""
        driver=self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        #调用登录模块        
        login.login(self)
        #调用登出模块
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

