#coding=utf-8
import unittest, time, os, io
import HTMLTestRunner

#导入测试文件
#import sys
#把testcase目录添加到path下
#sys.path.append("\testcase")

#导入testcase目录下面所有文件
#from testcase import *
#import UBO_login,UBO_Search

listaa='C:\\Python27\\Test_Case_UBO\\testcase'

def creatsuitel():
	testunit=unittest.TestSuite()
	discover=unittest.defaultTestLoader.discover(listaa,
		pattern='UBO_*.py',
		top_level_dir=None)
	for test_suite in discover:
		for test_case in test_suite:
			testunit.addTests(test_case)
			print testunit
	return testunit
alltestnames=creatsuitel()


#testunit=unittest.TestSuite()

#将测试用例加入到测试容器(套件)中
#testunit.addTest(unittest.makeSuite(UBO_login.Login))
#testunit.addTest(unittest.makeSuite(UBO_Search.UBOSearch))

#定义测试报告存放路径，支持相对路径（路径及html文件需要先创建）
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
filename = "C:\\Python27\\Test_Case_UBO\\report\\"+now+'_result.html'
fp = file(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'UBO测试报告',
    description=u'用例执行情况：')

runner.run(alltestnames)

'''
#控制时间执行脚本
k=1
while k<2:
        timing = time.strftime('%H_%M', time.localtime(time.time()))
        if timing == '15_45':
                print u"test running:"
                runner.run(alltestnames) #执行测试用例
                print u"testing is done"
                break
        else:
                time.sleep(5)
                print timing
#执行测试用例
#runner.run(testunit)
'''

