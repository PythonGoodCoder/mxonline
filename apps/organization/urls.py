# -*-coding:utf-8 -*-

from django.urls import path

from .views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView

app_name = 'org'

urlpatterns = [
    # 课程列表页
    path('list/', OrgView.as_view(), name='list'),
    path('add_ask/', AddUserAskView.as_view(), name='add_ask'),
    path('home/<org_id>', OrgHomeView.as_view(), name='org_home'),
    path('course/<org_id>', OrgCourseView.as_view(), name='org_course')
]