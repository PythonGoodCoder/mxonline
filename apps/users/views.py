# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.views.generic.base import View

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm
from utils.email_send import send_register_email


# Create your views here.
# 自定义认证函数，使其支持邮箱或用户名登录
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 基于类的用户的登录
class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        # 未登录则返回登录界面
        return render(request, 'login.html', {'login_form': login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)  # model form 验证
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            # form验证通过后，取出用户名密码
            user = authenticate(username=user_name, password=pass_word)
            # 验证用户密码是否正确
            if user is not None:
                if user.is_active:
                    login(request, user)  # 验证结果不为空，则登录成功
                    return render(request, 'index.html', {'username': user_name})
                else:
                    return render(request, 'login.html', {'msg': '用户名没有激活！', 'login_form': login_form})
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误！', 'login_form': login_form})
        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误！', 'login_form': login_form})


# 基于函数的用户登录
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


# 注册页面
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            if UserProfile.objects.filter(email=user_name):
                return render(request, 'register.html', {'register_form': register_form, 'msg': '用户已经存在'})
            pass_word = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()
            # 发送激活链接
            send_register_email(user_name, 'register')
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'msg': '信息填写有误！', 'register_form': register_form})


# 邮件激活码的逻辑控制
class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, 'active_fail.html')
        login_form = LoginForm
        return render(request, 'login.html', {'login_form': login_form})


# 忘记密码
class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, 'forget_pwd.html', {'forget_form': forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email', '')
            send_register_email(email, 'forget')
            return render(request, 'send_success.html')
        else:
            return render(request, 'forget_pwd.html', {'forget_form': forget_form})


# 重置密码
class ResetView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, 'password_reset.html', {'email': email})
        else:
            return render(request, 'active_fail.html')
        return render(request, 'login.html')


# 由于get方法url传入需要带active_code参数，导致无法重用，只能另外写一个view
class ModifyPwdView(View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            email = request.POST.get('email', '')
            if pwd1 != pwd2:
                return render(request, 'password_reset.html', {'email': email, 'msg': '密码不一致！'})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()
            return render(request, 'login.html')
        else:
            email = request.POST.get('email', '')
            return render(request, 'password_reset.html', {'email': email, 'modify_form': modify_form})
