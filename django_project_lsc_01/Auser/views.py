# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.urls import reverse

# 操作 反向解析的包
from django.urls import reverse
# Create your views here.
def indexChild(request):
#     2.1 接收请求

#     2.2 返回响应对象
    return HttpResponse('总路由--子路由--视图函数')

# 1.创建视图函数  功能函数
def index(request):
    # 1.1 接收请求对象

    # 1.2 返回响应对象
    # return HttpResponse('hello world --- 第一个子功能!')
    return redirect(reverse("Busers:son"))

def show_xxg(request):
    # 1.1 接收请求对象

    # 1.2 返回响应对象
    # return HttpResponse('hello world --- 第一个子功能!')
    return redirect(reverse("Busers:son2"))

