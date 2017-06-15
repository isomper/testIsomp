#coding=utf-8
u''' 
#文件名：login
#被测软件版本号：V2.8.1
#作成人：于洋
#生成日期：2015-09-16
#模块描述：登录页面
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append("/testIsomp/common/")
from _initDriver import *
from _icommon import getElement,selectElement,frameElement,commonFun
from _cnEncode import cnEncode

 
class loginPage(object):
    #登录方式
    LOGIN_METHOD = "loginMethod"
    #用户名(ad+口令)
    LOGIN_USERNAME = "username"
    #AD域方式用户名
    LOGIN_LDAP_USERNAME = "ldapUsername"
    #口令(ad+口令)
    LOGIN_PWD = "pwd"
    #AD域方式口令
    LOGIN_LDAP_PWD = "ldapPwd"
    #radius+口令登录方式口令
    LOGIN_RADIUS_PWD = "radiusPwd"
    #登录按钮
    LOGIN_BUTTON = "do_login"
    #系统名称
    LOGIN_SYSTEM_NAME = "systemName"
    #帮助与控件下载
    LOGIN_DOWNLOAD = "/html/body/div[2]/div[5]/a"
    #版权所有
    LOGIN_COPYRIGHT = "/html/body/div[2]/div[5]/text()[2]"
    #访问失败次数
    ACCESS_MAX_ACCOUNT = "lockStrategyCount"
    #会话策略保存按钮
    STRATEGY_SAVE_BUTTON = "save_globalStrategy"
    #退出
    QUIT = "logout"

    def __init__(self,driver):
        #selenuim驱动
        self.driver = driver
        self.getElem = getElement(driver)
        self.selectElem = selectElement(driver)
        self.frameElem = frameElement(self.driver)
        self.commElem = commonFun(self.driver)
        self.cnEnde = cnEncode()
        
   
    #获取登录方式
    def get_login_method(self):
        loginMethod = self.getElem.find_element_with_wait('id',self.LOGIN_METHOD)
        return self.selectElem.get_option_text(loginMethod,0)
        
    #设定登录方式
    def set_login_method(self,index): 
        try:
            if index != '':
                index = int(index)
            else :
                index = str(index)
            #self.frameElem.switch_to_content()
            #button_js = "var btn = document.getElementById(self.LOGIN_METHOD);"
            #self.driver.execute_script(button_js)
            loginMethod = self.getElem.find_element_with_wait('id',self.LOGIN_METHOD)
            self.selectElem.select_element_by_index(loginMethod,index)
        except Exception as e:
            print "login type error:" + str(e)
        
    #填写用户名
    def set_login_username(self,username):
        #self.frameElem.switch_to_content()
        try:
            reusername = self.cnEnde.is_float(username)
            self.getElem.find_element_with_wait('id',self.LOGIN_USERNAME).clear()
            self.getElem.find_element_wait_and_sendkeys('id',self.LOGIN_USERNAME,reusername)
        except Exception as e:
            print "login name error:" + str(e)
            
    #填写AD域用户名
    def set_ad_login_username(self,adUsername):
        #self.frameElem.switch_to_content()
        try:
            reADUsername = self.cnEnde.is_float(adUsername)
            self.getElem.find_element_with_wait('id',self.LOGIN_LDAP_USERNAME).clear()
            self.getElem.find_element_wait_and_sendkeys('id',self.LOGIN_LDAP_USERNAME,reADUsername)
        except Exception as e:
            print "LDAP login adUsername error:" + str(e)            
        
    #填写口令
    def set_login_pwd(self,pwd):
        #self.frameElem.switch_to_content()
        #print pwd
        try:
            repwd = self.cnEnde.is_float(pwd)
            self.getElem.find_element_with_wait('id',self.LOGIN_PWD).clear()
            self.getElem.find_element_wait_and_sendkeys('id',self.LOGIN_PWD,repwd)
        except Exception as e:
            print "login password error:" + str(e)
            
    #填写AD域密码
    def set_ad_login_pwd(self,adPwd):
        #self.frameElem.switch_to_content()
        try:
            readPwd = self.cnEnde.is_float(adPwd)
            self.getElem.find_element_with_wait('id',self.LOGIN_LDAP_PWD).clear()
            self.getElem.find_element_wait_and_sendkeys('id',self.LOGIN_LDAP_PWD,readPwd)
        except Exception as e:
            print "LDAP login adPwd error:" + str(e)
            
    #填写radius密码
    def set_radius_login_pwd(self,radiusPwd):
        #self.frameElem.switch_to_content()
        try:
            reRadiusPwd = self.cnEnde.is_float(radiusPwd)
            self.getElem.find_element_with_wait('id',self.LOGIN_RADIUS_PWD).clear()
            self.getElem.find_element_wait_and_sendkeys('id',self.LOGIN_RADIUS_PWD,reRadiusPwd)
        except Exception as e:
            print "Radius login radiusPwd error:" + str(e)
        
    #点击登录按钮
    def click_login_button(self):
        #self.frameElem.switch_to_content()
        try:
            login_button_js = "var btn = document.getElementById(self.LOGIN_BUTTON);if(btn != null)btn.click();"
            self.driver.execute_script(login_button_js)
            self.getElem.find_element_wait_and_click('id',self.LOGIN_BUTTON) 
        except Exception as e:
            print "login button error:" + str(e)


    #点击版权所有
    def click_login_copyright(self,driver): 
        pass
        
    #用户名口令认证登录
    def login(self,list):
        self.frameElem.switch_to_content()
        self.set_login_method(list[2])
        self.set_login_username(list[3])
        self.set_login_pwd(list[4])
        self.click_login_button()
    
    #登陆成功
    def is_login_success(self):
        success = False
        #self.frameElem.switch_to_content()
        try:
            self.frameElem.switch_to_top()
            text = self.getElem.find_element_wait_and_get_text("id","message")
        except Exception as e:
            text = ""
        
        if text == "个人信息维护":
            success = True

        return success
        
    #AD域认证登录
    def ad_login(self,list):
        self.frameElem.switch_to_content()
        self.set_login_method(int(list[2]))
        self.set_ad_login_username(list[3])
        self.set_ad_login_pwd(list[5])
        self.click_login_button()
        
    #AD域+口令认证登录
    def ad_pwd_login(self,list):
        self.frameElem.switch_to_content()
        self.set_login_method(int(list[2]))
        self.set_login_username(list[3])
        self.set_login_pwd(int(list[4]))
        self.set_ad_login_pwd(list[5])
        self.click_login_button()
    
    #Radius认证登录
    def radius_pwd_login(self,list):
        self.frameElem.switch_to_content()
        self.set_login_method(list[2])
        self.set_login_username(list[3])
        self.set_login_pwd(list[4])
        self.set_radius_login_pwd(list[5])
        self.click_login_button()
        
    #证书认证登录
    def cert_login(self,list):
        #self.frameElem.switch_to_content()
        brower_name = self.driver.capabilities['browserName']
        if brower_name == 'chrome':
            pass
        elif brower_name == 'internet explorer':
            pass
        else:
            self.set_login_method(list[2])
            os.system(r"D:\testIsomp\au3\cert_firefox.exe")
        
    #设置访问失败最大次数   
    def set_max_login_count(self):
        
        self.frameElem.from_frame_to_otherFrame('topFrame')
        self.commElem.select_role(1)
        time.sleep(3)
        #self.frameElem.from_frame_to_otherFrame('topFrame')
        #WebDriverWait(self.driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "topFrame")))
        #self.driver.find_element_by_xpath("//html/body/div[1]/div[1]/div[2]/u1/li/span/a[1]").click()
        #self.driver.find_element_by_css_selector("a[value=\"1009030000000\"]")
        self.commElem.select_menu(u"策略配置",u"会话配置")
        self.frameElem.from_frame_to_otherFrame('mainFrame')
        strategy_option = self.getElem.find_element_with_wait('id','fortPasswordStrategyId',2)
        self.selectElem.select_element_by_index(strategy_option,0)
        #time.sleep(2)
        self.getElem.find_element_with_wait('id',self.ACCESS_MAX_ACCOUNT).clear()
        access_max_account = self.getElem.find_element_wait_and_sendkeys('id',self.ACCESS_MAX_ACCOUNT,3,4)
        #button_js = "var btn = document.getElementById(self.STRATEGY_SAVE_BUTTON);if(btn != null)btn.click();"
        #self.driver.execute_script(button_js) 
        time.sleep(3)    
        #strategy_save_button = "//form[@id='globalStratoryForm']/div[1]/div[2]/table[1]/tbody/tr[3]/td[2]/input[1]"
        #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.STRATEGY_SAVE_BUTTON))).click()   
        self.getElem.find_element_wait_and_click('id',self.STRATEGY_SAVE_BUTTON)
        self.frameElem.switch_to_content()
        self.commElem.click_login_msg_button()

    #RADIUS认证登录
    def otp_pwd_login(self,driver,loginMethod,username,pwd):
        pass

    
    #点击退出
    def quit(self):
        self.frameElem.switch_to_content()
        self.frameElem.from_frame_to_otherFrame('topFrame')
        self.getElem.find_element_wait_and_click('id',self.QUIT)
    
#if __name__ == "__main__":
    #启动页面
#    browers = initDriver().open_driver()
#    

#    login_page = loginPage(browers)
#    list = ["","","0","test","1",'22',""]
#    login_page.login(list)
#    list = ["","","0","aaaa","1"]
#    login_page.login(list)
#    login_page.set_max_login_count()
#    login_page.quit()
#    login_page.click_msg_button()
    
    #关闭页面
    #initDriver().close_driver(browers)