#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsomp/common/")
from _excelRead import excelRead
from _cnEncode import cnEncode
from _elementText import *

sys.path.append("/testIsomp/testData/")
from _testDataPath import dataFileName

sys.path.append("/testIsomp/webElement/login/")
from loginElement import *

class testLogin:
    
    def __init__(self):
        pass
    
    #从sheet1获取登陆数据
    def get_login_data_by_sheet1(self):
        
        #获取登录数据路径
        login_test_data_url = dataFileName().get_login_test_data_url()
        #获取sheet名称
        sheet1 = dataFileName().GET_SHEET1()
        #获取excel数据
        loginData = excelRead().get_excel_data(login_test_data_url,sheet1)
        
        return loginData

    #登陆测试
    def login_test(self,driver):
        u'''可以循环设定数据测试堡垒主机登录'''
        element = elementText()
        loginData = self.get_login_data_by_sheet1()
        
        for dataRow in range(len(loginData)):
            #把单行的数据赋值给列表data
            data = loginData[dataRow]
                
            #print data
            if dataRow == 0:
                pass
            else:
                loginPage().login(driver,int(data[0]),data[1],str(int(data[2])))
                print element.get_element_text_by_class("aui_content",driver)
                element.click_element_by_class("aui_state_highlight",driver)


if __name__ == "__main__":
    browser = initDriver().open_driver()
    testLogin().login_test(browser)