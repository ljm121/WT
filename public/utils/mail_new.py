# -*- coding: utf-8 -*-
# @Time    : 2022/2/7 14:32
# @Author  : Ljm
# @Email   : lijm@woketech.com
# @File    : mail_new.py
# @Software: PyCharm
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


class Maile_test():
    def __init__(self, filename, smtpserver='smtp.163.com',
                 user='l1323702@163.com',
                 password='DPBWHVZYJVBZHYBM',
                 sender='l1323702@163.com',
                 receiver=None,
                 subject='test_信息'):
        if receiver is None:
            receiver = ['1015206696@qq.com']
        self.mail_address = filename  # 发送邮件的地址
        self.smtpserver = smtpserver  # 发送邮件的服务器
        self.user = user  # 发送邮箱的用户
        self.password = password   # 发送邮箱的密码
        self.sender = sender  # 发送邮件
        self.receiver = receiver  # 接受邮件的用户
        self.subject = subject  # 发送邮件主题

    # 把报告路径拿到，报告名称切出来
    def report_name(self):
        mail_name = str(self.mail_address)
        repost_name1 = mail_name.split("\\")
        return repost_name1[-1]

    # 发送邮件的附件
    def send_mail(self):
        sendfile = str(open(self.mail_address, 'rb').read())
        att = MIMEText(sendfile, "plain", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        # att["Content-Disposition"]="attachment;filename =report_name"
        att.add_header('Content-Disposition', 'attachment', filename=self.report_name())
        msg_root = MIMEMultipart('related')
        msg_root['Subject'] = Header(self.subject, 'utf-8')
        msg_root['From'] = Header(self.user)
        msg_root.attach(att)

        smtp = smtplib.SMTP()
        smtp.connect(self.smtpserver)
        # 用户登录并发送邮件
        smtp.login(self.user, self.password)
        smtp.sendmail(self.sender, self.receiver, msg_root.as_string())
        smtp.quit()


# if __name__ == '__main__':
#     mail_address = r'C:\pycharm\WT\report\2022_02_08_11_25_18_ui_report.html'
#     mail_test = Maile_test(mail_address)
#     mail_test.send_mail()
