# -*- coding:utf-8 -*-
__author__ = 'Dante'
from django.urls import path

from .views import CourseListView, CourseDetailView

app_name = 'course'

urlpatterns = [
    # 课程列表页
    path('list/', CourseListView.as_view(), name='course_list'),
    path('detail/<course_id>', CourseDetailView.as_view(), name='course_detail')
]