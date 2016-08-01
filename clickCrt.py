#coding=utf-8
u''' 
#文件名：clickCrt
#被测软件版本号：V2.8.1
#作成人：于洋
#生成日期：2015-03-24
#模块描述：
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import subprocess
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


#打开驱动
ieDriver = "C:\Program Files\Internet Explorer\IEDriverServer.exe"
os.environ["webdriver.ie.driver"] = ieDriver
driver = webdriver.Ie(ieDriver)

#最大化窗口
#driver.maximize_window()

#打开url连接
driver.get("https://192.168.23.228/fort")

#填登陆用户名
username = driver.find_element_by_id("username")
username.send_keys("a")

#填登陆密码
pwd = driver.find_element_by_id("pwd")
pwd.send_keys("1")

#点登陆按钮
loginButton = driver.find_element_by_id("do_login")
loginButton.click()

#定位到rightFrame中
time.sleep(1)
driver.switch_to_frame("content1")
time.sleep(1)
driver.switch_to_frame("mainFrame")
time.sleep(1)
driver.switch_to_frame("rigthFrame")

time.sleep(3)
account = "html/body/div[1]/div[7]/div[2]/div[1]/table/tbody/tr[1]/td[6]/select"
ssh = "html/body/div[1]/div[7]/div[2]/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr/td[2]/a[1]/img"
#cb = "html/body/div[1]/div[7]/div[2]/div[1]/table/tbody/tr[1]/td[1]/span/input"

#定位checkbox并选中
#checkBox = driver.find_element_by_xpath(cb)
#checkBox.click()

#定位select
selectAccount = driver.find_element_by_xpath(account)
#选择第二个名字为root的账号
Select(selectAccount).select_by_index(1)

time.sleep(2)

#os.system("G:\\testWin\\example\\mouse.exe")

#点击CRT图标
#driver.find_element_by_xpath(ssh).click()
'''
count = 2
for i in range(count):

    driver.find_element_by_css_selector("a[alt=\"secureCRT\"]").click()
    
    time.sleep(2)
    command ='taskkill /f /im SecureCRT.exe'
    os.system(command)
        

    time.sleep(1)
    driver.switch_to_default_content()
    driver.switch_to_frame("artIframe")
    
    time.sleep(1)
    #点击弹出窗口的下一步
    driver.find_element_by_id("nextPage").click()
    #勾选不选审计指引
    driver.find_element_by_id("noGuideline").click()
    driver.switch_to_default_content()
    #点击确定按钮
    driver.find_element_by_id("okButton").click()

    button = "/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[1]"
    driver.find_element_by_xpath(button).click()

    time.sleep(2)
    #关闭CRT窗口

        
#关闭驱动
driver.close()
driver.quit()
'''