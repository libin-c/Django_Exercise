# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http.response import HttpResponse

# 操作 反向解析的包
from django.urls import reverse
# Create your views here.
def index(request):

    return redirect(reverse("ind"))