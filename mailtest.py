#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#浏览器数组
lists=['firefox','internet explorer','chrome']
#通过不同的浏览器执行脚本
for browser in lists:
    print browser
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities={'platform': 'ANY',
                              'browserName':browser,
                              'version': '',
                              'javascriptEnabled': True
                              }
        )
    driver.get("http://www.youdao.com")
    time.sleep(30)
    driver.close()
