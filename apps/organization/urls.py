# -*-coding:utf-8 -*-

from django.urls import path, include

from .views import OrgView, AddUserAskView

app_name = 'org'

urlpatterns = [
    # 课程列表页
    path('list/', OrgView.as_view(), name='list'),
    path('add_ask/', AddUserAskView.as_view(), name='add_ask')
]