# !/usr/bin/env python
# _*_ coding:utf-8 _*_

from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^index/', views.index,name="ind"),
]
