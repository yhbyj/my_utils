# _*_ coding: utf-8 _*_
__author__ = 'Yang Haibo'
__date__ = '2020/6/24 8:43'

import smtplib
from email.mime.text import MIMEText
from email.header import Header


def get_test_message():
    """返回供邮件发送测试的信息"""
    message = MIMEText('邮件发送测试正文……', 'plain', 'utf-8')
    message['From'] = Header('发送者', 'utf-8')
    message['To'] = Header('接收者', 'utf-8')

    subject = '测试邮件'
    message['Subject'] = Header(subject, 'utf-8')
    return message


def test_mail_sending():
    """测试邮件发送"""
    mail_host = 'smtp.qq.com'
    mail_user = '6887993@qq.com'
    mail_pass = '123456'

    sender = '6887993@qq.com'
    receivers = ['lizhaijixiao@sina.com']

    message = get_test_message()

    try:
        mail_server = smtplib.SMTP()
        mail_server.connect(mail_host, 25)
        mail_server.login(mail_user, mail_pass)
        mail_server.sendmail(sender, receivers, message.as_string())
    except smtplib.SMTPException:
        print('Error: 无法发送邮件')


def send_mails(mails):
    """群发邮件"""
    mail_host = 'smtp.qq.com'
    mail_user = '6887993@qq.com'
    mail_pass = '123456'

    mail_server = smtplib.SMTP()
    mail_server.connect(mail_host, 25)
    mail_server.login(mail_user, mail_pass)

    sender = '6887993@qq.com'

    for m in mails:
        mail_server.sendmail(sender, [m['receiver'], ], m['message'])


if __name__ == '__main__':
    # 测试邮件发送
    test_mail_sending()
