from email.mime.text import MIMEText
from email.header import Header
import smtplib

###准备邮件, 内容
message = MIMEText('test python send mail\r\n','plain', 'utf8')
message['From'] = Header('root', 'utf8')
message['to'] = Header('student', 'utf8')
message['subject'] = Header('py mail test')

##发送邮件

smtp = smtplib.SMTP('127.0.0.1')
smtp.sendmail('root',['root', 'student'], message.as_bytes())
# 查看本地邮件 mail
# 查看指定用户的邮件 mail -u 用户