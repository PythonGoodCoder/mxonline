# -*- encoding:utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from django.

from .models import CourseOrg, CityDict


# Create your views here.
class OrgView(View):
    """
    课程机构列表功能
    """
    def get(self, request):
        # 取出课程机构
        all_orgs = CourseOrg.objects.all()
        org_nums = all_orgs.count()
        # 取出城市
        all_citys = CityDict.objects.all()

        # 分页功能
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
            p = Paginator(all_orgs, request=request)
            orgs = p.page(page)
        return render(request, 'org-list.html', {
            'all_orgs': orgs,
            'all_citys': all_citys,
            'org_nums': org_nums
        })
