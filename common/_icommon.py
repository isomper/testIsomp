#coding=utf-8
u''' 
#文件名：_icommon
#被测软件版本号：V2.8.1
#作成人：于洋
#生成日期：2016-04-04
#模块描述：自定义封装方法（通用模块）
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsomp/common/")
from _initDriver import *
from _cnEncode import cnEncode

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

#获取定位元素
class getElement(object):
    def __init__(self,driver):
        #selenium驱动
        self.driver = driver
    
    
    
    '''查找元素
        parameter:
            - type:定位的类型，如id,name,tag name,class name,css,xpath等
            - value：页面的元素值
    '''
    def find_element(self,type,value):
        return {
            "id" : lambda value:self.driver.find_element_by_id(value),
            "name" : lambda value:self.driver.find_element_by_name(value),
            "tagname" : lambda value:self.driver.find_elements_by_tag_name(value),
            "classname" : lambda value:self.driver.find_element_by_class_name(value),
            "css" : lambda value:self.driver.find_element_by_css_selector(value),
            "xpath" : lambda value:self.driver.find_element_by_xpath(value),
            "link" : lambda value:self.driver.find_element_by_link_text(value),
            "plt" : lambda value:self.driver.find_element_by_partial_link_text(value)
        }[type](value)
    
    
    
    '''查找元素并发送键值
        Parameters:
             - type:定位的类型，如id,name,tag name,class name,css,xpath等
             - value：页面的元素值
             - key：发送的字符或者键盘的键值
    '''
    def find_element_and_sendkeys(self,type,value,key):
        return {
            "id" : lambda value:self.driver.find_element_by_id(value).send_keys(key),
            "name" : lambda value:self.driver.find_element_by_name(value).send_keys(key),
            "tagname" : lambda value:self.driver.find_elements_by_tag_name(value).send_keys(key),
            "classname" : lambda value:self.driver.find_element_by_class_name(value).send_keys(key),
            "css" : lambda value:self.driver.find_element_by_css_selector(value).send_keys(key),
            "xpath" : lambda value:self.driver.find_element_by_xpath(value).send_keys(key),
            "link" : lambda value:self.driver.find_element_by_link_text(value).send_keys(key),
            "plt" : lambda value:self.driver.find_element_by_partial_link_text(value).send_keys(key)
        }[type](value)
    
    
    
    '''查找元素并单击
        Parameters:
            - type:定位的类型，如id,name,tag name,class name,css,xpath等
            - value：页面的元素值
    '''
    def find_element_and_click(self,type,value):
        return {
            "id" : lambda value:self.driver.find_element_by_id(value).click(),
            "name" : lambda value:self.driver.find_element_by_name(value).click(),
            "tagname" : lambda value:self.driver.find_elements_by_tag_name(value).click(),
            "classname" : lambda value:self.driver.find_element_by_class_name(value).click(),
            "css" : lambda value:self.driver.find_element_by_css_selector(value).click(),
            "xpath" : lambda value:self.driver.find_element_by_xpath(value).click(),
            "link" : lambda value:self.driver.find_element_by_link_text(value).click(),
            "plt" : lambda value:self.driver.find_element_by_partial_link_text(value).click()
        }[type](value)
        
    
    
    '''等待元素出现后再定位元素
        parameter:
            - type:定位的类型，如id,name,tag name,class name,css,xpath等
            - value：页面的元素值
            - timeout:超时前等待的时间        
    '''    
    def find_element_with_wait(self,type,value,timeout=1):
        if type == "xpath":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_xpath(value))
        elif type == "id":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_id(value))
        elif type == "name":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_name(value))
        elif type == "tagname":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_elements_by_tag_name(value))
        elif type == "classname":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_class_name(value))
        elif type == "css":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_css_selector(value))
        elif type == "link":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_link_text(value))
        elif type == "plt":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_partial_link_text(value))
    
    
    '''等待元素出现后再定位元素并发送键值
        parameter:
            - type:定位的类型，如id,name,tag name,class name,css,xpath等
            - value：页面的元素值
            - key：发送的字符或者键盘的键值
            - timeout:超时前等待的时间        
    '''    
    def find_element_wait_and_sendkeys(self,type,value,key,timeout=1):
        if type == "xpath":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_xpath(value)).send_keys(key)
        elif type == "id":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_id(value)).send_keys(key)
        elif type == "name":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_name(value)).send_keys(key)
        elif type == "tagname":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_elements_by_tag_name(value)).send_keys(key)
        elif type == "classname":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_class_name(value)).send_keys(key)
        elif type == "css":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_css_selector(value)).send_keys(key)
        elif type == "link":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_link_text(value)).send_keys(key)
        elif type == "plt":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_partial_link_text(value)).send_keys(key)

    
    '''等待元素出现后再定位元素并点击
        parameter:
            - type:定位的类型，如id,name,tag name,class name,css,xpath等
            - value：页面的元素值
            - timeout:超时前等待的时间        
    '''    
    def find_element_wait_and_click(self,type,value,timeout=1):
        if type == "xpath":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_xpath(value)).click()
        elif type == "id":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_id(value)).click()
        elif type == "name":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_name(value)).click()
        elif type == "tagname":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_elements_by_tag_name(value)).click()
        elif type == "classname":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_class_name(value)).click()
        elif type == "css":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_css_selector(value)).click()
        elif type == "link":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_link_text(value)).click()
        elif type == "plt":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_partial_link_text(value)).click()


#select元素
class selectElement(object):
    def __init__(self,driver):
        #selenium驱动
        self.driver = driver

    '''根据索引选择
        Parameters:
            - selem:定位到的元素
            - index:select的索引，例0,1,2,从0开始计数
    '''
    def select_element_by_index(self, selem, index):
        return Select(selem).select_by_index(index)
    
    '''获取select中的option数量
        Parameters:
            - selem:定位到的select元素
        Return:返回select元素的option数量
    '''
    def get_options_count(self,selem):
        
        options_list = selem.find_elements_by_tag_name("option")

        return len(options_list)
    
    '''获取select选中的option文本
        Parameters:
            - selem:定位到的select元素
            - index:选择的option的索引
        Return：select元素中的index对应的text列表
    '''
    def get_option_text(self,selem,index):
        options_list = selem.find_elements_by_tag_name("option")
        
        for cnt,option in enumerate(options_list):
            if index == cnt:
                selem_text = option.text
                
        return selem_text
    
    '''获取select所有option文本
        Parameters:
            - selem:定位到的select元素
        Return: select元素中的所有option的text列表
    '''
    def get_all_option_text(self,selem):
        options_list = selem.find_elements_by_tag_name("option")
        
        return [option_text_list.text for option_text_list in options_list]
    
    
    '''获取select选中的option的value
        Parameters:
            - selem:定位到的select元素
            - index:选择的option的索引
        Return：select元素中的index对应的value列表
    '''
    def get_option_value(self,selem,index):
        options_list = selem.find_elements_by_tag_name("option")
        
        for cnt,option in enumerate(options_list):
            if index == cnt:
                selem_value = option.get_attribute("value")
                
        return selem_value
        
    '''获取select中的所有option的value
        Parameters:
            - selem:定位到的select元素
        Return: select元素中的所有option的value列表
    '''
    def get_all_option_value(self,selem):
        options_list = selem.find_elements_by_tag_name("option")
        
        return [option_value_list.get_attribute("value") for option_value_list in options_list]





#frame元素
class frameElement(object):
    def __init__(self,driver):
        #selenium驱动
        self.driver = driver
    
    '''定位到topFrame'''
    def switch_to_top(self):
        self.driver.switch_to_frame("content1")
        self.driver.switch_to_frame("topFrame")

    '''定位到mainFrame'''
    def switch_to_main(self):
        self.driver.switch_to_frame("content1")
        self.driver.switch_to_frame("mainFrame")
    
    '''定位到leftFrame'''
    def switch_to_left(self):
        self.driver.switch_to_frame("content1")
        self.driver.switch_to_frame("mainFrame")
        self.driver.switch_to_frame("leftFrame")
        
    '''定位到rightFrame'''
    def switch_to_right(self):
        self.driver.switch_to_frame("content1")
        self.driver.switch_to_frame("mainFrame")
        self.driver.switch_to_frame("rightFrame")
    
        
    '''定位到bottomFrame'''
    def switch_to_bottom(self):
        self.driver.switch_to_frame("content1")
        self.driver.switch_to_frame("bottomFrame")

    '''返回上级frame'''
    def switch_to_content(self):
        self.driver.switch_to_default_content()
    
    '''从一个frame跳转到其他frame
        Parameters:
            - frameName:要跳转到的frame的名字      
    '''
    def from_frame_to_otherFrame(self,frameName):
        #实例化frameElement
        frameElt = frameElement(self.driver)
        frameElt.switch_to_content()
        
        if frameName == "mainFrame":
            #定位到mainFrame
            frameElt.switch_to_main()
            
        elif frameName == "bottomFrame":
            #定位到bottomFrame
            frameElt.switch_to_bottom()
            
        elif frameName == "topFrame":
            #定位到topFrame            
            frameElt.switch_to_top()
            
        elif frameName == "leftFrame":
            #定位到topFrame            
            frameElt.switch_to_left()
        
        elif frameName == "rightFrame":
            #定位到topFrame            
            frameElt.switch_to_right()
        


#table元素
class tableElement(object):
    
    def __init__(self,driver):
        #selenium驱动
        self.driver = driver

    '''获取表格中的所有行对象
        Parameters:
            - table_xpath:定位table的xpath
        Return: table的所有行对象
    '''
    def get_table_rows(self,table_xpath):
        get_elem = getElement(self.driver)
        
        #定位到table
        table_elem = get_elem.find_element_with_wait("xpath",table_xpath)
        #获取table中的所有行
        row_elems = table_elem.find_elements_by_tag_name("tr")
             
        return row_elems

    '''获取表格中一列的文本内容
        Parameters:
            - table_xpath:定位table的xpath
            - row:行号
            - col:列号  
        Return: table列中的文本,table列的列对象
    '''
    def get_table_cell_text(self,table_xpath,row,col):
        
        get_rows = tableElement(self.driver)
        
        #获取表格中的所有行
        row_elems = get_rows.get_table_rows(table_xpath)
        
        #获取行中的所有列
        col_elems = row_elems[row].find_elements_by_tag_name("td")               
            
        return col_elems[col].text,col_elems[col]

        
    '''获取表格中的行数
        Parameters:
            - table_xpath:定位table的xpath
        Return: table的行数
    '''
    def get_table_rows_count(self,table_xpath):
        
        get_rows = tableElement(self.driver)

        #获取表格中的所有行
        row_elems = get_rows.get_table_rows(table_xpath)

        return len(row_elems)



#通用函数
class commonFun(object):
    
    def __init__(self,driver):
        #selenium驱动
        self.driver = driver

    '''选择角色
        Parameters:
            - index:下拉列表的索引（0,1,2）
    '''
    def select_role(self,index):
        getElem = getElement(self.driver)
        getElem.find_element_wait_and_click("id","js_z")
        role = getElem.find_element("id","js_x")
        selectElem.select_element_by_index(role,index)
        
        
    '''获取开关的状态
        return: 0代表开关关闭，1代表开关打开
    '''
    def switch_status(self,elem):
        status = 1
        
        switch = elem.find_element_by_id("btn_qh")
        
        #获取开关class的属性
        switch_value = switch.get_attribute('class')
        
        if switch_value == "switch_off":
            status = 0
        
        return status
        
    '''点击列表页面中的操作项
        Parameters:
            - elem：定位到table中对应的列对象
            - index: 点击索引（0,1,2代表操作列内的项目）
    '''
    def click_operate(self,elem,index):
        op = cell_elem.find_elements_by_tag_name("input")[index]
        op.click()
        
    '''点击分页中的按钮
        Parameters:
            - type：first表示首页，last表示尾页，up表示上一页，
                    down表示下一页，jump表示跳转按钮
    '''
    def click_paging(self,type):
        time.sleep(1)
        
        getElem = getElement(self.driver)
        pageDiv = getElem.find_element_with_wait("id","pager")
        pagerBtn = pageDiv.find_elements_by_tag_name("input")
        
        #点击首页
        if type == "first":
            pagerBtn[2].click()
            
        #点击上一页
        elif type == "up":
            pagerBtn[3].click()
            
        #点击下一页
        elif type == "down":
            pagerBtn[4].click()
        
        #点击尾页
        elif type == "last":
            pagerBtn[5].click()
        
        #点击跳转
        elif type == "jump":
            pagerBtn[0].click()
        
    '''菜单选择
        Parameters:
            - levelText1：1级菜单文本
            - levelText2：2级菜单文本 
            - levelText3：3级菜单文本           
    '''
    def select_menu(self,levelText1,levelText2='no',levelText3='no'):
        #进入topframe
        frameElem = frameElement(self.driver)
        frameElem.from_frame_to_otherFrame("topFrame")
        
        getElem = getElement(self.driver)
        #点击一级菜单
        getElem.find_element_wait_and_click("link",levelText1)
        
        #如果有2级菜单，再点击2级菜单
        if levelText2 != 'no':
            getElem.find_element_wait_and_click("link",levelText2)
        
        #如果有3级菜单，根据名称点击3级菜单
        if levelText3 != 'no':
            frameElem.from_frame_to_otherFrame("leftFrame")
            getElem.find_element_wait_and_click("link",levelText3)
        


if __name__ == "__main__" :
#    #启动页面
    browers = initDriver().open_driver()
   
#登陆操作开始
    getElem = getElement(browers)
    a = getElem.find_element("id","loginMethod")
    
    selectElem = selectElement(browers)
    selectElem.select_element_by_index(a,0)
    #print selectElem.get_options_count(a)
    #print cnEncode().cnCode(selectElem.get_option_text(a,0))
    #print cnEncode().cnCode(selectElem.get_all_option_text(a)[0])
    #print cnEncode().cnCode(selectElem.get_all_option_text(a)[1])

    pwd = "html/body/div[2]/div[3]/form/table/tbody[2]/tr[4]/td/input"
    #getElem.find_element_and_sendkeys("id","username","isomper")
    getElem.find_element_wait_and_sendkeys("id","username","a")
    getElem.find_element_wait_and_sendkeys("xpath",pwd,"1")
    getElem.find_element_wait_and_click("id","do_login")
#登陆操作结束

    frameElem = frameElement(browers)
    frameElem.switch_to_bottom()
    #aa = getElem.find_element("classname","lt")
    frameElem.from_frame_to_otherFrame("topFrame")
#    getElem.find_element_and_click("xpath","html/body/div[1]/div/div[2]/ul/li[2]/span/a")
#    getElem.find_element_and_click("xpath","html/body/div[1]/div/div[2]/ul/li[2]/p/a[1]")
    #frameElem.from_frame_to_otherFrame("mainFrame")
    
    #登陆后选择用户角色
    common = commonFun(browers)
#    common.select_role(1)
#    common.select_role(2)
#    common.select_role(0)
#    swithvalue = common.switch_status()
#    print swithvalue
    
#    print getElem.find_element("id","hostName").text
#    frameElem.from_frame_to_otherFrame("mainFrame")
#    getElem.find_element_and_sendkeys("id","fortUserAccountOrName","a")
#    b = getElem.find_element("id","fortRoleId")
#    selectElem.select_element_by_index(b,2)
    
    #用户页面的添加按钮
    #userAdd_xpath = r"html/body/form/div/div[5]/input[1]"
    #getElem.find_element_wait_and_click("xpath",userAdd_xpath)
    
#    #用户页面的表格
#    table_elem = tableElement(browers)
#    tx = "html/body/form/div/div[7]/div[2]/div/table"
#    print table_elem.get_table_cell_text(tx,0,1)
#    print table_elem.get_table_rows_count(tx)

    
    #用户页面的表格
#    table_elem = tableElement(browers)
#    tx = "html/body/form/div/div[7]/div[2]/div/table"
    
    #返回两个返回值的第一个
    #cell_text = table_elem.get_table_cell_text(tx,0,6)[0]
    
    #返回两个返回值的第二个
    #cell_elem = table_elem.get_table_cell_text(tx,1,8)[1]
    #print table_elem.get_table_cell_text(tx,1,1)[0]
    
    #用户页面的角色选择开始
#    common.click_operate(cell_elem,1)
#    se = getElem.find_element("id","Roles")
#    selectElem.select_element_by_index(se,1)
#    #用户页面的角色选择结束
    
    #用户列表的锁定开关
#    switch_status = common.switch_status(cell_elem)
#    print switch_status
    
    #返回两个返回值分别放进cell_text和cell_elem
    #cell_text,cell_elem = table_elem.get_table_cell_text(tx,0,6)
    
    

    #print cell_elem
#    print cnEncode().cnCode(table_elem.get_table_cell_text(tx,0,7))
#    print table_elem.get_table_rows_count(tx)

    #部门选择
#    getElem.find_element_wait_and_click("id","department_name")
#    #getElem.find_element_wait_and_click("id","query_zijiedian")
#    getElem.find_element_wait_and_click("id","tree_1_switch")
#    getElem.find_element_wait_and_click("link",u"测试部门a")
    
    #点击分页的首页，上一页，下一页，尾页，跳转
#    getElem.find_element_with_wait("id","goto_text").clear()
#    getElem.find_element_wait_and_sendkeys("id","goto_text","2")
#    common.click_paging("jump")
#    common.click_paging("up")
#    common.click_paging("down")
#    common.click_paging("first")    
#    common.click_paging("last") 

    #选择菜单
#    common.select_menu(u"系统配置",u"关联服务",u"邮件")
#    common.select_menu(u"系统配置",u"系统状态",u"关机重启")
#    common.select_menu(u"运维管理",u"用户")
    
#退出操作
    #getElem.find_element_wait_and_click("id","logout")