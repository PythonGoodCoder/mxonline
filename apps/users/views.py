#-*- coding: UTF-8 -*-

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View

from .models import UserProfile
from .forms import LoginForm


# Create your views here.
#自定义认证函数，使其支持邮箱或用户名登录
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username = username) | Q(email = username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


#基于类的用户的登录
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})  #未登录则返回登录界面
    def post(self, request):
        login_form =LoginForm(request.POST)   # model form 验证
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '') #form验证通过后，取出用户名密码
            user = authenticate(username=user_name, password=pass_word)#验证用户密码是否正确
            if user is not None:
                login(request, user) #验证结果不为空，则登录成功
                return render(request, 'index.html', {})
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误！'})
        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误！'})



#基于函数的用户登录
# def user_login(request):
#     if request.method == 'POST':
#         user_name =request.POST.get('username', '')
#         pass_word = request.POST.get('password', '')
#         user = authenticate(username = user_name, password = pass_word)
#         if user is not None:
#             login(request, user)
#             return render(request, 'index.html', {})
#         else:
#             return render(request, 'login.html',{'msg':'用户名或密码错误！'})
#     elif request.method == 'GET':
#         return render(request, 'login.html', {})
