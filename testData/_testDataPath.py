#coding=utf-8
#设定excel数据文件名字，统一调用
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#登陆excel数据文件
LOGIN_TEST_DATA_URL = "/testIsomp/testData/login_test_data.xlsx"

#自然人excel数据位置
PERSON_TEST_DATA_URL = "/testSimp/testData/person_test_data.xlsx"

#unix资源excel数据位置
UNIX_TEST_DATA_URL = "/testSimp/testData/unix_test_data.xlsx"

#unix资源账号excel数据位置
UNIX_USER_TEST_DATA_URL = "/testSimp/testData/unix_user_test_data.xlsx"

#windows资源excel数据位置
RESOURCE_TEST_DATA_URL = "/testSimp/testData/windows_test_data.xlsx"

#windows资源账号excel数据位置
RESOURCE_TEST_USER_DATA_URL = "/testSimp/testData/windows_user_test_data.xlsx"

#网络设备local资源excel数据位置
LOCAL_TEST_DATA_URL = "/testSimp/testData/local_test_data.xlsx"

#网络设备local资源账号excel数据位置
LOCAL_USER_TEST_DATA_URL = "/testSimp/testData/local_user_test_data.xlsx"


#sheet1
SHEET_1 = "Sheet1"
#sheet2
SHEET_2 = "Sheet2"
#sheet3
SHEET_3 = "Sheet3"
#sheet4
SHEET_4 = "Sheet4"

class dataFileName:
    #获取excel中页的名称
    def GET_SHEET1(self):
        return SHEET_1
    
    def GET_SHEET2(self):
        return SHEET_2
    
    def GET_SHEET3(self):
        return SHEET_3
    
    def GET_SHEET4(self):
        return SHEET_4
    
    def get_login_test_data_url(self):
        return LOGIN_TEST_DATA_URL
    
    #获取自然人excel中的数据
    def get_person_test_data_url(self):
        return PERSON_TEST_DATA_URL
    
    #获取unix资源excel中数据
    def get_unix_test_data_url(self):
        return UNIX_TEST_DATA_URL
    
    #获取unix资源账号excel数据位置
    def get_unix_user_test_data_url(self):
        return UNIX_USER_TEST_DATA_URL
    
    #获取网络设备local资源excel中的数据
    def get_local_test_data_url(self):
        return LOCAL_TEST_DATA_URL

    #获取资源excel中的数据
    def get_resource_test_data_url(self):
        return RESOURCE_TEST_DATA_URL
    
    #获取资源用户中excel中的数据
    def get_resource_test_user_data_url(self):
        return RESOURCE_TEST_USER_DATA_URL
    
    
    #获取网络设备local资源账号excel中的数据
    def get_local_user_test_data_url(self):
        return LOCAL_USER_TEST_DATA_URL

#print dataFileName().getLogin_Test_Data()