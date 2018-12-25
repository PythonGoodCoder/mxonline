#_*_ encoding:utf-8 _*_
#python默认包
from datetime import datetime

#第三方包
from django.db import models
from django.contrib.auth.models import AbstractUser


#用户model，继承于系统默认用户model AbstractUser
# Create your models here.
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称', default='')
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(max_length=6, choices=(('male',u'男'),('female',u'女')), default = 'female')
    address = models.CharField(max_length=100, default=u'')
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image= models.ImageField(upload_to='image/%Y%m',default=u'image/default.png',max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


#邮箱验证码model
class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=50, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(choices=(('register','注册'),('forget','找回密码')),max_length=10, verbose_name= '验证码类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name= '发送时间')

    class Meta:
        #指定这个model类在后台管理系统中显示的名字
        verbose_name = u'邮箱验证码'
        #指定这个model类的复数形式
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


#轮播图验证码model
class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name= u'标题')
    image = models.ImageField(upload_to='banner/%Y%m', verbose_name= u'轮播图', max_length=100)
    url = models.URLField(max_length=200, verbose_name= u'访问地址')
    index = models.IntegerField(default=100, verbose_name= u'顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name= u'添加时间')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name
