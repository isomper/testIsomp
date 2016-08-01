#coding=utf-8
u''' 
#文件名：_elementText
#被测软件版本号：V2.8.1
#作成人：于洋
#生成日期：2015-11-04
#模块描述：根据元素获取文本（共通模块）
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsomp/common/")
from _cnEncode import cnEncode

class elementText:

    #根据class name获取文本信息
    def get_element_text_by_class(self,driver,class_name):
        return cnEncode().cnCode(driver.find_element_by_class_name(class_name).text)

    #根据class name点击
    def click_element_by_class(self,driver,class_name):
        driver.find_element_by_class_name(class_name).click()
    
    #根据id属性获取文本信息
    def get_element_text_by_id(self,driver,id):
        return cnEncode().cnCode(driver.find_element_by_class_name(id).text)

    #根据id属性点击
    def click_element_by_id(self,driver,id):
        driver.find_element_by_class_name(id).click()
    
    #根据name属性获取文本信息
    def get_element_text_by_name(self,driver,name):
        return cnEncode().cnCode(driver.find_element_by_class_name(name).text)

    #根据name属性点击
    def click_element_by_name(self,driver,name):
        driver.find_element_by_class_name(name).click()
    
    #根据xpath属性获取文本信息
    def get_element_text_by_xpath(self,driver,xpath):
        return cnEncode().cnCode(driver.find_element_by_class_name(xpath).text)

    #根据xpath属性点击
    def click_element_by_xpath(self,driver,xpath):
        driver.find_element_by_class_name(xpath).click()
    