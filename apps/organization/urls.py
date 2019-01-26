# -*-coding:utf-8 -*-

from django.urls import path

from .views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, AddFavView

app_name = 'org'

urlpatterns = [
    # 机构列表页
    path('list/', OrgView.as_view(), name='list'),
    path('add_ask/', AddUserAskView.as_view(), name='add_ask'),
    path('home/<org_id>', OrgHomeView.as_view(), name='org_home'),
    path('course/<org_id>', OrgCourseView.as_view(), name='org_course'),
    path('desc/<org_id>', OrgDescView.as_view(), name='org_desc'),
    path('teachers/<org_id>', OrgTeacherView.as_view(), name='org_teacher'),

    # 机构收藏
    path('add_fav/', AddFavView.as_view(), name='add_fav'),
]