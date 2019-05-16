
# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
def say(request):
    '''
    index 视图
    :param request: 包含了请求信息的请求对象
    :return: 响应对象
    '''
    return HttpResponse("I want say say say")

# def saylala(request):
#     return HttpResponse("I want say lalalalalalala")

def saylala(request):
    # return HttpResponse("I want say lalalalalalala")
    return redirect(reverse('Ausers-son'))

def xiuxiuguai(request):
    return HttpResponse("I am super super xiuxiuguai")


def hahaguai(request):
    return HttpResponse("I am lowper lower hahaguai")

def hhge(request):
    return redirect(reverse("Busers:hhge"))
