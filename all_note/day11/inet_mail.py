from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass

def send_mail(server, sender, receivers, msg, subject, passwd):
    # 准备邮件, 纯文本文件
    message = MIMEText(msg, 'plain', 'utf8')
    # message['From'] = Header(sender, 'utf8')
    ###新浪smtp服务器要求 客户设置的邮件地址与实际发件人地址不一致 会报553 错误 ,这里不能填写 第二个参数utf8
    message['From'] = Header(sender)
    message['To'] = Header(receivers[0], 'utf8')
    message['Subject'] = Header(subject, 'utf8')

    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(server)  # 建立连接
    # smtp.starttls()   # 如果服务器要求安全连接，打开注释
    smtp.login(sender, passwd)  # 登陆
    smtp.sendmail(sender, receivers, message.as_bytes())

if __name__ == '__main__':
    server = 'smtp.sina.cn'
    ###发件人
    sender = 'jkgaoyuan@sina.cn'
    #  ###收件人
    # receivers = ['jkgaoyuan@sina.cn']
    receivers = ['yjyhwsad@sina.com']
    msg = '这是一封测试邮件\r\n'
    subject = 'py mail'
    passwd = getpass.getpass()  # 填写邮件服务器的授权码，不是登陆密码
    send_mail(server, sender, receivers, msg, subject, passwd)