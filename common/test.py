#! /usr/bin/env python
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsomp/common/")
from _initDriver import *
from _cnEncode import cnEncode
from _log import log
from  _icommon import *
from _excelRead import *
import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

browers = initDriver().open_driver()
getElem = getElement(browers)
a = getElem.find_element_with_wait("id","loginMethod")
    
selectElem = selectElement(browers)
selectElem.select_element_by_index(a,0)
pwd = "html/body/div[2]/div[3]/form/table/tbody[2]/tr[4]/td/input"
getElem.find_element_wait_and_sendkeys("id","username","test")
getElem.find_element_wait_and_sendkeys("xpath",pwd,"1")
getElem.find_element_wait_and_click("id","do_login",5)

frameElem = frameElement(browers)
frameElem.from_frame_to_otherFrame("topFrame")
common = commonFun(browers)
#common.click_login_msg_button()
#选泽xt角色
common.select_role(1)
#选泽bm角色
#common.select_role(2)
#跳转到用户模块
common.select_menu(u"运维管理",u"用户")
#跳转到资源模块
#common.select_menu(u"运维管理",u"资源")
#跳转到时间规则
#common.select_menu(u'运维管理',u'规则定义',u'时间规则')
#跳转到sso页面
#common.select_menu(u'运维操作',u'SSO')
time.sleep(3)
#frameElem.switch_to_content()
#frameElem.switch_to_main()
#frameElem.switch_to_rigth()
frameElem.from_frame_to_otherFrame("mainFrame")
#frameElem.from_frame_to_otherFrame("rigthFrame")

#frameElem.switch_to_rigth()
#frameElem.from_frame_to_otherFrame("rigthFrame")
#获取用户开关状态
#print common.switch_status('id','btn_qh')

#切换到日期控件frame
#frame_xpath = "html/body/div/iframe"
#切换到用户日期控件table
#table_xpath = "html/body/div/div[3]/table"

#时间规则添加按钮
#getElem.find_element_wait_and_click('css',"input[class=\"btn_tj\"]")
#时间规则自定义日期
#common.select_time("fortStartTime",frame_xpath,'0','q',table_xpath,'2017-06-02 12:34:45')
#时间规则启动日选择今天
#common.select_time('fortStartTime',frame_xpath)
#用户列表table的xpath路径
table_elem = tableElement(browers)
tx = "html/body/form/div/div[7]/div[2]/div/table"
#table中第一个tr
tr = "html/body/form/div/div[7]/div[2]/div/table/body/tr[1]"
#资源列表table的xpath路径
#res_xpath = "html/body/form/div/div[8]/div[2]/div/table"
#print table_elem.get_table_rows_count(tx)
#print table_elem.get_table_rows(tx)
#点击用户列表中的编辑
#common.click_operate(tx,0,8,1)
#selem = getElem.find_element_with_wait("id","Roles")
#text = selectElem.get_all_option_text(selem)
#selectElem.get_option_selected(selem)
table_elem.get_table_cols_count(tr)
#print text
#去掉第一个checkbox的勾选
#common.cancel_first_select()
#用户开始日期选择今天
#common.select_time('fortStartTime',frame_xpath)
#用户开始日期自定义
#common.select_time('fortStartTime',frame_xpath,'1','q',table_xpath,'2017-08-09 12:34:45')
#点击资源列表的账号管理
#common.click_operate(res_xpath,0,6,0)
#common.select_time("fortStartTime",frame_xpath)
#cell_elem = table_elem.get_table_cell_text(tx,0,8)[1]
#print common.switch_status(cell_elem)
#print table_elem.get_table_cell_text(tx,0,8)
#common.click_operate(cell_elem,2)
#common = commonFun(browers)
#common.click_operate(cell_elem,2)
#跳转至首页
#common.click_paging('first')
#点击用户页面删除按钮
#getElem.find_element_wait_and_click('id','delete_user')
#点击弹出框确定按钮
#读取excel数据
#excel_elem = excelRead()
#data = excel_elem.get_excel_data(r"D:\testIsomp\testData\login_test_data.xlsx",'Sheet1')
#print data


#frameElem.switch_to_content()
#data = ('登录时输入不存在账号或口令','账号或口令错误')
#xpath = "//div[@id='aui_buttons']/button"
#common.test_win_check_point('xpath',xpath,data,True)

#用户时间选择今天
#frame_xpath = "html/body/iframe"
#table_xpath = "html/body/div/div[3]/table"
#common.select_time("backUpTime",frame_xpath)
#改变日期控件input输入框的属性
#js = "$('input[id=fortStartTime]').attr('readonly',false)"
#browers.execute_script(js)
#getElem.find_element_wait_and_sendkeys('id','fortStartTime','1','q','2017-06-02 14:15:23')
#sso页面选择账号
#tx = "html/body/div[1]/div[7]/div[2]/div[1]/table"
#tdElem = table_elem.get_table_cell_text(tx,3,5)[1]
#tdElem.click()
#mstsc_xapth = "html/body/div[1]/div[7]/div[2]/div[1]/table/tbody/tr[4]/td/div/tbody/tr/td[2]/a/img"
#account_sel = getElem.find_element_with_wait('css',"select[trtarget=\"1_fieldAccount\"]")
#selectElem.select_element_by_index(account_sel,2)
#time.sleep(5)
#image_ele = getElem.find_element_wait_and_click('css',"a[alt=\"mstsc\"]")
#image_ele.find_element_by_css('css',"img[alt=\"mstsc\"]")
#selectElem.select_element_by_index(account_sel,0)
#table_elem.get_table_td_select(0,5,2)
#sso列表点击单点登录图标
#WebDriverWait(browers,5).until(EC.element_to_be_clickable((By.XPATH, "//td[@id='open01']/div/table/tbody/tr/td[2]/a/img[1]"))).click()
