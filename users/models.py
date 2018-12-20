#_*_ encoding:utf-8 _*_
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


#创建用户model，继承于系统默认用户model AbstractUser
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称', default='')
    birday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(max_length=5, choices=(('male',u'男'),('female',u'女')), default = 'female')
    address = models.CharField(max_length=100, default=u'')
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image= models.ImageField(upload_to='image/%Y%m',default=u'image/default.png',max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username