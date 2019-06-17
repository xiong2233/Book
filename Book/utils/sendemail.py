from random import Random
from django.core.mail import send_mail
from Book.settings import EMAIL_FROM

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'Book.settings'

# 生成随机字符串
class SendEmail(object):
    def __init__(self):
        self.randomlength = 4
        self.send_type = "register"
    def random_str(self):
        str = ''
        chars = '1234567890'
        length = len(chars) - 1
        random = Random()
        for i in range(self.randomlength):
            str += chars[random.randint(0, length)]
        return str


    def send_register_email(self,email):
        codenum = self.random_str()
        code = codenum
        send_type = self.send_type
        # 保存到数据库完成
        email_title = "愉阅社注册"
        email_body = "若非本人操作请无视这封邮件\n"+"感谢您能注册愉阅社会员\n"+"请打开链接进行验证：http://127.0.0.1:8000/test\n"+"验证码："+code
        send_mail(email_title, email_body, EMAIL_FROM, [email])
        return code
if __name__ == "__main__":
    send = SendEmail()
    code = send.send_register_email("763003970@qq.com")
    print(code)
