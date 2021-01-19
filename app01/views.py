# -*- coding:utf-8 -*-

from django.shortcuts import render, HttpResponse
from django import forms
from app01 import models
from django.core.validators import RegexValidator


# Create your views here.
class UserInfoModelForm(forms.ModelForm):
    phone = forms.CharField(label='电话', validators=[RegexValidator(r'^(1|2|3|4|5|6|7|8|9)\d{9}$)', '手机号格式错误'), ])
    password = forms.CharField(label='密码', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='重复密码', widget=forms.PasswordInput)
    code = forms.CharField(label='验证码')

    class Meta:
        model = models.UserInfo
        fields = '__all__'


def register(request):
    form = UserInfoModelForm()
    return render(request, 'register.html', {'form': form})
