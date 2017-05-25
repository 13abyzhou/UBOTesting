# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

def logout(self):
    driver = self.driver
    driver.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/header/div[3]/a").click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[3]/md-dialog/div/button[2]").click()
    driver.find_element_by_xpath("//input[@type='password']").clear()
    driver.find_element_by_xpath("//input[@type='password']").send_keys("ASdf!@34")
    time.sleep(3)
    driver.close()
    
