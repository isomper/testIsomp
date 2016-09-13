#coding=utf-8
u''' 
#文件名：_initDriver
#被测软件版本号：V2.8.1
#作成人：于洋
#生成日期：2015-12-09
#模块描述：日志模块（共通模块）
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time
from _fileRead import *
from _cnEncode import cnEncode

class log(object):
    
    def __init__(self):
        self.cn = cnEncode()

    #日志记录开始
    def log_start(self,caseName):
        #获取当前时间
        startTime = time.strftime('%Y-%m-%d %X',time.localtime())
        
        msg = "[" + startTime + "]" + caseName + "----start"
        
        fileWrite().file_write(msg)
        print "[" + startTime + "]" + caseName + "---------start"

    #日志记录结束
    def log_end(self,caseName):
        #获取当前时间
        endTime = time.strftime('%Y-%m-%d %X',time.localtime())
        
        msg = "[" + endTime + "]" + caseName + "----end"
        
        fileWrite().file_write(msg)
        print "[" + endTime + "]" + caseName + "---------end\n"
        
    '''日志的详细内容
        Parameters:
            - msg：日志信息
            - flag：判定通过或未通过的标识，True代表通过，False代表未通过
    '''
    def log_detail(self,msg,flag):
        #获取当前时间
        iTime = time.strftime('%Y-%m-%d %X',time.localtime())
        
        #通过信息
        passMsg = "["+ iTime + "]" + self.cn.cnCode(msg) + self.cn.cnCode(u"---------测试通过")

        #未通过信息
        unPassMsg = "[" + iTime + "]" + self.cn.cnCode(msg) + self.cn.cnCode(u"---------测试未通过")
        
        if flag:
            #写通过信息进日志
            fileWrite().file_write(passMsg)
            print passMsg
            
        else:
            #写未通过信息进日志
            fileWrite().file_write(unPassMsg)
            print unPassMsg
            

#if __name__ == "__main__":
