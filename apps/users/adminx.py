# -*- coding:utf-8 -*-
__author__ = 'dante'
__date__ = '2018/12/22 14:05'

import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner


#开启xadmin的主题功能
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


#修改xadmin的网站名称,页脚,左侧菜单收起
class GlobalSettings(object):
    site_title = '慕学后台管理系统'
    site_footer = '慕学在线网'
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    #在xadmin中model显示的列内容
    list_display = ['code', 'email', 'send_type', 'send_time']
    #在xadmin中model增加搜索功能
    search_fields = ['code', 'email', 'send_type']
    #在xadmin中model增加过滤器功能
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


#把model注册到xadmin中
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

