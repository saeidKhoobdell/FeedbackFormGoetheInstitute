from smtplib import SMTP
from email.mime.text import MIMEText
import smtplib


def send_email(email,teacher,rate,comment):
    message= f"""<h3>results of rating</h3> <ul><li>email:{email}</li><li>teacher: {teacher}</li>
    <li>rate: {rate}</li><li>comment: {comment}</li></ul>"""
    msg = MIMEText(message, 'html')
    msg['subject']='goethe feedback'
    sender_mail='asaeidkhoobdell@programmer.com'
    receiver_mail='admin@goethe.com'
    msg['from']=sender_mail
    msg['to']=receiver_mail
    with smtplib.SMTP('smtp.mailtrap.io',2525) as server:
        server.login('3cb89b2c3869ca','0802eb8e9c499a')
        server.sendmail(sender_mail, receiver_mail , msg.as_string())