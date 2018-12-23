# -*- coding:utf-8 -*-
__author__ = 'dante'
__date__ = '2018/12/23 23:35'
from random import Random

from users.models import EmailVerifyRecord


def generate_random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str


#保存邮件到数据库中
def send_register_email(email, type='register'):
    email_record = EmailVerifyRecord()
    random_str = generate_random_str(16)
    email_record.code = random_str
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()