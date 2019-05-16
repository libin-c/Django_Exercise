# !/usr/bin/env python
# _*_ coding:utf-8 _*_
from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^say/$', views.say),
    url(r'^saylala/$', views.saylala,name="son"),
    url(r'^xxg/', views.xiuxiuguai, name="son2"),
    url(r'^hhg/$', views.hahaguai, name="hhge"),
    url(r'^hhge/$', views.hhge),

]
