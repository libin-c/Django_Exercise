
# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def say(request):
    '''
    index 视图
    :param request: 包含了请求信息的请求对象
    :return: 响应对象
    '''
    return HttpResponse("I want say say say")
def saylala(request):
    '''
    index 视图
    :param request: 包含了请求信息的请求对象
    :return: 响应对象
    '''
    return HttpResponse("I want say lalalalalalala")
