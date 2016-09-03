#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import unittest
import HTMLTestRunner

sys.path.append("/testIsomp/common/")
from _mail import *

class testSuite(unittest.TestCase):
    u'''测试test_personsuite的所有测试用例'''
    if __name__ == "__main__":
        #定义测试报告的输出页面
        reportFile = "G:/testIsomp/report/testReport.html"
        rf = file(reportFile,'wb')
        
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        
        dir = "/testIsomp/testSuite"
        package_tests = loader.discover(start_dir=dir,pattern='test*.py')
        suite.addTests(package_tests)
        
        runner = HTMLTestRunner.HTMLTestRunner(stream=rf,title="Report_title",description="Report_description")
        runner.run(suite)
        #直接跑测试用例
        #unittest.TextTestRunner().run(suite)
        #sendMail().send_mail()
