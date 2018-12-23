# -*- coding:utf-8 -*-
__author__ = 'dante'
__date__ = '2018/12/23 14:48'
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)