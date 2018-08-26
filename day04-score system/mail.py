import smtplib  # 加载smtplib模块
from email.mime.text import MIMEText
#from email.mime.multipart import MIMEMultipart
#from email.mime.image import MIMEImage
from email.utils import formataddr
from email.header import Header
# 第三方 SMTP 服务
server = "smtp.qq.com"      # SMTP服务器
#mail_user = "***"                  # 用户名
#mail_pass = "***"               # 授权密码，非登录密码 


my_sender = '2364173153@qq.com'
# 发件人邮箱账号，为了后面易于维护，所以写成了变量
my_pass = 'mfbrivbeaylvdjie'#qq邮箱授权码
#my_user = '2364173153@qq.com'
# 收件人邮箱账号，为了后面易于维护，所以写成了变量
#content = ''
def mail(my_user,content):

        ret = True
        
                
            # 代码替换开始行

        message = MIMEText(content, 'plain', 'utf-8')
            # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码

        message['From'] = formataddr(["发件人邮箱昵称", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        message['To'] = formataddr(["收件人邮箱昵称", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        message['Subject'] = "发送邮件测试"  # 邮件的主题，也可以说是标题
            # 标准邮件需要三个头部信息： From, To, 和 Subject ，每个信息直接使用空行分割。

            # 代码替换结束行
        try:
            smtpObj = smtplib.SMTP_SSL(server,465)
        # 发件人邮箱中的SMTP服务器，端口是25
        # POP3服务器: pop.163.com
        # SMTP服务器: smtp.163.com
        # IMAP服务器: imap.163.com
                
            smtpObj.login(my_sender, my_pass)
        # 括号中对应的是发件人邮箱账号、邮箱密码
            smtpObj.sendmail(my_sender,[my_user,],message.as_string())
        # 括号中对应的是发件人邮箱账号、收件人邮箱账号(字符串列表)、发送的邮件

            smtpObj.quit()  # 这句是关闭连接的意思
        except smtplib.SMTPException as e:  # 如果try中的语句没有执行，则会执行下面的ret=False
            print(e)
            ret = False
        return ret
'''
if __name__ == '__main__':        #程序主体入口
    mail() '''                  