#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time
import sys
import userinfo
def login(self):
    driver = self.driver
    username,password = userinfo.fun()
    driver.find_element_by_xpath("/html/body/div/div/div/div/ul/li[2]/a/span[2]").click()
    driver.find_element_by_xpath("/html/body/div/div/div/div/form/fieldset/ng-switch/div/div[1]/input").clear()
    driver.find_element_by_xpath("/html/body/div/div/div/div/form/fieldset/ng-switch/div/div[1]/input").send_keys("")
    driver.find_element_by_xpath("/html/body/div/div/div/div/form/fieldset/ng-switch/div/div[2]/input").clear()
    driver.find_element_by_xpath("/html/body/div/div/div/div/form/fieldset/ng-switch/div/div[2]/input").send_keys("")
    driver.find_element_by_xpath("/html/body/div/div/div/div/form/fieldset/ng-switch/div/div[1]/input").clear()
    driver.find_element_by_xpath("/html/body/div/div/div/div/form/fieldset/ng-switch/div/div[1]/input").send_keys(username)
    driver.find_element_by_xpath("/html/body/div/div/div/div/form/fieldset/ng-switch/div/div[2]/input").clear()
    driver.find_element_by_xpath("/html/body/div/div/div/div/form/fieldset/ng-switch/div/div[2]/input").send_keys(password)
    driver.find_element_by_xpath("/html/body/div/div/div/div/form/fieldset/div/button").click()
    time.sleep(2)
