# -*- coding: utf-8 -*-
'''
发送html文本邮件
'''
import smtplib  
from email.mime.text import MIMEText   
from email.mime.multipart import MIMEMultipart  
from email.mime.image import MIMEImage  

class sendMail:
    def send_mail(self):
        
        msg = MIMEMultipart()
        #发送方邮箱
        sender = ["susuzhuan0321@163.com"] 
       
        #mailto_list=["qingniao0321@sina.com"] 
        #接收方邮箱
        to_list = ["tyu1850@163.com","26001698@qq.com"]
        #msg['To']=";".join(to_list) 
        #设置服务器
        mail_host="smtp.163.com"
        #用户名
        mail_user="susuzhuan0321"
        
        #口令    
        mail_pass="susu321" 
       
        #发件箱的后缀  
        mail_postfix="163.com" 

        msgRoot = MIMEMultipart('related')  
        msgRoot['Subject'] = '测试itt' 
          
        #构造附件  
        #读取HTML
        att = MIMEText(open('G:\\testIsomp\\report\\testReport.html', 'rb').read(), 'base64', 'utf-8')  
        att["Content-Type"] = 'application/octet-stream'  
        att["Content-Disposition"] = 'attachment; filename="testReport.html"'  
        msgRoot.attach(att) 
#        print "a" 

        smtp = smtplib.SMTP()  
        smtp.connect('smtp.163.com')
        smtp.login(mail_user, mail_pass)  
        smtp.sendmail(sender,to_list, msgRoot.as_string())  
        smtp.quit() 
        
#if __name__ == "__main__":
#    sendMail().send_mail()