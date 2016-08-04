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
from _cnEncode import *

from selenium.webdriver.support.ui import Select
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
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_tag_name(value))
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
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_tag_name(value)).send_keys(key)
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
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_tag_name(value)).click()
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
        


#table元素
class tableElement(object):
    
    def __init__(self,driver):
        #selenium驱动
        self.driver = driver

    '''获取表格中的所有
        Parameters:
            - table_xpath:定位table的xpath
           
    '''
    def get_table_rows(self,table_xpath):
        get_elem = getElement(self.driver)
        
        #定位到table
        table_elem = get_elem.find_element_with_wait("xpath",table_xpath)
        #获取table中的所有行
        row_elems = table_elem.find_elements_by_tag_name("tr")
             
        return row_elems

    '''获取表格中的文本内容
        Parameters:
            - table_xpath:定位table的xpath
            - row:行号
            - col:列号            
    '''
    def get_table_cell_text(self,table_xpath,row,col):
        
        get_rows = tableElement(self.driver)
        
        #获取表格中的所有行
        row_elems = get_rows.get_table_rows(table_xpath)
        
        #获取行中的所有列
        col_elems = row_elems[row].find_elements_by_tag_name("td")               
            
        return col_elems[col].text
        
    '''获取表格中的行数
        Parameters:
            - table_xpath:定位table的xpath
           
    '''
    def get_table_rows_count(self,table_xpath):
        
        get_rows = tableElement(self.driver)

        #获取表格中的所有行
        row_elems = get_rows.get_table_rows(table_xpath)

        return len(row_elems)



#通用函数，等待元素显示，checkbox，radiobutton的操作
class commonFun(object):
    pass



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
    getElem.find_element_wait_and_sendkeys("id","username","isomper")
    getElem.find_element_wait_and_sendkeys("xpath",pwd,"1")
    getElem.find_element_wait_and_click("id","do_login")
#登陆操作结束

    frameElem = frameElement(browers)
    frameElem.switch_to_bottom()
    aa = getElem.find_element("classname","lt")
    frameElem.from_frame_to_otherFrame("topFrame")
    getElem.find_element_and_click("xpath","html/body/div[1]/div/div[2]/ul/li[2]/span/a")
    getElem.find_element_and_click("xpath","html/body/div[1]/div/div[2]/ul/li[2]/p/a[1]")
    frameElem.from_frame_to_otherFrame("mainFrame")
    
    
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
    table_elem = tableElement(browers)
    tx = "html/body/form/div/div[6]/div[2]/div/table"
    print table_elem.get_table_cell_text(tx,0,1)
    print table_elem.get_table_rows_count(tx)