from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import *
import ybc_trans
import ybc_weather
import os
import csv
import requests
import json


# Create your views here.


def login_server(request):

    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user = request.POST.get('user')
        password = request.POST.get('password')
        c = User.objects.filter(user_name=user, user_password=password).count()

        if c == 1:
            return redirect('index/')
        else:
            return HttpResponse('密码错误 <a href="/">返回</a>')


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        user_name = request.POST.get('user')
        password = request.POST.get('password')
        if user_name and password:
            try:
                user = User(user_name=user_name, user_password=password)
                user.save()
                return HttpResponse('<a href="/">注册成功</a>')
            except:
                return HttpResponse('<a href="/">注册失败</a>')
