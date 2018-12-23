"""mxonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
import xadmin

#基于函数登录的导入
#from users.views import user_login
from users.views import LoginView


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    #index作为静态首页文件
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    #基于函数的用户登录url
    #path('login/', user_login, name='login')
    path('login/', LoginView.as_view(), name='login')
]
