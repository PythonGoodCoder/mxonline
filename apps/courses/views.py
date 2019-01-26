from django.shortcuts import render
from django.views.generic.base import View

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import Course, Lesson, Video, CourseResource
# Create your views here.


class CourseListView(View):
    def get(self, request):
        current_page = 'course-list.html'
        all_courses = Course.objects.all().order_by('-add_time')
        fav_courses = all_courses.order_by('-fav_nums')[:3]

        # 根据学习人数或者课程数排列
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'hot':
                all_courses = all_courses.order_by('-click_nums')
            elif sort == 'students':
                all_courses = all_courses.order_by('-students')

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses, 5, request=request)
        page_courses = p.page(page)

        return render(request, 'course-list.html', {
            'page_courses': page_courses,
            'current_page': current_page,
            'fav_courses': fav_courses,
            'sort': sort
        })


class CourseDetailView(View):
    def get(self, request, course_id):
        all_courses = Course.objects.filter(id=int(course_id))
        return render(request, 'course-detail.html', {
            'all_courses': all_courses
        })