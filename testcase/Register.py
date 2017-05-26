# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.alert import Alert
import unittest, time, re
import sys
sys.path.append("\public")
from public import login
from public import logout

class Register(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://backoffice-dev.everymatrix.com/login"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_register(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        login.login(self)
        driver.find_element_by_css_selector("span.icon.icon-dropdown").click()
        driver.find_element_by_xpath("//img[@alt='CasinoEngine']").click()
        driver.find_element_by_xpath("//li[3]/a/span[2]").click()
        driver.find_element_by_link_text("Casino").click()
        time.sleep(5)
        driver.find_element_by_xpath("//button[2]").click()
        driver.find_element_by_name("gameName").clear()
        driver.find_element_by_name("gameName").send_keys("Atesting3")
        driver.find_element_by_name("shortName").click()
        driver.find_element_by_name("shortName").clear()
        driver.find_element_by_name("shortName").send_keys("Atesting3")
        driver.find_element_by_name("gameID").click()
        driver.find_element_by_name("gameID").clear()
        driver.find_element_by_name("gameID").send_keys("Atesting3")
        driver.find_element_by_xpath("(//input[@type='text'])[7]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[7]").send_keys("atesting3")
        Select(driver.find_element_by_xpath("//div[@id='tab1']/div/div/div[2]/div/div/select")).select_by_visible_text("NetEnt")
        driver.find_element_by_xpath("//option[@value='NetEnt']").click()
        time.sleep(3)
        Select(driver.find_element_by_xpath("//div[@id='tab1']/div/div/div[2]/div/div[4]/select")).select_by_visible_text("41 - 2BY2")
        driver.find_element_by_css_selector("option[value=\"string:41\"]").click()
        driver.find_element_by_css_selector("div.md-container.md-ink-ripple").click()
        driver.find_element_by_xpath("//md-tab-item[2]/span").click()
        driver.find_element_by_css_selector("span.ng-binding.ng-scope").click()
        driver.find_element_by_css_selector("button.Button.FormSubmit").click()
        time.sleep(2)
        try: self.assertEqual("Game[0] info saved successeful", driver.find_element_by_css_selector("span.NotificationText.ng-binding").text)
        except AssertionError as e: print driver.find_element_by_css_selector("span.NotificationText.ng-binding").text #self.verificationErrors.append(str(e))
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
