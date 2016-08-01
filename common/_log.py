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

from _fileRead import *

class log:
    
    def add_log(self ,caseName ,msg):
        #添加日志到log目录下的log.txt文件，记录测试过程
        fileWrite().file_write(caseName + "----start")
        fileWrite().file_write(msg)
        fileWrite().file_write(caseName + "----stop")


if __name__ == "__main__":
    log().add_log("login_test","test")