import smtplib
from email.mime.text import MIMEText

msg=MIMEText("The body of the email is here")

msg['Subject']='An Email Alert'
msg['From']='1532014681@qq.com'
msg['to']='ruanyang_njut@163.com'

s=smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()
