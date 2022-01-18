# 主要是配置发送邮件的主题、正文
import os
import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendEmail(object):
    # email_host 是本地邮件发送邮件的服务器地址(SMTP)，要自己去检查
    # ssl_port 是本地邮件发送的服务器的ssl端口
    def __init__(self, username, passwd, recv, title, content,
                 file=None, ssl=False,
                 email_host='mail.midea.com', port=25, ssl_port=994):
        # 用户名
        self.username = username
        # 密码
        self.passwd = passwd
        # 收件人，多个要传List['aa@qq.com','bb@qq.com']
        self.recv = recv
        # 邮件标题
        self.title = title
        # 邮件正文
        self.content = content
        # 邮件路径，如果不在当前目录下，要写绝对路径
        self.file = file
        # smtp服务器地址
        self.email_host = email_host
        # 普通端口
        self.port = port
        # 是否安全链接
        self.ssl = ssl
        # 安全链接端口
        self.ssl_port = ssl_port

    def send_email(self):
        # 发送内容对象
        msg = MIMEMultipart()
        # 处理附件
        if self.file:
            # 只读文件名，不取路径
            file_name = os.path.split(self.file)[-1]
            try:
                f = open(self.file, 'rb').read()
            except Exception as e:
                raise Exception('附件打不开！！！')
            else:
                att = MIMEText(f, "base64", "utf-8")
                att["Content-Type"] = 'application/octet-stream'
                # base64.b64encode(file_name.encode()).decode()
                new_file_name = '=?utf-8?b?' + base64.b64encode(file_name.encode()).decode() + '?='
                # 这里是处理文件名为中文的，必须这么写
                att["Content-Disposition"] = 'attachment; filename="%s"' % (new_file_name)
                msg.attach(att)
        # 邮件正文内容
        msg.attach(MIMEText(self.content))
        # 邮件主题
        msg['Subject'] = self.title
        # 发送者账号
        msg['From'] = self.username
        # 接收者账号列表
        msg['To'] = ','.join(self.recv)
        if self.ssl:
            self.smtp = smtplib.SMTP_SSL(self.email_host, port=self.ssl_port)
        else:
            self.smtp = smtplib.SMTP(self.email_host, port=self.port)
        # 发送邮件服务器的对象
        self.smtp.login(self.username, self.passwd)
        try:
            self.smtp.sendmail(self.username, self.recv, msg.as_string())
            pass
        except Exception as e:
            print("出错了。。。", e)
        else:
            print("邮件发送成功")
        self.smtp.quit()


if __name__ == '__main__':
    m = SendEmail(
        # 邮箱账号
        username='zxxxx@mxxxd.com',
        # 邮箱密码
        passwd='',
        # 收件人邮箱
        recv=[''],
        title='测试自动发送邮件',
        content='测试发送邮件',
        file=r'D:\pyhton\xmyInterfaceTest\result\report.html',
        ssl=True,
    )
    m.send_email()

