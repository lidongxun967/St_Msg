import smtplib
import email.message
import EVCLib

class EVCode():
    def __init__(self, smtp_server, address, password, subject="DebugEpoch留言板", nickname="DebugEpoch", captcha_page=EVCLib.index):
        """
        初始化 EVCode 实例。
        
        参数：
        smtp_server：SMTP 服务器地址
        address：发件人邮箱地址
        password：发件人邮箱密码
        subject：邮件主题，默认为 "EVCode验证码"
        nickname：发件人昵称，默认为 "EVCode"
        captcha_page：验证码页面，默认为 EVCLib.index
        random_func：生成随机验证码的函数，默认为 EVCLib.generate_random_code
        """
        self.index = captcha_page
        self.smtp_domain, self.smtp_port = EVCLib.domain_split(smtp_server, 587)
        self.send_email_address = address
        self.send_email_password = password
        self.send_email_subject = subject
        self.send_email_nickname = nickname

    def _send_email(self, msg):
        """
        发送邮件。
        
        参数：
        msg：邮件消息对象
        
        返回：
        发送成功返回 True，否则返回 False
        """
        try:
            with smtplib.SMTP(self.smtp_domain, self.smtp_port) as server:
                server.starttls()
                server.login(self.send_email_address, self.send_email_password)
                server.send_message(msg)
                return True
        except Exception as e:
            print(e)
            return e

    def send_verification_code(self, received_email,fem,fm):
        """
        发送验证码邮件。
        
        参数：
        received_email：接收验证码邮件的邮箱地址
        
        返回：
        发送成功返回验证码，发送失败返回 None
        """
        # 生成验证码

        html_content = self.index

        # 替换HTML内容中的验证码占位符
        html_content = html_content.replace('!User_Email!', fem).replace('!User_Message!', fm)

        # 创建邮件对象
        msg = email.message.EmailMessage()
        msg.add_alternative(html_content, subtype='html')
        msg['Subject'] = self.send_email_subject
        msg['From'] = self.send_email_nickname + ' <' + self.send_email_address + '>'
        msg['To'] = received_email

        # 连接SMTP服务器并发送邮件
        if self._send_email(msg):
            return True
        return None
